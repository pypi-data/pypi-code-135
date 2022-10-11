# created 2022.10.10 pip install python-redis-cache
import redis, time, requests,json,sys,collections,os,random, traceback,fire, random
from penly.rcache import RedisCache #from redis_cache import RedisCache | https://pypi.org/project/python-redis-cache/
from functools import lru_cache
apihost		= "data.penly.cn:16666"
tat_api		= lambda :requests.get(f"http://{apihost}/feishu/tat").json()
tat			= lambda :requests.post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/", data={"app_id":"cli_a390c187f1f9d00b", "app_secret":"sL6udKjwYarn3y8QKb4nyfO18OFqyp3F"}).json()['tenant_access_token']
headers		= lambda : {"content-type":"application/json", "Authorization":"Bearer " + tat()}
rhost		= os.getenv('rhost', 'data.penly.cn') # 136
redis.r		= redis.Redis(host=rhost, port=os.getenv('redis_port', 6665), decode_responses=True) 
redis.kvr	= redis.Redis(host=rhost, port=os.getenv('kvr_port', 6666),  decode_responses=True) 
cache		= RedisCache(redis_client=redis.r)
@lru_cache(maxsize=None) # cache_clear()
def hgetall(key:str='ap:CC1BE0E29824:sub-folder'): return redis.kvr.hgetall(key)

today		= lambda : time.strftime("%Y%m%d", time.localtime(time.time() ))
now			= lambda: time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
get_sheet	= lambda file_token="shtcnxMkvkwo1NdE36h9wtS95Cd", sheet_title='Sheet1': [ar['sheet_id'] for ar in requests.get(f"https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{file_token}/sheets/query",headers = headers()).json()['data']['sheets'] if ar['title'] == sheet_title ][0]
pen_name	= lambda ap, pen: redis.kvr.hgetall(f"ap:{ap}:pen-name").get(pen, pen[-2:])
ap_title	= lambda ap:	hgetall(f"ap:{ap}").get("title", ap[-2:])
page_title	= lambda page:	hgetall(f"page:{page}").get("title", page)
sub_title	= lambda sub:	hgetall(f"config:sub-title").get(sub, sub)
new_folder	= lambda title, parent: requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/create_folder", headers = headers(), json={"name": title,"folder_token": parent}).json().get('data',{}).get('token','')
replay		= lambda ap='CC1BE0E29824', date=today(),page='0.0.0', pen='D80BCB7002AE': [redis.r.publish("pen_stroke", f"{ap}:{page}:{pen}:{tm}:{stroke}") for stroke, tm in redis.kvr.zrange(f"strokelog:ap-{ap}:date-{date}:page-{page}:pen-{pen}",0,-1, withscores=True)]
mid			= lambda s, left, right=':':  s.split(left)[-1].split(right)[0]
subscribe	= lambda token, type='bitable': requests.post("https://open.feishu.cn/open-apis/drive/v1/files/{token}/subscribe?file_type={type}", headers = headers()).json() # bitable
#https://open.feishu.cn/open-apis/drive/v1/files/bascnqXOTGO9epDdjNyCc60wRsg/subscribe?file_type=bitable
#https://open.feishu.cn/open-apis/drive/v1/files/bascnqXOTGO9epDdjNyCc60wRsg/subscriptions | bitable failed

@lru_cache(maxsize=None)
def first_sheet(file_token:str="shtcnxMkvkwo1NdE36h9wtS95Cd"):	return requests.get(f"https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{file_token}/sheets/query",headers = headers()).json()['data']['sheets'][0]['sheet_id']
#@lru_cache(maxsize=None)
#def bitable_first_table(bitable:str="bascnHETIcLbAttTsTwjQA9Lpkf"):  return requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables",headers = headers()).json()['data']['items'][0]['table_id']

from penly.ink import * 
from penly.img import * 
from penly.wiki import * 

