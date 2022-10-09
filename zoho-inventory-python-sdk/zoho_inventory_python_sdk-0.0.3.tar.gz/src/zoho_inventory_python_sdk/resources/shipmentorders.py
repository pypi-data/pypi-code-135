from ..client import Client


'''
TODO: Override or refactor Client methods create and update to accept query parameters.
'''


class ShipmentOrders(Client):
    def __init__(self, **opts):
        super(ShipmentOrders, self).__init__(**{**opts, **{"resource": "shipmentorders"}})

    def mark_as_delivered(self, id_: str = ""):
        return self.authenticated_fetch(path=f"{id_}/status/delivered/",
                                        req={
                                            "method": "POST"
                                        },
                                        mimetype="application/x-www-form-urlencoded",
                                        )
