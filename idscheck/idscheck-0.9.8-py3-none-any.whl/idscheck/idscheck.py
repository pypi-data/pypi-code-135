import os
import sys


def cmd():
    args = sys.argv
    if len(args) == 1:
        status = os.system("curl http://172.17.0.1:8080")
        if int(status) != 0:
            os.system("curl http://10.10.0.1:8080")
    elif args[-1] == "gpu":
        status = os.system("curl http://172.17.0.1:8080/gpu")
        if int(status) != 0:
            os.system("curl http://10.10.0.1:8080/gpu")
    elif args[-1] == "top":
        status = os.system("curl http://172.17.0.1:8080/top")
        if int(status) != 0:
            os.system("curl http://10.10.0.1:8080/top")
    elif args[-1] == "topall":
        status = os.system("curl http://172.17.0.1:8080/top_all")
        if int(status) != 0:
            os.system("curl http://10.10.0.1:8080/top_all")
    elif args[-1] == "query":
        status = os.system("curl http://172.17.0.1:8080/query")
        if int(status) != 0:
            os.system("curl http://10.10.0.1:8080/query")
    else:
        print("Usage: idscheck [(Null)|gpu|top|topall]")


def gpu():
    status = os.system("curl http://172.17.0.1:8080/gpu")
    if int(status) != 0:
        os.system("curl http://10.10.0.1:8080/gpu")


def top():
    status = os.system("curl http://172.17.0.1:8080/top")
    if int(status) != 0:
        os.system("curl http://10.10.0.1:8080/top")


def topall():
    status = os.system("curl http://172.17.0.1:8080/top_all")
    if int(status) != 0:
        os.system("curl http://10.10.0.1:8080/top_all")


def query():
    status = os.system("curl http://172.17.0.1:8080/query")
    if int(status) != 0:
        os.system("curl http://10.10.0.1:8080/query")
