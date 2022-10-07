# -*- coding: utf-8 -*-
# Origin : Target ID를 Map으로 수집
import json
from .resource_map import ResourceMap


class ResultMap:
    map = ResourceMap()

    def __init__(self):
        pass

    def print_map(self):
        print(self.map.__str__())
        pass
