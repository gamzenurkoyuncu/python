# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true

while 1==1:
  print("Help! I'm stuck in a loop") # it will go forever

name = ''

while len(name) == 0:
    name = input('Enter a name: ')
print('Hello ' + name + '!') 

name = None

while not name:
    name = input("Enter a name: ")
print("Hello " + name + "!")

# another way of writing the code above 


