from threading import *
from time import *

class Alphabets(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            sleep(0.5) #doing sleep just for the sake of seeing mixed output
        

t = Alphabets()
t.start()
for i in range(65,91):
    print(i)
    sleep(0.5)

#joining the thread with main execution
t.join()
