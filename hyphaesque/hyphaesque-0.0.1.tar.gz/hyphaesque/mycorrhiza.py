from .data_util import DataConnection, new_id_str


class Hypha:
    def __init__(self):
        self.data_conn = None

    def open_data_conn(self):
        self.data_conn = DataConnection()
