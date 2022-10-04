""" maxar_ard_grid
    Tools for the 5k Maxar ARD grid
    based on https://github.com/DigitalGlobe/tiletanic

    Tiling scheme is a 5km UTM grid at a 12th quadkey level
    Tiles are identified based on quadkeys using a top-left naming scheme

    ---------
    | 0 | 1 |
    --------
    | 2 | 3 |
    ---------
"""

import json
import math
import operator
import re
import warnings
from collections import namedtuple
from functools import lru_cache
from itertools import chain
from math import floor

import pyproj
from pyproj import CRS
from shapely import prepared, wkt
from shapely.affinity import translate
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiPolygon,
    Polygon,
    base,
    box,
    mapping,
    shape,
)
from shapely.ops import split, transform

__all__ = ["Cell", "Grid", "covers"]

Coords = namedtuple("Coords", ["x", "y"])
CoordsBbox = namedtuple("CoordsBbox", ["xmin", "ymin", "xmax", "ymax"])

quadkey_regex = re.compile(r"^[0-3]+$")
id_regex = re.compile(r"^[zZ]*(\d\d)[-/]([0-3]+)$")


class Cell(object):
    """general quadtree cells at any zoom in a given zone

    Initialize with:

    Cell(x, y, z, zone=zone)
        x(int): x-index of cell
        y(int): y-index of cell
        z(int): z-index (zoom) of cell
        zone(int): UTM zone number, required

    Cell(quadkey, zone=zone)
        quadkey(str): quadkey of cell
        zone(int): UTM zone number, required

    Cell(cell_id)
        cell_id(str): Cell identifier in form 'Z{zone}-{quadkey}' or '{zone}/{quadkey}'

    """

    def __init__(self, *args, zone=None):
        self._geom_WGS84 = None
        # x, y, z, zone=XX
        if len(args) == 3:
            if zone is None:
                raise ValueError("Zone cannot be None")
            self.x, self.y, self.z = args
            self.zone = zone
        elif len(args) == 1:
            # quadkey or cell id or already a cell
            arg = args[0]
            if type(arg) == Cell:
                self.x, self.y, self.z, self.zone = arg.x, arg.y, arg.z, arg.zone
            elif quadkey_regex.match(arg):
                # quadkey, zone=XX
                if zone is None:
                    raise ValueError("Zone cannot be None")
                self.x, self.y, self.z = Grid.quadkey_to_index(arg)
                self.zone = int(zone)
            else:
                match = id_regex.match(arg)
                if not match:
                    raise ValueError("Unknown cell identifier")
                self.zone = int(match.group(1))
                self.x, self.y, self.z = Grid.quadkey_to_index(match.group(2))
        else:
            raise ValueError("Unknown cell identifiers - wrong number of args")

    @property
    def hemisphere(self):
        """Hemisphere of cell
        Used to determine correct EPSG code"""

        if self.quadkey[0] in ("0", "1"):
            return "N"
        return "S"

    @property
    def proj(self):
        """Projection code string of cell"""

        hemisphere_code = {"N": 6, "S": 7}[self.hemisphere]
        return "EPSG:32%s%02d" % (hemisphere_code, self.zone)

    @property
    def bounds(self):
        """bounds of cell in its true UTM coordinates"""
        cell_bounds = Grid.cell_to_bounds(self.x, self.y, self.z)
        # The Canvas Grid does all calculations in North UTM
        # Cells in UTM South need to be adjusted in Y
        if self.hemisphere == "S":
            cell_bounds[1] += 10_000_000
            cell_bounds[3] += 10_000_000
        return cell_bounds

    @property
    def grid_bounds(self):
        """bounds of cell in its grid (North) UTM coordinates"""
        return Grid.cell_to_bounds(self.x, self.y, self.z)

    @property
    @lru_cache()
    def bounds_WGS84(self):
        """Bounding box of cell in WGS84
        NOTE: this is the envelope! `Don't box(*cell.bounds_WGS84)`
        to get the WGS84 geometry. Use cell.geom_WGS84 instead"""
        warnings.warn("deprecating: use Cell.geom_WGS84.bounds")
        return self.geom_WGS84.bounds

    @property
    @lru_cache()
    def geom_WGS84(self):
        """Geometry of cell in WGS84 (l)ongitude, latitude)"""
        if self._geom_WGS84 is None:
            # reprojection is expensive, so we cache the result
            tfm = get_transform(self.proj, 4326)
            self._geom_WGS84 = transform(tfm, shape(self))
        return self._geom_WGS84

    def to_feature(self):
        """Returns basic GeoJSON representation of cell as Python dict"""

        return {
            "type": "Feature",
            "properties": {"id": self.id},
            "geometry": mapping(self.geom_WGS84),
        }

    def to_geojson(self):
        warnings.warn(
            "to_geojson() will be deprecated, use to_feature() for Python dicts, to_GeoJSON for json strings"
        )
        return self.to_feature()

    def to_GeoJSON(self):
        """returns basic GeoJSON string of the cell"""
        return json.dumps(self.to_feature())

    @property
    def quadkey(self):
        """Quadkey of cell"""
        return Grid.index_to_quadkey(self.x, self.y, self.z)

    @property
    def id(self):
        """Cell identifier, in form:
        `Z{zone}-{quadkey}`"""

        return "Z%02d-%s" % (self.zone, self.quadkey)

    @property
    def tile_id(self):
        """Alternative identifier used in tile paths and pipelines in form:
        `{zone}/{quadkey}`"""

        return "%02d/%s" % (self.zone, self.quadkey)

    @property
    def zoom(self):
        return self.z

    @property
    def __geo_interface__(self):
        """Python geospatial interface
        To get a Shapely geometry representation of a cell do:

        geom = shape(cell)"""

        return box(*self.bounds).__geo_interface__

    @property
    def coords(self):
        """Coordinates of the cell in the quadkey system"""
        return self.x, self.y, self.z

    @property
    def parent(self):
        """Parent cell for the cell"""

        return self._get_parent()

    def get_parent_at_zoom(self, zoom):
        """Parent cell at a given zoom"""

        assert self.z >= zoom, "Requested zoom is larger than cell zoom"
        if self.z == zoom:
            return self
        cell = self.parent
        while cell.z > zoom:
            cell = cell._get_parent()
        return cell

    def _get_parent(self):
        """Calculate parent cell"""

        parent_z = self.z - 1
        if self.x % 2 == 0:
            parent_x = self.x // 2
        else:
            parent_x = (self.x - 1) // 2
        if self.y % 2 == 0:
            parent_y = self.y // 2
        else:
            parent_y = (self.y - 1) // 2
        return Cell(parent_x, parent_y, parent_z, zone=self.zone)

    @property
    def children(self):
        """Returns 4 child cells for a given cell"""

        return [
            Cell(2 * self.x, 2 * self.y, self.z + 1, zone=self.zone),
            Cell(2 * self.x + 1, 2 * self.y, self.z + 1, zone=self.zone),
            Cell(2 * self.x, 2 * self.y + 1, self.z + 1, zone=self.zone),
            Cell(2 * self.x + 1, 2 * self.y + 1, self.z + 1, zone=self.zone),
        ]

    def get_children_at_zoom(self, zoom):
        """Generator of all child cells at a given zoom"""
        if self.z == zoom:
            yield self
        elif self.z > zoom:
            raise ValueError("Requested zoom is less than cell zoom")
        else:
            for cell in (
                cell
                for child_cell in self.children
                for cell in child_cell.get_children_at_zoom(zoom)
            ):
                yield cell

    def neighbor(self, direction):
        """returns a neighboring cell in any cardinal or ordinal direction

        Based on method given in "A Practical Algorithm for Computing
            Neighbors in Quadtrees, Octrees, and Hyperoctrees" by
            Robert Yoder and Peter Bloniarz, published in
            "Modeling, Simulation and Visualization Methods (The 2017
            WorldComp International Conference Proceedings)"

        see http://web.archive.org/web/20120907211934/http://ww1.ucmss.com/books/LFS/CSREA2006/MSV4517.pdf

        Args:
            direction(str): one of N, S, E, W, NW, NE, SW, SE
        Returns:
            Cell"""

        def lookup(quadkey, direction, i=None):
            """use the Yoder & Bloniarz lookup table to find neighboring quadkeys"""
            # start at the last quad digit if not specified
            i = i or len(quadkey) - 1

            # look up the next quad and direction
            next_quad, next_direction = neighbor_lookup[quadkey[i]][direction]

            # substitute the current (i) quad digit
            new_quadkey = quadkey[:i] + next_quad + quadkey[i + 1 :]

            # if we're done, return the new quadkey
            # otherwise follow the direction to calculate the next digit to the left
            if next_direction == "halt":
                return new_quadkey
            else:
                i -= 1
                return lookup(new_quadkey, next_direction, i)

        qk = self.quadkey
        for d in direction.upper():
            qk = lookup(qk, d)

        return Cell(qk, zone=self.zone)

    @property
    def neighbors(self):
        """returns all neighboring cells"""
        directions = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
        return {d: self.neighbor(d) for d in directions}

    def __repr__(self):
        return "<Cell %s>" % self.id

    def __eq__(self, other):
        """Two cells are equivalent if they have the same ID"""

        return self.id == other.id

    def __contains__(self, other):
        """Overloading `in` operator to see if a cell contains another cell

        >>> cell('Z40-3012302221') in cell('Z40-301230222')
        True
        """

        return other.id.startswith(self.id)

    def __hash__(self):
        """Hash of cell ID"""
        return hash(self.id)


