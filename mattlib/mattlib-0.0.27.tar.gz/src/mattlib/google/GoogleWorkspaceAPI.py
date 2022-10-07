from BaseGoogleAPI import BaseGoogleAPI
from google.oauth2 import service_account
import googleapiclient.discovery


class GoogleWorkspaceAPI(BaseGoogleAPI):
    def __init__(self, credentials_file, domain, subject):
        self.scopes = [
                'https://www.googleapis.com/auth/admin.directory.user.readonly',
                 ]
        super().__init__(credentials_file, subject)
        self.domain = domain
       

    def list_users(self):
        admin = googleapiclient\
            .discovery.build('admin',
                             'directory_v1',
                             credentials=self.credentials)
        args = {
             'domain': self.domain
         }
        data_ws = self.call_api(admin.users().list,
                                args, "users")
        return data_ws
