def divide(func):
    def inner(x,y):
        print('divide x and y.')
        if y==0:
            print('Cannot be divided')
            return
        return func(x,y)
    return inner
@divide
def divide(x,y):
    print(x/y)
divide(6,0)