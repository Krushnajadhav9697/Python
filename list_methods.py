#list methods

#append :- Add value at last index

a=[1,12,'krushna']
a.append(45)
print(a)

#extend :- Add 2 list

a=['krushna',45,23,'apple']
b=[1,2,'mango']
a.extend(b) # add b in a
b.extend(a)
print(a)
print(b)

#insert :- add the value at desired index/position

a= ['apple',23,14,56,45]
a.insert(2,'mango')
print(a)

#pop:- delete the last  value

a= [1,2,56,'kru']
a.pop()
print(a)

#remove :- remove/delete the value we want from list

a=['abc','naruto',36,458,'krush']
a.remove(36)
print(a)

#count :- gives the count of duplicate values in list

a=[1,2,2,4,4,4,5]
b=a.count(4)
print(b)

#index:- gives the index value

a=[1,2,34,45,66]
print(a.index(1))
print(a.index(a[2]))

#reverse :- reverse the list

a=['krushna',56,108,'rohit45',78]
a.reverse()
print(a)

#del :- delete the all list value

b=[21,'krush','abc',44,56]
del b
print(b)



