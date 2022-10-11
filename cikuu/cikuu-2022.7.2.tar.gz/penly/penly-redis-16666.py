# 2022.9.26 cp from uviredis.py  | rhost=172.18.0.1 uvicorn penly-redis-6667:app --host 0.0.0.0 --port 6667 --reload 
import json,requests,hashlib,os,time,redis,fastapi, uvicorn , random,asyncio, platform 
from fastapi.responses import HTMLResponse, StreamingResponse, PlainTextResponse,  RedirectResponse
from fastapi.requests import Request
from collections import Counter
from typing import Iterator
app			= fastapi.FastAPI()
rhost		= os.getenv('rhost', 'data.penly.cn') # 136
redis.r		= redis.Redis(host=rhost, port=os.getenv('redis_port', 6665), decode_responses=True) 
redis.kvr	= redis.Redis(host=rhost, port=os.getenv('kvr_port', 6666),  decode_responses=True) 
now			= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
from fastapi.staticfiles import StaticFiles #http://localhost/static/index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', tags=["feishu"])
def home(): return HTMLResponse(content=f"<h2> penly, feishu redis api on 6665(redis) and 6666(kvrocks) </h2><a href='/docs'> docs </a> | <a href='/redoc'> redoc </a>")

from penly import *
@app.get('/feishu/date_folder', tags=["feishu"])
def feishu_date_folder(ap:str="CC1BE0E29824", sub:str='en', date:str=None):
	''' 返回  apsub 在某天的 folder , created if none '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
	return date_folder(ap, sub, date)

@app.get('/feishu/snt/editdistance', tags=["feishu"])
def feishu_snt_editdistance(snt:str="how are you :", refer:str='how are you?'):
	''' 2022.10.11'''
	import editdistance # pip install editdistance  https://pypi.org/project/editdistance/
	from nltk.tokenize import wordpunct_tokenize # pip install nltk  https://www.nltk.org/api/nltk.tokenize.html
	arr_snt = wordpunct_tokenize(snt.lower())
	arr_ref = wordpunct_tokenize(refer.lower())
	ed		= editdistance.eval(arr_ref, arr_snt )
	wc		= len(arr_ref)
	return round( abs(wc - ed) / float(wc), 2)

@app.get('/feishu/wiki/date_file', tags=["feishu"])
def feishu_wiki_date_file(ap:str="CC1BE0E29824", page:str='0.0.0', date:str=None, suffix:str="page-xls"):
	''' date=20220930 '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
	#return wiki_date_file(ap, page, date, suffix)
	return wiki_date_pagefile(ap, page, date, suffix)

