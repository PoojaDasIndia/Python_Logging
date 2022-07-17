"""With the python module inspect, one can inspect (not kidding) the run-time python stack.
 Among other things, this makes it possible to get the name of the current function or callers. 
 Handy for logging or debugging purposes. A simple script to illustrate:"""

import inspect

# functions
def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]
def foo():
    print ("hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
    bar()
def bar():
    print ("hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
johny = foo
# call them!
foo()
bar()
johny()


"""

output:

hello, I'm foo, daddy is ?
hello, I'm bar, daddy is foo
hello, I'm bar, daddy is ?
hello, I'm bar, daddy is ?
How does it work?    
 
"""

"""inspect.stack() returns a list with frame records.

In function whoami(): 

inspect.stack()[1] is the frame record of the function that calls whoami, like foo() and bar().

The fourth element of the frame record (inspect.stack()[1][3]) is the function name.
The rest should be obvious (check the python docs on inspect for more information),except that johny() thinks he's function bar().
 
 That's because johny actually just points to the code of bar() and 
 the function name bar is associated with the code and not with the variables."""