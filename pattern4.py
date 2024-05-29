'''
i=0
row=4
while i<=row:
    a=0  
    while a<=(row - i-1):
        print(" ",end=" ")
        a=a+1
    j=0
    while j<=i:
        print(chr(97+i),end=" ")
        j=j+1
    i=i+1
    
    print()
'''
'''
row=97
i=1
while row<=101:
    cols=1
    while cols<=5-i:
        print(" ",end=" ")
        cols=cols+1
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col+=1
    i+=1
    row+=1
    print()
'''
i=97
b=4
while i<=101:
    a=1
    while a<=b:
        print("@",end=" ")
        b=b-1
        
    j=97
    while j<=i:
        print(chr(i),end=" ")
        j=j+1
    i=i+1
    
    
   
    print()
    





