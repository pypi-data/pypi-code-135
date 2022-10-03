import requests
import json
import pdb

class MisskeyAPI:

    name = 'Python Wrapper for Misskey API'

    __DEFAULT_TIMEOUT = 300
    __SCOPE_SETS = [
            'read:account', 
            'read:blocks', 
            'read:drive', 
            'read:favorites', 
            'read:following', 
            'read:messaging', 
            'read:mutes', 
            'read:notifications', 
            'read:reactions', 
            'read:pages',
            'read:page-likes',
            'read:user-groups',
            'read:channels',
            'read:gallery',
            'read:gallery-likes',
            'write:account', 
            'write:blocks', 
            'write:drive', 
            'write:following', 
            'write:messaging', 
            'write:mutes', 
            'write:notes', 
            'write:notifications', 
            'write:reactions', 
            'write:votes',
            'write:pages',
            'write:page-likes',
            'write:user-groups',
            'write:channels',
            'write:gallery',
            'write:gallery-likes'
            ]

    def __init__(
        self,
        api_base_url = None,
        callback = None,
        permission = __SCOPE_SETS,
        name: str = None,
        request_timeout = __DEFAULT_TIMEOUT,
        session = None,
        ):

        self.api_base_url = api_base_url
        if self.api_base_url == None:
            raise WrapperError("A Misskey instance's URL is required!") 
        if self.api_base_url != None:
            self.callback = f'{self.api_base_url}/callback'

        self.permission = permission
        self.request_timeout = request_timeout

        self.__name = name

        if session:
            self.session = session
        else:
            self.session = requests.Session()

        self.__request_timeout = request_timeout

    def account_i(self, i=None):

        params = {
                'i': i
                }

        endpoint = self.api_base_url + '/api/i'
        
        response = self.__api_request(endpoint, params)

        return response

    def app_create(self, name=None, description=None, permission=None, callbackUrl=None, session=None):
   
        params = {
            'name': name,
            'description': description,
            'permission': permission,
            'callbackUrl': callbackUrl
        }

        try:

            if session:
                ret = session.post(self.api_base_url + '/api/app/create', json=request_data, timeout=self.request_timeout)
                response = ret.json()
            else:
                response = requests.post(self.api_base_url + '/api/app/create', json=params, timeout=self.request_timeout)

        except Exception as e:

            raise MisskeyNetworkError("Could not complete request: %s" % e)

        return response

    def app_show(self, app_id=None, session=None):

        params = {
            'appId': app_id
        }

        try:

            if session:
                ret = session.post(self.api_base_url + '/api/app/show', json=request_data, timeout=self.request_timeout)
                response = ret.json()
            else:
                response = requests.post(self.api_base_url + '/api/app/show', json=params, timeout=self.request_timeout)
                #response = response.json()

        except Exception as e:

            raise MisskeyNetworkError("Could not complete request: %s" % e)

        return response

    def auth_session_generate(self, app_secret=None):

        params = {
            'appSecret': app_secret,
            }

        endpoint = self.api_base_url + '/api/auth/session/generate'

        response = self.__api_request(endpoint, params)       
        
        return response

    def auth_session_show(self, token=None):

        params = {
                'token': token
                }

        endpoint = self.api_base_url + '/api/auth/session/show'
        
        response = self.__api_request(endpoint, params)

        return response

    def auth_session_userkey(self, app_secret=None, token=None):

        params = {
                'appSecret': app_secret,
                'token': token
                }

        endpoint = self.api_base_url + '/api/auth/session/userkey'
        
        response = self.__api_request(endpoint, params)

        return response

    def notes_create(self, i=None, visibility=None, text=None, local_only=True):

        params = {
                'i': i,
                'visibility': visibility,
                'text': text,
                'localOnly': local_only
                }

        endpoint = self.api_base_url + '/api/notes/create'
        
        response = self.__api_request(endpoint, params)

    def users_groups_create(self, i=None, name=None):

        params = {
                'i': i,
                'name': name
                }

        endpoint = self.api_base_url + '/api/users/groups/create'

        response = self.__api_request(endpoint, params)

        return response

    def users_groups_delete(self, i=None, groupId=None):

        params = {
                'i': i,
                'groupId': groupId
                }

        endpoint = self.api_base_url + '/api/users/groups/delete'

        response = self.__api_request(endpoint, params)

        return response

    def __api_request(self, endpoint, params):

        try:

            response = requests.post(url = endpoint, json=params)

        except Exception as e:

            raise MisskeyNetworkError(f"Could not complete request: {e}")

        if response is None:

            raise MisskeyIllegalArgumentError("Illegal request.")

        if not response.ok:

                try:
                    if isinstance(response, dict) and 'error' in response:
                        error_msg = response['error']
                    elif isinstance(response, str):
                        error_msg = response
                    else:
                        error_msg = None
                except ValueError:
                    error_msg = None

                if response.status_code == 404:
                    ex_type = MisskeyNotFoundError
                    if not error_msg:
                        error_msg = 'Endpoint not found.'
                        # this is for compatibility with older versions
                        # which raised MisskeyAPIError('Endpoint not found.')
                        # on any 404
                elif response.status_code == 401:
                    ex_type = MisskeyUnauthorizedError
                elif response.status_code == 500:
                    ex_type = MisskeyInternalServerError
                elif response.status_code == 502:
                    ex_type = MisskeyBadGatewayError
                elif response.status_code == 503:
                    ex_type = MisskeyServiceUnavailableError
                elif response.status_code == 504:
                    ex_type = MisskeyGatewayTimeoutError
                elif response.status_code >= 500 and \
                    response.status_code <= 511:
                    ex_type = MisskeyServerError
                else:
                    ex_type = MisskeyAPIError

                raise ex_type(
                    'Misskey API returned error',
                    response.status_code,
                    response.reason,
                    error_msg)

        else:

            return response