neighbor_lookup = {
    "0": {"E": ("1", "halt"), "W": ("1", "W"), "S": ("2", "halt"), "N": ("2", "N")},
    "1": {"E": ("0", "E"), "W": ("0", "halt"), "S": ("3", "halt"), "N": ("3", "N")},
    "2": {"E": ("3", "halt"), "W": ("3", "W"), "S": ("0", "S"), "N": ("0", "halt")},
    "3": {"E": ("2", "E"), "W": ("2", "halt"), "S": ("1", "S"), "N": ("1", "halt")},
}


@lru_cache()
def get_transform(src_proj, dest_proj):
    """Generate and cache a reprojection transform

        Initializing a transform is expensive so in cases
        of chipping we don't want to recreate the transform for every chip!

    Args:
        src_proj: any pyproj acceptable input for the source projection
        dest_proj: any pyproj acceptable input for the destination projection

    Returns:
        pyproj transformation function"""

    return pyproj.Transformer.from_crs(src_proj, dest_proj, always_xy=True).transform


@lru_cache()
def get_CRS(code):
    """Generate and cache a Coordinate Reference System object

        Initializing a CRS is expensive so in cases
        of checking lots of geoms with covers() we don't want to
        recreate the CRS for every check

    Args:
        code: any pyproj acceptable input for a CRS

    Returns:
        pyproj CRS"""

    return CRS(code)


