from threading import *
from time import *

class Data:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.condition= Condition()
        
    def write(self,data):
        self.condition.acquire()
        self.condition.wait(timeout = 0)
        self.data = data
        self.condition.notify()
        self.condition.release()
        
    def read(self):
        self.condition.acquire()
        self.condition.wait(timeout = 0)
        x = self.data
        self.flag = False
        self.condition.notify()
        self.condition.release()
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
