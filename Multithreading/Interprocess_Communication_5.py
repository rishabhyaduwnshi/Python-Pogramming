from threading import *
from time import *

class Data:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()
        
    def write(self,data):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = data
        self.flag = True
        self.lock.release()
        
    def read(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
        return x
        
def producer(data):
    i = 1
    while True:
        data.write(i)
        print("Producer : ",i)
        i += 1
        
def consumer(data):
    while True:
        x = data.read()
        print("Consumer : ",x)
        
data = Data()

t1 = Thread(target = lambda:producer(data))
t2 = Thread(target = lambda:consumer(data))
    
t1.start()
t2.start()

t1.join()
t2.join()
