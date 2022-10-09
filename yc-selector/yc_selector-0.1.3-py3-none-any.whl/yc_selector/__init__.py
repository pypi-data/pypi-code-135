import json
class Query:
    def __init__(self,event,context):
        self.query=event['queryStringParameters']
        self.body=event['body']
        #self.json=json.loads(self.body)
        self.original={
            'event':event,
            'context':context
        }
    def json(self):
        return json.loads(self.body)



routes={}

def route(path:str):
    print(f'decorating with {path}')
    def retry(func):
        routes[path]=func
        return func
    return retry


def call_from_routes(route:str,query):
    if route in routes:
        return {
        'statusCode': 200,
        'body': routes[route](query),
        'headers':{
            'Content-Type': 'application/json'
        }
    }
    else:
        print(f"ERROR:Cant find route {route}")
        return {
        'statusCode': 404,
        'body': f'Route not {route} not found',
    }

def accept_request(event,context,routevar="Action"):
    action=event['params'][routevar]
    query=Query(event,context)
    return call_from_routes(action,query=query)
    #print(locals())

def init(event, context):
    accept_request(event,context)

