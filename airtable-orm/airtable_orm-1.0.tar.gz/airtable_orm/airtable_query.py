import requests
from dataclasses import dataclass


@dataclass
class IBase:
    pass


class AirtableQuery:
    def __init__(self, api_url, header, entity: IBase):
        self.api_url = api_url
        self.header = header
        self.entity = entity

    def all(self):
        print(f'========{self.api_url}')
        res = requests.get(
            self.api_url,
            headers=self.header,
        )
        return self.output(res.json()["records"])

    def output(self, all_data: list):
        res = []
        for data in all_data:
            d = {}
            for key in self.entity.__dataclass_fields__:
                if key in data['fields']:
                    d[key] = data['fields'][key]
                else:
                    d[key] = None
                d['id'] = data['id']
            new_data = self.entity(**d)
            print(new_data)
            res.append(new_data)
        return res