def covers(geom_src, zoom=12, src_proj=4326):
    """Generator of cells covered by a given object.

    Args
        geom_src: a source of geometry, see below
        zoom: zoom level of cells to return, defaults to 12
        src_proj: optional projection code of source data, default is WGS84

    Geometry Sources:
        - Python Geospatial Interface
        - Shapely geometries
        - Canvas Cells
        - Canvas Cell IDs
        - GeoJSON-like geometry dict
        - GeoJSON-like feature dict
        - Well Know Text (WKT)"""

    if src_proj != 4326:
        try:
            src_proj = get_CRS(src_proj)
        except:
            raise ValueError(f"Unknown projection source: {src_proj}")
    try:
        if type(geom_src) == dict:
            geom = shape(geom_src)
        elif issubclass(type(geom_src), base.BaseGeometry):
            geom = geom_src
        elif type(geom_src) == Cell:
            return geom_src.get_children_at_zoom(zoom)
        elif type(geom_src) == str:
            try:
                # make more robust, less dumb
                geom_dict = json.loads(geom_src)
                if "geometry" in geom_dict:
                    geom = shape(geom_dict["geometry"])
                else:
                    geom = shape(geom_dict)
            except:
                try:
                    cell = Cell(geom_src)
                    return cell.get_children_at_zoom(zoom)
                except:
                    geom = wkt.loads(geom_src)
        else:
            geom = shape(geom_src.__geo_interface__)

    except:
        raise ValueError("Unable to convert input to a geometry object")
    return _covers_geom(geom, zoom, src_proj)


def lon2zone(lon):
    return (floor((lon + 180) / 6) % 60) + 1


def geom2zones(geom, zoom):
    """Find the UTM zones a geometry's covering ARD cells might lay in

    Note:
        ARD cells are not completely within UTM zone boundaries,
        so a input on or near the boundary may be covered by cells
        from both zones

    Args:
        geom(shapely geometry): input geometry
        zoom(int): zoom of cells to intersect

    Returns:
        tuple(start(int), stop(int)): start and stop of range of covering zones"""
    min_lon, min_lat, max_lon, max_lat = geom.bounds
    # calculate buffer for N/S bound farthest from equator
    max_lat_abs = max(abs(min_lat), abs(max_lat))
    cell_width = Grid.cell_size(zoom)
    buffer = cell_width / 40_075_000 * 360 / math.cos(math.radians(max_lat_abs))

    start = lon2zone(min_lon - buffer)
    stop = lon2zone(max_lon + buffer)

    return start, stop


