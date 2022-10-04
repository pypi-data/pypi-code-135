import click
import os
import requests
from sieve.api.constants import API_URL, API_BASE

@click.command()
@click.option('--command', default='upload', help='commands using models')
def model(command):
	if command == "upload":
		build_command()

def build_command():
	api_key = os.environ.get('SIEVE_API_KEY')
	if not api_key:
		print("Please set environment variable SIEVE_API_KEY with your API key")
		return

	os.system('zip dir * -r > zipout')

	url = f'{API_URL}/{API_BASE}/upload_model'
	payload = {}
	files = [('directory_zip', ('dir.zip', open('dir.zip', 'rb'), 'application/zip'))]
	headers = {
		'X-API-KEY': api_key
	}
	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	os.remove("dir.zip")
	os.remove("zipout")

	if 200 <= response.status_code < 300:
		print("Your model is being built. Your model id is " + response.text)
		return
	if 400 <= response.status_code < 500:
		print("There was an issue processing your model. " + response.text)
		return

	print("There was an internal error while processing your model. If this problem persists, please contact sieve support")
