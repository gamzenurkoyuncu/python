# function = a block of code which is executed only when it is called

def hello(name): # when we put one parameter here, we can use one value below
    print("Hello World" + name)
    print('Have a nice day')

hello(' Coding') # we have to call the function
Hello World Coding
Have a nice day

def hello(first_name, last_name): # now we have two parameters
    print("Hello " + first_name + " " + last_name)
    print('Have a nice day')

hello('Coding','World')

def hello(first_name, last_name,age):
    print("Hello " + first_name + " " + last_name + " " + age)
    print('Have a nice day')

hello('Coding','World','21')

# Hello Coding World 21
# Have a nice day
