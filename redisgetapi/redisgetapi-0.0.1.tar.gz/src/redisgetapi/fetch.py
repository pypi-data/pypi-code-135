#!/usr/bin/env python3
from ssl import SSLSyscallError
import requests, redis, ast, logging, sys, time, fire


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(".debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class RedisEndPoint:


    def __init__(self,url,redis_host,redis_port,redis_expire):
        self.url = url
        self.redis_host = redis_host # default is localhost
        self.redis_port = redis_port # default is 6379
        self.redis_expire = redis_expire


    def get_client(self):
        try:
            return redis.Redis(host=f'{self.redis_host}', port=self.redis_port, db=0)
        except Exception as e:
            logging.error(f'{e}')

    def get_results(self):
        try:
            obj = requests.get(self.url).text
            self.get_client().set('res', obj)
            self.get_client().expire('res',self.redis_expire)
            return obj
        except Exception as e:
            logging.error(f'{e}')
 
    def cache_data(self):
        try:
            return ast.literal_eval(self.get_client().get('res').decode())
        except Exception as e:
            logging.error(f'{e}')
        
    def fetch_endpoint(self):
        try:
            if not self.get_client().get('res'):
                logging.info('fresh return ...')
                return self.get_results()
            else:
                logging.info('cached return cross-check for authenticity ...')
                return self.cache_data()
        except Exception as e:
            logging.error(f'{e}')

def script_call(url,host,port,expire):
    try:
        return RedisEndPoint(f'{url}',f'{host}',port,expire).fetch_endpoint()
    except Exception as e:
        logging.error(f'{e}')


def cli_call(url,host,port,expire):
    try:
        return logging.info(RedisEndPoint(f'{url}',f'{host}',port,expire).fetch_endpoint())
    except Exception as e:
        logging.error(f'{e}')

if __name__ == '__main__':
    while True:
        fire.Fire(cli_call)
        time.sleep(5)