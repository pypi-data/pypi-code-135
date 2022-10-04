import requests
import random
import uuid
from datetime import datetime

def login(username,password):
 timpp = int(datetime.now().timestamp())
 gg = uuid.uuid1()
 phid = uuid.uuid1()
 url = "https://i.instagram.com/api/v1/accounts/login/"
 user00='1234567890qwertyuiopasdfghjklzxcvbnm'
 user01 = '1234567890'
 user02='QWERTYUIOPASDFGHJKLZXCVBNM'
 us1 = str("".join(random.choice(user00)for i in range(int(16))))
 us2= str("".join(random.choice(user01)for i in range(int(8))))
 us3= str("".join(random.choice(user02)for i in range(int(10))))
 us4= str("".join(random.choice(user01)for i in range(int(3))))
 headers = {
'x-ig-app-locale': 'en_US',
'x-ig-device-locale':'en_US',
'x-ig-mapped-locale':'en_US',
'x-pigeon-session-id':f'UFS-{uuid.uuid1()}-0',
'x-pigeon-rawclienttime':'1664819960.345',
'x-ig-bandwidth-speed-kbps':'-1.000',
'x-ig-bandwidth-totalbytes-b': '0',
'x-ig-bandwidth-totaltime-ms': '0',
'x-bloks-version-id':f'5cc1c229fc4fefd80dd601a{us2}6a218892bccaed0d68692b37e325c768b',
'x-ig-www-claim':'0',
'x-bloks-is-layout-rtl':'false',
'x-ig-device-id':str(gg),
'x-ig-family-device-id':str(phid),
'x-ig-android-id':'android-'+str(us1),
'x-ig-timezone-offset': '19800',
'x-fb-connection-type':'WIFI',
'x-ig-connection-type':'WIFI',
'x-ig-capabilities': '3brTv10=',
'x-ig-app-id':'567067343352427',
'priority':'u=3',
'user-agent':'Instagram 253.0.0.23.114 Android (28/9; 320dpi; 720x1280; samsung; SM-G'+str(us4)+'N; star2qltechn; qcom; en_US; 399993167)',
'x-mid':f'YzscNwAB{us3}Wm9KA33QKO',
'ig-intended-user-id':'0',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'content-length':'1016',
'accept-encoding':'zstd, gzip, deflate',
'x-fb-http-engine':'Liger',
'x-fb-client-ip': 'True',
'x-fb-server-cluster':'True',
}
 data = {
    'signed_body': 'SIGNATURE.{"jazoest":"22472","country_codes":"[{\\"country_code\\":\\"91\\",\\"source\\":[\\"default\\"]}]","phone_id":"'+str(phid)+'","enc_password":"#PWD_INSTAGRAM:0:'+str(timpp)+':'+str(password)+'","username":"'+str(username)+'","adid":"'+str(uuid.uuid1())+'","guid":"'+str(gg)+'","device_id":"android-'+str(us1)+'","google_tokens":"[]","login_attempt_count":"0"}',
}

 reqq = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
 return reqq