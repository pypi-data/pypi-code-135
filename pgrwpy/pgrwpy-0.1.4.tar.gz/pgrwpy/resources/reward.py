from .base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Reward(Resource):
    def __init__(self, client=None):
        super(Reward, self).__init__(client)

    def send(self, data={}, **kwargs):
        url = URL.REWARD
        if "email" not in data:
            raise ValueError("MISSING REQUEST PARAMS for email")
        if "prepaid" not in data:
            raise ValueError("MISSING REQUEST PARAMS for prepaid")
        if "amount" not in data:
            raise ValueError("MISSING REQUEST PARAMS for amount")
        if type(data["amount"]) != int:
            raise ValueError("Amount should be of type integer")
        body = {
            "amount": data["amount"],
            "email": data["email"],
            "isPrepaid":  data["prepaid"],
        }
        return self.post_url(url, body, api_id=API_NAMES.SEND_REWARD, **kwargs)
