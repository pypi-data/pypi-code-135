from dataclasses import asdict, dataclass
import requests, json
from airtable_orm.airtable_query import AirtableQuery

@dataclass
class IBase:
    pass


class AirtableSession:
    def __init__(self, api_key, app_key, table_name = None):
        self.api_key = api_key
        self.app_key = app_key
        self.table_name = table_name
        self.data = []

    def get_api_url(self, table_name):
        self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        return f"https://api.airtable.com/v0/{self.app_key}/{table_name}"

    @staticmethod
    def __get_table_name(entity: IBase):
        tbl_name = entity.__class__.__name__
        if tbl_name == "type":
            tbl_name = entity.__doc__.split("(")[0]
        return tbl_name.lower()

    def add(self, entity: IBase):
        self.table_name = self.__get_table_name(entity)
        print(f"Writing to table: {self.table_name}")
        entity.id = 1
        self.data.append(
            {"fields": asdict(entity)}
        )

    def query(self, entity):
        print(f"========{entity}")
        self.table_name = self.__get_table_name(entity)
        print(f"========={self.table_name}")
        return AirtableQuery(
            api_url = self.get_api_url(self.table_name),
            header = self.headers,
            entity = entity
        )
        
            

    def commit(self):
        print(self.get_api_url(self.table_name))
        print({"records": self.data})
        res = requests.post(
            self.get_api_url(self.table_name),
            data=json.dumps({"records": self.data}),
            headers=self.headers
        )
        print(res)

    def flush(self):
        print("Returning")

