from heinlein import load_dataset

from astropy.coordinates import SkyCoord
import astropy.units as u
radius = 120*u.arcsec
hsc = load_dataset("cfht")
c = SkyCoord('02 08 33.10','-07 14 14.1', unit=("hourangle", "deg"))
lens_data = hsc.cone_search(c, radius,dtypes=["catalog", "mask"]),
print(lens_data)