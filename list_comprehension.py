#list comprehension

odd=[i for i in range(1,101,2) ]
print(odd)
even=[i for i in range(2,101,2)]
print(even)

a=['robart','anuj','abc']

b=[i.upper() for i in a ]
print(b)

c=[i for i in a if 'b' in i ]
print(c)
    
import random
name=['abc','krushna','ramrao','jadhav','kishsn','pritii']
#a= random.choice(name)
print(random.choice(name))

pin=[1,2,6,4,5,3,7,8,9,0]
for i in range(1,5,1):
    print(random.choice(pin),end="")