def wiki_date_node(ap:str="CC1BE0E29824", page:str="0.0.0", date:str='20220829', type:str='docx'): 
	''' 2022.9.29, no redis token cache '''
	sub			= hgetall(f"page:{page}").get('sub','en')
	space_id	= sub_wiki_space(ap, sub) 

	def wiki_month_folder(ap:str="CC1BE0E29824", sub:str="en", month:str='202208', type:str='docx'): # has_more 
		''' '''
		space_id = sub_wiki_space(ap, sub) #https://open.feishu.cn/api-explorer/cli_a390c187f1f9d00b?apiName=list&from=op_doc&project=wiki&resource=space.node&version=v2
		for item in requests.get(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes?page_size=50", headers = headers()).json().get('data',{}).get('items',[{}]):
			if item['title'] == month  : return item # obj_token/node_token 
		res	= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes", headers = headers(), json={
				"obj_type": type,
				"parent_node_token": "",
				"node_type": "origin",
				"title": month,
				"origin_node_token": ""
			}).json()
		print ( res) 
		return res.get('data',{}).get('node',{})

	month_folder= wiki_month_folder(ap, sub, date[0:6], type)['node_token']
	pagetitle   = page_title(page) #"20220729-cardname"
	res = requests.get(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes?page_size=50&parent_node_token={month_folder}", headers = headers()).json()
	#print ( res) #{'code': 0, 'data': {'has_more': False, 'page_token': ''}, 'msg': 'success'}
	for item in res.get('data',{}).get('items',[{}]):
		if item.get('title','') == f"{date}-{pagetitle}"  : return item 
	res	= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes", headers = headers(), json={
			"obj_type": type,
			"parent_node_token": month_folder,
			"node_type": "origin",
			"title": f"{date}-{pagetitle}",
			"origin_node_token": ""
		}).json()
	#print ( res) 
	redis.r.publish("pen_wiki_create_node", json.dumps(res)) 
	return res.get('data',{}).get('node',{})
#print ( wiki_date_node() )

def wiki_date_file0(ap:str="CC1BE0E29824", page:str="0.0.0", date:str="20220731", suffix:str="page-bitable"): 
	'''	wiki per page , 20220729-{pagetitle}-{penname} | # pen is a pen or a suffix  ''' 
	sub		= hgetall(f"page:{page}").get('sub','en')
	space	= sub_wiki_space(ap, sub) 
	parent	= wiki_date_node(ap,page, date)['node_token']
	title	= f"{date}-{page_title(page)}-" + hgetall('config:suffix-title').get(suffix, suffix) 
	res		= requests.get(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space}/nodes?page_size=50&parent_node_token={parent}", headers = headers()).json()	#print ( res) #{'code': 0, 'data': {'has_more': False, 'page_token': ''}, 'msg': 'success'}
	for item in res.get('data',{}).get('items',[{}]):
		if item.get('title','') == title  : return item # when failed, sleeping randow time, and try again ? 

	src_spaceid	= hgetall("config:wiki")["template-space-id"] 
	src_token	= hgetall(f"page:{page}")[f"wiki-{suffix}"]
	arr			= {"target_parent_token": parent,  "target_space_id": space,  "title": title}
	res			= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{src_spaceid}/nodes/{src_token}/copy", headers = headers(), json=arr).json()
	redis.r.publish("pen_wiki_new_datefile", json.dumps(res) )
	return res.get('data',{}).get('node',{})
#print (wiki_date_file())

