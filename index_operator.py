# index operator [] = gives access to a sequence's elements (str,list,tuples)

name = 'coding World'

if(name[0].islower()):
    name = name.capitalize()

print(name) # Coding World

first_name = name[0:3].upper()
last_name = name[7:].lower()
last_character = name[-1]
print(first_name) # COD
print(last_name) # world
print(last_character) # d 
