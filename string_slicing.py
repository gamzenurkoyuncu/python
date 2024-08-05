# slicing = create a substring by extracting elements from another string
             indexing [] or slice ()
             [start:stop:step]

name = 'Coding World'
first_name = name[0]
print(first_name)  # C

first_name = name.split()[0]
last_name = name.split()[1]
print(first_name, last_name)  # Coding World

first_name = name[2]
print(first_name) # d

first_name = name[0:2]
print(first_name) # Co , it takes 0 and 1 until 2

first_name = name[:6]
last_name = name[7:12]
print(first_name, last_name)  # Coding World

first_name = name[:3]  # [0:3]
last_name = name[4:]  # [4:end]
funky_name = name[::2]  # [0:end:2]
reversed_name = name[::-1]  # [0:end:-1]
print(first_name)  # Cod
print(last_name)  # ng World
print(funky_name)  # Cdn ol
print(reversed_name)  # dlroW gnidoC

website = 'https://google.com'
website2 = 'https://wikipedia.com'
slice = slice(7,-4)

print(website[slice])  # /google
print(website2[slice])  # /wikipedia


