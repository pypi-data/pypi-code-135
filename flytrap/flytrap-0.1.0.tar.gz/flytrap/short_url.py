import httpx

# https://dev.bitly.com - маст

# http://yourls.org/#About
# https://developer.hootsuite.com/docs/owly-api-reference

import json

linkRequest = {
  "destination": "https://www.youtube.com/channel/UCHK4HD0ltu1-I212icLPt3g"
  , "domain": { "fullName": "rebrand.ly" }
# , "slashtag": "A_NEW_SLASHTAG"
# , "title": "Rebrandly YouTube channel"
}

requestHeaders = {
  "Content-type": "application/json",
  "apikey": "YOUR_API_KEY",
  "workspace": "YOUR_WORKSPACE_ID"
}

r = httpx.post("https://api.rebrandly.com/v1/links",
    data = json.dumps(linkRequest),
    headers=requestHeaders)

if (r.status_code == httpx.codes.ok):
    link = r.json()
    print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))


# ==============================
import requests

headers = {
    'Authorization': 'Bearer {TOKEN}',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://dev.bitly.com", "domain": "bit.ly", "group_guid": "Ba1bc23dE4F" }'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)


# Удалить ссылку:
response = requests.delete('https://api-ssl.bitly.com/v4/bitlinks/bit.ly/12a4b6c', headers=headers)
