from uuid import uuid4
from base58 import b58encode
from couchdblink import server_functions as sfn


def new_id_str() -> str:
    u_id = uuid4()
    id_str = b58encode(u_id.bytes).decode()
    return id_str


class DataConnection:
    def __init__(self):
        self.server = sfn.get_couchdb_connection()
