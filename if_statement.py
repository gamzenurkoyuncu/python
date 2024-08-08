# if statement = a block of code that will execute if it's condition is true

age = int(input("Enter your age: "))

if age >= 18:
    print("You are a teenager.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not a teenager.")

# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input('What is the temperature outside?: '))

if temp>=0 and temp<=30: # all conditions must be true
    print('the temperature is good today!')
    print('go outside!')

elif temp< 0 or temp>30: # one of them must be true
    print('the temperature is bad!')
    print('stay inside!')

if not(temp>=0 and temp<=30):
    print('the temperature is good today!')
    print('go outside!')

elif not(temp< 0 or temp>30):
     print('the temperature is bad!')
     print('stay inside!')

# if temperature is 0
# the outcome will be 'the temperature is bad' and 'stay inside!'
# if temperature is 40
# the outcome will be 'the temperature is good today' and 'go outside'

