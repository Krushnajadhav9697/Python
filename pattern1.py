#print(ord('A'))
#print(chr(65))
i=1
while i<=5:
    j=1
    while j<=5:
        if i==1:
            print('A',end=" ")
        elif j==1:
            print('c',end=" ")
        elif i==j:
            print('b',end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
        
        


