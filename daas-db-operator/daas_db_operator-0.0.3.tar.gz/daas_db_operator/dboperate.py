import requests
import  json
import pandas as pd

from urllib import parse
session=requests.session()
def login(username,password):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    API='http://daas.smartsteps.com/qsqltest/certificateauth/authen/login'
    data={
           "userName":username,
            "password":password
        }
    data=parse.urlencode(data)
    res=session.post(API,headers=headers,data=data,verify=False)
    print(res.text)

    return res.headers['Authorization']


def excuteSql(username,password,excuteSql,sqlType):
    API='http://daas.smartsteps.com/qsqltest/qsql/sqlexecute'
    header = {"Content-Type":"application/x-www-form-urlencoded","Authorization":login(username,password)}
    data={
           "executeSql": excuteSql,
           "sqlBasicExecuteType": sqlType
        }
    data=parse.urlencode(data)
    res=session.post(API,headers=header,data=data,verify=False)
    result =json.loads(res.text)
    return pd.DataFrame(result['result'])

