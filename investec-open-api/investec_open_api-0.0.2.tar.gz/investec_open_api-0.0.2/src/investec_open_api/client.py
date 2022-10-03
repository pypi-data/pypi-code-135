import requests
import datetime

class InvestecClient:

  url = 'https://openapi.investec.com'
  auth_token = ''
  expires_at = datetime.datetime.now()

  def __init__(self, client_id, secret):
    self.client_id = client_id
    self.secret = secret

  def get_token(self) -> dict:
      url = f'{self.url}/identity/v2/oauth2/token'
      
      headers = {"Accept": "application/json"}
      headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
      
      response = requests.post(
        url,
        auth=requests.auth.HTTPBasicAuth(self.client_id, self.secret),
        headers=headers,
        data="grant_type=client_credentials&scope=accounts"
      )
      response = response.json()
      self.auth_token = response['access_token']
      self.expires_at = datetime.datetime.now() + datetime.timedelta(seconds=response['expires_in'])
      return response

  def get_accounts(self)-> dict:
      url = f'{self.url}/za/pb/v1/accounts'
      return self.query_api_get(url)['accounts']

  def get_account_balance(self, account_id) -> dict:
      url = f'{self.url}/za/pb/v1/accounts/{account_id}/balance'
      return self.query_api_get(url)

  def get_account_transactions(self, account_id) -> dict:
      url = f'{self.url}/za/pb/v1/accounts/{account_id}/transactions'
      return self.query_api_get(url)['transactions']

  def transfer(self, account_id, beneficiary, amount) -> dict:
      data = f'beneficiaryAccountId={beneficiary}&amount={amount}&myReference=API transfer&theirReference=API transfer'
      url = f'{self.url}/za/pb/v1/accounts/{account_id}/transactions'
      return self.query_api_post(url, data)

  def get_countries(self) -> dict:
      url = f'{self.url}/za/v1/cards/countries'
      return self.query_api_get(url)['result']

  def get_currencies(self) -> dict:
      url = f'{self.url}/za/v1/cards/currencies'
      return self.query_api_get(url)['result']

  def get_merchants(self) -> dict:
      url = f'{self.url}/za/v1/cards/merchants'
      return self.query_api_get(url)['result']

  def query_api_get(self, url) -> dict:
    expiry = datetime.datetime.now() + datetime.timedelta(seconds=360)
    if self.auth_token == '' or self.expires_at < expiry:
      print('fetching new token')
      self.get_token()

    headers = {
        'Authorization': 'Bearer ' + self.auth_token,
        'Accept': 'application/json'
        }
    response = requests.get(url,headers=headers)
    return response.json()['data']

  def query_api_post(self, url, data) -> dict:
    headers = {
        'Authorization': 'Bearer ' + self.auth_token,
        'Accept': 'application/json'
        }
    response = requests.post(url,headers=headers, data=data)
    print(response.json())
    return response.json()