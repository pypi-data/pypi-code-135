'''
Created on Mar 25, 2022

@author: Siro

'''

import json
from atframework.tools.log.config import logger


class ApiResponseChecking(object):

    """
    Check response for registration

    {
    "success": true,
    "t": "bb13cf8e15fd435a91e1b41562dfcb51"
    }

    """

    def check_response_registration(self, response_data):
        # json_data = json.dumps(response_data)
        families_dic = json.loads(response_data)

        logger.info(families_dic)

        registration_key_list = []
        registration_value_list = []
        for i, j in families_dic.items():
            registration_key_list.append(i)
            registration_value_list.append(j)
        # families key should be games
        for k in range(len(registration_key_list)):
            if registration_key_list[k] == "success":
                result = (registration_value_list[k])
                return result
        return False

    """
    Check response for login
    """
    def check_response_login(self, response_data):
        # json_data = json.dumps(response_data)
        families_login_dic = json.loads(response_data)

        logger.info(families_login_dic)

        login_key_list = []
        login_value_list = []
        for i, j in families_login_dic.items():
            login_key_list.append(i)
            login_value_list.append(j)
        # families key should be games
        for k in range(len(login_key_list)):
            if login_key_list[k] == "success":
                result = (login_value_list[k])
                return result
        return False

    """
    Check response for logout
    """
    def check_response_logout(self, response_data):
        # json_data = json.dumps(response_data)
        families_logout_dic = json.loads(response_data)

        logger.info(families_logout_dic)

        logout_key_list = []
        logout_value_list = []
        for i, j in families_logout_dic.items():
            logout_key_list.append(i)
            logout_value_list.append(j)
        # families key should be games
        for k in range(len(logout_key_list)):
            if logout_key_list[k] == "success":
                result = (logout_value_list[k])
                return result
        return False

    """
    Check response for games/family/favorites
    """

    def check_response_game_family_favorites(self, response_data):
        # json_data = json.dumps(response_data)
        families_dic = json.loads(response_data)

        families_key_list = []
        families_value_list = []
        for i, j in families_dic.items():
            families_key_list.append(i)
            families_value_list.append(j)
        # families key should be games
        assert families_key_list[0] == 'games'

        # print(key_list)
        family = families_value_list[0][0]

        family_key_list = []
        for k in family:
            family_key_list.append(k)
        logger.info(family_key_list)

        list_string = ['familyId', 'name', 'status', 'provider', 'translations']
        string_set = set(family_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    """
    Check response for /positioning
    """

    def check_response_positioning_group(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)
        positionings_key_list = []
        positionings_value_list = []
        for i, j in positioning_dic.items():
            positionings_key_list.append(i)
            positionings_value_list.append(j)
        # group's key should be Jackpots
        assert positionings_value_list[0] == 'Jackpots'

        logger.info(positionings_key_list)
        list_string = ['name', 'friendlyName', 'slug', 'tags', 'classifyName', 'classifyId', 'type', 'status', 'families',
                       'count', 'size', 'currentPage', 'pageCount']
        string_set = set(positionings_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    """
    Check response for /positioning/{group}
    """

    def check_response_positioning_not_logged_in(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)

        positioning_keys_list = []
        positioning_values_list = []
        for i, j in positioning_dic.items():
            positioning_keys_list.append(i)
            positioning_values_list.append(j)
        # positioning key should be positioning
        assert positioning_keys_list[0] == 'positioning'

        # print(positioning)
        positioning = positioning_values_list[0][0]
        assert positioning.get("name") == 'automation group'

        positioning_key_list = []
        for k in positioning:
            positioning_key_list.append(k)

        print(positioning_key_list)
        list_string = ['name', 'friendlyName', 'slug', 'tags', 'classifyName', 'classifyId', 'type', 'status', 'order', 'families', 'count', 'size', 'currentPage', 'pageCount']
        string_set = set(positioning_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    def check_response_positioning_logged_in(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)
        positioning_keys_list = []
        positioning_values_list = []
        for i, j in positioning_dic.items():
            positioning_keys_list.append(i)
            positioning_values_list.append(j)
        # positioning key should be positioning
        assert positioning_keys_list[0] == 'positioning'

        # print(positioning)
        positioning = positioning_values_list[0][0]
        assert positioning.get("name") == 'Taiwan'

        positioning_key_list = []
        for k in positioning:
            positioning_key_list.append(k)

        print(positioning_key_list)
        list_string = ['name', 'friendlyName', 'slug', 'tags', 'classifyName', 'classifyId', 'type', 'status', 'order', 'families', 'count', 'size', 'currentPage', 'pageCount']
        string_set = set(positioning_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    def check_response_groups_not_logged_in(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)

        positioning_keys_list = []
        positioning_values_list = []
        for i, j in positioning_dic.items():
            positioning_keys_list.append(i)
            positioning_values_list.append(j)
        # positioning key should be positioning
        assert positioning_keys_list[0] == 'groups'

        # print(positioning)
        positioning = positioning_values_list[0][0]
        assert positioning.get("name") == 'automation group'

        positioning_key_list = []
        for k in positioning:
            positioning_key_list.append(k)

        print(positioning_key_list)
        list_string = ['name', 'friendlyName', 'slug', 'tags', 'classifyName', 'classifyId', 'type', 'status', 'order', 'families', 'count', 'size', 'currentPage', 'pageCount']
        string_set = set(positioning_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    def check_response_groups_logged_in(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)

        positioning_keys_list = []
        positioning_values_list = []
        for i, j in positioning_dic.items():
            positioning_keys_list.append(i)
            positioning_values_list.append(j)
        # positioning key should be positioning
        assert positioning_keys_list[0] == 'groups'

        # print(positioning)
        positioning = positioning_values_list[0][0]
        assert positioning.get("name") == 'Taiwan'

        positioning_key_list = []
        for k in positioning:
            positioning_key_list.append(k)

        print(positioning_key_list)
        list_string = ['name', 'friendlyName', 'slug', 'tags', 'classifyName', 'classifyId', 'type', 'status', 'order', 'families', 'count', 'size', 'currentPage', 'pageCount']
        string_set = set(positioning_key_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    def check_response_positioning_friendly_name_provider(self, response_data):
        # json_data = json.dumps(response_data)
        positioning_dic = json.loads(response_data)
        positioning_keys_list = []
        positioning_values_list = []
        for i, j in positioning_dic.items():
            positioning_keys_list.append(i)
            positioning_values_list.append(j)
        # positioning friendly name should be [2]
        friendly_name = positioning_values_list[2]
        assert friendly_name == 'Book Of Dead'

        list_string = ['position', 'familyId', 'familyName', 'provider', 'providerName', 'tags', 'status', 'translations', 'games']
        string_set = set(positioning_keys_list)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    """
    Check response for /games/family/favorites
    """
    def check_response_games_family_favorites(self, response_data):
        # json_data = json.dumps(response_data)
        games_dic = json.loads(response_data)
        games_keys_list = []
        games_values_list = []
        for i, j in games_dic.items():
            games_keys_list.append(i)
            games_values_list.append(j)
        assert games_keys_list[0] == 'games'

        game_family_id = []
        for game_dic in games_values_list[0]:
            game_family_id.append(game_dic.get("familyId"))

        list_string = [75559, 73609, 70021, 63911, 57957, 57931, 41343, 30163, 18801, 12015, 5307, 2187]
        string_set = set(game_family_id)
        result = all([word in string_set for word in list_string])
        assert result
        return True

    """
    Check response for /games/family/favorites?text=hello
    """
    def check_response_games_family_favorites_text(self, response_data):
        # json_data = json.dumps(response_data)
        games_dic = json.loads(response_data)

        for game_dic in games_dic['games']:
            game_family_id = game_dic['familyId']

        assert game_family_id == 30163
        return True

    """
    Check response for /games/families/recent?limit=50
    """
    def check_response_games_family_recent(self, response_data):
        # json_data = json.dumps(response_data)
        games_dic = json.loads(response_data)
        game_family_recent = []
        for game_dic in games_dic:
            game_family_recent.append(game_dic["familyId"])

        list_string = [71659, 71061, 57957, 59387, 12015, 43137, 55903, 6529, 52861, 54447, 10975, 21505, 3955, 57931,
                       41343, 61649, 14537, 45919, 76495, 71503, 47037, 54707, 5307]
        string_set = set(game_family_recent)
        result = all([word in string_set for word in list_string])
        assert result
        return True
