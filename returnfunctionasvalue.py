
"""def greetings(name):
    def hello():
        return'Hello '+ name+'!'
    return hello#returns the inner hello() function
greet=greetings('Anne')
print(greet())"""
#python decorators 
#is a function that takes in a function and returns it ny adding some functionality
#an object that implements the special __call_- method is termed as a calable
#a decorator is thus callable that returns a callable
def make_pretty(func):
    def inner():
        print('I got decorated.')
        func()
    return inner
def ordinary():
    print('I am ordinary.')
decorated_func=make_pretty(ordinary)#make pretty is a decorator
decorated_func()
#@symbol with decorator
#decorating functions with parameters
def divide(x,y):
    return x,y
#if we pass y as 0 we get an error. 
#make a decorator to check if this is the case
