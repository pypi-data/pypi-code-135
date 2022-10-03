class Group(object):
    def __init__(self, json):
        self.uuid = json['uuid']
        self.id = json['links'][0]['id']
        self.name = json['name']
        self.href = json['links'][0]['href']

class VaultRecord(object):
    def __init__(self, json):
        self.uuid = json['uuid']
        self.name = json['name']
        self.color = json['color'] if 'color' in json else ''
        self.username = json['username'] if 'username' in json else ''
        self.url = json['url'] if 'url' in json else ''
        self.links = json['links'][0]
        self.additionalObjects = json['additionalObjects']
        self.password = json['additionalObjects']['secret']['password'] if 'secret' in json['additionalObjects'] and 'password' in json['additionalObjects']['secret'] else ''
        self.totp = json['additionalObjects']['secret']['totp'] if 'secret' in json['additionalObjects'] and 'totp' in json['additionalObjects']['secret'] else ''
        self.filename = json['filename'] if 'filename' in json else ''
        self.file = json['additionalObjects']['secret']['file'] if 'secret' in json['additionalObjects'] and 'file' in json['additionalObjects']['secret'] else ''


class KeyHubVault(object):
    def __init__(self, authentication):
        self._session = authentication.session
        self._uri = authentication.uri

    def get_group(self, group_uuid):
        response = self._session.get(self._uri + "/keyhub/rest/v1/group?uuid=" + group_uuid)
        return Group(response.json()['items'][0])
    
    def get_vault_records(self, group_uuid):
        # TODO: support for client vault -> group_uuid=None
        group = self.get_group(group_uuid)
        response = self._session.get(group.href + '/vault')
        records = []
        for record in response.json()['records']:
            records.append(VaultRecord(record))
        return records

    def get_vault_record(self, group_uuid, record_uuid):
        group = self.get_group(group_uuid)
        response = self._session.get(group.href + "/vault/record/uuid/" + record_uuid + "?additional=secret&groupid=" + group.id) 
        return VaultRecord(response.json())
        
    def post_vault_record(self, group_uuid, payload):
        group = self.get_group(group_uuid)
        response = self._session.post(group.href + "/vault/record?additional=secret", json=payload)
        return VaultRecord(response.json()['items'][0])

def vault(authentication):
    return KeyHubVault(authentication=authentication)

