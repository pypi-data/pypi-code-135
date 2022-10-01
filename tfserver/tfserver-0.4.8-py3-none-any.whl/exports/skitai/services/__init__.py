from . import management
from . import predict

def __setup__ (context, app, opts):
    app.mount ('/', predict)
    app.mount ('/', management)
