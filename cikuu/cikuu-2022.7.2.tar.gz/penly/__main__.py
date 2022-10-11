# 2022.9.23  https://github.com/larksuite/oapi-sdk-python/blob/4274991a0c112f5b8e5d99d798e3bcd5b2b748e3/sample/api/docx.py
from penly import * 
now	= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))

def testblpop():
	pass 

def replay(ap='CC1BE0E29824', date='20220929',page='0.0.0', pen='D80BCB7002AE', minsec:int=2):
	''' python -m penly replay , add the corresponding sleeping time '''
	rows = redis.kvr.zrange(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}",0,-1, withscores=True)
	for i, row in enumerate(rows):
		if i > 0 : time.sleep( min( int(rows[i][1]) - int(rows[i-1][1]), minsec)  )
		print (row[1], redis.r.xadd("xstroke", {"ap":ap, "page":page, "pen":pen, "tm":float(row[1]), "stroke":row[0], "date":time.strftime("%Y%m%d", time.localtime(int(float(row[1]))))}) )
		#print (row[1], redis.r.publish("pen_stroke", f"{ap}:{page}:{pen}:{row[1]}:{row[0]}"), flush=True)

filelist = lambda folder:  [file.split(".")[0] for root, dirs, files in os.walk(folder,topdown=False) for file in files if file.endswith(".py") and not file.startswith("_") ]
#print (filelist('pen-bitrec')) 

def connect(name, debug:bool=False): 
	''' python -m penly connect pen-bitrec '''
	funcs = [ __import__(f"penly.{name}.{file}", fromlist=['process']) for file in filelist(name) ] # no exception handler
	print (f"listen: {name}, with all the files under {name}, process inside | ", funcs, redis.r, redis.kvr, flush=True)
	ps = redis.r.pubsub()
	ps.subscribe(name)
	for item in ps.listen():
		if item['type'] == 'message':
			try:
				if debug: print( item['data'], flush=True)
				[x.process(json.loads(item['data']) ) for x in funcs]
			except Exception as ex:
				print ( ">> penly process ex:", ex, "\t|", item, flush=True)

def subscribe(name, func, debug:bool=False): 
	''' python -m penly subscribe pen_label pen-label-toxls '''
	print (f"listen: {name} with {func}", redis.r, redis.kvr, flush=True)
	x = __import__(func if '.' in func else f"penly.{func}", fromlist=['process'])
	ps = redis.r.pubsub()
	ps.subscribe(name)
	for item in ps.listen():
		if item['type'] == 'message':
			try:
				if debug: print( item['data'], flush=True)
				x.process(json.loads(item['data']) ) #  if item['data'].startswith("{") or item['data'].startswith("[") else item['data']) 
			except Exception as ex:
				print ( ">> penly process ex:", ex, "\t|", item, flush=True)

def consume(stream, func, waitms=3600000):
	''' python -m penly consume xlabel pen-label-toxls '''
	group = func 
	try:
		redis.r.xgroup_create(stream, group,  mkstream=True)
		x = __import__(func if '.' in func else f"penly.{func}", fromlist=['process'])
	except Exception as e:
		print(e)

	consumer_name = f'consumer_{socket.gethostname()}_{os.getpid()}'
	print(f"Started: {consumer_name}|{stream}|{group}\t{now()}| ", r, flush=True)
	while True:
		item = redis.r.xreadgroup(group, consumer_name, {stream: '>'}, count=1, noack=True, block= waitms )
		try:
			if not item: break
			print(now(), "\t|", item)
			id,params = item[0][1][0]  #[['_new_snt', [('1583928357124-0', {'snt': 'hello worlds'})]]]
			x.process(params)
			redis.r.xdel(stream, id) 
		except Exception as e:
			print(">>[xconsumeEx]", e, "\t|", item, "\t|",  now())

	redis.r.xgroup_delconsumer(stream, group, consumer_name)
	redis.r.close()
	print ("Quitted:", consumer_name, "\t",now())

if __name__ == '__main__': 
	fire.Fire({"subscribe":subscribe, "replay":replay, "consume":consume, "connect":connect})

