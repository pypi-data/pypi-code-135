from fastapi import FastAPI

from fief.app import app as fief_app
from fief_cloud.cloud import app as cloud_app

app = FastAPI(openapi_url=None)

app.mount("/cloud", cloud_app)
app.mount("/", fief_app)
