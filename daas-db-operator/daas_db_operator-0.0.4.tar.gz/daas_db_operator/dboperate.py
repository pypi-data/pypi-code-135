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
    if result['message']!='成功' :         # 判断变量是否为 python
        return result    # 并输出欢迎信息
    else:             # 条件不成立时输出变量名称
        if isinstance(result['result'],list) :
            result['result']=pd.DataFrame(result['result'])
        return result

