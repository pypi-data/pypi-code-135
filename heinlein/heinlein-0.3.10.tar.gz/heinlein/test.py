from heinlein import load_dataset

from astropy.coordinates import SkyCoord
import astropy.units as u
radius = 120*u.arcsec
hsc = load_dataset("hsc")
lens_data = hsc.cone_search((341.39128815, 3.73235916), radius,dtypes=["catalog", "mask"])
print(lens_data)