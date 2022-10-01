"""
mundipy.cache provides spatial caches as function decorators.
"""

import geopandas as gpd
from shapely.geometry.base import BaseGeometry

def spatial_cache_footprint(fn, maxsize=128):
	"""
	Cache this function for all geometries that fit within the returned
	shape, which is this function's footprint.

	The returned value must be valid for all geometries inside the
	footprint.

	Will cache up to maxsize items in an LRU cache.

	Function must return (result, footprint).
	"""
	# list of (shape, result)
	cache = []

	def check_cache_first(*args, **kwargs):
		nonlocal cache

		# args[0] must be shapely
		if len(args) == 0 or not isinstance(args[0], BaseGeometry):
			raise TypeError('first arg passed to spatial_cache_footprint is not a shapely BaseGeometry')

		shape = args[0]
		for cache_item in cache:
			# cache hit
			if cache_item[1].contains(shape):
				return cache_item[0]

		# cache miss
		res, footprint = fn(*args, **kwargs)

		# re-order cache list to include the new hit
		cache = [(res, footprint)] + cache[:maxsize-1]

		return res

	return check_cache_first
