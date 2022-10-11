#2022.10.2		
from penly import * 

def wiki_month_folder(ap:str="CC1BE0E29824", sub:str='en',space:str="7148443017811132420", month:str="202205", type:str='docx'): 
	assert len(month) == 6
	v = redis.kvr.hget(f"ap:{ap}:sub:{sub}:wiki", month)
	if v is not None: return json.loads(v) 
	res	= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space}/nodes", headers = headers(), json={
			"obj_type": type,
			"parent_node_token": "",
			"node_type": "origin",
			"title": month,
			"origin_node_token": ""
		}).json()
	redis.r.publish('pen_wiki_space',json.dumps(res))
	data = json.dumps( res.get('data',{}).get('node',{}) )
	redis.kvr.hset(f"ap:{ap}:sub:{sub}:wiki", month, data) 
	return res.get('data',{}).get('node',{})
#print (month_folder()) 

def wiki_date_folder(ap:str="CC1BE0E29824", sub:str='en', space:str="7148443017811132420", date:str="20220528", type:str='docx'): 
	assert len(date) == 8 
	v = redis.kvr.hget(f"ap:{ap}:sub:{sub}:wiki", date)
	if v is not None and v : return json.loads(v) 
	res	= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space}/nodes", headers = headers(), json={
			"obj_type": type,
			"parent_node_token": wiki_month_folder(ap, sub, space, date[0:6], type)['node_token'],
			"node_type": "origin",
			"title": date,
			"origin_node_token": ""
		}).json()
	redis.r.publish('pen_wiki_space',json.dumps(res))
	data = json.dumps( res.get('data',{}).get('node',{}) )
	redis.kvr.hset(f"ap:{ap}:sub:{sub}:wiki", date, data) 
	return res.get('data',{}).get('node',{})
#print (date_folder()) 

def wiki_date_file(ap:str="CC1BE0E29824", page:str="0.0.0", date:str="20220628", suffix:str="page-bitable"): 
	'''	wiki per page , 20220729-{page}:page-bitable   ''' 
	sub		= hgetall(f"page:{page}").get('sub','en')
	space	= hgetall(f"ap:{ap}:sub:{sub}").get("space",'0') #sub_wiki_space(ap, sub) , change to a default space id later 
	key		= f"{date}-{page}:{suffix}"
	v		= redis.kvr.hget(f"ap:{ap}:sub:{sub}:wiki", key)
	if v is not None and v : return json.loads(v) 

	parent		= wiki_date_folder(ap, sub, space, date)['node_token']
	src_spaceid	= hgetall("config:wiki")["template-space-id"] 
	src_token	= hgetall(f"page:{page}")[f"wiki-{suffix}"]
	arr			= {"target_parent_token": parent,  "target_space_id": space,  "title": f"{date}-{page_title(page)}-" + hgetall('config:suffix-title').get(suffix, suffix) }
	res			= requests.post(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{src_spaceid}/nodes/{src_token}/copy", headers = headers(), json=arr).json()
	redis.r.publish("pen_wiki_new_datefile", json.dumps(res) )
	data =  res.get('data',{}).get('node',{}) 
	redis.kvr.hset(f"wiki:space-{space}", key, json.dumps(data) )
	return data

if __name__ == '__main__': 
	print (wiki_date_file())
