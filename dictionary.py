#Dictionary
# is mutable , key cant be duplicate , cvalue can be duplicate
a={'name':'krushna','age': 23}

print(a)
print(len(a))
print(type(a))

a['age']=25

a['city']='ambenath'

print(a)

for i in a:
    print(f"{i}")

