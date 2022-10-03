# Untested

import requests

class Group(object):
    def __init__(self, json):
        self.auditedGroups = json['auditedGroups']
        self.unauditedGroups = json['unauditedGroups']
        self.overdueAuditGroups = json['overdueAuditGroups']
        self.validVaultPolicies = json['validVaultPolicies']
        self.vaultsWithoutPolicies = json['vaultsWithoutPolicies']
        self.overdueVaultPolicies = json['overdueVaultPolicies']

        self.groupClassificationsUuid = json['classifications'][0]['uuid']
        self.groupClassificationsName = json['classifications'][0]['name']
        self.groupClassificationsDefaultClassification = json['classifications'][0]['defaultClassification']
        self.groupClassificationsMaxAuditInterval = json['classifications'][0]['maximumAuditInterval']
        self.groupClassificationsAuditMonths = json['classifications'][0]['requiredMonths']
        self.groupClassificationsAuditTrail = json['classifications'][0]['recordTrailRequired']
        self.groupClassificationsRotPasswd = json['classifications'][0]['rotatingPasswordRequired']
        self.groupClassificationsAuthGroupProv = json['classifications'][0]['authorizingGroupProvisioningRequired']
        self.groupClassificationsAuthGroupMembershp = json['classifications'][0]['authorizingGroupMembershipRequired']
        self.groupClassificationsAuthGroupGroupAudit = json['classifications'][0]['authorizingGroupAuditingRequired']
        self.groupClassificationsVaultAct = json['classifications'][0]['vaultRequiresActivation']
        self.groupClassificationsMinNrManagers = json['classifications'][0]['minimumNrManagers']
        self.groupClassificationsDesc = json['classifications'][0]['description']


class Misc(object):
    def __init__(self, authentication):
        self._headers = authentication.headers
        self._uri = authentication.uri

    def get_auditstats(self):
        response = requests.get(self._uri + "/keyhub/rest/v1/group/auditstats", headers=self._headers, verify=True)
        # return Group(response.json())
        return response.text

    def get_certificates(self):
        response = requests.get(self._uri + "/keyhub/rest/v1/certificate", headers=self._headers, verify=True)
        # return Group(response.json())
        return response.text

def misc(authentication):
    return Misc(authentication=authentication)

