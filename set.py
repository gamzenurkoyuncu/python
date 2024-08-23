# set = collection which is unordered, unindexed. No duplicate values

utensils = {'fork','spoon','knife','knife'} # juts one knife appears
dishes = {'bowl','plate','cup'}

utensils.add('napkin')
utensils.remove('fork')
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes) # elements from both of them

print(utensils.difference(dishes)) # utensils have dishes do not have
print(utensils.intersection(dishes)) # elements that have common
for x in dinner_table:
    print(x)
