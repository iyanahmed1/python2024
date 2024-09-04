from time import sleep,time
#define a function which takes some arguements 
def f(sleep_time=0.1):
    sleep(sleep_time)#f is expected to be fed sleep. default value of 0.1
# we therefore donr need g anymore
def measure(func):#holds all the time calculations
    def wrapper(*args,**kwargs):
        t=time()
        func(*args,**kwargs)
    print(func.__name__,'took:', time()-t)#indent under the func paramenter
    return wrapper
f=measure(f)#decoration point
f(0.2)
f(sleep_time=0.3)