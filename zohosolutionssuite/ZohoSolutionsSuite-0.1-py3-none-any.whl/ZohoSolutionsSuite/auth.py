"""
	This should be the first module in this Library that you become familiar with.

	It consists of only one Class definition, the Token.
"""
import time
import requests
import json
import os
from datetime import datetime # possibly remove
import pickle



class Token:
	"""
	Object representing an OAuth token for Zoho's APIs. 

	Methods:
	--------
	generate(self) ->								 Refreshes the current access token, sets value of self.access to new access token.
					  								 Calls self.write_to_file() as well

	write_to_file(self, filename='zohotoken.pkl') -> Creates a dictionary to store all Token data,
													 and writes it to a file.

	@classmethod: from_file(cls, filename) ->  		Returns a Token object, generated from Token data 
													stored in '.pkl' file.
	
	init_token_dir(self) ->							Checks if User's home directory has directory for 
													token data, directory is named ".zoauth", if not found
													creates the directory. If found, prompts user to select a
													Token file.
	"""
	def __init__(
		self,
		client_id, client_secret,
		grant_token=None,
		refresh_token=None,
		save_refresh=True,
		default_filename='zohotoken.pkl'
	):
		"""
		client_id: 						Can be found in Self Client option in api-console.zoho.com
		client_secret: 					Can be found in Self Client option in api-console.zoho.com
		grant_token: 					Token generated from Self Client interface in api-console.zoho.com, must have valid scope
		refresh_token: 					Token from previous OAuth session that can be used to refresh your session.
		save_refresh: 					Boolean configuration option for User, save on token refresh to file or not?
		filename:						String of the file name that token data should be written to.
		messages:						List of strings, all Token operations and API calls made with Token will be logged here
		"""
		self.client_id = client_id
		self.client_secret = client_secret
		self.access = None
		self.refresh = refresh_token
		self.save_refresh = save_refresh
		self.filename = default_filename
		self.messages = []
		self.init_token_dir()

		if refresh_token is not None:
			self.generate()
		if grant_token is not None:
			self.access, self.refresh = self._authorize(grant_token)
		if save_refresh:
			self.write_to_file(os.path.join(self.token_dir, self.filename))

	def _authorize(self, grant_token):
		"""
		Magic method that generates a fresh set of Access/Refresh tokens using a generated
		grant token from api-console.zoho.com.
		Returns:

		access_token 	->  (str) Used to authenticate when making any API call
		refresh_token 	->	(str) Used to generate a new access token 
		"""
		url = "https://accounts.zoho.com/oauth/v2/token"
		data = {
			"grant_type": "authorization_code",
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"code": grant_token
		}

		response = requests.post(url=url, data=data)
		if response.status_code == 200:
			content = json.loads(response.content.decode('utf-8'))
			access_token = content.get("access_token")
			refresh_token = content.get("refresh_token")
			self.auth_time = datetime.utcnow()
			self.valid_for = content.get("expires_in")
			if access_token is not None:
				message = f'Token {access_token} generated at {self.auth_time}\nValid for {self.valid_for}'
			else:
				message = f'Empty Token returned\nResponse Content:\n{content}'
			self.messages.append(message)
			# Need to implement token lifetime calculation 
			return access_token, refresh_token
		elif response.status_code >= 400 and response.status_code < 500:
			content = json.loads(response.content.decode('utf-8'))
			message = f"Token generation failed with status code {response.status_code}.\nResponse Content:\n{content}"
			self.messages.append(message)

	def _generate(self):
		"""
		Magic method that is called automatically whenever your access token has expired. 
		This should be never be called by any other method than self.generate(), which will be called
		when the response returns a 400 series error. Requires a valid Refresh Token to work, should be
		stored in self.refresh attribute.

		Returns:
		access_token 		->	(str) Used to authenticate when making any API call
		"""
		url = f"https://accounts.zoho.com/oauth/v2/token?refresh_token={self.refresh}"
		url += f"&client_id={self.client_id}"
		url += f"&client_secret={self.client_secret}"
		url += "&grant_type=refresh_token"

		response = requests.post(url=url)
		if response.status_code == 200:
			content = json.loads(response.content.decode('utf-8'))
			access_token = content.get("access_token")
			self.auth_time = datetime.utcnow()
			self.valid_for = content.get("expires_in")
			if access_token is not None:
				message = f'Token {access_token} generated at {self.auth_time.isoformat()}\nValid for {self.valid_for}'
			else:
				message = f'Empty Token returned\nResponse Content:\n{content}'
			self.messages.append(message)
			return access_token

	def _verify_token_dir(self):
		"""
		Magic method that returns a directory path if path is verified and exists.
		Else returns None object
		"""
		current_login = os.getlogin()
		dir_path = os.path.join("Users", current_login, ".zoauth")
		if not os.is_dir(dir_path):
			try:
				os.mkdir(dir_path)
				message = f"Token directory initialized at {dir_path}"
				self.messages.append(message)
				return dir_path
			except Exception as e:
				message = f"Error initializing token directory.\nError:\n{str(e)}"
				self.messages.append(message)
				return None
		else:
			message = f"Token directory verified at {dir_path}"
			self.messages.append(message)
			return dir_path

	def write_to_file(self, filename=self.filename):
		"""
		Method that will save your current Token data to the designated Token directory.

		filename 		-> (str) Name of the file to store token data
		"""
		dir_path = self._verify_token_dir()
		if dir_path is None:
			message = "No Token directory found or verified. Cannot save token data to file!"
			self.messages.append(message)
			return 
		data_object = {
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"refresh_token": self.refresh
		}

		with open(os.path.join(dir_path, filename), 'wb') as handle:
			pickle.dump(data_object, handle, protocol=pickle.HIGHEST_PROTOCOL)
		saved_at = datetime.utcnow()
		message = f"Token data successfully saved at {os.path.join(dir_path, filename)}\nTime: {saved_at.isoformat()}"
		self.messages.append(message)
		return

	@classmethod
	def from_file(cls, filename):
		""" 
		Class method that is meant to be used for Authenticating after your first intialization and authorization.
		To generate an access token using previous Token data, you need the 
		* Client ID
		* Client Secret
		* Refresh Token (only acquired after generating access tokens atleast ONCE)

		These values are pulled from the file that lives at the specified filename.
		"""
		dir_path = self._verify_token_dir()
		if dir_path is None:
			message = "No token directory found or verified. Cannot generate Token from file!"
			self.messages.append(message)
			return

		token_path = os.path.join(dir_path, filename)
		try:
			with open(token_path, 'rb') as handle:
				data_object = pickle.load(handle)
				client_id = data_object['client_id']
				client_secret = data_object['client_secret']
				refresh = data_object['refresh_token']
			return Token(client_id, client_secret, grant_token=None, refresh_token=refresh)

		except FileNotFoundError as e:
			message = f"There was a FileNotFoundError while attempting to read or load the data\nError:\n{str(e)}"
			self.messages.append(message)
			return None 

		except KeyError as e:
			message = f"Something went wrong while attempting to read your token data from the file.\nErrors\n{str(e)}"
			self.messages.append(message)
			return None 

	def generate(self):
		""" 
		Primary method that both users, and the library will interact with to trigger re-authentication.
		"""
		self.access = self._generate()
		if self.save_refresh:
			dir_path = self._verify_token_dir()
			if dir_path is None:
				message = "No token directory found or verified. Cannot generate Token from file!"
				self.messages.append(message)
			token_path = os.path.join(dir_path, self.filename)
			self.write_to_file(filename=self.filename)
		

