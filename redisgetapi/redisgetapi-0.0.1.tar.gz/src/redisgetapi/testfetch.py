from fetch import RedisEndPoint, cli_call, script_call




def getNgrok(url,host,port,expire):
	return script_call(url,host,port,expire)

url = 'https://a0a0-91-156-176-20.eu.ngrok.io/api/v1/public/'
host = 'localhost'
port = 6379
expire = 300

print(script_call(url,host,port,expire))
