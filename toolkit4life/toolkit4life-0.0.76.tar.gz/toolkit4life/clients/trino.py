# Third-party imports
from toolkit4life.db.clients.sqlalchemy import SQLAlchemy


class TrinoClient(SQLAlchemy):

    def __init__(self, host: str, port: str, catalog: str, schema: str, username: str, password: str) -> None:
        """
            Creates and initializes a PostgreSQL engine instance that connects to the database

            Parameters:
                host (str): Host IP address
                port (str): Port number
                catalog (str): Database name
                schema (str): Schema name
                username (str): Username for authentication/privileges
                password (str): Password for authentication
        """
        super().__init__(engine = "trino", host = host, port = port, catalog = catalog, schema = schema, username = username, password = password)