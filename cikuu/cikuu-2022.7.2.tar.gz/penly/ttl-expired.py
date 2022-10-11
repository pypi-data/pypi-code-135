# 2022.10.7 , one instance only 
import redis, time, json,sys,collections,os,random, fire,  socket,traceback

def listen(redis_port, name:str="xttl", host='172.17.0.1', debug:bool=False): 
	''' python ttl-expired.py 6665 '''
	redis.r	= redis.Redis(host=host, port=redis_port,  decode_responses=True)  # for ttl and publish 
	redis.r.execute_command("config set notify-keyspace-events KEA") 
	print (f"listen: ", redis.r,  flush=True)

	ps = redis.r.pubsub()
	ps.subscribe('__keyevent@0__:expired')
	for item in ps.listen():
		if item['type'] == 'message':
			try:
				if debug: print( item['data'], flush=True)
				redis.r.xadd(name, json.loads(item['data']) )
			except Exception as ex:
				print ( ">> penly process ex:", ex, "\t|", item, flush=True)

if __name__ == '__main__': 
	fire.Fire(listen)