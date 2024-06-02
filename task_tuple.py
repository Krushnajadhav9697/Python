#in given list change value of middle no to yes

a=[1,2,3,([33,88,'abc',('yes','no','yes')])]

a[3][3]=('yes','yes','yes')

    #OR

b=list(a[3][3])
b[1]='yes'
a[3][3]=tuple(b)
print(a)
















