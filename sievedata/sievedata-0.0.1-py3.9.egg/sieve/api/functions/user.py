"""
User related helper for Sieve API
"""

from ...types.api import SieveUser
from ..utils import get
from ..constants import API_URL, API_BASE, USER_API_KEY, USER_NAME

def info() -> SieveUser:
    """
    Get user info
    """
    res = get(f'{API_URL}/{API_BASE}/user')
    if res.status_code == 200:
        res_json = res.json()
        slug = res_json[USER_NAME]
        api_key = res_json[USER_API_KEY]
        return SieveUser(slug, api_key)
    else:
        try:
            res_json = res.json()
            raise Exception(res_json['description'])
        except:
            raise Exception(f'Error: {res.status_code} {res.text}')