@lru_cache(maxsize=None)
def cloned_sheet(spreadsheetToken:str="shtcn8mtcWKFRP40kIYbgIYgXdb", template_sheetid:str="fc8edf", sheet_title:str="pen-hh"):
	''' {'code': 0, 'data': {'replies': [{'copySheet': {'properties': {'index': 1, 'sheetId': '43XHeo', 'title': 'string'}}}]}, 'msg': 'success'} '''
	res = requests.get(f"https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{spreadsheetToken}/sheets/query",headers = headers()).json()
	for ar in res['data']['sheets'] :
		if ar['title'] == sheet_title :  return ar['sheet_id'] 

	arr = { "requests": [  {"copySheet": {  "source": {  "sheetId": template_sheetid },   "destination": {  "title": sheet_title       }   }    }  ]}
	res = requests.post(f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{spreadsheetToken}/sheets_batch_update",headers = headers(),json=arr).json()
	return res['data']['replies'][0]['copySheet']['properties']['sheetId']
#print (cloned_sheet())

def upsert_bitable(arr:dict={},  bitable:str="bascniTZYLHQFZjfN9ondVkAeAf", table:str=None, recid:str=None): 
	''' return recid = res.get('data',{}).get('record', {}).get('record_id', '') '''
	if table is None: table = bitable_first_table(bitable) 
	data = {"fields": arr} if not 'fields' in arr else arr 
	res = requests.post(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records",headers = headers(),json=data).json() if recid is None else  requests.put(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records/{recid}",headers = headers(),json=data).json()
	if res.get('msg','') == 'RecordIdNotFound': #{'code': 1254043, 'msg': 'RecordIdNotFound', 'error': {'log_id': '202209280751270102091570260A1F6A7B'}}
		res = requests.post(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{bitable}/tables/{table}/records",headers = headers(),json=data).json() # invalid recid in the redis
	redis.r.publish("pen_bitable_upsert", json.dumps(res) ) # publish new recid, to nitify listeners to update the 'recid' in redis 
	return res 

@lru_cache(maxsize=None)
def get_folder(hkey, name, parent): 
	''' if None, create a new fold under parent '''
	try:
		folder =  redis.kvr.hget(hkey, name)
		if folder : return folder 
		folder	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/create_folder", headers = headers(), json={"name": name,"folder_token": parent}).json().get('data',{}).get('token','')
		if folder: redis.kvr.hset(hkey, name, folder)
		return folder 		
	except Exception as ex:
		print ( ">>get_folder ex:", ex, "\t|", hkey, name,parent, flush=True)
		traceback.print_exc()

month_folder = lambda ap, sub, month:	get_folder(f"ap:{ap}:sub-folder", f"{sub}-{month}", hgetall(f"ap:{ap}").get("rootfolder",''))
date_folder  = lambda ap, sub, date:	get_folder(f"ap:{ap}:sub-folder", f"{sub}-{date}", month_folder(ap, sub, date[0:6]) )

def clone( template_token, title, parent_folder:str="", type:str='bitable'):
	''' 2022.9.27 '''
	try:
		assert template_token 
		res	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template_token}/copy", headers = headers(), json={"name":title,	"type": type,"folder_token":parent_folder }).json()
		print ("cloned:", res )  #cloned: {'code': 0, 'data': {'file': {'name': 'hello', 'parent_token': '', 'token': 'bascnCLZKmJmMIul3NSrL3fUcrf', 'type': 'bitable', 'url': 'https://sentbase.feishu.cn/base/bascnCLZKmJmMIul3NSrL3fUcrf'}}, 'msg': 'success'}
		token = res.get('data',{}).get('file',{}).get('token','') 
		if not token or token is None: return print (">> Failed to clone:", res, template_token, title, parent_folder, flush=True) 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{token}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		return token 
	except Exception as ex:
		print ( ">>clone ex:", ex, "\t|", template_token, title, parent_folder, type, flush=True)
		traceback.print_exc()
#clone("shtcn4RlvSMOMupD4Hf5bgMfBuN", "xxx", "fldcnx3eFWhksJkjy03BJ55P7bh", "sheet") 

def clone_bitable( template_token, title, parent_folder:str=""):
	''' 2022.10.2 '''
	try:
		assert template_token 
		res	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template_token}/copy", headers = headers(), json={"name":title,	"type": "bitable","folder_token":parent_folder }).json()
		print ("cloned:", res ) 
		token = res.get('data',{}).get('file',{}).get('token','') 
		if not token or token is None: return print (">> Failed to clone:", res, template_token, title, parent_folder, flush=True) 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{token}/public?type=bitable",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		print( requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{token}/subscribe?file_type=bitable", headers = headers()).json())
		return token 
	except Exception as ex:
		print ( ">>clone ex:", ex, "\t|", template_token, title, parent_folder, type, flush=True)
		traceback.print_exc()

@lru_cache(maxsize=None)
def pen_datexls(ap, page, pen, date): 
	''' every pen every day -> one xls  '''
	try:
		xls = redis.kvr.hget(f"ap:{ap}:date-{date}:page-{page}:pen-xls", pen)
		if xls : return xls
		sub	= hgetall(f"page:{page}").get('sub','en') 
		template = hgetall(f"page:{page}")["pen-xls-template"] # must exists 
		xls	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={"name":
			f"{date}-{ap_title(ap)}-{sub_title(sub)}-{pen_name(ap,pen)}",	"type": "sheet","folder_token": date_folder(ap, sub, date)  }).json().get('data',{}).get('file',{}).get('token','') 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{xls}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		redis.kvr.hset(f"ap:{ap}:date-{date}:page-{page}:pen-xls", pen, xls)
		return xls 
	except Exception as ex:
		print ( ">>pen_datexls ex:", ex, "\t|", ap, page, pen, date, flush=True)
		traceback.print_exc()
#print (pen_datexls ('CC1BE0E29824',"177.0.1", "D80BCB7002AE", '20220728') )

