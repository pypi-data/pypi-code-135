# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pygeofun']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pygeofun',
    'version': '0.0.5',
    'description': 'Geographic Functions: geodesics and rhumblines, orthodromes and loxodromes',
    'long_description': "# GeoFun\n\nLibrary for doing geographic calculations like distance, azimuth and position determination\nfor geodesics and rhumb lines, orthodromes and loxodromes, respectively.\n\nThis version makes use of GeographicLib for doing most of the calculations.\n\nThis is a C++ package that uses pybind11 to wrap the C++ version of GeographicLib, which\nmakes it faster (~100x) than the pure python version of [geographiclib](https://geographiclib.sourceforge.io/html/python/index.html).\n\nCompare:\n```Python\nIn [1]: from geofun import geodesic_inverse\n\nIn [2]: %timeit geodesic_inverse(52, 4, 28, -16.6)\n1.17 µs ± 37 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)\n\nIn [3]: from geographiclib.geodesic import Geodesic\n\nIn [4]: %timeit Geodesic.WGS84.Inverse(52, 4, 28, -16.6)\n107 µs ± 170 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n\nIn [5]: geodesic_inverse(52, 4, 28, -16.6)\nOut[5]: (-139.28471885516532, 3168557.154495447, -152.90624110350674)\n\nIn [6]: Geodesic.WGS84.Inverse(52, 4, 28, -16.6)\nOut[6]:\n{'lat1': 52,\n 'lon1': 4.0,\n 'lat2': 28,\n 'lon2': -16.6,\n 'a12': 28.519118381735783,\n 's12': 3168557.1544954455,\n 'azi1': -139.28471885516532,\n 'azi2': -152.90624110350674}\n```\n\n## Building\n\n-   Get\n    [poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)\n    if you don\\'t have it\n\n-   Check out the source code:\n    `git clone https://github.com/jrversteegh/geofun.git --recurse-submodules`\n\n-   Execute `poetry build` to build the package or `poetry install` to get a virtual environment \n    to work in. Both require a working modern C++ compiler. GCC 9.4 and MSVC 14.3 were tested. \n    Others may work.\n\n\n## Examples\n\nSome operator abuse was used to mark the difference between geodesic and mercator based operations.\n`+` and `-` are addition and subtraction in the mercator projection (loxodromes) and `*` and `/`\nare addition and subtraction on geodesics (orthodromes). If you object to this, you're probably\nright. Any suggestions for a better way are quite welcome.\n\n```python\nfrom geofun import Position, Vector\n\n# Just off Hoek van Holland\norg = Position(52.0, 4.0)\nnm95 = 95 * 1852.0\n\n# Go west 95 nm to Felixstowe\nrmbv = Vector(270.0, nm95)\npos1 = org + rmbv\n\n# Go to the same point using great circle line\ngcv = pos1 / org\npos2 = org * gcv\n\n# We should end up at the same location\nassert pos1 == pos2\n\n# How disappointing: we managed to gain just 9m by crossing the\n# North sea using a great circle :p\nassert nm95 - gcv.length == 9.101067085022805, f'Unexpected: {gcv.length}'\n\nprint(f'From {org} to {pos1}')\nprint(f'Rhumb: {rmbv}')\nprint(f'Great circle: {gcv}')\n\n# Another verification\nassert pos1 - org == rmbv\nassert pos1 / org == gcv\n```\n\n## Classes\n\nPosition\n - latitude\n - longitude\n\nVector\n - azimuth\n - length\n\nPoint\n - x\n - y\n\n## Functions\n\n`get_version() -> str`\n\n   Get the library version\n\n`geodesic_direct(latitude: float, longitude: float, azimuth: float, distance: float) -> tuple`\n\n   Get position and final azimuth after moving distance along great circle with starting azimuth\n\n`geodesic_inverse(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> tuple`\n\n   Get starting azimuth, distance and ending azimuth of great circle between positions\n\n`rhumb_direct(latitude: float, longitude: float, azimuth: float, distance: float) -> tuple`\n\n   Get position and final azimuth after moving distance from starting position at fixed azimuth/along rhumb line\n\n`rhumb_inverse(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> tuple`\n\n   Get rhumb line azimuth, distance and final azimuth between positions\n\n`angle_diff(arg0: numpy.ndarray[numpy.float64], arg1: numpy.ndarray[numpy.float64]) -> object`\n\n   Signed difference between to angles\n\n`angle_mod(arg0: numpy.ndarray[numpy.float64]) -> object`\n\n   Return angle bound to [0.0, 360.0>\n\n`angle_mod_signed(arg0: numpy.ndarray[numpy.float64]) -> object`\n\n   Return angle bound to [-180.0, 180.0>\n",
    'author': 'Jaap Versteegh',
    'author_email': 'j.r.versteegh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jrversteegh/geofun',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
