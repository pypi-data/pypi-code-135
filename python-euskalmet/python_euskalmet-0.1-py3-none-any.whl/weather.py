from euskalmet import Euskalmet
import configparser
import datetime
import json
import os
from functools import partial
from multiprocessing import Pool
from pathlib import Path
from typing import Union

import jwt
import numpy as np
import pandas as pd
import pytz
import requests
from tqdm import tqdm

from exceptions import EuskalmetException

class Weather(Euskalmet):
    def __init__(self, location):
        super().__init__()
        self.location = location

    def get_weather(self):
        return self.get_data(self.location)