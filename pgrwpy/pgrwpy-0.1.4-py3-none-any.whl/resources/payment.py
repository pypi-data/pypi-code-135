from .base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Payment(Resource):
    def __init__(self, client=None):
        super(Payment, self).__init__(client)

    def moncash(self, data={}, **kwargs):
        url = URL.MONCASH
        if "referenceId" not in data:
            raise ValueError("MISSING REQUEST PARAMS for referenceId")
        if "successUrl" not in data:
            raise ValueError("MISSING REQUEST PARAMS for successUrl")
        if "errorUrl" not in data:
            raise ValueError("MISSING REQUEST PARAMS for errorUrl")
        if "amount" not in data:
            raise ValueError("MISSING REQUEST PARAMS for amount")
        if type(data["amount"]) != int:
            raise ValueError("Amount should be of type integer")
        body = {
            "gdes": data["amount"],
            "userID": self.client.auth[0],
            "referenceId": data["referenceId"],
            "successUrl":  data["successUrl"],
            "errorUrl":  data["errorUrl"]
        }
        return self.post_url(url, body, api_id=API_NAMES.CREATE_PAYMENT_MONCASH, **kwargs)

    def get_payment_details(self, orderId, **kwargs):
        url = "{}{}".format(URL.ORDER, orderId)
        if orderId is None:
            raise ValueError("MISSING REQUEST PARAMS for orderId")
        return self.fetch(None, url, None, api_id=API_NAMES.GET_PAYMENT, **kwargs)
