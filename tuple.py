# tuple = collection which is ordered and unchangeable
#      used to group together related data

student = ('Coding World',21,'male')

print(student.count('Coding World'))
print(student.index('male'))

for x in student:
    print(x)

if 'Coding World' in student:
    print('yes')
