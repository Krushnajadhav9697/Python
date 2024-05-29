'''
n=17

for i in range (2,n,1):
    if n/i==1 :
        print("Number is prime")
else:
    print("NO is not prime")

'''


'''
n=17
for i in range (2,n,1):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime no")
'''
'''
for i in range (1,51,1):
    for j in range (2,i,1):
        if i/j==1:
            print(i)
        else:
            pass
'''
for i in range (1,101,1):
    for j in range (2,i,1):
        if i%j==0:
            break
    else:
        print(i)
            
