# 2022.10.7,  will run at docker with several instances, no dependency
import redis, time, requests,json,sys,collections,os,random, fire,  socket,traceback
from functools import lru_cache
now			= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
avg		= lambda arr: sum(arr) / len(arr) if len(arr) > 0 else 0 
xy_avg	= lambda rows: (round(avg([int(row[0]) for row in rows]),1), round(avg([int(row[1]) for row in rows]),1))  

@lru_cache(maxsize=None)
def xy_to_item(page:str='177.0.1'): return redis.kvr.hgetall(f"page:{page}:xy_to_item")
@lru_cache(maxsize=None)
def hgetall(key:str='ap:CC1BE0E29824:sub-folder'): return redis.kvr.hgetall(key)

def process(arr):  
	''' quick:1713.537.31.92:BP2-0L3-03I-4V:1658389523.028:3752,1389,100,1658389523 3738,1395,428,1658389523 3719,1429,720,1658389523 3731,1602,832,1658389523 3797,1605,848,1658389523 3845,1551,808,1658389523 3876,1375,708,1658389523 3840,1330,748,1658389523 3782,1331,740,1658389523 '''
	try:
		if not 'stroke' in arr: return print("invalid data in xstroke:", arr ) 
		redis.r.publish("pen-stroke", json.dumps(arr)) 
		ap,page,pen,tm,date,stroke,ip = arr.get('ap',''),  arr.get('page',''), arr.get('pen',''), float(arr.get('tm', time.time())), arr.get('date',''), arr.get('stroke',''), arr.get('ip','') 

		redis.kvr.zadd(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}", {stroke:float(tm)}) # store in kvr6666, for replay, put to 8182 later 
		redis.r.zadd( f"strokenum:ap-{ap}:date-{date}:page-{page}:pen-{pen}", { redis.kvr.zcard(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}"):float(tm)}) # used to show speed , 2022.10.1, try to use ts if needed later 
	
		x,y			= xy_avg([ trp.split(",")  for trp in stroke.strip().split(" ")]) 
		item_key	= xy_to_item(page).get(f"{int(x/redis.ratio)},{int(y/redis.ratio)}","") #10,24 => select-1:A   x/100?
		redis.r.publish("pen-item", json.dumps({"item_key": item_key, "ap":ap, "date":date, "page":page, "pen":pen, "tm":float(tm),"stroke":stroke}) ) #redis.r.publish("pen_item", time.strftime("%Y%m%d %H:%M:%S", time.localtime(int(float(tm)))) + f" item_key:{item_key},ap:{ap},page:{page},pen:{pen},x={x},y={y},strokelen:{len(stroke.split(' '))}," + time.strftime("%Y%m%d %H:%M:%S", time.localtime(time.time())) ) # for debug only 
		if not item_key : return redis.kvr.zadd(f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:unk", {stroke:float(tm)}) # will NOT trigger xls writing 

		ar = item_key.split(':') # select-1:A
		item = ar[0].strip() #  fill-2 
		if len(ar) > 1: #':' in item_key:  
			redis.r.xadd("xlabel",{"item": item, "label": ar[-1].strip(), "ap":ap, "date":date, "page":page, "pen":pen, "sub":hgetall(f"page:{page}").get('sub','en'), "tm":float(tm),"stroke":stroke} ) 
		else:
			redis.r.setex(json.dumps({"penttl":redis.ttl, "lang":'zh_CN' if "zh_CN" in item else 'en_US', "ap":ap, "date":date, "page":page, "pen":pen, "item":item}), redis.ttl, "")

		redis.kvr.zadd(f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}", {stroke:float(tm)})  # how to do , if exists ? WRONG type conflicts
	except Exception as ex:
		print ( ">>pen_stroke ex:", ex, "\t", msg, flush=True) 
		redis.r.publish('pen-log', f"pen_stroke ex: {msg}")
		exc_type, exc_value, exc_obj = sys.exc_info() 	
		traceback.print_tb(exc_obj)

def consume(stream, group='dispatch', redis_port:int=6665, kvr_port:int=6666, host='172.17.0.1',  ttl:int=2, ratio:int=100,waitms=3600000):
	''' python xstroke.py  xstroke '''
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

''' 
psubscribe __key*@0__:*
publish __keyspace@0__:mykey del
publish __keyevent@0__:del mykey

docker run -d --restart=always --name rpen -p 6665:6379 wrask/redismod:spacy311
config set notify-keyspace-events KEA 
config set save ""

docker run -d --restart=always --name kvr -p 6666:6666 -v /data/kvr-penly:/var/lib/kvrocks/db kvrocks/kvrocks:v2.0.6
docker run -d --rm --name redUI -e REDIS_1_HOST=172.17.0.1 -e REDIS_1_NAME=local-136 -e REDIS_1_PORT=6379 -e REDIS_2_HOST=192.168.44.3 -e REDIS_2_NAME=penly-44 -e REDIS_2_PORT=6379 -e REDIS_3_HOST=172.17.0.1 -e REDIS_3_NAME=redis6665 -e REDIS_3_PORT=6665 -e REDIS_4_HOST=172.17.0.1 -e REDIS_4_NAME=penkvr6666 -e REDIS_4_PORT=6666  -p 6300:80 erikdubbelboer/phpredisadmin:v1.13.2

docker run -d --name insight -p 8001:8001 redislabs/redisinsight
#xyt	= lambda tups: { "x": [int(tup[0]) for tup in tups] ,  "y": [int(tup[1]) for tup in tups],  "t": [int(tup[-1]) for tup in tups]}
#xyts	= lambda stroke: xyt([ s.split(',')  for s in stroke.split(' ')])#reco = { "en": 'http://ap.penly.cn:18461/' ,"en_US": 'http://ap.penly.cn:18461/' , "zh_CN":'http://ap.penly.cn:18462/'}
'''