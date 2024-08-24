# keyword arguments = arguments preceded by an identified when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first,middle, last):
    print('Hello ' +first+' '+middle+' '+last)

hello('John','Doe','Smith')

# the output will be Hello John Doe Smith

def hello(first,middle, last):
    print('Hello ' +first+' '+middle+' '+last)

hello(last='John',first='Doe',middle='Smith')

# the output will be Hello Doe Smith John
