#gererator

#when we use yield keyword, the function retains it's state, which is why every time when we call,
#new value is getting printed
def get_current_Day():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    i = -1;
    while True:
        i = (i+1)%7
        yield days[i]
        

d = get_current_Day()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
