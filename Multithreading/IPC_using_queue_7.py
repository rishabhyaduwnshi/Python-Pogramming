from threading import *
from time import *
from queue import *

def producer(queue):
    i = 0
    while True:
        queue.put(i)
        print("Produer : ",i)
        sleep(0.2)
        i += 1

def consumer(queue):
    while True:
        x = queue.get()
        print("Consumer : ", x)
        sleep(0.2)

#queue module has all the functionality of acquiring the lock and releasing it internally so we don't have to handle it  
q = Queue()

t1 = Thread(target = lambda:producer(q))
t2 = Thread(target = lambda:consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()


