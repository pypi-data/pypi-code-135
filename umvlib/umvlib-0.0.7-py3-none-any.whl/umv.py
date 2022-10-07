import xml.etree.ElementTree as ET
import requests
import datetime
import re

from src.umvlib.Constants import Constants as c
from src.umvlib.Fields import Fields as f


class Umov:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'http://api.umov.me/CenterWeb/api/{self.api_key}'

    @staticmethod
    def __get(url):
        print(f'Getting {url}')
        response = requests.get(url)
        if 200 <= response.status_code <= 299:
            return response

    def get_activity_history_hierarchical(self, execution_id: str = None):
        url = f'{self.base_url}/activityHistoryHierarchical.xml'
        if execution_id:
            url = f'{self.base_url}/activityHistoryHierarchical/{execution_id}.xml'
        response = self.__get(url)
        return response.text

    def get_activity_history(self, execution_id: str = None):
        url = f'{self.base_url}/activityHistory.xml'
        if execution_id:
            url = f'{self.base_url}/activityHistory/{execution_id}.xml'
        response = self.__get(url)
        return response.text

    def get_activities(self):
        url = f'{self.base_url}/activity.xml'
        response = self.__get(url)
        return response.text

    def create_activity_history(self, alternative_identifier: str, activity: dict,
                                sections: list = None,
                                initial_start_time_on_system: str = None,
                                end_finish_time_on_system: str = None,
                                ):
        url = f'{self.base_url}/schedule/alternativeIdentifier/{alternative_identifier}/activityHistory.xml'

        activity_history = ET.Element(f.ACTIVITY_HISTORY)
        _activity = ET.SubElement(activity_history, f.ACTIVITY)
        self._sub_element(_activity, f.ALT_ID, activity['alternative_identifier'])

        if initial_start_time_on_system:
            self._sub_element(activity_history, f.INITIAL_START_TIME_ON_SYSTEM, initial_start_time_on_system)
        if end_finish_time_on_system:
            self._sub_element(activity_history, f.END_FINISH_TIME_ON_SYSTEM, end_finish_time_on_system)

        _sections = ET.SubElement(activity_history, f.SECTIONS)
        for section in sections:
            _section = ET.SubElement(_sections, f.SECTION)
            self._sub_element(_section, f.ALT_ID, section[f.ALT_ID])
            for item in section[f.ITEMS]:
                _fields = ET.SubElement(_section, f.FIELDS)
                for field in item[f.FIELDS]:
                    _field = ET.SubElement(_fields, f.FIELD)
                    self._sub_element(_field, f.ALT_ID, field[f.ALT_ID])
                    _field_history = ET.SubElement(_field, f.FIELD_HISTORY)
                    self._sub_element(_field_history, f.VALUE, field[f.FIELD_HISTORY][f.VALUE])
                    self._sub_element(_field_history, f.VALUE_FOR_EXHIBITION,
                                      field[f.FIELD_HISTORY][f.VALUE_FOR_EXHIBITION])

        print(ET.tostring(activity_history))
        response = requests.post(url, data={'data': ET.tostring(activity_history)})
        if response.status_code == 201 or response.status_code == 200:
            # print('Response', response.text)
            return response.text
        else:
            if 'already exists' in response.text or 'alternativeIdentifier' in response.text:
                # print(f"Got activity history {alternative_identifier}")
                print(response.text)
                return alternative_identifier
            else:
                raise Exception(url, response.status_code, response.text)

    def create_custom_entity(self,
                             entity: str = None,
                             description: str = None,
                             alternative_identifier: str = None,
                             **kwargs):
        custom_entity = ET.Element(f.CUSTOM_ENTITY_ENTRY)

        self._sub_element(custom_entity, f.DESCRIPTION, description)
        self._sub_element(custom_entity, f.ALT_ID, alternative_identifier)

        url = f'{self.base_url}/customEntity/alternativeIdentifier/{entity}/customEntityEntry.xml'
        response = requests.post(url, data={'data': ET.tostring(custom_entity)})
        if response.status_code == 201 or response.status_code == 200:
            print('Response', response.text)
            return alternative_identifier
        else:
            if 'already exists' in response.text or 'alternativeIdentifier' in response.text:
                print(f"Got custom entity {alternative_identifier}")
                return alternative_identifier
            else:
                raise Exception(response.status_code, response.text)

    def create_service_local_type(self,
                                  description: str,
                                  id: int = None,
                                  alternative_identifier: str = None,
                                  active: bool = True):
        s_local_type = ET.Element(f.SERVICE_LOCAL_TYPE)

        self._sub_element(s_local_type, f.DESCRIPTION, description)
        self._sub_element(s_local_type, f.ID, id)
        self._sub_element(s_local_type, f.ALT_ID, alternative_identifier)
        self._sub_element(s_local_type, f.ACTIVE, active)

        url = f'{self.base_url}/serviceLocalType.xml'
        response = requests.post(url, data={'data': ET.tostring(s_local_type)})
        if response.status_code == 201 or response.status_code == 200:
            print('Response', response.text)
            return alternative_identifier
        else:
            if 'alternativeIdentifierAlreadyInUse' in response.text:
                print(f"Got service local {alternative_identifier}")
                return alternative_identifier
            else:
                raise Exception(response.status_code, response.text)

    @staticmethod
    def _sub_element(element: ET.SubElement, key: str, value):
        if value:
            element = ET.SubElement(element, key)
            element.text = str(value).strip()
            return element
        return None

    def create_service_local(self,
                             description: str, active: bool = True, corporate_name: str = None,
                             alternative_identifier: str = None, state: str = None, city: str = None,
                             country: str = None, id: str = None, street: str = None, zip_code: str = None,
                             street_type: str = None, street_number: int = None, street_complement: str = None,
                             cellphone_idd: int = None, cellphone_std: int = None, cellphone_number: int = None,
                             phone_idd: int = None, phone_std: int = None, phone_number: int = None, email: str = None,
                             city_neighborhood: str = None, observation: str = None, service_local_type: str = None):

        service_locals = ET.Element(f.SERVICE_LOCALS)
        s_local = ET.SubElement(service_locals, f.SERVICE_LOCAL)

        self._sub_element(s_local, f.ID, id)
        self._sub_element(s_local, f.ACTIVE, active)
        self._sub_element(s_local, f.ALT_ID, alternative_identifier)
        self._sub_element(s_local, f.DESCRIPTION, description)
        self._sub_element(s_local, f.CORPORATE_NAME, corporate_name)
        self._sub_element(s_local, f.EMAIL, email)
        self._sub_element(s_local, f.OBSERVATION, observation)

        self._sub_element(s_local, f.ZIP_CODE, zip_code)
        self._sub_element(s_local, f.STREET, street)
        self._sub_element(s_local, f.STREET_TYPE, street_type)
        self._sub_element(s_local, f.STREET_NUMBER, street_number)
        self._sub_element(s_local, f.STREET_COMPLEMENT, street_complement)
        self._sub_element(s_local, f.CITY, city)
        self._sub_element(s_local, f.STATE, state)
        self._sub_element(s_local, f.COUNTRY, country)
        self._sub_element(s_local, f.NEIGHBORHOOD, city_neighborhood)

        self._sub_element(s_local, f.CELLPHONE_NUMBER, cellphone_number)
        self._sub_element(s_local, f.CELLPHONE_DDI, cellphone_idd)
        self._sub_element(s_local, f.CELLPHONE_DDD, cellphone_std)
        self._sub_element(s_local, f.PHONE_DDI, phone_idd)
        self._sub_element(s_local, f.PHONE_DDD, phone_std)
        self._sub_element(s_local, f.PHONE_NUMBER, phone_number)

        if service_local_type:
            s_local_type = ET.SubElement(s_local, f.SERVICE_LOCAL_TYPE)
            self._sub_element(s_local_type, f.ALT_ID, service_local_type)

        url = f'{self.base_url}/batch/serviceLocals.xml'
        response = self.__post(url, ET.tostring(service_locals))
        print('Response', response.text)
        return alternative_identifier

    def create_schedule(self,
                        update_if_exists: bool = True,
                        service_local: str = None,
                        date: str = None,
                        hour: str = None,
                        active: bool = True,
                        activities_origin: int = 7,
                        agent: str = None,
                        team: int = None,
                        team_execution: int = None,
                        alternative_identifier: str = None,
                        id: int = None,
                        observation: str = None,
                        origin: int = None,
                        situation: int = c.WAITING,
                        schedule_type: str = None,
                        activity_type: str = None,
                        sender_local_id: str = None,
                        priority: int = None,
                        filter_1: str = None,
                        **kwargs):

        today = datetime.datetime.now()
        if not date:
            date = today.strftime('%Y-%m-%d')
        if not hour:
            hour = today.strftime('%H:%M')

        schedules = None
        if update_if_exists:
            schedules = ET.Element(f.SCHEDULES)
            schedule = ET.SubElement(schedules, f.SCHEDULE)
        else:
            schedule = ET.Element(f.SCHEDULE)

        self._sub_element(schedule, f.DATE, date)
        self._sub_element(schedule, f.HOUR, hour)
        self._sub_element(schedule, f.ACTIVE, active)
        self._sub_element(schedule, f.ATCIVITIES_ORIGIN, activities_origin)
        self._sub_element(schedule, f.TEAM, team)
        self._sub_element(schedule, f.TEAM_EXECUTION, team_execution)
        if alternative_identifier:
            self._sub_element(schedule, f.ALT_ID, alternative_identifier)
        self._sub_element(schedule, f.ID, id)
        self._sub_element(schedule, f.OBSERVATION, observation)
        self._sub_element(schedule, f.ORIGIN, origin)
        if priority:
            self._sub_element(schedule, f.PRIORITY, priority)
        if filter_1:
            self._sub_element(schedule, f.FILTER_1, filter_1)

        _custom_fields = ET.SubElement(schedule, f.CUSTOM_FIELDS)
        for key, value in kwargs.items():
            _cf = ET.SubElement(_custom_fields, key)
            self._sub_element(_cf, f.ALT_ID, value)

        if agent:
            _agent = ET.SubElement(schedule, f.AGENT)
            self._sub_element(_agent, f.ALT_ID, agent)

        _service_local = ET.SubElement(schedule, f.SERVICE_LOCAL)
        self._sub_element(_service_local, f.ALT_ID, service_local)

        _schedule_type = ET.SubElement(schedule, f.SCHEDULE_TYPE)
        self._sub_element(_schedule_type, f.ALT_ID, schedule_type)

        _situation = ET.SubElement(schedule, f.SITUATION)
        self._sub_element(_situation, f.ID, situation)

        if activity_type:
            activity_relationship = ET.SubElement(
                schedule, f.ACTIVITY_RELATIONSHIP)
            activity = ET.SubElement(activity_relationship, f.ACTIVITY)
            self._sub_element(activity, f.ALT_ID, activity_type)

        if sender_local_id:
            s_local_origin = ET.SubElement(schedule, f.SERVICE_LOCAL_ORIGIN)
            self._sub_element(s_local_origin, f.ALT_ID, sender_local_id)

        if update_if_exists and schedules:
            url = f'{self.base_url}/batch/schedules.xml'
            data = ET.tostring(schedules)
            print('sched_data', ET.tostring(schedules))
        else:
            url = f'{self.base_url}/schedule.xml'
            data = ET.tostring(schedule)
            print('sched_data', ET.tostring(schedule))

        response = self.__post(url, data)
        xml_response = ET.fromstring(response.text)
        print('xml_response', xml_response)
        if update_if_exists:
            created_alt_id = xml_response.find(f.ENTRIES).find(f.ENTRY).get(f.ID, alternative_identifier)
        else:
            created_alt_id = xml_response.find(f.RESOURCE_ID).text
        print('created_alt_id', created_alt_id)
        return created_alt_id

    def create_items(self, items):
        print(items)
        url = f'{self.base_url}/batch/items.xml'

        items_to_create = ET.Element(f.ITEMS)

        max_list_size = 50  # API limit
        list_of_items_list = list()

        for i in range(0, len(items), max_list_size):
            list_of_items_list.append(items[i:i + max_list_size])

        for items_list in list_of_items_list:
            for item in items_list:
                alt_id = str(item["alt_id"])
                description = str(
                    re.sub(r'[^a-zA-Z0-9 ()-]', '', item["description"].upper()))

                new_item = ET.SubElement(items_to_create, f.ITEM)
                ET.SubElement(new_item, f.ALT_ID).text = alt_id
                ET.SubElement(new_item, f.DESCRIPTION).text = description
                sub_group = ET.SubElement(new_item, f.SUB_GROUP)
                ET.SubElement(sub_group, f.ALT_ID).text = "01"
            self.__post(url, ET.tostring(items_to_create))

    def add_schedule_items(self, schedule_id, items):
        url = f'{self.base_url}/batch/scheduleItems.xml'

        schedule_items = ET.Element(f.SCHEDULE_ITEMS)
        for item in items:
            alt_id = str(item["alt_id"])
            quantity = str(float(item["quantity"]))

            schedule_item = ET.SubElement(schedule_items, f.SCHEDULE_ITEM)
            schedule = ET.SubElement(schedule_item, f.SCHEDULE)
            ET.SubElement(schedule, f.ALT_ID).text = schedule_id
            item = ET.SubElement(schedule_item, f.ITEM)
            ET.SubElement(item, f.ALT_ID).text = alt_id
            custom_fields = ET.SubElement(schedule_item, f.CUSTOM_FIELDS)
            ET.SubElement(custom_fields, 'quantidade').text = quantity

        self.__post(url, ET.tostring(schedule_items))

    def approve_activity_history(self, execution_id):
        url = f'{self.base_url}/activityHistory/{execution_id}.xml'
        activity_history = ET.Element(f.ACTIVITY_HISTORY)
        self._sub_element(activity_history, f.STATUS_APPROVAL, c.STATUS_APPROVED)
        self.__post(url, ET.tostring(activity_history))

    @staticmethod
    def __post(url, data):
        print(f'Posting {url}')
        response = requests.post(url, data={'data': data})
        if 200 <= response.status_code <= 299:
            print('Response', response.text)
            return response
        else:
            raise Exception(url, response.status_code, response.text)