##
# Exceptions
##
class WrapperError(Exception):
    """Wrapper base class"""

class MisskeyAPIConfigError(Exception):
    """This class exception"""
    
class MisskeyError(Exception):
    """Base class for MisskeyAPI exceptions"""

class MisskeyIllegalArgumentError(ValueError, MisskeyError):
    """Raised when an incorrect parameter is passed to a function"""
    pass

class MisskeyIOError(IOError, MisskeyError):
    """Base class for MisskeyAPI I/O errors"""

class MisskeyNetworkError(MisskeyIOError):
    """Raised when network communication with the server fails"""
    pass
class MisskeyReadTimeout(MisskeyNetworkError):
    """Raised when a stream times out"""
    pass
class MisskeyAPIError(MisskeyError):
    """Raised when the mastodon API generates a response that cannot be handled"""
    pass
class MisskeyServerError(MisskeyAPIError):
    """Raised if the Server is malconfigured and returns a 5xx error code"""
    pass
class MisskeyInternalServerError(MisskeyServerError):
    """Raised if the Server returns a 500 error"""
    pass

class MisskeyBadGatewayError(MisskeyServerError):
    """Raised if the Server returns a 502 error"""
    pass

class MisskeyServiceUnavailableError(MisskeyServerError):
    """Raised if the Server returns a 503 error"""
    pass

class MisskeyGatewayTimeoutError(MisskeyServerError):
    """Raised if the Server returns a 504 error"""
    pass
class MisskeyNotFoundError(MisskeyAPIError):
    """Raised when the ejabberd API returns a 404 Not Found error"""
    pass

class MisskeyUnauthorizedError(MisskeyAPIError):
    """Raised when the ejabberd API returns a 401 Unauthorized error

       This happens when an OAuth token is invalid or has been revoked,
       or when trying to access an endpoint that can't be used without
       authentication without providing credentials."""
    pass
