import logging

BASEURL = "https://pv.inteless.com"

API_TIMEOUT = 10

LOG_LEVEL = logging.INFO

DEGREE_CELSIUS = "°C"
WATT = "W"
KWATT = "kW"
WATT_HOUR = "Wh"
KWATT_HOUR = "kWh"
AMPERE = "A"
AMPEREHOUR = "Ah"
VOLT = "V"
PERCENT = "%"
HERTZ = "Hz"
PER_KILOWATTHOUR = "{}/kWh"

APIHEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Cache-Control": "no-cache",
    "Origin" : "https://sunsynk.net",
    "Referrer" : "https://sunsynk.net"
}