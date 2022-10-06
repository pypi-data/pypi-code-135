from flask import Flask
from importlib import import_module


class FlaskGeo:

    def __init__(self, app: Flask = None, db = None):
        if app is not None:
            self.init_app(app, db)

    def init_app(self, app: Flask, db):
        app.flask_geo = self
        self.db = db
        import_module('flask_geo.database').init_app(app)
        import_module('flask_geo.api').init_app(app)
