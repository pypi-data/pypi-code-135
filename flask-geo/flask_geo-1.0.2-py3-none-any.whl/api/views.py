from flask import Blueprint, jsonify, abort, Response

from flask_geo.repositories import CountryRepository

bp = Blueprint('flask_geo_api', __name__, url_prefix='/api/v1')


@bp.get('/cities/<string:country_code>')
def cities(country_code) -> Response:
    country = CountryRepository().get_by_code(country_code)
    if country:
        return jsonify([city.name for city in country.cities])
    return abort(404)
