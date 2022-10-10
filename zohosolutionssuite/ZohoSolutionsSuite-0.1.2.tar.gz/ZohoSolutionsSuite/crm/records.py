"""
This will likely be the easiest to use, as well as the most complete module in this library.
It is a good place after learning the auth module to acquaint yourself with the way we manipulate JSON data
returned and required by the Zoho APIS
"""
import requests
import json
from datetime import datetime


def make_header(token):
	"""A helper function that creates a Dictionary with our header data before making a request. 
	Each module shoiuld use its own helper function, as sometimes the headers may change.
	
	Arguments:
	token 		->	Token() object from the auth module. 

	Returns:
	headers		->	Dictionary object containing all Header keys and values
	"""
	return {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}


def get_record(token, module, record_id, **kwargs):
	""" 
	Takes a module API name from CRM, a record ID, and any parameters the endpoint accepts

	Returns a single record in the form of a dictionary.
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}/{record_id}'
	headers = make_header(token)

	response = requests.get(url=url, headers=headers, params=kwargs)
	message["STATUS"] = response.status_code
	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return get_record(token, module, record_id, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		data = content['data'][0]
		message["INFO"] = "Get record operation successful."
		message['DATA'] = data

		token.flush_log(message)
		return token, data


def get_records(token, module, **kwargs):
	"""
	Takes a module API name and any parameters the endpoint accepts

	Returns a List of one or many records; Each a Dictionary object
	"""

	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}'
	headers = make_header(token)

	response = requests.get(url=url, headers=headers, params=kwargs)
	message['STATUS'] = response.status_code
	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return get_records(token, module, **kwargs)
	else:
		content = json.loads(response.content.decode('utf-8'))
		records = content.get("data")
		message["INFO"] = "Get records operation successful"
		message["DATA"] = records 
		
		token.flush_log(message)
		return token, records


def update_record(token, module, record_id, data_object):
	"""
	Takes a module API name, record ID, and Dictionary object containing field API names 
	and values.

	Updates the associated record in CRM with new data.
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}'
	headers = make_header(token)

	data_object['id'] = record_id
	request_body = {}
	record_list = []

	record_list.append(data_object)
	request_body['data'] = record_list

	data = json.dumps(request_body).encode('utf-8')
	response = requests.put(url=url, headers=headers, data=data)
	message['STATUS'] = response.status_code
	if response.status_code <= 400 and response.status_code < 500:
		token.generate(retry=True)
		return update_record(token, module, record_id, data_object)

	else:
		content = json.loads(response.content.decode('utf-8'))
		message['INFO'] = "Update records operation successful."
		message["DATA"] = content
		#token.messages.append(message)
		token.flush_log(message)
		return token, content 


def delete_record(token, module, record_id, **kwargs):
	"""
	Takes a module API name ane a record ID, deletes the record from the CRM.
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}/{record_id}'
	headers = make_header(token)

	response = request.delete(url=url, headers=headers, params=kwargs)
	message["STATUS"] = response.status_code
	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return delete_record(token, module, record_id, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		message["INFO"] = "Delete record operation successful."
		message["DATA"] = content
		#token.messages.append(message)
		token.flush_log(message)
		return token, content


def create_record(token, module, data_object):
	"""
	Takes a module API name and a Dictionary of field names, then creates a new record with data 
	in Module
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}'
	headers = make_header(token)

	request_body = {}
	record_list = [data_object]
	request_body['data'] = record_list

	data = json.dumps(request_body).encode('utf-8')

	response = requests.post(url=url, headers=headers, data=data)
	message['STATUS'] = response.status_code

	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return create_record(token, module, data_object)

	else:
		content = json.loads(response.content.decode('utf-8'))
		message['INFO'] = "Create record operation successful."
		message['DATA'] = content
		#token.messages.append(message)
		token.flush_log(message)
		return token, content 


