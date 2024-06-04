#dictionary methods
a={'name':'krushna','age':23,'city':'ambernath','pin':421}
print(a.keys()) # printing only keys
print(a.values()) #printing only values
print(a.items())  #printing value and keys both

for keys,values in a.items():  # printing value with keys 
    print(keys,values)

#adding key in dict

a['phone']=5252525252
print(a)

a.update({'tel':78787878})
print(a)

#deleting item from dictionary

a.pop('tel') # delting value as per given keys
print(a)

a.popitem() #delete last key form dictionary
print(a)



del a['age'] # delete the key as per given key
print(a)

a.clear()
print(a)  #empty the dict

del a   #delete the whole dict
print(a)  





