# list = used to store multiple items in a single variable

food = ['pizza','hamburger','hotdog','spaghetti','pudding']

print(food[0])
print(food[1])
print(food[2])
print(food[3])
print(food[4])

food.append('ice cream')
food.remove('hotdog')
food.pop() # it will remove the last element
food.insert(0,'cake')
food.sort() # it will make a list
food.clear() # it will clear everything on the list

for x in food:
    print(x)
