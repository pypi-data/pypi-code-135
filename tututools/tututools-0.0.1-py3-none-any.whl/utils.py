import os
import zmq
import numpy as np
import pickle
from matplotlib import pyplot as plt

def getFiles(dir):
    flist=[]
    for root,dirs,files in os.walk(dir+'/'):
            for file in files:
                flist.append(os.path.join(root,file))
    return flist


class rpyplot(object):
    def __init__(self, addr = '127.0.0.1', port = 1234) -> None:
        self.pipe = zmq.Context().socket(zmq.PAIR)
        self.pipe.bind('tcp://{}:{}'.format(addr, port))

    def imshow(self, ndarray):
        plt.imshow(ndarray)
        data = pickle.dumps(ndarray)
        send_data = {'op':'imshow', 'data':data}
        send_data = pickle.dumps(send_data)
        self.pipe.send(send_data)
        
    def subplot(self, index: int):
        send_data = {'op':'subplot', 'index':index}
        send_data = pickle.dumps(send_data)
        self.pipe.send(send_data)

    def show(self,):
        send_data = {'op':'show'}
        send_data = pickle.dumps(send_data)
        self.pipe.send(send_data)
        while True:
            end_op = self.pipe.recv_string()
            if end_op == 'end_show':
                break
