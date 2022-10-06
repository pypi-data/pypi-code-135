import os
import sys


def cmd():
    args = sys.argv
    if len(args) == 1:
        os.system("curl http://172.17.0.1:8080")
    elif args[-1] == "gpu":
        os.system("curl http://172.17.0.1:8080/gpu")
    elif args[-1] == "top":
        os.system("curl http://172.17.0.1:8080/top")
    elif args[-1] == "topall":
        os.system("curl http://172.17.0.1:8080/top_all")
    elif args[-1] == "query":
        os.system("curl http://172.17.0.1:8080/query")
    else:
        print("Usage: idscheck [(Null)|gpu|top|topall]")


def gpu():
    os.system("curl http://172.17.0.1:8080/gpu")


def top():
    os.system("curl http://172.17.0.1:8080/top")


def topall():
    os.system("curl http://172.17.0.1:8080/top_all")


def query():
    os.system("curl http://172.17.0.1:8080/query")