def apdate_bitable(ap, page, date): 
	''' every pen every day -> one bitable  '''
	try:
		token = redis.kvr.hget(f"ap:{ap}:date-{date}:page-{page}:ap-filetoken", "bitable")
		if not token or token is None: 
			token = clone(hgetall(f"page:{page}")["ap-bitable-template"], f"{date}-{ap_title(ap)}-{page_title(page)}", date_folder(ap, hgetall(f"page:{page}").get('sub','en') , date) )
			redis.kvr.hset(f"ap:{ap}:date-{date}:page-{page}:ap-filetoken", "bitable", token)

		tables = requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json()
		if not 'items' in tables.get('data',{}) or tables.get('msg','') == 'NOTEXIST' : #{'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
			redis.kvr.hdel(f"ap:{ap}:date-{date}:page-{page}:ap-filetoken", "bitable")
			return apdate_bitable(ap, page, date) # dead loop? cannot put into a LRUcache | will be trigger when file is manually deleted 

		return (token,  tables['data']['items'][0]['table_id'])  # first_table
	except Exception as ex:
		print ( ">>apdate_bitable ex:", ex, "\t|", ap, page, date, flush=True)
		traceback.print_exc()
#apdate_bitable("CC1BE0E29824", "0.100.0", "20220728")

@lru_cache(maxsize=None)
def page_datexls(ap, page, date): # every page every day -> one excel 
	try:
		xls = redis.kvr.hget(f"ap:{ap}:date-{date}:page-xls", page)
		if xls : return xls
		template = hgetall(f"page:{page}")["xls-template-page"] # must exists 
		xls	= requests.post(f"https://open.feishu.cn/open-apis/drive/v1/files/{template}/copy", headers = headers(), json={"name":
			f"{date}-{ap_title(ap)}-{sub_title(page)}",	"type": "sheet","folder_token": date_folder(ap, hgetall(f"page:{page}").get('sub','en'), date)  }).json().get('data',{}).get('file',{}).get('token','') 
		requests.patch(f"https://open.feishu.cn/open-apis/drive/v1/permissions/{xls}/public?type=sheet",headers = headers(),json={"external_access": True, "security_entity": "anyone_can_view", "comment_entity": "anyone_can_view", "share_entity": "anyone",  "link_share_entity": "tenant_readable",  "invite_external": True})
		redis.kvr.hset(f"ap:{ap}:date-{date}:page-xls", page, xls)
		return xls 
	except Exception as ex:
		print ( ">>page_date_xls ex:", ex, "\t|", ap, page, pen, date, flush=True)

