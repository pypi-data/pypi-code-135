# -*- coding: utf-8 -*-
import json


class ResourceMap:
    def __init__(self):
        self.__map = dict()
        self.__total_map = dict()
        self.__total_set = set()

    def get_map(self):
        return self.__map

    def __getitem__(self, index):
        if index == "_total":
            for key in self.__map:
                self.__total_map.update(self.__map[key])
            return self.__total_map
        else:
            # if index not in self.__map:
            #     self.__map[index] = dict()
            #     return self[index]

            return self.__map[index]

    def __setitem__(self, index, value):
        self.__map[index] = value
        if type(value) is dict:
            self.__total_map.update(value)
        elif type(value) is set:
            self.__total_set.update(value)

    def __str__(self):
        return json.dumps(self.__map, indent=4)
