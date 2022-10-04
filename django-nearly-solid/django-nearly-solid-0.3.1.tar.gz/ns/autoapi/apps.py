from ns.application_layer.apps import NSAppConfig


class AutoApiConfig(NSAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ns.autoapi'
