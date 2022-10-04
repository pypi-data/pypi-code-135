"""Calc_weights_catalog_proceess."""
import json
import logging
from typing import Any
from typing import Dict
from typing import Tuple

import geopandas as gpd
import pandas as pd
from gdptools.run_weights_engine import RunWghtEngine
from pygeoapi.process.base import BaseProcessor

LOGGER = logging.getLogger(__name__)

PROCESS_METADATA = {
    "version": "0.1.0",
    "id": "run_weights_catalog",
    "title": "run area-weighted aggregation",
    "description": """Run area-weighted aggredation using  OpenDAP endpoint and
        user-defined Features""",
    "keywords": ["area-weighted intersections"],
    "links": [
        {
            "type": "text/html",
            "rel": "canonical",
            "title": "information",
            "href": "https://example.org/process",
            "hreflang": "en-CA",
        }
    ],
    "inputs": {
        "param_dict": {
            "title": "param_dict",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "grid_dict": {
            "title": "grid_dict",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "weights": {
            "title": "weights_json_string",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "shape_file": {
            "title": "shape_file_json_string",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "shape_crs": {
            "title": "shape_file_crs_string",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "shape_poly_idx": {
            "title": "shape_poly_idx_string",
            "schema": {
                "type": "string",
            },
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "start_date": {
            "title": "Beginning date to pull from openDAP endpoint",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "end_date": {
            "title": "Ending date to pull from openDAP endpoint",
            "schema": {"type": "string"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
        "numdiv": {
            "title": "Split download of openDAP endpoint by numdiv as integer",
            "schema": {"type": "number"},
            "minOccurs": 1,
            "maxOccurs": 1,
        },
    },
    "outputs": {
        "aggregated_json": {
            "title": "json records file of aggregated values",
            "schema": {"type": "object", "contentMediaType": "application/json"},
        }
    },
    "example": {
        "inputs": {
            "param_dict": (
                '{"aet": {"id": "terraclim", "grid_id": 116.0, "URL": '
                '"http://thredds.northwestknowledge.net:8080/thredds/dodsC/agg_terraclimate_aet_1958_CurrentYear_GLOBE.nc", '  # noqa
                '"tiled": "", "variable": "aet", "varname": "aet", "long_name": '
                '"water_evaporation_amount", "T_name": "time", "duration": '
                '"1958-01-01/2020-12-01", "interval": "1 months", "nT": 756.0, "units": "mm", '  # noqa
                '"model": NaN, "ensemble": NaN, "scenario": "total"}, "pet": {"id": '
                '"terraclim", "grid_id": 116.0, "URL": '
                '"http://thredds.northwestknowledge.net:8080/thredds/dodsC/agg_terraclimate_pet_1958_CurrentYear_GLOBE.nc", '  # noqa
                '"tiled": "", "variable": "pet", "varname": "pet", "long_name": '
                '"water_potential_evaporation_amount", "T_name": "time", "duration": '
                '"1958-01-01/2020-12-01", "interval": "1 months", "nT": 756.0, "units": "mm", '  # noqa
                '"model": NaN, "ensemble": NaN, "scenario": "total"}}'
            ),
            "grid_dict": (
                '{"aet": {"grid_id": 116.0, "X_name": "lon", "Y_name": "lat", "X1": '
                '-179.9792, "Xn": 179.9792, "Y1": 89.9792, "Yn": -89.9792, "resX": 0.0417, '  # noqa
                '"resY": 0.0417, "ncols": 8640, "nrows": 4320, "proj": "+proj=longlat '
                '+a=6378137 +f=0.00335281066474748 +pm=0 +no_defs", "toptobottom": 0.0, '
                '"tile": NaN, "grid.id": NaN}, "pet": {"grid_id": 116.0, "X_name": "lon", '  # noqa
                '"Y_name": "lat", "X1": -179.9792, "Xn": 179.9792, "Y1": 89.9792, "Yn": '
                '-89.9792, "resX": 0.0417, "resY": 0.0417, "ncols": 8640, "nrows": 4320, '
                '"proj": "+proj=longlat +a=6378137 +f=0.00335281066474748 +pm=0 +no_defs", '  # noqa
                '"toptobottom": 0.0, "tile": NaN, "grid.id": NaN}}'
            ),
            "weights": (
                '{"i":{"0":1,"1":1,"2":2,"3":2},"j":{"0":2,"1":3,"2":2,"3":3},'
                '"poly_idx":{"0":"1","1":"1","2":"1","3":"1"},'
                '"wght":{"0":0.0906272694,"1":0.001795472,"2":0.7689606915,"3":0.138616567}}'  # noqa
            ),
            "shape_file": (
                '{"type": "FeatureCollection", "features": [{"id": "0", "type": "Feature", '  # noqa
                '"properties": {"id": 1, "poly_idx": "1"}, "geometry": {"type": "Polygon", '  # noqa
                '"coordinates": [[[-70.60141212297273, 41.9262774500321], '
                "[-70.57199544021768, 41.91303994279233], [-70.5867037815952, "
                "41.87626908934851], [-70.61906213262577, 41.889506596588284], "
                "[-70.60141212297273, 41.9262774500321]]]}}]}"
            ),
            "shape_crs": "4326",
            "shape_poly_idx": "poly_idx",
            "start_date": "1980-01-01",
            "end_date": "1980-12-31",
            "numdiv": 1,
        }
    },
}


class GDPRunWeightsCatalogProcessor(BaseProcessor):  # type: ignore
    """Run area-weighted grid-to-poly aggregation."""

    def __init__(self, processor_def: dict[str, Any]):
        """Initialize Processor.

        Args:
            processor_def (_type_): _description_
        """
        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data: Dict[str, Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
        """Execute run_weights_catalog web service."""
        pdict = str(data["param_dict"])
        gdict = str(data["grid_dict"])
        wghts = str(data["weights"])
        shpfile = str(data["shape_file"])
        shpidx = str(data["shape_poly_idx"])
        sdate = str(data["start_date"])
        edate = str(data["end_date"])
        ndiv = int(data["numdiv"])
        shpcrs = str(data["shape_crs"])

        param_dict = json.loads(pdict)
        grid_dict = json.loads(gdict)
        weights = pd.DataFrame.from_dict(json.loads(wghts))
        shp_file = gpd.GeoDataFrame.from_features(json.loads(shpfile))
        shp_file.set_crs(shpcrs, inplace=True)

        LOGGER.info(f"param_dict: {param_dict}  type: {type(param_dict)}\n")
        LOGGER.info(f"grid_dict: {grid_dict} type: {type(grid_dict)}\n")
        LOGGER.info(f"weights: {weights} type: {type(weights)}\n")
        LOGGER.info(f"shp_file: {shp_file.head()} type: {type(shp_file)}\n")
        LOGGER.info(f"shp_poly_idx: {shpidx} type: {type(shpidx)}\n")
        LOGGER.info(f"start_date: {sdate} type: {type(sdate)}\n")
        LOGGER.info(f"end_date: {edate} type: {type(edate)}\n")
        LOGGER.info(f"numdiv: {ndiv} type: {type(ndiv)}\n")

        eng = RunWghtEngine()
        eng.initialize(
            param_dict=param_dict,
            grid_dict=grid_dict,
            wghts=weights,
            gdf=shp_file,
            gdf_poly_idx=shpidx,
            start_date=sdate,
            end_date=edate,
        )
        ngdf, nvals = eng.run(numdiv=ndiv)

        json_str = eng.finalize_json(gdf=ngdf, vals=nvals)

        return "application/json", json.loads(str(json_str))

    def __repr__(self):  # type: ignore
        """Return representation."""
        return f"<GDPCalcWeightsCatalogProcessor> {self.name}"