def _covers_geom(geom, zoom, src_proj):
    """Calculate covering cells recursively

    Args:
        geom(Shapely geometry): input geometry
        zoom(int): zoom of cells to intersect
        src_proj(int, stf, pyproj.CRS): projection of input geometry"""

    tfm = get_transform(src_proj, 4326)
    geom_84 = transform(tfm, geom)
    all_zones = set()
    all_geoms = []

    # If the object is a multi-geometry, we need to figure out
    # what zone(s) each part covers
    # However, it's possible we might have to split a part,
    # so we will reassemble the multi-geometry from the processed parts

    # break up a multi-geom or fake one
    try:
        geoms = geom_84.geoms
    except:
        geoms = [geom_84]

    for geom in geoms:
        start, stop = geom2zones(geom, zoom)
        if start == stop:
            # only one zone
            zones = [start]
            spanning = False
        elif stop >= start:
            # multiple contiguous zones
            zones = range(start, stop + 1)
            spanning = True
        else:
            # antimeridian case
            # multiple zones split into two ranges
            zones = chain(range(start, 61), range(1, stop + 1))

            # if we cross the antimeridian, we probably have to split up geometries
            shifted = []
            g_west = split(geom, LineString([(-180, -90), (-180, 90)]))
            for gw in g_west.geoms:
                if gw.bounds[2] <= -180:
                    shifted.append(translate(gw, xoff=360))
                else:
                    g_east = split(gw, LineString([(180, -90), (180, 90)]))
                    for ge in g_east.geoms:
                        if ge.bounds[0] >= 180:
                            shifted.append(translate(ge, xoff=-360))
                        else:
                            shifted.append(ge)
            geom = GeometryCollection(shifted)
            spanning = True
        all_geoms.append(geom)
        all_zones.update(zones)

    # reassemble the parts
    all_geoms = GeometryCollection(all_geoms)

    # check the geometry per zone
    for zone in all_zones:
        utm_proj = "EPSG:326%02d" % zone
        grid = Grid(zone)
        cell_width = Grid.cell_size(zoom)
        # the maximum possible cell buffer at 84d longitidude
        # plus a little extra
        buffer = cell_width / 40_075_000 * 360 / 0.1
        zone_box = box(grid.min_lon - buffer, -90, grid.max_lon + buffer, 90)
        clipped_geom = all_geoms.intersection(zone_box)
        tfm = get_transform(4326, utm_proj)
        utm_geom = transform(tfm, clipped_geom)
        for cell in grid.covers(utm_geom, zoom=zoom):
            if not spanning:
                if cell in grid:
                    yield cell
            else:
                cell_min_lon, _, cell_max_lon, _ = cell.geom_WGS84.bounds
                if cell_min_lon <= grid.max_lon and cell_max_lon >= grid.min_lon:
                    if cell in grid:
                        yield cell


