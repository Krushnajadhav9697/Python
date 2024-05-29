#create list of 1 to 10 and  saparate list of odd and even number 

a=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]


for i in a :
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    

print(even)
print(odd)


print("-------------------------------------------------")

# find count of duplicate number and their count  

a=[1,2,3,4,5,6,7,7,6,6,4]
b=[]
c1=[]
c=0
for i in a :
    if i not in b:
        b.append(i)
    else:
        c1.append(i)
print(b)
print(c1)
for i in b:
    c2=0
    for j in c1:
        if j ==i:
            c2=c2+1

    if c2:
        print(f"{i} duplicate are {c2}")

print("-------------------------------------------------")

#print list value using for loop

a=[[['abc','pqr','jahfh']]]
for i in a[0][0]:
    print(i)

    
print("-------------------------------------------------")
#print list value using if  

a=[[['abc','pqr','jahfh']]]
i=0

if i <len(a[0][0]):
    print(a[0][0][i])
    i=i+1
    print(a[0][0][i])
    i=i+1
    print(a[0][0][i])


print("-------------------------------------------------")

#print list value using while loop
a=[[['abc','pqr','jahfh']]]
i=0
print(len(a[0][0]))
while i<len(a[0][0]):
    print(a[0][0][i])
    i=i+1


print("-------------------------------------------------")


a=[[1,2,3,4],[5,6,7,8]]
for i in a :
    for j in i:
        print(j)
  
