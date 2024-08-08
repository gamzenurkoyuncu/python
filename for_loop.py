# for loop = a statement that will execute it's block of code
#           a limited amount of time

           while loop = unlimited
           for loop = limited

for i in range(10): # we will execute this code 10 times (0-9)
    print(i)

for i in range(10): # (0-10)
    print(i+1)

for i in range(50,100+1,2): # (50 to 100 by increasing 2)
    print(i)

for i in 'Coding World': # each letter will be appeared
    print(i)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(2) # it will go from 10 to 0 2 seconds apart
print('Happy new year!')
