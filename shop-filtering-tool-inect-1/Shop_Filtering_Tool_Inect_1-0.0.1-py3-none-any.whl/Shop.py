import csv
import requests
import xmltodict
import unicodedata
import warnings
import os
import copy
import pandas
from bs4 import BeautifulSoup
try:
    from Record import Record
except ModuleNotFoundError:
    from shop.Record import Record

try:
    import Parsers
except ModuleNotFoundError:
    import shop.Parsers as Parsers

warnings.filterwarnings('ignore')


def handle_nested_dicts(di: dict) -> dict:
    def is_nested(d: dict):
        for val in d.values():
            if isinstance(val, dict):
                return True
        return False
    if not is_nested(di):
        return di
    list_of_keys = list(copy.copy(di))
    for key in list_of_keys:
        if isinstance(di[key], dict):
            temp = handle_nested_dicts(di[key])
            for i in temp:
                di[str(key) + str(i)] = temp[i]
            del di[key]
    return di


def dfs(graph: dict, target_key) -> list:
    results = []

    if not isinstance(graph, dict):
        return []

    if target_key in graph:
        if isinstance(graph[target_key], list):
            return graph[target_key]
        else:
            return [graph[target_key]]

    for key in graph:
        if len(dfs(graph[key], target_key)) > 0:
            results += dfs(graph[key], target_key)
    return results


#  the main point of class Shop is it being container for items
#   which are represented as Record which inherits from dict
class Shop(list):
    # init
    def __init__(self):
        super().__init__(self)
        self.all_keys = set()

    def get_keys(self):
        return self.all_keys

    def unify(self) -> None:
        for i in self:
            for key in self.all_keys:
                if key not in i:
                    i[key] = ''

    def normalize(self) -> None:
        for i in self:
            for key in i:
                i[key] = str(i[key])
                i[key] = unicodedata.normalize('NFKD', i[key])

    # init
    @staticmethod
    def from_list(lst):
        self = Shop()
        self.all_keys = set()
        for i in lst:
            if isinstance(i, dict):
                self.append(Record.from_dict(i, Parsers.default))
                self.all_keys.update(i.keys())
        return self

    # init
    @staticmethod
    def from_url(url, interesting_tags=None):
        if interesting_tags is None:
            interesting_tags = {'item'}

        # setup
        self = Shop()
        response = requests.get(url)
        data = xmltodict.parse(response.content)
        items = []
        for tag in interesting_tags:
            items += dfs(data, tag)
        self.all_keys = set()
        items = [handle_nested_dicts(i) for i in items]

        for i in items:
            for key in i:
                if isinstance(i[key], str):
                    string = unicodedata.normalize("NFKD",
                                                   BeautifulSoup(i[key], features="html.parser").get_text())
                    i[key] = string.replace('\n', ' ').replace('\t', ' ')
            list_of_keys = list(i.keys())

            for key in list_of_keys:
                if key[:2] == 'g:':
                    i[key[2:]] = i[key]
                    del i[key]
            self.all_keys.update(i.keys())
            self.append(Record.from_dict(i, Parsers.default))
        return self

    # init
    @staticmethod
    def from_csv(input_file=None):
        if input_file is None:
            return Shop()

        df = pandas.read_csv(input_file, na_filter=False)
        list_of_items = df.to_dict('records')
        self = Shop.from_list(list_of_items)
        self.normalize()
        return self

    @staticmethod
    def print_to_csv(shop, output_file=None):
        shop.unify()
        if output_file is None:
            output_file = 'output.csv'

        try:
            os.remove(output_file)
            print('removing old output file')
        except OSError:
            pass

        with open(output_file, "w", encoding='UTF-8', newline='') as csvfile:
            categories = list(shop.all_keys)
            categories.sort()
            writer = csv.DictWriter(csvfile, fieldnames=categories)
            writer.writeheader()
            for i in shop:
                writer.writerow(i)

    @staticmethod
    def unify_shops(shop1, shop2):
        all_keys = shop1.get_keys()
        all_keys.update(shop2.get_keys())
        shop1.all_keys.update(all_keys)
        shop2.all_keys.update(all_keys)
        shop1.unify()
        shop2.unify()

    @staticmethod
    def differences(shop1, shop2, out=None):
        # shop1 is new, shop2 is old
        if out is None:
            out = 'console'
        shop1_exclusive = Shop()
        shop2_exclusive = Shop()

        j = len(shop1) + len(shop2)
        ctr = 0

        for i in shop1:
            print(f'{ctr}/{j}')
            ctr += 1
            if i not in shop2:
                shop1_exclusive.append(i)
                shop1_exclusive.all_keys.update(i.keys())

        for i in shop2:
            print(f'{ctr}/{j}')
            ctr += 1
            if i not in shop1:
                shop2_exclusive.append(i)
                shop2_exclusive.all_keys.update(i.keys())

        if out == 'console':
            print('New items:')
            for i in shop1_exclusive:
                print(i)
            print('Retired items')
            for i in shop2_exclusive:
                print(i)

        if out == 'file':
            try:
                os.makedirs('comparison_results')
            except OSError:
                pass
            Shop.unify_shops(shop1_exclusive, shop2_exclusive)
            Shop.print_to_csv(shop1_exclusive, 'comparison_results/new_items.csv')
            Shop.print_to_csv(shop2_exclusive, 'comparison_results/retired_items.csv')


def test():
    #  a = Shop.from_url("https://magazynuj.pl/pliki/get/integracja2022/google.xml")
    b = Shop.from_csv('output.csv')
    for i in b:
        print(i)


if __name__ == '__main__':
    test()