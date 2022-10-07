from BaseGoogleAPI import BaseGoogleAPI
import googleapiclient.discovery

class GCPAPI(BaseGoogleAPI):
    def __init__(self, credentials_file):
        self.scopes = ['https://www.googleapis.com/auth/cloud-platform']
        super().__init__(credentials_file)

    def list_project_assets(self, project):
        security_center = googleapiclient\
            .discovery.build('securitycenter',
                             'v1',
                             credentials=self.credentials)
        args = {
            'parent': f'projects/{project}',
            'pageSize': 1000
        }
        data = self.call_api(security_center.projects()\
            .assets()\
            .list,
            args, 'listAssetsResults')
        return data