class Grid(object):
    """A quadkey grid covering a given zone

    Args
        zone(int): UTM zone of grid"""

    cell_zoom = 12
    map_size = 10_240_000
    _bounds = CoordsBbox(-map_size + 500_000.0, -map_size, map_size + 500_000.0, map_size)

    def __init__(self, zone):
        if zone is None:
            raise ValueError("UTM zone cannot be None")
        if type(zone) is not int:
            raise ValueError("UTM zone must be an integer")
        if zone < 1 or zone > 60:
            raise ValueError("Invalid UTM zone number")
        self.zone = zone

        self.min_lon = (zone - 1) * 6 - 180
        self.max_lon = self.min_lon + 6

    @classmethod
    def cell_size(cls, zoom):
        return cls.map_size / 2 ** (zoom - 1)

    def __contains__(self, cell):
        """Test if a cell is in the grid.

        Zone grids are assymmetric - they extend further to the east
        to provide seamless coverage. See the grid cell geopackage files.

        Args:
            cell(Cell): Cell to test

        Returns:
            bool: True if cell is in grid"""

        min_lon, _, max_lon, _ = cell.geom_WGS84.bounds

        # cell is inside the zone
        if min_lon >= self.min_lon and max_lon <= self.max_lon:
            return True

        # cells spanning the east boundary are considered in
        if max_lon >= self.max_lon and min_lon <= self.max_lon:
            return True

        # cells spanning west are in if the majority of their bottom side
        # is east of the boundary. Centroids do not work here!
        if max_lon >= self.min_lon and min_lon <= self.min_lon:
            # get unique coords
            co = list(cell.geom_WGS84.exterior.coords)[:4]
            # sort by X so we can get the points of the bottom side
            co_x = sorted(co, key=operator.itemgetter(0))
            # see if the bottom side is biased east or west of the boundary
            west = self.min_lon - co_x[1][0]
            east = co_x[3][0] - self.min_lon
            if east >= west:
                return True

        return False

    @staticmethod
    def quadkey_to_index(qk):
        x = 0
        y = 0
        for i, digit in enumerate(reversed(qk)):
            mask = 1 << i
            if digit == "1":
                x = x | mask
            elif digit == "2":
                y = y | mask
            elif digit == "3":
                x = x | mask
                y = y | mask
        return x, y, len(qk)

    @staticmethod
    def index_to_quadkey(x, y, z):
        quadkey = []
        for zoom in range(z, 0, -1):
            digit = 0
            mask = 1 << (zoom - 1)
            if int(x) & mask:
                digit += 1
            if int(y) & mask:
                digit += 2
            quadkey.append(digit)
        return "".join(str(d) for d in quadkey)

    @classmethod
    def cell_to_bounds(self, x, y, z):
        """Return the UTM bounds of a cell"""
        xmin = (x / (2.0**z) * (self._bounds.xmax - self._bounds.xmin)) + self._bounds.xmin
        xmax = ((x + 1) / (2.0**z) * (self._bounds.xmax - self._bounds.xmin)) + self._bounds.xmin
        ymin = self._bounds.ymax - ((y + 1) / (2.0**z) * (self._bounds.ymax - self._bounds.ymin))
        ymax = self._bounds.ymax - (y / (2.0**z) * (self._bounds.ymax - self._bounds.ymin))
        return [xmin, ymin, xmax, ymax]

    def covers(self, geom, zoom):
        """returns a generator of cells intersecting a geometry

        Args:
            geom(str or dict of geojson or Shapely geom): geometry to intersect (in UTM)

        Returns:
            generator of intersecting Canvas cells"""

        # Only shapely geometries allowed.
        if not isinstance(geom, base.BaseGeometry):
            raise ValueError("geometry is not valid")

        if geom.is_empty:
            return

        # Generate the covering.
        prep_geom = prepared.prep(geom)
        if isinstance(geom, (Polygon, MultiPolygon)):
            for cell in self._cover_polygonal(
                Cell(0, 0, 0, zone=self.zone), prep_geom, geom, zoom
            ):
                yield cell
        else:
            for cell in self._cover_geometry(Cell(0, 0, 0, zone=self.zone), prep_geom, geom, zoom):
                yield cell

    def _cover_geometry(self, curr_cell, prep_geom, geom, zoom):
        """Covers geometries with cells by recursion.
        Args:
            curr_cell: The current cell in the recursion scheme.
            prep_geom: The prepared version of the geometry we would like to cover.
            geom: The shapely geometry we would like to cover.
        Yields:
            An iterator of Cell objects that
            cover the input geometry.
        """
        if prep_geom.intersects(box(*curr_cell.grid_bounds)):
            if curr_cell.z == zoom:
                yield curr_cell
            else:
                for cell in (
                    cell
                    for child_cell in curr_cell.children
                    for cell in self._cover_geometry(child_cell, prep_geom, geom, zoom)
                ):
                    yield cell

    def _cover_polygonal(self, curr_cell, prep_geom, geom, zoom):
        """Covers polygonal geometries with cells by recursion.
        This is method is slightly more efficient than _cover_geometry in
        that we can check if a cell is completely covered by a geometry
        and if so, skip directly to the max zoom level to fetch the
        covered cells.
        Args:
            curr_cell: The current cell in the recursion scheme.
            prep_geom: The prepared version of the polygonal geometry we
                    would like to cover.
            geom: The shapely polygonal geometry we would like to cover.
        Yields:
            An iterator of Cell objects that cover the input polygonal geometry.
        """

        cell_geom = box(*curr_cell.grid_bounds)
        if prep_geom.intersects(cell_geom):
            if curr_cell.z == zoom:
                yield curr_cell
            elif prep_geom.contains(cell_geom):
                if curr_cell.z == zoom:
                    yield curr_cell
                else:
                    for cell in curr_cell.get_children_at_zoom(zoom):
                        yield cell
            else:
                for cell in (
                    cell
                    for child_cell in curr_cell.children
                    for cell in self._cover_polygonal(child_cell, prep_geom, geom, zoom)
                ):
                    yield cell
