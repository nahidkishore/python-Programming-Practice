name=['nahid','niloy','munni','tania','jannat','kishore','Hrdioy']
print(name)
print(name[1])
print(name[3])

print(name[-1])#Right side theke 1st e -1, -2, -3
print(name[-2])

# array list er moddhe niloy  ache kina seta check korar jonno "in " opeartion add korbo...jodi na thake  tahole false dekhabe, r thakle true return korbe

# in operation
print("niloy" in name ) # in operation

# not in opeartion
print("nahidul" not in name) # true
print("nahid" not in name) #false

# add element in list
print(name + ['ewu', 'BD'] )

#Range of Indexes
print(name[2:5])
#List Length
print(len(name))

#append mane push kora
# Add Items
#To add an item to the end of the list, use the append() method:

name.append('dhaka')
print(name)
#To add an item at the specified index, use the insert() method:

name.insert(2,'katiadi')
print(name)
#Remove Item
name.remove('tania')
print(name)
#pop
name.pop()
print(name)
#The del keyword removes the specified index:
del name[5]
print(name)
#The del keyword can also delete the list completely:
name1=['apple', 'banana', 'amm']
del name1
#The clear() method empties the list:
name2=['apple', 'banana', 'amm']
name2.clear()
print(name2)
