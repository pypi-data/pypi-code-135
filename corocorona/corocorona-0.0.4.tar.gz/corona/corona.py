import requests
import json
import sys

def printError(err_msg):
	print(err_msg)
	exit(1)


def parseJson(text):
	try:
		text = json.loads(text)
	except json.JSONDecodeError as e:
		printError(e)
	return text


def getCovidInfo():
	url = "https://data.corona.go.jp/converted-json/covid19japan-all.json"
	res = requests.get(url)
	text = res.text
	covid_info = parseJson(text)
	return covid_info


def getInputPref():
	if len(sys.argv) > 1:
		input_pref = sys.argv[1]
	else:
		input_pref = "東京都"
	return input_pref


def searchPrefs(area, input_pref):
	for i in range(47):
		if area[i]["name_jp"] == input_pref:
			return area[i]
	printError("find nothing.")


def printOutput(input_pref, npatients, last_update):
	print("[" + input_pref + "]")
	npatients = "{:,}".format(npatients)
	print("累計感染者数： " + npatients)
	print("(最終更新日：" + last_update + ")")


def printCorona():
	covid_info = getCovidInfo()[0]
	area = covid_info["area"]
	last_update = covid_info["lastUpdate"]
	input_pref = getInputPref()
	pref_info = searchPrefs(area, input_pref)
	npatients = pref_info["npatients"]
	printOutput(input_pref, npatients, last_update)
