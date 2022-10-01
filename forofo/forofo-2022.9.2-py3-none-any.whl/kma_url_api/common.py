from datetime import datetime, timedelta
import re
import os
import random
from clutter.aws import get_secrets
from clutter.logging import logger

BASE_URL = "http://203.247.66.126:8090/url"
API_KEY = ["woojin.cho@gmail.com"]

# 사용 가능한 수치모델
# key: url path, value: 해당 url path에 속한 수치모델
NWP = {
    "KIM": ["kim_g120", "kim_g128", "kim_g512"],
    "UMGL": ["g100", "g120", "g128", "g512", "g768"],
    "UMKR": ["l015"],
}

# KMA_URL_API의 ERROR NOTICE
ERROR_NOTICES = [
    "The number of requests has reached the limit",  # rate limit
    "The authKey is invalid",  # auth failed
]

# SECRETS_NAME
SECRETS_NAME = os.getenv("SM_API_KEY", "common/kma-url-api")

# Load API Key for Dev.
try:
    secrets = get_secrets(SECRETS_NAME)
    API_KEY = secrets.get("eugene")
except Exception as ex:
    logger.warning("no aws credential, you have only 1 api key!")
    pass

# Cyclic Api Key
# [NOTE]
#  - 한 API KEY는 1일 1,000회만 호출 가능
#  - 10분마다 지난 1일의 다운로드 가능한 URL 조회 -> 8 * 144 = 1,152회
#  - 0, 6, 12, 18시 49개 파일, 3, 9, 15, 21시 5개 파일 다운로드 -> 216회
#  - 1일 약 1,400번의 Key 사용 ~ 여러 Key 돌아가면서 사용해야 함
class CyclicApiKey:
    def __init__(self, randomly: bool = True):
        # props
        self.randomly = randomly
        secrets = get_secrets(SECRETS_NAME)
        self.apiKeys = [v for k, v in secrets.items()]

        # store
        self.n_keys = len(self.apiKeys)
        self.offset = 0

    def __call__(self):
        if self.randomly:
            return random.choice(self.apiKeys)
        self.offset = (self.offset + 1) % self.n_keys
        return self.apiKeys[self.offset]


def generate_filepath_from_url(url, delim="/"):
    filename = None
    query = url.split("?")[-1].split("&")
    for q in query:
        if q.startswith("file="):
            filename = q.split("=")[-1]
    assert filename is not None

    prefix = datetime.strptime(filename.split(".")[1], "%Y%m%d%H").strftime(f"%Y__%m__%d__%H__")
    return (prefix + filename).replace("__", delim)


# generate update datetimes
def generate_update_datetimes(start: datetime, end: datetime = None):
    OFFSET_HOUR = 0
    STEP_HOUR = 3

    dates = []

    # correct start datetime
    for _ in range(STEP_HOUR):
        if start.hour % STEP_HOUR == OFFSET_HOUR:
            dates += [start]
            break
        start += timedelta(hours=1)

    # parser end
    if end is not None:
        while True:
            date = dates[-1] + timedelta(hours=STEP_HOUR)
            if date > end:
                break
            dates += [date]

    return dates
