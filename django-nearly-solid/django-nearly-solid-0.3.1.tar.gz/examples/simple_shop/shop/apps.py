from ns.autoapi.apps import AutoApiConfig


class ShopConfig(AutoApiConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
