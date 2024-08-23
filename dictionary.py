# dictionary =  A changeable, unordered collection of unique key: value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'Ecuador':'Quito',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # it will add Germany to the dictionary
capitals.update({'USA':'Chicago'}) # it will change from Washington to Chicago
capitals.pop('Ecuador') # it will delete Ecuador from dictionary
capitals.clear() # it will clear all dictionary

print(capitals['Russia']) # Moscow
print(capitals['Germany']) # error first time before we add Germany to the dictionary
print(capitals.get('Germany')) # None
print(capitals.keys()) # dict_keys(['USA', 'India', 'Ecuador', 'Russia'])
print(capitals.values()) # dict_values(['Washington DC', 'New Dehli', 'Quito', 'Moscow'])
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('Ecuador', 'Quito'), ('Russia', 'Moscow')])

for key,value in capitals.items():
    print(key,value)

# USA Washington DC
# India New Dehli
# Ecuador Quito
# Russia Moscow
# Germany Berlin
