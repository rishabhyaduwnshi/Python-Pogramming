from threading import *
from time import *

def display(string):
    l.acquire()
    for x in string:
        print(x)
    l.release()


t1 = Thread(target=display,args=("HELLO",))
t2 = Thread(target=display,args=("welcome",))

l = Semaphore(2)

t1.start()
t2.start()

t1.join()
t2.join()
