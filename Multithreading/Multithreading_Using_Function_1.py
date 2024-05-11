from threading import *
from time import *


def display():
    for i in range(65,91):
        print(chr(i))
        sleep(0.5) #doing sleep just for the sake of seeing mixed output
        

t = Thread(target = display)
t.start()

for i in range(65,91):
    print(i)
    sleep(0.5)

#joining the thread with main execution
t.join()
