"""import b#import the whole module
from c import ordinary
# we want to use spam
b.spam('This is spam')
b.spam2()
#a is a top file.it only contains statement to be excuted top to bottom
from b import func
from c import func
func()"""
import b,c
#import c
b.func()
c.func()
from b import func as bfunc
from c import func as cfunc
cfunc()
bfunc()