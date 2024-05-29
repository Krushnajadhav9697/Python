a= ['robert','ANUJ','mishraji','saud','jadhav','nair']
b="aeiou"
#print name with last letter 'i'
for i in a:
    if i[-1]=='i':
        print(i)

print("----------------------------------------------------------------------")
#print name with 'r' letter in them
for i in a:
    for j in i:
        if j=='r':
            print(i)
            break
        
print("----------------------------------------------------------------------")
#print number of vowels in name using for loop 
for i in a:
    c=""
    for j in i:
        if j.lower() in b:
            c=c+j
            
            
    print(f"{i} = {c}  {len(c)}")

print("----------------------------------------------------------------------")
#print number of vowels in name using while loop
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j] in b:
            c=c+1
        j=j+1
    print(f"{a[i]} = {c} {len(c)}")
    i=i+1
    

print("----------------------------------------------------------------------")
#print name with 4 numbers of letter 
for i in a:
        if len(i)==4:
            print(i)
            


