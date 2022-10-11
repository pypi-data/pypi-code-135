# 2022.10.7  python xttl.py  xttl
import redis, time, requests,json,sys,collections,os,random, fire,  socket,traceback
from functools import lru_cache
now		= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
xyt		= lambda tups,mx=13779,my=19488: { "x": [ int (int(tup[0]) * 5600 / int(mx)) for tup in tups] ,  "y": [ int(int(tup[1]) * 7920/ int(my) ) for tup in tups],  "t": [int(tup[-1]) for tup in tups]}
xyts	= lambda stroke,mx=13779,my=19488: xyt([ s.split(',')  for s in stroke.split(' ')], mx, my)#reco = { "en": 'http://ap.penly.cn:18461/' ,"en_US": 'http://ap.penly.cn:18461/' , "zh_CN":'http://ap.penly.cn:18462/'}

@lru_cache(maxsize=None)
def hgetall(key:str='ap:CC1BE0E29824:sub-folder'): return redis.kvr.hgetall(key)
@lru_cache(maxsize=None)
def hpage(page:str='177.0.1'): return redis.kvr.hgetall(f"page:{page}")

def process(arr):  # move to xstream later, to increase perf 
	try:
		redis.r.publish("pen-ttlexpired", json.dumps(arr))
		ap,pen,page,item,date = arr.get('ap',''), arr.get('pen',''), arr.get('page',''), arr.get('item',''), arr.get('date','')
		if not item: return  #	if item.startswith('row-') and redis.r.exists(f"page:{page}:row-disable"): return 

		zkey	= f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}" 
		rows	= redis.kvr.zrange(zkey , 0, -1) # sorted by tm
		events	= {"events": [ xyts(row, hpage(page).get('max-x',13779), hpage(page).get('max-y',19488)) for row in rows ] }
		bbox	= requests.post( redis.reco[arr.get('lang','en')],data=json.dumps(events)).json() 
		label	= bbox.get('label','') # add cands later | list index out of range
		res		= {"key": zkey, "item": item, "label": label, "strokelen":len(rows), "ap":ap, "page":page, "pen":pen, 'date':date,"sub":hgetall(f"page:{page}").get('sub','en'), 'tm':time.time(), "stroke":";".join(rows) } #'cands': ",".join(bbox.get('words',[{}])[0].get('candidates',[])),
		redis.r.xadd("xlabel", res)  
		redis.r.publish("pen-ttl-label", json.dumps(res))
		print ( res, flush=True ) 
	except Exception as ex:
		print ( ">>ttl_expired ex:", ex, "\t|", arr, flush=True)
		exc_type, exc_value, exc_obj = sys.exc_info() 	
		traceback.print_tb(exc_obj)

def consume(stream, group='recoink', redis_port:int=6665, kvr_port:int=6666, host='172.17.0.1', inkeng='ap.penly.cn:18461', inkchs='ap.penly.cn:18462', ttl:int=2, ratio:int=100,waitms=3600000):
	''' python xttl.py  xttl '''
	redis.reco		= { "en": f'http://{inkeng}/' ,"en_US": f'http://{inkeng}/' , "zh_CN":f'http://{inkchs}/'}
	redis.r			= redis.Redis(host=host, port=redis_port,  decode_responses=True)  # for ttl and publish 
	redis.kvr		= redis.Redis(host=host, port=kvr_port,  decode_responses=True) # for data store only

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