def convert_lead(token, record_id, deals=None, **kwargs):
	"""
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/Leads/{record_id}/actions/convert'
	headers = make_header(token)

	request_body = {}
	record_list = []
	record_object = {"Deals": deals}
	record_object = {**record_object, **kwargs}

	record_list.append(record_object)

	request_body['data'] = record_list
	data = json.dumps(request_body).encode('utf-8')

	response = requests.post(url=url, headers=headers, data=data)
	message['STATUS'] = response.status_code

	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return convert_lead(token, record_id, deals=deals, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		message['INFO'] = "Convert lead operation successful."
		message['DATA'] = content
		#token.messages.append(message)
		token.flush_log(message)
		return token, content


def get_deleted_records(token, module, record_type="all", **kwargs):
	"""
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}/deleted'
	headers = make_header(token)
	params = {"type": record_type}
	params = {**params, **kwargs}

	response = requests.get(url=url, headers=headers, params=params)
	message['STATUS'] = response.status_code

	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return get_deleted_records(token, module, record_type=record_type, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		data = content.get("data")
		message['INFO'] = "Get deleted records operations successful."
		message['DATA'] = data 
		#token.messages.append(message)
		token.flush_log(message)
		return token, data


def search_records(token, module, criteria, **kwargs):
	"""
	"""
	message = {}
	url = f'https://www.zohoapis.com/crm/v3/{module}/search'
	headers = make_header(token)

	params = {'criteria': criteria}
	params = {**params, **kwargs}

	response = requests.get(url=url, headers=headers, params=params)
	message['STATUS'] = response.status_code

	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return search_records(token, module, criteria, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		records = content.get("data")
		page_info = content.get("info")
		message['INFO'] = "Search records operation successful."
		message['DATA'] = records 
		message['PAGE_CONTEXT'] = page_info 
		#token.messages.append(message)
		token.flush_log(message)
		return token, records 


def count_records(token, module, criteria=None, **kwargs):
	"""
	"""
	message = {}
	url= f'https://www.zohoapis.com/crm/v3/{module}/actions/count'
	headers - make_header(token)

	params = {'criteria': criteria}
	params = {**params, **kwargs}

	response = requests.get(url=url, headers=headers, params=params)
	message['STATUS'] = response.status_code

	if response.status_code >= 400 and response.status_code < 500:
		token.generate(retry=True)
		return count_records(token, module, criteria=criteria, **kwargs)

	else:
		content = json.loads(response.content.decode('utf-8'))
		count = content.get("count")
		message['INFO'] = "Count records operation successful."
		message["DATA"] = count 
		#oken.messages.append(message)
		token.flush_log(message)
		return token, count 


def mass_action(token, module, callback, **kwargs):
	main_message = {}
	empty = False
	url = f'https://www.zohoapis.com/crm/v3/{module}'
	headers = make_header(token)

	page = 1
	iterated = 0
	params = kwargs
	start_time = datetime.utcnow()

	while not empty:
		page_message = {}
		params['page'] = str(page)
		params['per_page'] = "200"

		response = requests.get(url=url, headers=headers, params=params)
		page_message['STATUS'] = response.status_code
		#if response.status_code >= 400 and response.status_code < 500:
		if 400 <= response.status_code < 500:
			token.generate(retry=True)
			headers = make_header(token)
			continue
		content = json.loads(response.content.decode('utf-8'))
		data = content.get("data")
		page_message['INFO'] = f"{len(data)} records successfully retrieved."
		page_message["DATA"] = data
		token.flush_log(page_message)

		if len(data) == 0:
			batch_message = {}
			batch_message['INFO'] = "Mass action finished"
			batch_message['DATA'] = f'{iterated} records operated on.'
			token.flush_log(batch_message)
			empty = True

		for record in data:
			record_message = {}
			token, callback_response = callback(token, module, record)
			record_message["INFO"] = f"Callback executed on record #{data.index(record) + 1}"
			record_message['DATA'] = callback_response
			token.flush_log(record_message)
			iterated += 1

		page += 1
		if len(data) < 200:
			batch_message = {}
			batch_message["INFO"] ="Mass action finished"
			batch_message["DATA"] = f'{iterated} records operated on.'
			token.flush_log(batch_message)
			empty = True
	end_time = datetime.utcnow()
	main_message['INFO'] = f"Mass action completed at {end_time.isoformat()}"
	main_message['DATA'] = iterated 
	token.flush_log(main_message)
	return token, iterated


def list_action(token, module, callback, record_id_list):
	main_message = {}
	iterated = 0
	stat_time = datetime.utcnow()
	headers = make_header(token)

	for record_id in record_id_list:
		record_message = {}
		url = f'https://www.zohoapis.com/crm/v3/{module}/{record_id}'
		token, callback_response = callback(token, module, record_id)
		record_message['INFO'] = f'Callback executed on record #{record_id_list.index(record) + 1}'
		record_message['DATA'] = callback_response
		token.flush_log(record_message)
		iterated += 1

	end_time = datetime.utcnow().isoformat()
	main_message['INFO'] =f'Mass action completed at {end_time}'
	main_message['DATA'] = iterated 
	token.flush_log(main_message)
	return token, iterated