def update_cells(xls, cell_label_dict, sheet_id=None):
	''' cell: C2, {C2 : one} '''
	if sheet_id is None: sheet_id = first_sheet(xls) 
	return [requests.put(f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{xls}/values", headers = headers(), json={"valueRange":{"range": f"{sheet_id}!{cell}:{cell}","values": [ [label] ]} }).json() for cell,label in cell_label_dict.items() if cell and label ]

write_png = lambda xls, range="Q7PlXT!H7:H7", name='test.png': requests.post(f"https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{xls}/values_image", headers = headers(), json={ 
									"range": range, 
									"image": json.loads(redis.kvr.hget('config:png', name)),
									"name": name} ).json()
#print ( write_png("shtcnMWL7GZMrJbWJCntkA9uiy6", "fc8edf!D3:D3", 'open.png'))

def bitable_first_table( token:str, retry:int=3):
	''' 2022.10.10 '''
	for i in range( retry ) : 
		res	= requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json() # 第一次调用常常失败	#print ("get table:", token, res )  #get table: wikcnEGzujMBKAKInlV5tDPUUlf {'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
		if res.get('code','') == 0: return res['data']['items'][0]['table_id'] #get table: bascn6LoA7vEyDCn47dTZfOtZdg {'code': 0, 'data': {'has_more': False, 'items': [{'name': '实时笔迹', 'revision': 0, 'table_id': 'tbl9PrDPNeWrEOah'}, {'name': '答题卡答案', 'revision': 0, 'table_id': 'tblh6scvoQHuTjLi'}, {'name': '数据字典', 'revision': 0, 'table_id': 'tblUp2CohwzCLDui'}], 'page_token': 'tblUp2CohwzCLDui', 'total': 3}, 'msg': 'success'}
		print ( f"No. {i}:", res) 
		time.sleep( max(1,  int (retry * random.random()) )  ) 

	return None 

@cache.cache()
def apdatepage_token(ap:str="CC1BE0E29824",date:str="20220929", page:str="0.0.0"): 
	'''	日卡每天一个文件bitable， 只建不删， 必须位置对应，不能用kwargs， 否则cache 失效 , 20221010 ''' 
	prefix	="apdatepage"
	sub		= hgetall(f"page:{page}").get('sub','en')
	template= redis.kvr.hget(f"page:{page}", f"template-{prefix}")
	folder	= redis.kvr.hget(f"ap:{ap}", f"sub-{sub}:folder")
	token	= clone_bitable( template, f"{date}-{page_title(page)}-" + hgetall('config:suffix-title').get(prefix, prefix), folder)
	if token: 
		redis.r.set(f"rc:token:{token}", apdatepage_token.key(ap, date, page) ) # token -> key 
		return  token

@cache.cache()
def apdatepage_table(token:str, retry:int=3):  #ap:str="CC1BE0E29824",date:str="20220929", page:str="0.0.0"
	''' 必须位置对应，不能用kwargs， 否则cache 失效 '''
	for i in range( retry ) : 
		res		= requests.get(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables",headers = headers()).json() # 第一次调用常常失败	#print ("get table:", token, res )  #get table: wikcnEGzujMBKAKInlV5tDPUUlf {'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
		print ( res ) 
		code	= res.get('code','')
		if code == 0: return res['data']['items'][0]['table_id'] #get table: bascn6LoA7vEyDCn47dTZfOtZdg {'code': 0, 'data': {'has_more': False, 'items': [{'name': '实时笔迹', 'revision': 0, 'table_id': 'tbl9PrDPNeWrEOah'}, {'name': '答题卡答案', 'revision': 0, 'table_id': 'tblh6scvoQHuTjLi'}, {'name': '数据字典', 'revision': 0, 'table_id': 'tblUp2CohwzCLDui'}], 'page_token': 'tblUp2CohwzCLDui', 'total': 3}, 'msg': 'success'}
		if code == 1002 : # { "code": 1002, "msg": "note has been deleted",  "data": {}}
			key		= redis.r.get(f"rc:token:{token}")
			redis.r.delete(f"rc:token:{token}", key if key is not None or key else "") # invalidate 
			return None
		print ( f"No. {i}:", res, token) #No. 0: {'code': 91402, 'msg': 'NOTEXIST', 'data': {}}
		time.sleep( max(1,  int (retry * random.random()) )	  ) 
	return None

@cache.cache()
def rec_id(token, table, ap,date, page, pen, item): 
	''' init at the very first time when the new item is born  '''
	#if not redis.r.exists( rec_id.key(token, table, ap,date, page, pen, item) ):
	data	= {"fields": { "ap":  ap, 	"page": page, "date" : date, "pen":pen, "姓名": pen_name(ap,pen), "item":item , "sub": hgetall(f"page:{page}").get('sub','en')} }
	res		= requests.post(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables/{table}/records",headers = headers(),json=data).json() 
	redis.r.publish(f"log-recid", json.dumps(res)) 
	return  res.get('data',{}).get('record', {}).get('record_id', '')

@cache.cache()
def img_put(token, table, recid, ap,date, page, pen, item, zlen):  #zlen = redis.kvr.zcard(f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}")
	''' run once, with different zlen , under cache machism '''
	try:
		if not recid or not item or 'select' in item or not token or not table: return 
		strokes		= redis.kvr.zrange(f"stroke:ap-{ap}:date-{date}:page-{page}:pen-{pen}:item-{item}", 0, -1)
		img_bytes	= strokes_to_png(strokes, aslist=False)
		img_token	= upload_media(token, img_bytes, file_name=f"{item}.png")['data']['file_token']
		res = requests.put(f"https://open.feishu.cn/open-apis/bitable/v1/apps/{token}/tables/{table}/records/{recid}",headers = headers(),json={"fields":{"原迹": [{"file_token": img_token}] }}).json()
		print( f"img-put: token={token}, table={table}, item={item}", zlen, img_token, res )
		return img_token
	except Exception as ex:
		print ( ">>img-put ex:", ex, "\t", token, flush=True) 
		exc_type, exc_value, exc_obj = sys.exc_info() 	
		traceback.print_tb(exc_obj)

if __name__ == '__main__': 
	print ( apdatepage_table.key("CC1BE0E29824", "20220932", "0.0.0") )