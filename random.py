#random

import random
#print name randomly form list 
name=['abc','krushna','ramrao','jadhav','kishsn','pritii']
print(random.choice(name))
print(random.sample(name,k=3))
print(name)
random.shuffle(name) # shuffle the list
print(name)

pin=[1,2,6,4,5,3,7,8,9,0]

print(random.randint(1,10)) # give random value form 1 to 9
print("".join(random.sample('1234567890',k=4)))
for i in range(1,5,1):
    print(random.choice(pin),end="")
