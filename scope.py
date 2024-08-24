# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = 'Coding' # global scope (available inside, outside functions)
def display_name():
    # name = 'Code' # local scope = variable is inside of the function
    print(name)

display_name() # It will use local variable first (local, enclosing, global, built-in)
print(name)
