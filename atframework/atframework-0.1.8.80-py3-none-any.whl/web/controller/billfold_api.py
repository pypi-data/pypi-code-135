import requests
# from requests.auth import HTTPBasicAuth
# import json

from atframework.web.common.maps.resource_maps import ResourceMaps
from atframework.tools.log.config import logger
from atframework.web.utils.utils import Utils


class BillfoldAPI:
    utils = Utils()
    rm = ResourceMaps()

    def registerByPayload(self, password, email='', user_name='', nick_name='', phone_number='', device='desktop'):
        logger.info('[AtLog] ----- API for registration by payload')
        url = self.rm.SITE_PREFIX + self.rm.REGISTER_URL
        password = str(password)
        email = str(email)
        user_name = str(user_name)
        nick_name = str(nick_name)
        phone_number = str(phone_number)
        payload = {}
        if email != '' and user_name == '' and nick_name == '' and phone_number == '':
            payload = {'email': email,
                       'policyChecked': 'true',
                       'password': password}
        elif user_name != '' and email == '' and nick_name == '' and phone_number == '':
            payload = {'userName': user_name,
                       'policyChecked': 'true',
                       'password': password}
        elif nick_name != '' and email == '' and user_name == '' and phone_number == '':
            payload = {'nickName': nick_name,
                       'policyChecked': 'true',
                       'password': password}
        elif phone_number != '' and email == '' and nick_name == '' and user_name == '':
            payload = {'phoneNumber': phone_number,
                       'policyChecked': 'true',
                       'password': password}
        else:
            assert "registration data error!!"
        response = requests.post(url, headers=self.utils.get_header(device), data=payload)
        return response

    def registerByParams(self, password, email='', user_name='', nick_name='', phone_number='', device='desktop'):
        logger.info('[AtLog] ----- API for registration by Params')
        url = self.rm.SITE_PREFIX + self.rm.REGISTER_URL
        password = str(password)
        email = str(email)
        user_name = str(user_name)
        nick_name = str(nick_name)
        phone_number = str(phone_number)
        if password == "":
            password = self.rm.TEST_PASSWORD_FOR_API
        if email != '' and user_name == '' and nick_name == '' and phone_number == '':
            url = url + "?email=" + email + "&" + "password=" + password + "?policyChecked=true"
        elif user_name != '' and email == '' and nick_name == '' and phone_number == '':
            url = url + "?userName=" + user_name + "&" + "password=" + password + "?policyChecked=true"
        elif nick_name != '' and email == '' and user_name == '' and phone_number == '':
            url = url + "?nickName=" + nick_name + "&" + "password=" + password + "?policyChecked=true"
        elif phone_number != '' and email == '' and nick_name == '' and user_name == '':
            url = url + "?phoneNumber=" + phone_number + "&" + "password=" + password + "?policyChecked=true"
        else:
            assert "registration data error!!"
        response = requests.post(url, headers=self.utils.get_header(device))
        return response

    def loginByParams(self, password='', email='', user_name='', nick_name='', phone_number='', device='desktop'):
        logger.info('[AtLog] ----- API for login by params')
        url = self.rm.SITE_PREFIX + self.rm.LOGIN_URL
        if password == "":
            password = self.rm.TEST_PASSWORD_FOR_API
        if email != "":
            url = url + "?email=" + email + "&" + "password=" + password
        elif user_name != "":
            url = url + "?userName=" + user_name + "&" + "password=" + password
        elif nick_name != "":
            url = url + "?nickName=" + nick_name + "&" + "password=" + password
        elif phone_number != "":
            url = url + "?phoneNumber=" + phone_number + "&" + "password=" + password
        else:
            url = url + "?email=" + self.rm.TEST_USEREMAIL_FOR_API + "&" + "password=" + password
        response = requests.post(url, headers=self.utils.get_header(device))
        print(response.cookies.get('JSESSIONID'))
        # print(response.cookies)
        return response

    def loginByPayload(self, payload=None, device='desktop'):
        logger.info('[AtLog] ----- API for login by payload')
        url = self.rm.SITE_PREFIX + self.rm.LOGIN_URL
        payload = {'email': self.rm.TEST_USEREMAIL_FOR_API,
                   'grant_type': 'password',
                   'password': self.rm.TEST_PASSWORD_FOR_API}
        response = requests.post(url, headers=self.utils.get_header(device), data=payload)
        print(response.cookies.get('JSESSIONID'))
        # print(response.cookies.values()[0])
        return response

    def loginByParamsCashio(self, password='', email='', user_name='', nick_name='', phone_number='', device='desktop'):
        logger.info('[AtLog] ----- API for login by params cashio')
        url = self.rm.SITE_PREFIX + self.rm.CASHIO_LOGIN_URL
        if password == "":
            password = self.rm.TEST_PASSWORD_FOR_API
        if email != "":
            url = url + "?email=" + email + "&" + "password=" + password
        elif user_name != "":
            url = url + "?userName=" + user_name + "&" + "password=" + password
        elif nick_name != "":
            url = url + "?nickName=" + nick_name + "&" + "password=" + password
        elif phone_number != "":
            url = url + "?phoneNumber=" + phone_number + "&" + "password=" + password
        else:
            url = url + "?email=" + self.rm.TEST_USEREMAIL_FOR_API + "&" + "password=" + password
        response = requests.post(url, headers=self.utils.get_header(device))
        print(response.cookies.get('JSESSIONID'))
        # print(response.cookies)
        return response

    def loginByPayloadCashio(self, payload=None, device='desktop'):
        logger.info('[AtLog] ----- API for login by payload')
        url = self.rm.SITE_PREFIX + self.rm.CASHIO_LOGIN_URL
        payload = {'email': self.rm.TEST_USEREMAIL_FOR_API,
                   'grant_type': 'password',
                   'password': self.rm.TEST_PASSWORD_FOR_API}
        response = requests.post(url, headers=self.utils.get_header(device), data=payload)
        print(response.cookies.get('JSESSIONID'))
        # print(response.cookies.values()[0])
        return response

    def logout(self, payload=None, device='desktop'):
        logger.info('[AtLog] ----- API for logout')
        url = self.rm.SITE_PREFIX + self.rm.LOGOUT_URL
        response = requests.post(url, headers=self.utils.get_header(device), data=payload)
        return response

    def game_family_favorites(self, cookie='', payload=None, params='', device='desktop'):
        logger.info('[AtLog] ----- API for games/family/favorites?text={text}')
        url = self.rm.SITE_PREFIX + self.rm.FAMILY_FAVORITES_URL + "?text=" + params
        response = requests.get(url, headers=self.utils.get_header(device, cookie), data=payload)
        return response

    def positioning(self, cookie='', payload=None, text='', size='', mobile='false', user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /positioning?&size={size}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "?size=20000"
        if text != '':
            url = url + "&text=" + text
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_mobile_true(self, cookie='', payload=None, text='', size='', mobile='true', user_agent_env='mobile'):
        logger.info('[AtLog] ----- API for /positioning?mobile={mobile}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "?mobile=" + mobile
        if text != '':
            url = url + "&text=" + text
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_mobile_false(self, cookie='', payload=None, text='', size='', mobile='false', user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /positioning?mobile={mobile}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "?mobile=" + mobile
        if text != '':
            url = url + "&text=" + text
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_group(self, cookie='', payload=None, text='', page='', size='', mobile='',
                          user_agent_env='desktop'):
        logger.info(
            '[AtLog] ----- API for /positioning/{group}?mobile={mobile}&text={searchtext}&page={page}&size={size}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "/" + self.rm.FAMILY_GROUP_NAME
        if text != '':
            url = url + "&text=" + text
        if page != '':
            url = url + "&page=" + page
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_groups(self, cookie='', payload=None, text='', page='', size='', mobile='',
                          user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /positioning/groups')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "/" + "groups"
        if text != '':
            url = url + "&text=" + text
        if page != '':
            url = url + "&page=" + page
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_group_mobile_true(self, cookie='', payload=None, text='', page='', size='', mobile='true',
                          user_agent_env='mobile'):
        logger.info(
            '[AtLog] ----- API for /positioning/{group}?mobile={mobile}&text={searchtext}&page={page}&size={size}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "/" + self.rm.FAMILY_GROUP_NAME + "?mobile=" + mobile
        if text != '':
            url = url + "&text=" + text
        if page != '':
            url = url + "&page=" + page
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_group_mobile_false(self, cookie='', payload=None, text='', page='', size='', mobile='false',
                          user_agent_env='desktop'):
        logger.info(
            '[AtLog] ----- API for /positioning/{group}?mobile={mobile}&text={searchtext}&page={page}&size={size}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_URL + "/" + self.rm.FAMILY_GROUP_NAME + "?mobile=" + mobile
        if text != '':
            url = url + "&text=" + text
        if page != '':
            url = url + "&page=" + page
        if size != '':
            url = url + "&size=" + size
        print(url)
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def positioning_friendlyName_provider(self, cookie='', payload=None, text='', friendlyName='', provider='', size='',
                                          mobile='', user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /positioning/{friendlyName}/{provider}?mobile={mobile}')
        url = self.rm.SITE_PREFIX + self.rm.POSITIONING_GROUP_URL + self.rm.FRIENDLY_NAME + self.rm.PROVIDER +"?mobile=" + mobile
        if text != '':
            url = url + "&text=" + text
        if size != '':
            url = url + "&size=" + size
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def games_family_favorites(self, cookie='', payload=None, text='', friendlyName='', provider='', size='',
                                          mobile='', user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /games/family/favorites')
        url = self.rm.SITE_PREFIX + self.rm.FAMILY_FAVORITES_URL
        if text != '':
            url = url + "?text=" + text
        if size != '':
            url = url + "&size=" + size
        print(url)
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response

    def games_family_recent(self, cookie='', payload=None, text='', friendlyName='', provider='', size='',
                                          mobile='', user_agent_env='desktop'):
        logger.info('[AtLog] ----- API for /games/families/recent?limit=50')
        url = self.rm.SITE_PREFIX + self.rm.GAME_RECENT_URL + "?" + "limit=50"
        if text != '':
            url = url + "&text=" + text
        if size != '':
            url = url + "&size=" + size
        print(url)
        response = requests.get(url, headers=self.utils.get_header(user_agent_env, cookie), data=payload)
        return response