'''
docker run -d --restart=always --name rpen -p 6665:6379 wrask/redismod:spacy311
config set notify-keyspace-events KEA 
config set save ""

docker run -d --restart=always --name kvr -p 6666:6666 -v /data/kvr-penly:/var/lib/kvrocks/db kvrocks/kvrocks:v2.0.6
docker run -d --rm --name redUI -e REDIS_1_HOST=172.17.0.1 -e REDIS_1_NAME=local-136 -e REDIS_1_PORT=6379 -e REDIS_2_HOST=192.168.44.3 -e REDIS_2_NAME=penly-44 -e REDIS_2_PORT=6379 -e REDIS_3_HOST=172.17.0.1 -e REDIS_3_NAME=redis6665 -e REDIS_3_PORT=6665 -e REDIS_4_HOST=172.17.0.1 -e REDIS_4_NAME=penkvr6666 -e REDIS_4_PORT=6666  -p 6300:80 erikdubbelboer/phpredisadmin:v1.13.2

docker run -d --name insight -p 8001:8001 redislabs/redisinsight

websocketd --port 6664 --address=0.0.0.0 python print_channel.py pen_* --host 172.17.0.1 --port 6665

def listen(name, host='data.penly.com', redis_port=6665, kvr_port=6666): 
	redis.r		= redis.Redis(host=host, port=redis_port, decode_responses=True) 
	redis.kvr	= redis.Redis(host=host, port=kvr_port,   decode_responses=True) 
	print ("started:", redis.r, redis.kvr, flush=True)
	ps = redis.r.pubsub()
	ps.subscribe(name)
	for item in ps.listen():
		if item['type'] == 'message':
			process(item['data']) 

{'key': 'stroke:ap-CC1BE0E29824:date-20220923:page-177.0.1:pen-D80BCB7002AE:item-fill-12', 'item': 'fill-12', 'label': 'per the d n', 'cands': ['per', 'pen', 'Pen', 'pes', 'Per'], 'strokelen': 8, 'ap': 'CC1BE0E29824', 'page': '177.0.1', 'pen': 'D80BCB7002AE', 'date': '20220923', 'tm': 1663940582.4785774, 'stroke': '2406,8515,141,1663936409 2415,8596,201,1663936409 2432,8821,55,1663936409 2436,8931,1,1663936409 2444,8982,1,1663936409 2444,8982,0,1663936409;2371,8556,99,1663936409 2388,8550,105,1663936409 2446,8551,163,1663936409 2501,8582,173,1663936409 2514,8662,162,1663936409 2514,8662,1,1663936409 2514,8662,1,1663936409 2513,8661,0,1663936409;2506,8666,55,1663936409 2551,8667,86,1663936409 2575,8666,92,1663936409 2615,8660,110,1663936409 2638,8649,103,1663936409 2650,8626,108,1663936409 2653,8600,127,1663936409 2621,8581,177,1663936409 2577,8610,154,1663936409 2571,8649,136,1663936409 2620,8710,40,1663936409 2642,8703,24,1663936409 2668,8682,23,1663936409 2686,8656,24,1663936409 2723,8603,53,1663936410 2749,8578,87,1663936410 2756,8611,183,1663936410 2764,8716,171,1663936410 2770,8666,108,1663936410 2855,8675,1,1663936410 2853,8682,1,1663936410 2850,8693,0,1663936410;3097,8628,77,1663936410 3153,8620,84,1663936410 3192,8613,23,1663936410 3192,8613,1,1663936410 3282,8603,0,1663936410;3189,8518,103,1663936411 3169,8545,118,1663936411 3191,8615,127,1663936411 3196,8658,129,1663936411 3203,8718,89,1663936411 3203,8718,1,1663936411 3203,8718,0,1663936411;3300,8517,98,1663936411 3310,8682,130,1663936411 3314,8710,94,1663936411 3346,8683,55,1663936411 3356,8625,57,1663936411 3361,8604,69,1663936411 3392,8660,120,1663936411 3391,8689,120,1663936411 3397,8714,105,1663936411 3427,8708,55,1663936411 3452,8700,57,1663936411 3490,8661,63,1663936412 3494,8617,114,1663936412 3516,8717,1,1663936412 3535,8711,1,1663936412 3535,8711,0,1663936412;3938,8589,81,1663936412 3890,8573,134,1663936412 3868,8597,153,1663936412 3862,8629,164,1663936412 3857,8675,161,1663936412 4007,8565,26,1663936412 4023,8519,34,1663936412 4034,8478,55,1663936412 4028,8436,97,1663936412 4016,8413,162,1663936412 4007,8455,185,1663936412 4003,8539,189,1663936412 3998,8614,156,1663936412 4001,8700,91,1663936412 4010,8723,47,1663936412 4019,8731,1,1663936412 4046,8709,1,1663936412 4064,8684,0,1663936412;4345,8582,64,1663936413 4368,8615,168,1663936413 4381,8641,200,1663936413 4392,8685,206,1663936413 4394,8717,211,1663936413 4396,8679,104,1663936413 4500,8655,39,1663936413 4514,8664,1,1663936413 4508,8671,1,1663936413 4508,8671,0,1663936413'}

pen:D80BCB7002AE:date-20220721:ap-CC1BE0E29824:sub-en:page-177.0.0 shtcnnqQawzjyWGkTXmPRgeNxlf
[{'code': 0, 'data': {'revision': 3, 'spreadsheetToken': 'shtcnvg0AqGC0SW4fRr7SXsKkkf', 'updatedCells': 1, 'updatedColumns': 1, 'updatedRange': 'fc8edf!C10:C10', 'updatedRows': 1}, 'msg': 'success'}]

HSET "ap:CC.1B.E0.E1.FA.60" "date-20220721:sub-en:pensfolder" "fldcnZVtfWLh7MAFuXUkpanixAh"
HSET "ap:CC.1B.E0.E1.FA.60" "date-20220721:sub-en:xls" "shtcnSv5b8qoonqJLF8noenOMMd"
HSET "ap:CC.1B.E0.E1.FA.60" "date-20220721:sub-en:xls:page-1713.537.31.92:sheet" "4Gode8"
HSET "ap:CC.1B.E0.E1.FA.60" "mac" "CC:1B:E0:E1:FA:60"
HSET "ap:CC.1B.E0.E1.FA.60" "madeby" "tql"
HSET "ap:CC.1B.E0.E1.FA.60" "rootfolder" "fldcnxgWQpoXvVhVMEalnKIFLkd"
HSET "ap:CC.1B.E0.E1.FA.60" "sub-en:rootfolder" "fldcnZQKBt94RIlxyyf2Nt9z1oh"
HSET "ap:CC.1B.E0.E1.FA.60" "sub-en:xlstemplate" ""

CC1BE0E1FA60  - 44
CC1BE0E29824  - 136

HSET "ap:CC1BE0E29824:sub-en" "root-folder" "fldcnZQKBt94RIlxyyf2Nt9z1oh"
HSET "ap:CC1BE0E29824:sub-en" "xls-template" "shtcnMWL7GZMrJbWJCntkA9uiy6"
HSET "ap:CC1BE0E29824:sub-en:month-folder" "202207" "fldcnvi3Lt78ir8fvYa35HUyauh"
HSET "ap:CC1BE0E29824:sub-en:month-folder" "202208" "fldcnTajGpTSDE9TElgWbuNKkxg"

def apsub_penpage_datexls0(ap, sub, pen, page, date): #print (apsub_penpage_datexls ('CC1BE0E1FA60', 'en', "BP2-0L3-03I-4V","1713.537.31.92", '20220723') )
	# every pen every day -> one xls  pen:BP2-0L3-03I-4V:date-20220721:ap-CC.1B.E0.E1.FA.60:sub-en:page-1713.537.31.92 -> xls page-1713.537.31.92
	try:
		if redis.kvr.hexists(f"pen:{pen}:date-{date}:ap-{ap}:sub-{sub}:page-{page}", "xls"):	
			return redis.kvr.hget(f"pen:{pen}:date-{date}:ap-{ap}:sub-{sub}:page-{page}", "xls")
		template = hpage(page)["xls-template"]
		res	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={
    "name": f"{date}-{ap}-{sub}-pen-{pen[-2:]}",
    "type": "sheet",
    "folder_token": apsub_date_folder(ap, sub, date) 
}).json() 
		xls  = res.get('data',{}).get('file',{}).get('token','')
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{xls}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		redis.kvr.hset(f"pen:{pen}:date-{date}:ap-{ap}:sub-{sub}:page-{page}", "xls", xls)
		return xls
	except Exception as ex:
		print ( ">>ap_sub_pen_date_xls ex:", ex, "\t|", ap, sub, date, flush=True)

@lru_cache(maxsize=None)
def apsub_date_folder(ap, sub, date, hkey='pensfolder'): 
	try:
		if redis.kvr.hexists(f"ap:{ap}:sub-{sub}:date-{date}", hkey):	return redis.kvr.hget(f"ap:{ap}:sub-{sub}:date-{date}", hkey)
		month_folder = apsub_month_folder(ap, sub, date[0:6]) 
		folder	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/create_folder", headers = headers(), json={"name": f"{date}-{sub}","folder_token": month_folder}).json().get('data',{}).get('token','')
		if folder: redis.kvr.hset(f"ap:{ap}:sub-{sub}:date-{date}", hkey, folder)
		return folder 		
	except Exception as ex:
		print ( ">>apsub_date_folder ex:", ex, "\t|", ap, sub, date, flush=True)
#apsub_date_folder ('CC1BE0E1FA60', 'en', '20220722')

@lru_cache(maxsize=None)
def apsub_month_folder(ap, sub, month): # en-202207
	try:
		folder =  redis.kvr.hget(f"ap:{ap}:sub-folder", f"{sub}-{month}")
		if folder : return folder 
		parent_folder = hgetall(f"ap:{ap}").get("rootfolder",'') # must exists 
		folder	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/create_folder", headers = headers(), json={"name": f"{sub}-{month}","folder_token": parent_folder}).json().get('data',{}).get('token','')
		if folder: redis.kvr.hset(f"ap:{ap}:sub-folder", f"{sub}-{month}", folder)
		return folder 		
	except Exception as ex:
		print ( ">>ap_month_folder ex:", ex, "\t|", ap, sub, month, flush=True)
		traceback.print_exc()

@lru_cache(maxsize=None)
def apsub_date_pensfolder(ap, sub, date): 
	try:
		folder = redis.kvr.hget(f"ap:{ap}:sub-folder", f"{sub}-{date}")
		if folder : return folder
		month_folder = apsub_month_folder(ap, sub, date[0:6]) 
		folder	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/create_folder", headers = headers(), json={"name": f"{sub}-{date}","folder_token": month_folder}).json().get('data',{}).get('token','')
		if folder: redis.kvr.hset(f"ap:{ap}:sub-folder", f"{sub}-{date}", folder)
		return folder 		
	except Exception as ex:
		print ( ">>apsub_date_pensfolder ex:", ex, "\t|", ap, sub, date, flush=True)
#apsub_date_pensfolder ('CC1BE0E29824', 'en', '20220722')

@lru_cache(maxsize=None)
def apsub_penpage_datexls(ap, sub, pen, page, date): 
	# every pen every day -> one xls  pen:BP2-0L3-03I-4V:date-20220721:ap-CC.1B.E0.E1.FA.60:sub-en:page-1713.537.31.92 -> xls page-1713.537.31.92
	try:
		sub	= hpage(page).get('sub','en') 
		xls = redis.kvr.hget(f"ap:{ap}:date-{date}:page-{page}:pen-xls", pen)
		if xls : return xls
		template = hgetall(f"page:{page}")["xls-template"] # must exists 
		xls	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={"name":
			f"{date}-{hap(ap).get('title',ap)}-{hapsub(ap,sub).get('title','en')}-{pen_name(ap,pen)}",	"type": "sheet","folder_token": date_folder(ap, sub, date)  }).json().get('data',{}).get('file',{}).get('token','') 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{xls}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		redis.kvr.hset(f"ap:{ap}:date-{date}:page-{page}:pen-xls", pen, xls)
		return xls 
	except Exception as ex:
		print ( ">>ap_sub_pen_date_xls ex:", ex, "\t|", ap, sub, date, flush=True)

@lru_cache(maxsize=None)
def apsub_page_datexls(ap, sub, page, date): 
	try:
		arr = redis.kvr.hgetall(f"ap:{ap}:sub-{sub}:date-{date}")
		if len(arr) >= 3 : return arr #{'pensfolder': 'fldcnlSqoqq5geFj6v75n8ZrUHh', 'xls': 'shtcntWa5ubq8vx7HtNE8qbRO7L', 'page-1713.537.31.92': 'fc8edf'}
		arr['pensfolder'] = apsub_date_folder(ap, sub, date) 

		template = hapsub(ap,sub)["xls-template"]
		res	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={
    "name": f"date-{date}:ap-{ap}:sub-{sub}",
    "type": "sheet",
    "folder_token": apsub_month_folder(ap, sub, date[0:6])
}).json() 
		xls  = res.get('data',{}).get('file',{}).get('token','')
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{xls}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		arr.update( {"xls": xls, f"page-{page}": first_sheet(xls)}) # assuming there is only one sheet in the template 
		redis.kvr.hmset(f"ap:{ap}:sub-{sub}:date-{date}", arr )
		return arr
	except Exception as ex:
		print ( ">>apsub_page_datexls ex:", ex, "\t|", ap, sub, date, flush=True)
		return {}
#print (apsub_page_datexls ('CC.1B.E0.E1.FA.60', 'en', "1713.537.31.92", '20220723'))

@lru_cache(maxsize=None)
def hpen(pen:str='BP2-0L3-03I-4V'): return redis.kvr.hgetall(f"pen:{pen}")
@lru_cache(maxsize=None)
def hpage(page:str='1713.537.31.92'): return redis.kvr.hgetall(f"page:{page}")
@lru_cache(maxsize=8192)
def hap(ap:str='CC1BE0E1FA60'): return redis.kvr.hgetall(f"ap:{ap}")
@lru_cache(maxsize=None)
def hapsub(ap:str='CC1BE0E1FA60', sub:str='en'): return redis.kvr.hgetall(f"ap:{ap}:sub-{sub}")

@lru_cache(maxsize=None)
def ap_datebit(ap, page, date): 
	try:
		token = redis.kvr.hget(f"ap:{ap}:date-{date}:page-{page}:ap-filetoken", "bitable")
		if token : return token
		sub	= hgetall(f"page:{page}").get('sub','en') 
		template = hgetall(f"page:{page}")["ap-bitable"] # must exists 
		res	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={"name":
			f"{date}-{ap_title(ap)}-{sub_title(page)}",	"type": "bitable","folder_token":date_folder(ap, sub, date)   }).json()
		print(template, res) 
		token = res.get('data',{}).get('file',{}).get('token','') 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{token}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		redis.kvr.hset(f"ap:{ap}:date-{date}:page-{page}:ap-filetoken", "bitable", token)
		return token 
	except Exception as ex:
		print ( ">>ap_datebit ex:", ex, "\t|", ap, page, date, flush=True)
		traceback.print_exc()

def walk(folder):
	for root, dirs, files in os.walk(folder,topdown=False):
		for file in files: 
			if file.endswith(".py") and not file.startswith("_") : 
				file = file.split(".")[0]
				st.write(f"[{file}](?f={file})")

[program:pubsub-pen-bitrec-homebit]
directory=/data/cikuu/pypi/penly
command=python -m penly subscribe pen_bitrec pen-bitrec-homebit
startsecs = 5 
autorestart = true 
startretries = 3
redirect_stderr=true 
numprocs=1
process_name=%(program_name)s

[program:connect-pen-label]
directory=/data/cikuu/pypi/penly
#command=python -m penly subscribe pen_label pen-label-pagebit
command=python -m penly connect pen-label
startsecs = 5 
autorestart = true 
startretries = 3
redirect_stderr=true 
numprocs=1
process_name=%(program_name)s
stdout_logfile=/data/cikuu/pen-label.log
stdout_logfile_maxbytes=20MB

#[program:kvr-stroke-6665-6666]
#directory=/data/cikuu/pypi/penly
#command=python kvr-stroke.py 6665 6666
#command=python tmp-stroke.py 6665 6666
#startsecs = 5 
#autorestart = true 
#startretries = 3
#redirect_stderr=true 
#numprocs=1
#process_name=%(program_name)s
'''