@app.get('/feishu/wiki/delete', tags=["feishu"])
def feishu_wiki_delete(ap:str="CC1BE0E29824", page:str='0.0.0', date:str="20220628", suffix:str="page-bitable"):
	''' 删除wiki中的目录或者文件， 需要同步删除 redis 中的 wiki:space-{space}里面的item '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
	sub		= hgetall(f"page:{page}").get('sub','en')
	space	= sub_wiki_space(ap, sub) 
	res		= redis.kvr.hget(f"wiki:space-{space}", f"{date}-{page}:{suffix}")
	if res is None or not res : return "No items found"

	redis.kvr.hdel(f"wiki:space-{space}", f"{date}-{page}:{suffix}")
	res		= json.loads(res) 
	token = res['obj_token']
	return requests.delete(f"https://open.feishu.cn/open-apis/drive/v1/files/{token}", headers = headers(), json={"type": res['obj_type']}).json()

@app.get('/feishu/date/penxls', tags=["feishu"])
def feishu_date_penxls(ap:str="CC1BE0E29824", page:str="0.100.0", pen:str="D80BCB7002AE", date:str=None): 
	''' ap:{ap}:pen-xls  |每天 (ap,date,  page,pen) 生成一个 sheet 文件 | every pen every day -> one pen xls  '''
	try:
		if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
		v = redis.kvr.hget(f"ap:{ap}:pen-xls", f"date-{date}:page-{page}:pen-{pen}")  
		if v : return json.loads(v) # {"token":"xx", "sheet":"zz"}

		sub		= hgetall(f"page:{page}").get('sub','en') 
		token	= clone(hgetall(f"page:{page}")["pen-xls-template"], f"{date}-{ap_title(ap)}-{sub_title(sub)}-{pen_name(ap,pen)}", date_folder(ap, sub, date) , type='sheet')
		if token is not None:
			arr		= {"token":token, "sheet": hgetall(f"page:{page}")["pen-xls-sheetid"] }
			redis.kvr.hset(f"ap:{ap}:pen-xls", f"date-{date}:page-{page}:pen-{pen}",json.dumps(arr))  
			redis.kvr.hset(f"ap:{ap}:pen-xls", token,  json.dumps({"key":f"date-{date}:page-{page}:pen-{pen}", "ap":ap, "page":page, "pen":pen, "date":date}))  
			return arr
		return {} #{'token': 'shtcnA2LVeUYF3QLT9EqMr7c3Qc', 'sheet': '96bdd1'}
	except Exception as ex:
		print ( ">>pen_datexls ex:", ex, "\t|", ap, page, pen, date, flush=True)
		traceback.print_exc()
		return {}

@app.get('/feishu/date/apbitable', tags=["feishu"])
def feishu_date_apbitable(ap:str="CC1BE0E29824", page:str="0.0.0", date:str=None): 
	''' ap:{ap}:ap-bitable | {'bitable': 'bascnV4mFStGOfsdSdiimtA5uBg', 'table': 'tblbXGoSAB2lSG3l'}  | 每天 (ap,date, page) 生成一个 bitable文件 '''
	try:
		if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
		v = redis.kvr.hget(f"ap:{ap}:ap-bitable", f"date-{date}:page-{page}" ) # {"bitable": xxx, "table": xxx}
		if v : return json.loads(v) 

		token	= clone(hgetall(f"page:{page}")["ap-bitable-template"], f"{ap_title(ap)}-{date}-{page_title(page)}", date_folder(ap, hgetall(f"page:{page}").get('sub','en') , date) )
		res		= requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json()
		print ( token, res ) 
		arr		= {"bitable":token, "table":res['data']['items'][0]['table_id']} # first_table 
		redis.kvr.hset(f"ap:{ap}:ap-bitable", f"date-{date}:page-{page}", json.dumps(arr)) # del in pair 
		redis.kvr.hset(f"ap:{ap}:ap-bitable", token, json.dumps({"key":f"date-{date}:page-{page}", "ap":ap,"page":page,"date":date}))
		return arr
	except Exception as ex:
		print ( ">>apdate_bitable ex:", ex, "\t|", ap, page, date, flush=True)
		traceback.print_exc()
		return {}
#print ( feishu_date_apbitable()) 
#bascn3AoqhK9OZHqGzIooGGbC3e {'code': 1254002, 'msg': 'Fail', 'error': {'log_id': '20220929170542010208016088271AB1E5'}}

@app.post('/feishu/bitable/upsert', tags=["feishu"])
def upsert_bitable(arr:dict={"笔号":"pen-ZZ"},  bitable:str="bascniTZYLHQFZjfN9ondVkAeAf", table:str="tbloeIV1SvLt4Img", recid:str=None): 
	''' return recid = res.get('data',{}).get('record', {}).get('record_id', '') '''
	data = {"fields": arr} if not 'fields' in arr else arr 
	res = requests.post(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records",headers = headers(),json=data).json() if recid is None else  requests.put(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records/{recid}",headers = headers(),json=data).json()
	if res.get('msg','') == 'RecordIdNotFound': #{'code': 1254043, 'msg': 'RecordIdNotFound', 'error': {'log_id': '202209280751270102091570260A1F6A7B'}}
		res = requests.post(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records",headers = headers(),json=data).json() # invalid recid in the redis
	return res 

@app.get('/feishu/date/apbitable/clear', tags=["feishu"])
def feishu_date_apbitable_clear(ap:str="CC1BE0E29824", page:str="0.100.0", date:str="20220728"): 
	''' '''
	v = redis.kvr.hget(f"ap:{ap}:ap-bitable", f"date-{date}:page-{page}" )
	if v or v is not None: 
		redis.kvr.hdel(f"ap:{ap}:ap-bitable", f"date-{date}:page-{page}" )
		redis.kvr.hdel(f"ap:{ap}:ap-bitable", json.loads(v).get('token','') )
	return v 

@app.get('/feishu/write_stroke_png', tags=["feishu"])
def feishu_write_stroke_png(xls:str="shtcnMWL7GZMrJbWJCntkA9uiy6", range:str='fc8edf!D5:D5', zkey:str='strokelog:ap-CC1BE0E29824:date-20220925:page-0.100.0:pen-D80BCB7002AE'):
	''' 把 stroke 写到 excel '''
	return write_stroke_png (xls, range, zkey)

@app.get('/strokelog/replay', tags=["stroke"])
def strokelog_replay(ap:str="CC1BE0E29824", page:str="0.0.0", penlist:str=None, date:str=None):
	''' 模拟重新投递到 6665 某笔某天的数据，log数据不会被覆盖  D80BCB7002AE,D80BCB7002AF '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() ))
	if penlist is None or not penlist: 
		return [ [redis.r.publish("pen_stroke", f"{ap}:{page}:{k.split('-')[-1]}:{tm}:{stroke}") for stroke, tm in redis.kvr.zrange(k,0,-1, withscores=True)] for k in redis.kvr.keys(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-*") ]
	return [ [redis.r.publish("pen_stroke", f"{ap}:{page}:{pen}:{tm}:{stroke}") for stroke, tm in redis.kvr.zrange(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}",0,-1, withscores=True)] for pen in penlist.strip().split(',') ]
#print (strokelog_replay()) 

def polyline(stroke:str='903,554,100,1656990923 911,559,161,1656990923 917,552,201,1656990923', xmin:int=0, ymin:int=0, width:int=10, color:str='black'): 
	res = []
	for s in stroke.split(' '): 
		arr = s.split(',')
		if len(arr) >= 4:  res.append( f"{int(arr[0]) - xmin},{int(arr[1]) - ymin}") 
	plist = " ".join(res)
	return f'<polyline points="{plist}" style="fill:none;stroke:{color};stroke-width:{width}" />'

@app.get('/stroke/itemsvg', response_class=HTMLResponse, tags=["stroke"])
def penly_itemsvg(ap:str="CC1BE0E29824", page:str="177.0.1", pen:str="D80BCB7002AE", date:str=None, item:str="item-fill-12", start:int=0, end:int=-1, color:str='black', title_color:str='darkgray', width:int=10, full:bool=True): 
	''' 一道题的笔迹原迹 , date=20220923 '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
	pen_name = redis.kvr.hget(f"ap:{ap}:pen-name", pen)
	if not pen_name: pen_name = f"pen-" + pen[-2:] #	<h2 style='color:darkgray'>王伟</h2>

	strokes = redis.kvr.zrange(f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:{item}", start, end)
	xypts	= [ ar.split(',') for stroke in strokes for ar in stroke.split(':')[-1].split(' ')]
	if not xypts: return ""
	x_min	= min([int(x) for x,y,p,t in xypts ])
	x_max	= max([int(x) for x,y,p,t in xypts ])
	y_min	= min([int(y) for x,y,p,t in xypts ])
	y_max	= max([int(y) for x,y,p,t in xypts ])
	polylines = "\n".join([ polyline(stroke, x_min, y_min, width, color) for stroke in strokes ])
	return HTMLResponse(content=f'<h2 style="color:{title_color}">{pen_name}</h2><svg viewBox="0 0 {5600 if full else x_max - x_min} {7920 if full else y_max - y_min}">{polylines}</svg>')

@app.get('/strokelog', response_class=HTMLResponse, tags=["stroke"])
def strokelog_svg(zkey:str="strokelog:ap-CC1BE0E29824:date-20220925:page-0.100.2:pen-D80BCB7002AE", start:int=0, end:int=-1, color:str='black', title_color:str='darkgray', width:int=10, full:bool=True): 
	''' 每支笔每天的原迹，有可能 无item信息  '''
	strokes = redis.kvr.zrange(zkey, start, end)
	xypts	= [ ar.split(',') for stroke in strokes for ar in stroke.split(':')[-1].split(' ')]
	x_min,x_max,y_min,y_max	= min([int(x) for x,y,p,t in xypts ]) , max([int(x) for x,y,p,t in xypts ]),  min([int(y) for x,y,p,t in xypts ]),  max([int(y) for x,y,p,t in xypts ])
	polylines = "\n".join([ polyline(stroke, x_min, y_min, width, color) for stroke in strokes ])
	return HTMLResponse(content=f'<svg viewBox="0 0 {5600 if full else x_max - x_min} {7920 if full else y_max - y_min}">{polylines}</svg>')

mid = lambda s, left, right=':':  s.split(left)[-1].split(right)[0]
@app.get('/grafana/pensum', tags=["grafana"])
def ap_pensum(ap='CC1BE0E29824', sub:str='en'):	 #, date='20220923',page='177.0.1'
	''' 2022.9.25 '''
	res = []
	dic = redis.kvr.hgetall(f"sub:{sub}")
	for k in redis.kvr.keys(f"ap:{ap}:date-*"): #
		if k.endswith(":pen-xls"): 
			page = k.split('page-')[-1].split(':')[0]
			if page in dic :  res.append( {'ap':ap, 'sub':sub, 'date':mid(k, 'date-'),  'page':page, 'pensum': redis.kvr.hlen(k) } ) 
	return res

@app.get('/grafana/apdate_pagepen', tags=["grafana"])
def apdate_pagepen(ap='CC1BE0E29824', date:str=None):	 
	''' date=20220925  ap:CC1BE0E29824:date-20220925:page-0.100.0:pen-xls  '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() ))
	res = []
	for k in redis.kvr.keys(f"ap:{ap}:date-{date}:*"): #
		if k.endswith(":pen-xls"): 
			page = k.split('page-')[-1].split(':')[0]
			[res.append( {'ap':ap,  'date':date,  'page':page, 'pen':pen, 'xls':xls } ) for pen, xls in redis.kvr.hgetall(k).items() ]
	return res

@app.get('/grafana/ap', tags=["grafana"])
def ap_pagepen(ap='CC1BE0E29824'):	 
	''' ap:CC1BE0E29824:date-20220925:page-0.100.0:pen-xls  '''
	res = []
	for k in redis.kvr.keys(f"ap:{ap}:*"): #
		if k.endswith(":pen-xls"): 
			[res.append( {'ap':ap,  'date':mid(k, 'date-'), 'page':mid(k, 'page-'), 'pen':pen, 'xls':xls } ) for pen, xls in redis.kvr.hgetall(k).items() ]
	return res

@app.get('/grafana/groupby/item', tags=["grafana"]) # to be deleted later 
def grafana_groupby_item(ap='CC1BE0E29824', date:str='20220928', page:str='0.100.0', item:str='item-fill-4', name:str='label'):
	''' 每道题的答案分布  label:ap-CC1BE0E29824:date-20220928:page-0.100.0:pen-D80BCB7002AE:item-fill-4  '''
	si = Counter()
	for k in redis.kvr.keys(f"label:ap-{ap}:date-{date}:page-{page}:pen-*"):
		if k.endswith(item): 
			si.update({redis.kvr.hget(k, name)})
	return si.most_common() 

@app.get('/grafana/rows', tags=["grafana"])
def grafana_rows(ap='CC1BE0E29824', date:str='20220928', page:str='0.100.0', names:str='ap,date,page,pen,item,label,tm'):
	''' label:ap-CC1BE0E29824:date-20220928:page-0.100.0:pen-D80BCB7002AE:item-fill-4  '''
	names = names.strip().split(',') 
	rows  = []
	for k in redis.kvr.keys(f"label:ap-{ap}:date-{date}:page-{page}:pen-*"):
		arr = redis.kvr.hgetall(k) 
		rows.append({n:arr.get(n,'') for n in names}) 
	return rows

@app.get('/redis/get', tags=["redis"])
def redis_get(key:str=""):  return redis.kvr.get(key)
@app.post('/redis/keylist', tags=["redis"]) 
def redis_keylist(keys:list=["ap-ap136:info:page-1713.537.31.107"],names:list=["ctime"]): return [{"key": key, "value":redis.kvr.hmget(key,*names)} for key in keys]
@app.post('/redis/keylistAll', tags=["redis"])
def redis_keylistAll(keys:list=["ap-ap136:info:page-1713.537.31.107"]): return [{"key": key, "value":redis.kvr.hgetall(key)} for key in keys]
@app.get('/redis/hgetall', tags=["redis"])
def redis_hgetall(key:str='rid-230537:tid-1', JSONEachRow:bool=False): return redis.kvr.hgetall(key) if not JSONEachRow else [{"key":k, "value":v} for k,v in redis.kvr.hgetall(key).items()]
@app.get('/redis/hgetalls', tags=["redis"])
def redis_hgetalls(pattern:str='label:ap-CC1BE0E29824:date-20220929:page-0.0.0:pen-*'):
	''' rid-230537:tid-1:uid-* | for JSONEachRow , added 2022.5.17 '''
	if not pattern.endswith("*") : pattern =  pattern +"*"
	return { key: redis.kvr.hgetall(key) for key in redis.kvr.keys(pattern) if redis.kvr.type(key) == 'hash' }
@app.get('/redis/zrangelist', tags=["redis"])
def redis_zrangelist(pattern:str='stroke:ap-quick:page-1713.537.31.92:pen-BP2-0L3-03I-4V:item-*', withscores:bool=False):
	''' stroke:ap-quick:page-1713.537.31.92:pen-BP2-0L3-03I-4V:item-fill-11  '''
	if not pattern.endswith("*") : pattern =  pattern +"*"
	return { key: list(redis.kvr.zrange(key,0,-1, withscores=withscores)) for key in redis.kvr.keys(pattern) if redis.kvr.type(key) == 'zset' }
@app.get('/redis/keys_hgetall', tags=["redis"])
def redis_hgetalls_map(pattern:str='rid-230537:tid-0:uid-*'): return [] if pattern.startswith("*") else [{"key": key, "value":redis.kvr.hgetall(key)} for key in redis.kvr.keys(pattern)]
@app.get('/redis/keys', tags=["redis"]) 
def redis_keys(pattern:str='rid-230537:tid-0:uid-*'):	return [] if pattern.startswith("*") else [{"key": key} for key in redis.kvr.keys(pattern)] 
@app.get('/redis/keys_hget', tags=["redis"])
def redis_keys_hget(pattern:str='rid-230537:tid-0:uid-*', hkey:str='rid', jsonloads:bool=False):
	if pattern.startswith("*"): return []
	return [{"key": key, "value": ( res:=redis.kvr.hget(key, hkey), json.loads(res) if res and jsonloads else res)[-1] } for key in redis.kvr.keys(pattern)]
@app.get('/redis/hget', tags=["redis"])
def redis_hget(key:str='config:rid-10086:tid-1', hkey:str='rid', jsonloads:bool=False):
	res = redis.kvr.hget(key, hkey)
	return json.loads(res) if res and jsonloads else res  
@app.post('/redis/execute_command', tags=["redis"])
def redis_execute_command(cmd:list='zrevrange rid-230537:snt_cola 0 10 withscores'.split()):	return redis.kvr.execute_command(*cmd)
@app.post('/redis/execute_commands', tags=["redis"])
def redis_execute_commands(cmds:list=["info"]):	return [redis.kvr.execute_command(cmd) for cmd in cmds]
@app.post('/redis/xinfo', tags=["redis"])
def redis_xinfo(keys:list=["rid-230537:xwordidf","xessay"], name:str="last-entry"):	return { key: redis.kvr.xinfo_stream(key)[name]  for key in keys }
@app.get('/redis/delkeys', tags=["redis"])
def redis_delkeys(pattern:str="rid-230537:*"): return [redis.kvr.delete(k) for k in redis.kvr.keys(pattern)]
@app.post('/redis/delkeys', tags=["redis"])
def redis_delkeys_list(patterns:list=["rid-230537:*","essay:rid-230537:*"]): return [ redis_delkeys(pattern) for pattern in patterns ]
@app.get('/redis/delete', tags=["redis"])
def redis_delete(key:str="stroke:ap-{ap}:page-{page}:pen-{pen}:item-{item}"): return redis.kvr.delete(key)
@app.post('/redis/xadd', tags=["redis"])
def redis_xadd(name:str="xitem", arr:dict={"rid":"230537", "uid":"1001", "tid":0, "type":"fill", "label":"open the door"}): return redis.kvr.xadd(name, arr )
@app.get('/redis/xrange', tags=["redis"])
def redis_xrange(name:str='xitem', min:str='-', max:str="+", count:int=1): return redis.kvr.xrange(name, min=min, max=max, count=count)
@app.get('/redis/lrange', tags=["redis"])
def redis_lrange(name:str='stroke:ap-quick:page-1713.537.31.92:pen-BP2-0L3-03I-4V:item-fill-11', start:int=0, end:int=-1): return redis.kvr.lrange(name, start, end)
@app.get('/redis/xrevrange', tags=["redis"])
def redis_xrevrange(name:str='xlog', min:str='-', max:str="+", count:int=1): return redis.kvr.xrevrange(name, min=min, max=max, count=count)
@app.get('/redis/zrevrange', tags=["redis"])
def redis_zrevrange(name:str='rid-230537:log:tid-4', start:int=0, end:int=-1, withscores:bool=True, JSONEachRow:bool=False): return redis.kvr.zrevrange(name, start, end, withscores) if not JSONEachRow else [{"member":member, "score":score} for member, score in redis.kvr.zrevrange(name, start, end, withscores)]
@app.get('/redis/zrange', tags=["redis"])
def redis_zrange(name:str='rid-230537:log:tid-4', start:int=0, end:int=-1, withscores:bool=True, JSONEachRow:bool=False): return redis.kvr.zrange(name, start, end, withscores=withscores) if not JSONEachRow else [{"member":member, "score":score} for member, score in redis.kvr.zrange(name, start, end, withscores=withscores)]
@app.get('/redis/set', tags=["redis"])
def redis_set(key:str='rid-230537:config',value:str=""): return redis.kvr.set(key, value) 
@app.post('/redis/hset', tags=["redis"])
def redis_hset(arr:dict={}, key:str='rid-10086:tid-1:uid-pen-zz', k:str="label", v:str="v"):	return redis.kvr.hset(key, k, v, arr) 
@app.post('/redis/hmset', tags=["redis"])
def redis_hmset(arr:dict={}, key:str='rid-10086:tid-1:uid-pen-zz'):	return redis.kvr.hmset(key,arr) 
@app.post('/redis/hdel', tags=["redis"])
def redis_hdel(keys:list=[], name:str='one'): return redis.kvr.hdel(name, *keys) 
@app.get('/redis/hdel', tags=["redis"])
def redis_hdel_get(key:str='one', hkey:str='k,k1' , sep:str=','): return [redis.kvr.hdel(key, k) for k in hkey.split(sep)]
@app.post('/redis/zadd', tags=["redis"])
def redis_zadd(arr:dict={}, key:str='rid-230537:config'): return redis.kvr.zadd(key, arr) 
@app.get('/redis/xlen', tags=["redis"])
def redis_xlen(key:str='xsnt',ts:bool=False): return redis.kvr.xlen(key) if not ts else {"time":time.time(), "Value":redis.kvr.xlen(key)}
@app.get('/redis/zsum', tags=["redis"])
def redis_zsum(key='rid-230537:essay_wordnum',ibeg=0, iend=-1): return sum([v for k,v in redis.kvr.zrevrange(key, ibeg, iend, True)])
@app.get('/redis/zrangebyscore', tags=["redis"])
def redis_zrangebyscore(key='pen-id', min:float=0, max:float=0, withscores:bool=False):  return redis.kvr.zrangebyscore(key, min=min, max=max, withscores=withscores) 
@app.get('/redis/publish', tags=["redis"])
def redis_publish(name:str='pen_key_update',msg:str='{"key":"tiku:ap-quick:date-20220919:page-1713.537.31.92:keyscore", "updated_hkeys":["select-5"]}'): return redis.kvr.publish(name, msg)
@app.post('/redis/join_even_odd', tags=["redis"])
def redis_even_odd(arr:list=['even line','odd line'], asdic:bool=False): return dict(zip(arr[::2], arr[1::2])) if asdic else list(zip(arr[::2], arr[1::2]))

four_int = lambda four, denom=100: [int( int(a)/denom) for a in four]
xy = lambda four : [f"{a},{b}" for a in range(four[0], four[2]+2) for b in range( four[1], four[3] + 2) ] # xy_to_item
@app.post('/redis/penly/xy_to_item', tags=["redis"])
def penly_xy_to_items(arr:list=[[861,1577,11712,2214,"fill-1"],[861,2239,11712,2706,"fill-2"],[861,2731,11712,3297,"fill-3"],[861,3321,11712,3801,"fill-4"],[861,3826,11712,4306,"fill-5"],[861,4330,11712,4798,"fill-6"],[861,4822,11712,5376,"fill-7"],[861,5401,11712,5905,"fill-8"],[861,5930,11712,6336,"fill-9"],[861,6360,11712,6988,"fill-10"],[861,7012,11712,7517,"fill-11"],[861,7541,11712,8009,"fill-12"],[861,8033,11712,8562,"fill-13"],[861,8587,11712,9104,"fill-14"],[861,9128,11712,9596,"fill-15"],[861,9620,11712,10186,"fill-16"],[861,10211,11712,10740,"fill-17"],[861,10765,11712,11232,"fill-18"],[861,11257,11712,11774,"fill-19"],[861,11798,11712,12303,"fill-20"],[861,12327,11712,12868,"fill-21"],[861,12893,11712,13398,"fill-22"],[861,13422,11712,13939,"fill-23"],[861,13963,11712,14468,"fill-24"],[861,14492,11712,14985,"fill-25"],[861,15009,11712,15661,"fill-26"]], denom:int=100,key:str="page:0.100.0:xy_to_item"): 
	''' submit data into the permanent store, updated 2021.10.8 '''
	return [redis.kvr.hset(key, k, tag) for x1,y1,x2,y2,tag in arr for k in xy( ( int(x1/denom), int(y1/denom), int(x2/denom), int(y2/denom)) )]

@app.post('/redis/penly/mock_send_stroke', tags=["redis"])
def penly_mock_send_stroke(strokes:list=["quick:1713.537.31.92:BP2-0L3-03I-4V:1658389523.028:3752,1389,100,1658389523 3738,1395,428,1658389523 3719,1429,720,1658389523 3731,1602,832,1658389523 3797,1605,848,1658389523 3845,1551,808,1658389523 3876,1375,708,1658389523 3840,1330,748,1658389523 3782,1331,740,1658389523",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1658389718.028:2641,2157,100,1658389718 2623,2160,624,1658389718 2611,2192,700,1658389718 2607,2290,728,1658389718 2639,2315,796,1658389718 2711,2279,760,1658389718 2756,2109,756,1658389718 2688,2078,552,1658389718",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1658389718.48:2604,2446,100,1658389718 2595,2482,700,1658389718 2606,2560,744,1658389718 2757,2442,788,1658389718 2609,2450,100,1658389718 2579,2508,100,1658389718",
"quick:1713.537.31.89:BP2-0L3-03I-4V:1658389981.072:3766,1648,676,1658389981 3755,1680,688,1658389981 3767,1811,772,1658389981 3807,1813,684,1658389981 3851,1790,708,1658389981 3881,1737,696,1658389981 3870,1682,724,1658389981 3836,1637,748,1658389981 3807,1635,748,1658389981 3796,1647,100,1658389981 3798,1643,100,1658389981",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688058.044:3781,1060,231,1659688058 3771,1058,477,1659688058 3759,1062,704,1659688058 3752,1097,732,1659688058 3732,1139,736,1659688058 3731,1178,780,1659688058 3747,1200,808,1659688058 3778,1208,824,1659688058 3818,1194,772,1659688058 3864,1146,792,1659688058 3889,1091,772,1659688058 3875,1016,756,1659688058 3844,1006,772,1659688058 3808,1008,792,1659688058 3786,1023,640,1659688058 3777,1030,165,1659688058",
#open
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688120.028:3747,4355,100,1659688120 3746,4355,141,1659688120 3747,4355,516,1659688120 3745,4364,640,1659688120 3745,4384,724,1659688120 3759,4408,752,1659688120 3768,4412,780,1659688120 3770,4402,744,1659688120 3780,4381,736,1659688120 3785,4366,768,1659688120 3782,4353,784,1659688120 3781,4336,792,1659688120 3776,4327,772,1659688120 3768,4330,764,1659688120 3760,4334,776,1659688120 3759,4337,712,1659688120 3750,4350,188,1659688120 3750,4361,188,1659688120",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688121.192:3810,4319,100,1659688121 3816,4315,198,1659688121 3819,4316,668,1659688121 3821,4317,740,1659688121 3822,4321,784,1659688121 3825,4328,812,1659688121 3833,4357,820,1659688121 3817,4492,840,1659688121 3813,4490,453,1659688121 3806,4479,104,1659688121",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688121.524:3821,4326,100,1659688121 3823,4324,412,1659688121 3835,4324,648,1659688121 3853,4331,708,1659688121 3868,4353,756,1659688121 3871,4378,760,1659688121 3865,4394,796,1659688121 3843,4406,756,1659688121 3820,4411,236,1659688121",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688122.02:3891,4369,100,1659688122 3892,4366,501,1659688122 3898,4367,660,1659688122 3902,4368,736,1659688122 3909,4370,784,1659688122 3921,4368,804,1659688122 3935,4360,792,1659688122 3939,4350,728,1659688122 3945,4339,776,1659688122 3937,4336,796,1659688122 3933,4330,816,1659688122 3924,4328,816,1659688122 3914,4331,840,1659688122 3906,4341,856,1659688122 3901,4359,856,1659688122 3902,4383,852,1659688122 3906,4409,852,1659688122 3922,4418,880,1659688122 3928,4417,868,1659688122 3935,4407,820,1659688122 3942,4390,100,1659688122 3944,4373,100,1659688122",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688122.588:3978,4319,100,1659688122 3976,4319,277,1659688122 3980,4325,540,1659688122 3979,4329,728,1659688122 3981,4344,828,1659688122 3980,4368,844,1659688122 3977,4385,844,1659688122 3979,4390,880,1659688122 3978,4389,872,1659688122 3977,4383,816,1659688122 3980,4364,740,1659688122 3984,4340,736,1659688122 3986,4330,764,1659688122 3991,4325,780,1659688122 4003,4318,796,1659688122 4011,4314,816,1659688122 4023,4313,816,1659688122 4029,4315,832,1659688122 4031,4317,816,1659688122 4032,4321,828,1659688122 4031,4323,872,1659688122 4032,4327,876,1659688122 4032,4333,900,1659688123 4033,4358,876,1659688123 4033,4373,868,1659688123 4033,4386,856,1659688123 4029,4405,860,1659688123 4040,4417,888,1659688123 4036,4416,872,1659688123 4034,4411,744,1659688123 4027,4399,252,1659688123 3994,4370,252,1659688123",
], name:str='pen_stroke'):
	''' mock sending strokes to redis:pen_stroke '''
	redis.r.delete("stroke:ap-quick:page-1713.537.31.92:pen-BP2-0L3-03I-4V:item-fill-11") # open stroke
	for s in strokes :  redis.r.publish(name, s ) 
	return 'Finished sending data: ' + time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))  

@app.get('/redis/penly/mock', tags=["redis"])
def penly_mock(): return penly_mock_send_stroke()

from PIL import Image,ImageDraw # pip install pillow 
from io import BytesIO
@app.get("/strokelog/png", response_class=StreamingResponse, tags=["stroke"])
def strokelog_png(ap:str="CC1BE0E29824", page:str="0.0.0", date:str="20220929", pen:str="D80BCB7002AE", start:int=0,end:int=-1, width:int=3):
	''' pen 在 page 上的答题痕迹, added 2022.10.1 '''
	hpage   = hgetall(f"page:{page}")
	img_url = hpage["img-url"] # "https://penly-1257827020.cos.ap-shanghai.myqcloud.com/1713.537.31.92.jpg"
	max_x	= int(hpage.get('max-x',13779))
	max_y	= int(hpage.get('max-x',19488))
	response = requests.get(img_url)
	im = Image.open(BytesIO(response.content))# im = Image.open("./paper.jpg")
	draw = ImageDraw.Draw(im)
	paperData = redis.kvr.zrange(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}", start, end) #paperData = requests.get("http://data.penly.cn:16666/redis/zrange?name=strokelog:ap-CC1BE0E29824:date-20220929:page-0.0.0:pen-D80BCB7002AE&start=0&end=-1&withscores=false&JSONEachRow=false").json()
	for pageLine in paperData:
		pageLineArr = pageLine.split(' ')
		points = []
		for line in pageLineArr:
			pointArr = line.split(',')
			points.append((int(pointArr[0]) / max_x) * im.width)
			points.append((int(pointArr[1]) / max_y) * im.height)
		draw.line(points, fill=(0,0,0), width=width)
	imgBytes = BytesIO()
	im.save(imgBytes, format='PNG') #JPEG
	#original_image = Image.open(img.file)
	#original_image = original_image.filter(ImageFilter.BLUR)
	#filtered_image = BytesIO()
	#original_image.save(filtered_image, "JPEG")
	#filtered_image.seek(0)
	imgBytes.seek(0)
	return StreamingResponse(imgBytes, media_type="image/png")

@app.get('/svg-test', response_class=HTMLResponse, tags=["stroke"])
def penly_svg_test(): 
	return HTMLResponse(content='''<head>
    <title>The Rock</title>
    <meta property="og:title" content="Hello world" />
    <meta property="og:description" content="The quick fox jumped over the lazy dog." />
    <meta property="og:url" content="https://pigaivip.feishu.cn" />
    <meta property="og:image"  content="https://penly-1257827020.cos.ap-shanghai.myqcloud.com/1713.537.31.92.jpg"  />
  </head>
<style type='text/css'>
	body {background:url("https://penly-1257827020.cos.ap-shanghai.myqcloud.com/1713.537.31.92.jpg")}
</style>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
   <circle cx="100" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />
</svg>''')
            
@app.get('/stroke/svg', response_class=HTMLResponse, tags=["stroke"])
def penly_svg(lkey:str="stroke:ap-CC1BE0E29824:date-20220923:page-177.0.1:pen-D80BCB7002AE:item-fill-12", start:int=0, end:int=-1, color:str='black', width:int=10, full:bool=True): 
	''' <svg viewBox="0 0 5600 7920">
  <polyline points="26,90 23,89 25,89 24,88 24,90 24,92 20,98 17,121 23,144 35,159 48,162 73,142 87,108 89,76 80,56 58,51 31,66 15,99 13,117" style="fill:none;stroke:blue;stroke-width:15" />
  <polyline points="97,54 94,52 97,47 109,44 110,41 111,42 112,43 112,41 116,42 114,44 117,53 124,113 134,167 140,174 153,143 164,109 167,83 170,64 172,62 166,61 155,59" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="175,108 178,114 188,118 199,121 215,120 242,112 247,102 248,92 247,84 237,75 219,72 211,77 205,95 199,125 200,153 210,171 220,173 247,155 273,116 290,89 297,78 298,71 296,64 294,61 294,63 295,64 296,66 297,68 299,76 302,107 309,145 310,156 310,145 312,118 319,91 325,86 327,89 332,99 340,105" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="410,81 423,50 399,62 381,85 377,135 384,166 392,173 405,174 424,150 444,134 448,126 449,125 447,125 448,125 447,125 448,128 448,131 450,141 456,157 467,166 482,169 489,149 492,133 490,117 478,102 450,91 445,94 444,99 459,110 481,102" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="527,89 532,82 532,79 534,81 535,84 534,102 526,134 524,140 526,139 531,132 535,113 546,90 558,75 568,64 569,64 571,67 570,71 577,97 578,114 578,117 579,117 582,114 586,108 594,91 604,74 613,60 614,58 615,59 616,63 618,82 615,111 616,133 614,162 614,156 625,124" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="655,84 655,87 659,93 668,96 681,95 696,90 710,82 718,70 718,57 715,52 709,48 698,47 670,57 655,96 652,145 681,175 710,174 724,168 728,160 733,128" style="fill:none;stroke:black;stroke-width:15" />
</svg> '''
	def polyline(stroke:str='903,554,100,1656990923 911,559,161,1656990923 917,552,201,1656990923', xmin:int=0, ymin:int=0): 
		res = []
		for s in stroke.split(' '): 
			arr = s.split(',')
			if len(arr) >= 4:  res.append( f"{int(arr[0]) - xmin},{int(arr[1]) - ymin}") 
		plist = " ".join(res)
		return f'<polyline points="{plist}" style="fill:none;stroke:{color};stroke-width:{width}" />'
	strokes = redis.kvr.lrange(lkey, start, end) if redis.kvr.type(lkey) == 'list' else redis.kvr.zrange(lkey, start, end)
	xypts	= [ ar.split(',') for stroke in strokes for ar in stroke.split(':')[-1].split(' ')]
	if not xypts: return ""
	x_min	= min([int(x) for x,y,p,t in xypts ])
	x_max	= max([int(x) for x,y,p,t in xypts ])
	y_min	= min([int(y) for x,y,p,t in xypts ])
	y_max	= max([int(y) for x,y,p,t in xypts ])
	polylines = "\n".join([ polyline(stroke, x_min, y_min) for stroke in strokes ])
	return HTMLResponse(content=f'<svg viewBox="0 0 {5600 if full else x_max - x_min} {7920 if full else y_max - y_min}">{polylines}</svg>')

@app.get('/stroke-svg/{key}', response_class=HTMLResponse, tags=["stroke"]) # 2022.9.28
def penly_stroke_svg(key:str="stroke:ap-CC1BE0E29824:date-20220923:page-177.0.1:pen-D80BCB7002AE:item-fill-12", start:int=0, end:int=-1, color:str='black', width:int=10, full:bool=True): 	return penly_svg(key, start, end, color, width, full)

avg		= lambda arr: sum(arr) / len(arr) if len(arr) > 0 else 0 
xy_avg	= lambda rows: (round(avg([int(row[0]) for row in rows]),1), round(avg([int(row[1]) for row in rows]),1))  
xyt		= lambda tups,mx=13779,my=19488: { "x": [ int (int(tup[0]) * 5600 / mx) for tup in tups] ,  "y": [ int(int(tup[1]) * 7920/ my ) for tup in tups],  "t": [int(tup[-1]) for tup in tups]}
xyts	= lambda stroke,mx=13779,my=19488: xyt([ s.split(',')  for s in stroke.split(' ')], mx, my)#reco = { "en": 'http://ap.penly.cn:18461/' ,"en_US": 'http://ap.penly.cn:18461/' , "zh_CN":'http://ap.penly.cn:18462/'}

@app.post("/stroke/bbox", tags=["stroke"])
def stroke_bbox( rows:list=["quick:1713.537.31.92:BP2-0L3-03I-4V:1659688120.028:3747,4355,100,1659688120 3746,4355,141,1659688120 3747,4355,516,1659688120 3745,4364,640,1659688120 3745,4384,724,1659688120 3759,4408,752,1659688120 3768,4412,780,1659688120 3770,4402,744,1659688120 3780,4381,736,1659688120 3785,4366,768,1659688120 3782,4353,784,1659688120 3781,4336,792,1659688120 3776,4327,772,1659688120 3768,4330,764,1659688120 3760,4334,776,1659688120 3759,4337,712,1659688120 3750,4350,188,1659688120 3750,4361,188,1659688120",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688121.192:3810,4319,100,1659688121 3816,4315,198,1659688121 3819,4316,668,1659688121 3821,4317,740,1659688121 3822,4321,784,1659688121 3825,4328,812,1659688121 3833,4357,820,1659688121 3817,4492,840,1659688121 3813,4490,453,1659688121 3806,4479,104,1659688121",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688121.524:3821,4326,100,1659688121 3823,4324,412,1659688121 3835,4324,648,1659688121 3853,4331,708,1659688121 3868,4353,756,1659688121 3871,4378,760,1659688121 3865,4394,796,1659688121 3843,4406,756,1659688121 3820,4411,236,1659688121",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688122.02:3891,4369,100,1659688122 3892,4366,501,1659688122 3898,4367,660,1659688122 3902,4368,736,1659688122 3909,4370,784,1659688122 3921,4368,804,1659688122 3935,4360,792,1659688122 3939,4350,728,1659688122 3945,4339,776,1659688122 3937,4336,796,1659688122 3933,4330,816,1659688122 3924,4328,816,1659688122 3914,4331,840,1659688122 3906,4341,856,1659688122 3901,4359,856,1659688122 3902,4383,852,1659688122 3906,4409,852,1659688122 3922,4418,880,1659688122 3928,4417,868,1659688122 3935,4407,820,1659688122 3942,4390,100,1659688122 3944,4373,100,1659688122",
"quick:1713.537.31.92:BP2-0L3-03I-4V:1659688122.588:3978,4319,100,1659688122 3976,4319,277,1659688122 3980,4325,540,1659688122 3979,4329,728,1659688122 3981,4344,828,1659688122 3980,4368,844,1659688122 3977,4385,844,1659688122 3979,4390,880,1659688122 3978,4389,872,1659688122 3977,4383,816,1659688122 3980,4364,740,1659688122 3984,4340,736,1659688122 3986,4330,764,1659688122 3991,4325,780,1659688122 4003,4318,796,1659688122 4011,4314,816,1659688122 4023,4313,816,1659688122 4029,4315,832,1659688122 4031,4317,816,1659688122 4032,4321,828,1659688122 4031,4323,872,1659688122 4032,4327,876,1659688122 4032,4333,900,1659688123 4033,4358,876,1659688123 4033,4373,868,1659688123 4033,4386,856,1659688123 4029,4405,860,1659688123 4040,4417,888,1659688123 4036,4416,872,1659688123 4034,4411,744,1659688123 4027,4399,252,1659688123 3994,4370,252,1659688123",
], max_x:int=11548, max_y:int=16404, host:str='http://ap.penly.cn:18461/' ):
	''' {'type': 'Text', 'bounding-box': {'x': 25.8803864, 'y': 23.2417908, 'width': 20.1695213, 'height': 8.2792263}, 'label': 'open', 'words': [{'label': 'open', 'candidates': ['open', 'Open', 'opens', 'oper', 'opera'], 'bounding-box': {'x': 25.8803864, 'y': 23.2417908, 'width': 20.1695213, 'height': 8.2792263}, 'items': [{'type': 'glyph', 'timestamp': '1970-01-20 06:12:16.413000', 'label': 'o', 'bounding-box': {'x': 26.8803864, 'y': 24.2417908, 'width': 4.16685867, 'height': 4.43142128}, 'baseline': 0.977611899, 'x-height': 0.955223978, 'left-side-bearing': -0.0952381045, 'id': '000031a901000700ff00'}, {'type': 'glyph', 'timestamp': '1970-01-20 06:12:16.413000', 'label': 'p', 'bounding-box': {'x': 32.130703, 'y': 24.2417908, 'width': 3.89403152, 'height': 6.2792263}, 'baseline': 0.689927518, 'x-height': 0.674127758, 'left-side-bearing': -0.176220804, 'id': '000032a901000700ff00'}, {'type': 'glyph', 'timestamp': '1970-01-20 06:12:16.413000', 'label': 'e', 'bounding-box': {'x': 36.8192177, 'y': 24.2417908, 'width': 3.69147491, 'height': 4.43142128}, 'baseline': 0.977611899, 'x-height': 0.955223978, 'left-side-bearing': -0.107502803, 'id': '000033a901000700ff00'}, {'type': 'glyph', 'timestamp': '1970-01-20 06:12:16.413000', 'label': 'n', 'bounding-box': {'x': 41.5361862, 'y': 24.2417908, 'width': 3.51372147, 'height': 4.33221054}, 'baseline': 0.999999762, 'x-height': 0.97709918, 'left-side-bearing': -0.195294127, 'id': '000034a901000700ff00'}]}], 'version': '2', 'id': 'MainBlock'} '''
	events	= {"events": [xyts(row.split(':')[-1], max_x, max_y) for row in rows ] }
	bbox	= requests.post( host,data=json.dumps(events)).json() 
	return bbox 
	
@app.get('/stroke/label', tags=["stroke"])
def penly_stroke_label(zkey:str="strokelog:ap-CC1BE0E29824:date-20220924:page-0.100.2:pen-D80BCB7002AE", start:int=0, end:int=-1, max_x:int=11548, max_y:int=16404, verbose:bool=False): 
	''' stroke 识别成文字  '''
	rows = redis.kvr.zrange(zkey, start, end)
	bbox = stroke_bbox(rows)
	return bbox if verbose else bbox.get('label','')

@app.get("/feishu/penxls", tags=["feishu"])
def ap_penxls(ap:str='CC1BE0E29824', pen:str="D80BCB7002AE", page:str='0.100.0', date:str=None): 
	''' date: 20220925 , pen:D80BCB7002AE '''
	if date is None : date = time.strftime("%Y%m%d", time.localtime(time.time() )) # today 
	xls = redis.kvr.hget(f"ap:{ap}:date-{date}:page-{page}:pen-xls", pen)
	return RedirectResponse(f"https://sentbase.feishu.cn/sheets/{xls}")  if xls else {"ap":ap, "pen":pen, "page":page, "xls":xls, "date":date}

def _del_key_tok(token, prefix:str='feishu'):
	key		= redis.r.hget(f"{prefix}:{token}", "key")
	if key is not None or key : 
		redis.r.delete(key) 
		redis.r.delete(f"{prefix}:{token}")
		print ( key, token, " is deleted", flush=True) 

@app.post('/feishu/event', tags=["feishu"])
def feishu_event(arr:dict={ "challenge": "ajls384kdjx98XX", "token": "xxxxxx",     "type": "url_verification"   } ):
	''' last update: 2022.9.19 '''
	arr['listener_count'] = redis.r.publish("pen-feishu-event", json.dumps(arr)) 
	if arr.get('header',{}).get('event_type','') == 'drive.file.trashed_v1': #'drive.file.bitable_record_changed_v1':
			token	= arr.get('event',{}).get('file_token','')
			key		= redis.r.get(f"rc:token:{token}")
			redis.r.delete(f"rc:token:{token}", key if key is not None or key else "") 

			_del_key_tok(token, 'feishu')
			_del_key_tok(token, 'apdatepage')
	return arr
#2) "pen-feishu-event"
#3) "{\"schema\": \"2.0\", \"header\": {\"event_id\": \"a036c2bbfa20418b99a227a17f1c9e08\", \"token\": \"RR46JViqqINRjWCUxZDnJcO4BeciK3r2\", \"create_time\": \"1665229080000\", \"event_type\": \"drive.file.trashed_v1\", \"tenant_key\": \"10685f4037d9975e\", \"app_id\": \"cli_a390c187f1f9d00b\", \"resource_id\": \"bascnTX1Isd3pcGvgRCyu3FGype\", \"user_list\": [{\"union_id\": \"on_3e42b52aeaa2e6b3359250dd31de17bf\"}]}, \"event\": {\"file_token\": \"bascnTX1Isd3pcGvgRCyu3FGype\", \"file_type\": \"bitable\", \"operator_id\": {\"open_id\": \"ou_9534a7c4dadcd9493d28400c8012fc22\", \"union_id\": \"on_3e42b52aeaa2e6b3359250dd31de17bf\", \"user_id\": \"\"}, \"subscriber_id_list\": [{\"open_id\": \"ou_9534a7c4dadcd9493d28400c8012fc22\", \"union_id\": \"on_3e42b52aeaa2e6b3359250dd31de17bf\", \"user_id\": \"\"}]}}"

@app.get('/feishu/newrec', tags=["feishu"])
def feishu_newrec(recid:str="", ap:str="", pen:str="", page:str="", item:str="", date:str=""):
	''' called by bitable http, last update: 2022.10.2 '''
	if recid and ap and pen and page and item and date: 
		redis.r.hset(f"label:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}", "recid", recid )
		arr = {"ap":ap, "page":page, "pen":pen, "item":item, "date":date, "recid":recid}
		arr['listener_count'] = redis.r.publish("feishu_newrec", json.dumps(arr)) 
		return arr

# sudo pip install fastapi-utils
tat		= lambda :requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/", data={"app_id":"cli_a390c187f1f9d00b", "app_secret":"sL6udKjwYarn3y8QKb4nyfO18OFqyp3F"}).json()['tenant_access_token']
headers = lambda : {"content-type":"application/json", "Authorization":"Bearer " + tat()} # redis.tat
from fastapi_utils.tasks import repeat_every #https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/
@app.on_event("startup")
@repeat_every(seconds=7100)  # < 2 hours
def timer_update() -> None:
	_tat = tat() 
	redis.r.setex("tat", 7100, _tat)
	print ( "feishu tat is updated:",  time.time(),  _tat, flush=True)
@app.get('/feishu/tat', tags=["feishu"])
def feishu_tat():  
	''' 返回feishu tenant_access_token,  两个小时更新一次， 存在 6665 中 '''
	v = redis.r.get("tat")
	if v is None or not v:
		v = tat()
		redis.r.setex("tat", 7100, v)
	return v 

@app.get('/feishu/wiki/node', tags=["feishu"])
def feishu_wiki_node(token:str="wikcnkOO1p7mV4ozGgDdAF9yaxg"):  
	return requests.get(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token={token}", headers = headers() )

@app.get('/feishu/wiki/itemkey', tags=["feishu"])
def wiki_itemkey(ap:str="CC1BE0E29824", page:str="0.0.0", date:str="20220929"): 
	'''	日卡答案 ''' 
	sub		= hgetall(f"page:{page}").get('sub','en')
	space	= hgetall(f"ap:{ap}").get(f"sub-{sub}:space",'0') #ap:CC1BE0E29824:sub-en:space
	suffix	= 'itemkey'
	key		= f"{date}-{page}:{suffix}"
	token	= redis.kvr.hget(f"label:ap-{ap}:date-{date}:page-{page}",suffix)
	if token is None or not token: 
		parent		= "" #wiki_date_folder(ap, sub, space, date)['node_token']
		src_spaceid	= hgetall("config:wiki")["template-space-id"] 
		src_token	= hgetall(f"page:{page}")[f"wiki-{suffix}"]
		arr			= {"target_parent_token": parent,  "target_space_id": space,  "title": f"{date}-{page_title(page)}-" + hgetall('config:suffix-title').get(suffix, suffix) }
		res			= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{src_spaceid}/nodes/{src_token}/copy", headers = headers(), json=arr).json()
		token		=  res.get('data',{}).get('node',{}).get('obj_token','') 
		redis.r.publish("pen_wiki_new_itemkey", json.dumps(res) )
		print("new bitable:", token, res) 
		redis.kvr.hset(f"label:ap-{ap}:date-{date}:page-{page}", suffix, token)
		redis.kvr.hset(f"feishu:{token}", "type","bitable", {"ap":ap, "page":page, "date":date, "token":token, "of": "itemkey", 'created': now() })
		print ( requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{token}/subscribe?file_type=bitable", headers = headers()).json() )
	return RedirectResponse(f"https://sentbase.feishu.cn/base/{token}")  if token else {"ap":ap, "page":page, "date":date}

@app.get('/feishu/tasklist/token', tags=["feishu"])
def feishu_tasklist(ap:str="CC1BE0E29824", sub:str='en', refresh:bool=False): 
	'''	 日卡作业列表，每个apsub对应一个文件，只建不删 ''' 
	space	= hgetall(f"ap:{ap}").get(f"sub-{sub}:space",'0') 
	key		= f"task:ap-{ap}:sub-{sub}" # 可以整体删除，自动重建
	if refresh: redis.kvr.delete(key) 
	token	= redis.r.hget(key, "token")  # NOT use hgetall with cache 
	if not token: 
		parent		= "" #wiki_date_folder(ap, sub, space, date)['node_token']
		src_spaceid	= hgetall("config:wiki")["template-space-id"] 
		src_token	= hgetall("config:wiki")[f"home-bitable-template:sub-{sub}"] 
		arr			= {"target_parent_token": parent,  "target_space_id": space,  "title":  f"[{sub_title(sub)}]作业列表" }
		res			= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{src_spaceid}/nodes/{src_token}/copy", headers = headers(), json=arr).json()
		print("new home bitable:", res) #{'code': 0, 'data': {'node': {'creator': 'ou_9534a7c4dadcd9493d28400c8012fc22', 'has_child': False, 'node_create_time': '1664758105', 'node_token': 'wikcnEGzujMBKAKInlV5tDPUUlf', 'node_type': 'origin', 'obj_create_time': '1664758104', 'obj_edit_time': '1664758104', 'obj_token': 'bascnDbpzIpmJlB89MFiz6Aarsh', 'obj_type': 'bitable', 'origin_node_token': 'wikcnEGzujMBKAKInlV5tDPUUlf', 'origin_space_id': '7148443017811132420', 'owner': 'ou_9534a7c4dadcd9493d28400c8012fc22', 'parent_node_token': 'wikcno4IJE7OnCJ3pQQc9G6X0zg', 'space_id': '7148443017811132420', 'title': '20220929-快速体验-题卡看板'}}, 'msg': 'success'}

		redis.r.publish("pen-wiki-new-homebit", json.dumps(res) )
		token =  res.get('data',{}).get('node',{}).get('obj_token','') 
		if token:
			print( requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{token}/subscribe?file_type=bitable", headers = headers()).json())
			redis.r.hset(key, "token", token)
			redis.r.hset(f"feishu:{token}", "key", key, {"of":"tasklist", 'ap':ap, 'sub':sub, 'space':space, 'created': now()}) # to sync delete 

	table	= redis.r.hget(key, "table") 
	if not table: 
		res		= requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json()
		print ("get table:", token, res )  #get table: wikcnEGzujMBKAKInlV5tDPUUlf {'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
		table	= res['data']['items'][0]['table_id']	#table   = bitable_first_table(token)
		redis.r.hset(key, "table", table)

	return {"token":token, "table":table}

@app.get('/feishu/pagebit/token', tags=["feishu"])
def feishu_pagebit_token(ap:str="CC1BE0E29824", page:str="0.0.3", date:str="20221009", suffix:str="page-bitable", retry:int=3): 
	'''	日卡每天一个文件bitable， 只建不删， 由cron 负责清理历史数据，不检查有效性 ''' 
	sub		= hgetall(f"page:{page}").get('sub','en')
	#space	= hgetall(f"page:{page}").get("space",'')  # page space first, added 2022.10.8
	#if space is None or not space:  
	space	= hgetall(f"ap:{ap}").get(f"sub-{sub}:space",'') #ap:CC1BE0E29824:sub-en:space
	key		= f"{date}-{page}:{suffix}"
	hpage	= redis.r.hgetall(f"feishu:ap-{ap}:date-{date}:page-{page}") # avoid to trigger hset-label event

	token	= hpage.get(suffix, '')
	if not token: 
		parent		= "" 
		src_spaceid	= hgetall("config:wiki")["template-space-id"] 
		src_token	= redis.kvr.hgetall(f"page:{page}")[f"wiki-{suffix}"]  #  to avoid cache
		arr			= {"target_parent_token": parent,  "target_space_id": space,  "title": f"{date}-{page_title(page)}-" + hgetall('config:suffix-title').get(suffix, suffix) }
		res			= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{src_spaceid}/nodes/{src_token}/copy", headers = headers(), json=arr).json()
		print(f"src token: {src_token}, new page bitable:", res) #{'code': 0, 'data': {'node': {'creator': 'ou_9534a7c4dadcd9493d28400c8012fc22', 'has_child': False, 'node_create_time': '1664758105', 'node_token': 'wikcnEGzujMBKAKInlV5tDPUUlf', 'node_type': 'origin', 'obj_create_time': '1664758104', 'obj_edit_time': '1664758104', 'obj_token': 'bascnDbpzIpmJlB89MFiz6Aarsh', 'obj_type': 'bitable', 'origin_node_token': 'wikcnEGzujMBKAKInlV5tDPUUlf', 'origin_space_id': '7148443017811132420', 'owner': 'ou_9534a7c4dadcd9493d28400c8012fc22', 'parent_node_token': 'wikcno4IJE7OnCJ3pQQc9G6X0zg', 'space_id': '7148443017811132420', 'title': '20220929-快速体验-题卡看板'}}, 'msg': 'success'}
		redis.r.publish("pen-pagebit", src_token + " " + json.dumps(res) )
		token =  res.get('data',{}).get('node',{}).get('obj_token','') 
		redis.r.hset(f"feishu:ap-{ap}:date-{date}:page-{page}", suffix, token)
		redis.r.hset(f"feishu:{token}", "key", f"feishu:ap-{ap}:date-{date}:page-{page}", {"of":"pagebit", 'ap':ap, 'page':page, 'date':date, 'space':space, 'sub':sub, 'created': now()})
		print( requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{token}/subscribe?file_type=bitable", headers = headers()).json())

	table	= hpage.get(f"{suffix}-table","")
	while not table and retry > 0: 
		retry	= retry - 1 
		try:
			#time.sleep( 1 ) # to wait for the construction completed
			res		= requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json() # 第一次调用常常失败
			print ("get table:", token, res )  #get table: wikcnEGzujMBKAKInlV5tDPUUlf {'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
			table	= res['data']['items'][0]['table_id']	#table   = bitable_first_table(token)
			if table: redis.r.hset(f"feishu:ap-{ap}:date-{date}:page-{page}", f"{suffix}-table", table)
		except Exception as ex:
			print ( ">>feishu_pagebit_token ex:", ex, "\t|", date, flush=True)
			redis.r.publish("pen-wiki-pagebit-ex", str(ex) ) 
			traceback.print_exc()
			time.sleep( 1 ) 

	return {"token":token, "table":table}

@app.get('/feishu/apdatepage', tags=["feishu"])
def feishu_apdatepage(ap:str="CC1BE0E29824",date:str="20220929", page:str="0.0.0"): 
	''' 日卡每天一个文件bitable， 只建不删 ''' 
	name = redis.kvr.hget('config:app', 'name')
	if name is None or not name: name= 'penly'
	token = apdatepage_token(ap, date, page) 
	return RedirectResponse(f"https://{name}.feishu.cn/base/{token}") 

if __name__ == '__main__':	
	feishu_apdatepage("CC1BE0E29824", "20220930", "0.0.0")
	uvicorn.run(app, host='0.0.0.0', port=16666)

'''
@app.get('/feishu/cron', tags=["feishu"])
def feishu_cron():  
	# 定期检查 wiki的根目录下文件， 只保留2天数据， 过期的挪到归档目录， datediff(1 day) 
	return redis.r.get("tat")

get table: bascnzTWc88LMMvRpW9Hisoe4Cb {'code': 1254036, 'msg': 'Bitable is copying, please try again later.', 'error': {'log_id': '202210101604360102091481441B0C474D'}}
'''