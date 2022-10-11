# 2022.10.7  python xlabel.py  xlabel
import redis, time, requests,json,sys,collections,os,random, fire,  socket,traceback
now	= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))

def process(arr):
	try:
		if not 'label' in arr: return print ('invalid data in xlabel', arr) 
		redis.r.publish("pen-label", json.dumps(arr)) # to notify registered listeners

		ap,pen,page,item, label,tm,date,sub,ip = arr.get('ap',''), arr.get('pen',''), arr.get('page',''), arr.get('item',''), arr.get('label',''), arr.get('tm',time.time()), arr.get('date','') , arr.get('sub',''), arr.get('ip','')
		redis.kvr.hset(f"label:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}", f"submit-{tm}", json.dumps(arr), arr )  # new version , 2022.9.21
		redis.r.hset(f"label:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}", f"submit-{tm}", json.dumps(arr), arr )  # cache, mirror , added 2022.9.28
		#redis.r.hset(f"label:ap-{ap}:date-{date}:page-{page}:item:{item}", pen, label ) # for grafana, verbose , not store in kvr
		#redis.r.zadd(f"label:ap-{ap}:date-{date}:page-{page}:pen-tm", {pen: float(tm)}) # added 2022.10.5 , gears中登记了 label:*, 避免引发动作
		redis.r.hset(f"task:ap-{ap}:sub-{sub}:{date}-{page}", "pensum", redis.r.zcard(f"label:ap-{ap}:date-{date}:page-{page}:pen-tm"), arr ) # added 2022.10.8

		if item.startswith("composition") or item.startswith("essay"): redis.r.publish('pen-essay', msg['data']) #notify essay has been updated
	except Exception as ex:
		print ( ">>pen-label ex:", ex, "\t", arr, flush=True) 

def consume(stream, group='process', redis_port:int=6665, kvr_port:int=6666, host='172.17.0.1',  inkeng='ap.penly.cn:18461', inkchs='ap.penly.cn:18462', ttl:int=2, ratio:int=100,waitms=3600000):
	''' python xlabel.py  xlabel '''
	redis.reco		= { "en": f'http://{inkeng}/' ,"en_US": f'http://{inkeng}/' , "zh_CN":f'http://{inkchs}/'}
	redis.r			= redis.Redis(host=host, port=redis_port,  decode_responses=True)  # for ttl and publish 
	redis.kvr		= redis.Redis(host=host, port=kvr_port,  decode_responses=True) # for data store only
	redis.r.execute_command("config set notify-keyspace-events KEA") 
	redis.ttl = ttl
	redis.ratio = ratio # 2312/100 => 23
	try:
		redis.r.xgroup_create(stream, group,  mkstream=True)
	except Exception as e:
		print(e)

	consumer_name = f'consumer_{socket.gethostname()}_{os.getpid()}'
	print(f"Started: {consumer_name}|{stream}|{group}\t{now()}| ", redis.r, flush=True)
	while True:
		item = redis.r.xreadgroup(group, consumer_name, {stream: '>'}, count=1, noack=True, block= waitms )
		try:
			if not item: break
			print(now(), "\t|", item)
			id,params = item[0][1][0]  #[['_new_snt', [('1583928357124-0', {'snt': 'hello worlds'})]]]
			process(params)
			redis.r.xdel(stream, id) 
		except Exception as e:
			print(">>[xconsumeEx]", e, "\t|", item, "\t|",  now())

	redis.r.xgroup_delconsumer(stream, group, consumer_name)
	redis.r.close()
	print ("Quitted:", consumer_name, "\t",now())

if __name__ == '__main__': 
	fire.Fire(consume)