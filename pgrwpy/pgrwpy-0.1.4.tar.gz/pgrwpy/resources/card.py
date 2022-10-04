from .base import Resource
from ..constants.url import URL
from ..constants.api_list import API_NAMES


class Card(Resource):
    def __init__(self, client=None):
        super(Card, self).__init__(client)

    def create(self, data={}, **kwargs):
        url = URL.CARD
        if "fullName" not in data:
            raise ValueError("MISSING REQUEST PARAMS for fullName")
        if "amount" not in data:
            raise ValueError("MISSING REQUEST PARAMS for amount")
        if type(data["amount"]) != int:
            raise ValueError("Amount should be of type integer")
        if "email" not in data:
            raise ValueError("MISSING REQUEST PARAMS for email")
        if "billingAddress" not in data:
            raise ValueError("MISSING REQUEST PARAMS for billingAddress")
        if "line1" not in data["billingAddress"]:
            raise ValueError(
                "MISSING REQUEST PARAMS for line1 in billingAddress")
        if "city" not in data["billingAddress"]:
            raise ValueError(
                "MISSING REQUEST PARAMS for city in billingAddress")
        if "country" not in data["billingAddress"]:
            raise ValueError(
                "MISSING REQUEST PARAMS for country in billingAddress")
        if "state" not in data["billingAddress"]:
            raise ValueError(
                "MISSING REQUEST PARAMS for state in billingAddress")
        if "postal_code" not in data["billingAddress"]:
            raise ValueError(
                "MISSING REQUEST PARAMS for postal_code in billingAddress")
        if "physical" not in data:
            raise ValueError("MISSING REQUEST PARAMS for physical")
        if "person" not in data:
            raise ValueError("MISSING REQUEST PARAMS for person")
        body = {
            "amount": data["amount"],
            "email": data["email"],
            "isPrepaid":  data["prepaid"],
            "fullName": data["fullName"],
            "amount": data["amount"],
            "email": data["email"],
            "billingAddress": {
                "line1": data["billingAddress"]["line1"],
                "city": data["billingAddress"]["city"],
                "country": data["billingAddress"]["country"],
                "state": data["billingAddress"]["state"],
                "postal_code": data["billingAddress"]["postal_code"]
            },
            "isPhysical": data["physical"],
            "person": data["person"]
        }
        return self.post_url(url, body, api_id=API_NAMES.CREATE_CARD, **kwargs)

    def get_card_details(self, cardId, cardHolderId, **kwargs):
        url = "{}?cardId={}&cardHolderId={}".format(
            URL.CARD, cardId, cardHolderId)
        if cardId is None:
            raise ValueError("MISSING REQUESTS PARAMS for cardId")
        if cardHolderId is None:
            raise ValueError("MISSING REQUESTS PARAMS for cardHolderId")
        return self.fetch(None, url, None, api_id=API_NAMES.GET_CARD_DETAIL, **kwargs)

    def get_all_cards(self, cardHolderId, **kwargs):
        url = "{}/all?cardHolderId={}".format(URL.CARD, cardHolderId)
        if cardHolderId is None:
            raise ValueError("MISSING REQUESTS PARAMS for cardHolderId")
        return self.fetch(None, url, None, api_id=API_NAMES.GET_ALL_CARD, **kwargs)

    # def delete_card(self, id=None, **kwargs):
    #     if id is None:
    #         raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
    #                          " \x1b[0m for codeId")
    #     url = "{}/{}".format(self.base_url, id)
    #     return self.delete(None, url, api_id=API_NAMES.DELETE_CARD, **kwargs)
