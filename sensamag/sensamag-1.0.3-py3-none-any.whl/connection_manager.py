"""
Connection wrapper.
"""
import mariadb
from rich import print as rprint

DEFAULT_USER = "sensamag_utility"
DEFAULT_PASSWORD = "verystrongpassword"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 3308
DEFAULT_DATABASE = "sensamag_sp"


class ConnectionManager:
    """
    Class-wrapper for a connection to MariaDB.
    """

    def __init__(self):
        self.user = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.database = DEFAULT_DATABASE

    def reset_connection(self) -> None:
        """
        Reset connection string to default values.
        """
        self.user = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.database = DEFAULT_DATABASE

    # pylint: disable=too-many-arguments
    def set_connection(
        self,
        user: str = None,
        password: str = None,
        host: str = None,
        port: int = None,
        database: str = None,
    ) -> None:
        """
        Set connection string parameters for next connection.

        :param user: username
        :param password: password
        :param host: ip of database server
        :param port: port of database server
        :param database: name of database
        """
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if database is not None:
            self.database = database

    def print_params(self) -> None:
        """
        Print current connection string to console.
        """
        rprint(
            f"""
        | > User: {self.user}
        | > Password: {self.password}
        | > Host: {self.host}
        | > Port: {self.port}
        | > Database: {self.database}
        """
        )

    def get_connection(self) -> mariadb.Connection:
        """
        Create and return connection to mariadb.
        :return: active connection to MariaDB.
        """
        rprint("> [bold yellow]New connection parameters:")
        self.print_params()
        try:
            conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )
            rprint("> [bold green]Connected successfully!")
            return conn
        except mariadb.Error as exception:
            raise Exception(
                "Error connecting to MariaDB, check connection params."
            ) from exception
