import requests

# r = requests.post(
#     'https://pub.orcid.org/oauth/token',
#     headers=dict(Accept='application/json'),
#     data=dict(client_id='APP-71ZX5MYHCDU3Y5TC',
#               client_secret='f38f373f-77fb-423d-b717-e5bb601ae4c0',
#               grant_type='client_credentials', scope='/read-public'))


# print(r)
# token = r.json()

# search_url = 'https://pub.orcid.org/v3.0/search/?q=%s'
# content_type = {'Content-type': 'application/vnd.orcid+json'}
# auth = {'Authorization': f"Bearer {token}"}
# r = requests.get(search_url % 'orcid', headers=content_type)
# print(r)


def get_orcid_id(firstName=None, lastName=None, **kwargs):
    if firstName is None and lastName is None:
        raise ValueError('firstName and lastName cannot both be None')

    kw = kwargs
    if firstName is not None:
        kw['given-names'] = firstName
    if lastName is not None:
        kw['family-name'] = lastName

    url = 'https://pub.orcid.org/v3.0/search/?q='

    for k, v in kw.items():
        url += f'{k}:{v}+AND+'

    if url.endswith('+AND+'):
        url = url[:-5]
    print(url)

    content_type = {'Content-type': 'application/vnd.orcid+json'}
    r = requests.get(url, headers=content_type)
    if r.status_code == 200:
        n = r.json()['num-found']
        if n > 1:
            print('multiple records found!')
            print('trying with keyword=astrophysics')
            return get_orcid_id(firstName, lastName, keyword='astrophysics',
                                **kwargs)
        elif n == 1:
            return r.json()['result'][0]['orcid-identifier']['path']
    else:
        raise ValueError(r.status_code)
# search('João', 'Faria')
