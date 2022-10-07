import logging
from rebel import Database, PgsqlDriver
from hashids import Hashids
import base64


class Sabi_Postgresql:
    session = None
    logger = None
    db = None
    schema = None
    private_key = None
    server = None
    lambda_client = None
    generic_hashid = None

    def __init__(self, hashid_salt, host, user, password, database, schema=None, port=5432, timezone=""):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.schema = schema
        self.generic_hashid = Hashids(salt=hashid_salt, min_length=16)

        driver = PgsqlDriver(host=host, port=int(port), database=database, user=user, password=password)
        self.db = Database(driver)
        if schema != None:
            self.db.execute(f"SET search_path TO :schema", schema=self.schema)
            self.generic_hashid = Hashids(salt=hashid_salt, min_length=16)

        if timezone != "":
            self.db.execute(f"SET TIMEZONE=:timezone; ", timezone=timezone)

    def encode(self, string):
        if string is None:
            return_value = None
        else:
            return_value = self.generic_hashid.encode(string)

        return return_value

    def decode(self, string):
        if string is None:
            return_value = None
        else:
            return_value = self.generic_hashid.decode(string)
            if len(return_value) > 0:
                return_value = return_value[0]
        return return_value

    def encode_to_base64(self, string):
        return base64.b64encode(bytes(string, "utf-8")).decode("utf-8")

    def decode_from_base64(self, string):
        base64_bytes = string.encode("ascii")
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode("ascii")
        return decoded

    def query(self, sql, params={}):
        rows = self.db.query(sql, **params)
        return rows
