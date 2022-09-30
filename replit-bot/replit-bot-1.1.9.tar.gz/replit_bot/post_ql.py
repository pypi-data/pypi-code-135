"""file that handles posting to replit graphql endpoint for queries and mutations"""

import json
from requests import post as _post, get as _get, delete as _delete
from typing import Dict, Any
from .queries import q
from .colors import green, end, purple, red, bold_green, bold_blue, blue
from time import sleep
import logging
import random

backup = "https://graphql-playground.pikachub2005.repl.co/"
endpoint = "https://replit.com/graphql"
headers = {
    "X-Requested-With": "replit",
    'Origin': 'https://replit.com',
    'Accept': 'application/json',
    'Referrer': 'https://replit.com',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Host': "replit.com",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
}
number_convert = ["1st", "2nd", "3rd", "4th", "5th"]


def post(connection: str,
         query: str,
         vars: Dict[str, Any] = {},
         raw: bool = False):
    """post query with vars to replit graph query language"""
    _headers = headers
    _headers["Cookie"] = f"connect.sid={connection}"

    class InitialRequest:

        def __init__(self):
            self.status_code = 429
            self.text = ""

    req = InitialRequest()
    number_of_attempts = 0
    while req.status_code == 429 and number_of_attempts < 5:  # only try 5 times
        current_endpoint = f"{endpoint}?e={int(random.random() * 100)}"
        req = _post(current_endpoint,
                    json={
                        "query": (query if raw else q[query]),
                        "variables": vars,
                    },
                    headers=_headers)
        if (req.status_code == 429):
            number_of_attempts += 1
            logging.warning(
                f"{green}[FILE] POST_QL.py{end}\n{red}[WARNING]{end}\n\t{red}[INFO]{end} You have been ratelimited\n\t{bold_blue}[SUMMARY]{end} Retrying query for the {number_convert[number_of_attempts]} time (max retries is 5)\n\t{purple}[EXTRA]{end}\n\t\t{bold_blue}"
            )
            sleep(
                5 * (number_of_attempts)
            )  # as not to overload the server, the sleep time increases per num attempts
            continue
        if (req.status_code == 200):
            vars_max = 200
            query_max = 100
            _query = query
            _vars = f" {vars}" if (
                len(json.dumps(vars, indent=8)) + 3 >= vars_max
                or len(vars) <= 1
            ) else f"\n\t\t\t{json.dumps(vars, indent=16)[:-1]}\t\t\t" + '}'
            if (len(_vars) >= vars_max): _vars = _vars[:vars_max - 3] + '...'
            if (len(_query) >= query_max):
                _query = _query[:query_max - 3] + '...'
            logging.info(
                f"{green}[FILE] POST_QL.py{end}\n{green}[INFO]{end} {bold_green}Successful graphql!{end}\n\t{blue}[SUMMARY]{end} queried replit's graphql with these query and vars.\n\t{purple}[EXTRA]{end}\n\t\t{bold_blue}[QUERY]{end} {query}\n\t\t{bold_blue}[VARS]{end}{_vars}\n\t\t{bold_blue}[RAW QUERY]{end} {raw}\n\t\t{bold_blue}[URL END POINT]{end} {current_endpoint}"
            )
        else:
            return logging.error(
                f"{red}[FILE] POST_QL.py{end}\n{red}[STATUS CODE] {req.status_code}\n\t{purple}[EXTRA]{end} {req.text}"
            )
        res = json.loads(req.text)
        try:
            _ = list(map(lambda x: x["data"], list(res["data"])))
            return _
        except:
            if ('data' in res['data']):
                return res["data"]["data"]
            else:
                return res["data"]