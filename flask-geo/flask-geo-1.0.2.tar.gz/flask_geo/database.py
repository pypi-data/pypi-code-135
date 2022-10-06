from flask import Flask
from sqlalchemy.orm import Session

db = None
session = None

def init_app(app: Flask) -> None:
    global db, session
    db = app.flask_geo.db
    session = Session(db)
