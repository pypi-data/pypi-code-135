import requests

url = 'https://openapi.investec.com/'

def get_token(client_id, secret, url) -> dict:
    new_url = url + "identity/v2/oauth2/token"
    
    headers = {"Accept": "application/json"}
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
    
    response = requests.post(
        new_url,
        auth=requests.auth.HTTPBasicAuth(client_id, secret),
        headers=headers,
        data="grant_type=client_credentials&scope=accounts"
    )
    return response.json()

def get_accounts(auth_token, url)-> dict:
    new_url = url + 'za/pb/v1/accounts'
    return query_api_get(auth_token, new_url)

def get_account_balance(auth_token, account_id, url) -> dict:
    new_url = url + 'za/pb/v1/accounts/' + account_id + '/balance'
    return query_api_get(auth_token, new_url)

def get_account_transactions(auth_token, account_id, url) -> dict:
    new_url = url + 'za/pb/v1/accounts/' + account_id + '/transactions'
    return query_api_get(auth_token, new_url)

def transfer(auth_token, account_id, beneficiary, amount, url) -> dict:
    data = "beneficiaryAccountId="+ beneficiary +"&amount=" + amount + "&myReference=API transfer&theirReference=API transfer"
    new_url = url + 'za/pb/v1/accounts/' + account_id + '/transactions'
    return query_api_post(auth_token, new_url, data)

def get_countries(auth_token, url) -> dict:
    new_url = url + 'za/v1/cards/countries'
    return query_api_get(auth_token, new_url)

def get_currencies(auth_token, url) -> dict:
    new_url = url + 'za/v1/cards/currencies'
    return query_api_get(auth_token, new_url)

def get_merchants(auth_token, url) -> dict:
    new_url = url + 'za/v1/cards/merchants'
    return query_api_get(auth_token, new_url)

def query_api_get(auth_token, url) -> dict:
    headers = {
        'Authorization': 'Bearer ' + auth_token,
        'Accept': 'application/json'
        }
    response = requests.get(url,headers=headers)
    print(response.json())
    return response.json()['data']

def query_api_post(auth_token, url, data) -> dict:
    headers = {
        'Authorization': 'Bearer ' + auth_token,
        'Accept': 'application/json'
        }
    response = requests.post(url,headers=headers, data=data)
    print(response.json())
    return response.json()

#response = get_token(client_id, secret, url)
#response = get_accounts(auth_token, url)
#response = get_account_balance(auth_token, account_id, url)
#response = get_account_transactions(auth_token, account_id, url)
#response = transfer(auth_token, account_id, beneficiary, amount, url)
#response = get_countries(auth_token, url)
#response = get_currencies(auth_token, url)
#response = get_merchants(auth_token, url)
