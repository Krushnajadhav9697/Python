##1)take input from user and print its input value using input function

##user=input("enter name ")
##print(user)

##2)create a string and print the last element

##name='krushna'
##print(name[-1])

##3)create a string and print second last element

##name='krushna'
##print(name[-2])

##4)create a string as eg:"hellohellohellohello" and print it

##a='hello'
##print(a*4)

##5)create  two string like "hello" and "world" and print "helloworld"

##a='hello'
##b='world'
##print(a+b)

##6)create two variable and swap its value eg a=10,b=20 afer swapping there output is a=20,b=10

##a=10
##b=20
##a,b=b,a
##print(a,b)

##7)create a tuple like(1,2,3,4,3,2) and count number of  occurrences  of 3

##a=(1,2,3,4,3,2)
##b=a.count(3)
##print(b)

##8)create a tuple like(1,2,3,4,3,2) and print the index number of 3

##a=(1,2,3,4,3,2)
##print(a.index(3))

##9)create a tuple like(1,2,3,4,3,2) and print (2,3,4) only

##a=(1,2,3,4,3,2)
##print(a[1:4])

##10)create tuple like(1,2,3,4,3,2) and remove 3 in this tuple

##a=(1,2,3,4,3,2)
##b=list(a)
####print(b)
##b.remove(3)
##a=tuple(b)
##print(a)
##
#### OR
##
##for i in range(b.count(3)):
##    b.remove(3)
##print(tuple(b))
##    
##
###by list comprehension
##
##c=tuple(i for i in a if i!=3)
##print(c)

##11)create a list like[1,2,3,4] and change the elements like[1,2,4,3] without using list methods

##a=[1,2,3,4]
##a[2],a[3]=a[3],a[2]
##print(a)

##12)create a list like[1,2,3,4] and delete all the elements in list and print empty list without using any method

##a=[1,2,3,4]
##a=[]
##print(a)

##13)create single value tuple

##a=('apple',)
##print(type(a))
##print(len(a))

##14)create empty set

##a=set()
##print(a)
##print(type(a))

##15)create a dictionery like {"a":10,"b":20} and print the value of "a" without using methods

##x={"a":10,"b":20}
##print(x['a'])
####    or
##
##print(x.get('a'))

##16)create a dictionery like {"a":10,"b":20} and change the value of "b" is 30 and print it without using methods

##a={"a":10,"b":20}
##a['b']=30
##print(a)

##17)create a dictionery like {"a":10,"b":20} and insert the key value pair which the key is "c" and the value is 30 and print it

##a={"a":10,"b":20}
##a['c']=30
##print(a)

##18)create two sets like {1,2,3,4} and {3,4,5,6} and find the union without using union method

##a={1,2,3,4}
##b={3,4,5,6}
##c=set()
##
##for i in a:
##    c.add(i)
##for i in b:
##    c.add(i)
##print(c)
##
####    or we can used | operator
##
##d=a|b
##print(d)
##
#### OR
##
##x=list(a) + list(b)
##print(set(x))

##19) create two sets like {1,2,3,4} and {3,4,5,6} and find the intersection without using intersection method

##a={1,2,3,4}
##b={3,4,5,6}
##c=set()
##
##for i in a:
##    for j in b:
##        if i==j:
##            c.add(i)
##print(c)
##
##
####     or  we cam used & operator
##
##d=a&b
##print(d)
##
#### OR
##
##for i in a :
##    if i in b:
##        c.add(i)
##print(c)

##20)create two sets like {1,2,3,4} and {3,4,5,6} and find there difference without using difference method

##a={1,2,3,4}
##b={3,4,5,6}
##c=set()
##for i in a :
##    if i not in b:
##        c.add(i)
##print(c)
##
####   or we can used - operator
##
##d=a-b
##print(d)



##21)create a set like {1,2,3,4} and remove 3

##a={1,2,3,4}
##
##a.remove(3)
##print(a)
##
####  or
##
##b=set()
##for i in a:
##    if i!=3:
##        b.add(i)
##print(b)

##22)create a set like {1,2,3,4} and remove 3 using discard method and undrstand what's the difference between remove and pop

##a={1,2,3,4}
##a.pop(0)
##print(a)

##23)create a string like "hello world" and count "o"

##a="hello world"
##b=a.count("o")
##print(b)

##24)create a string like "hello world" and find "z" or index "z" and understand difference between index and count

##a="hello world"
####print(a.index('z'))
##index_z=a.find('z')
##print(index_z)  #The index() function in Python searches lists. We pass it a value, and it returns the
                #index where that value is found. If no value is found, it returns -1. With count, we
                #count the matching elements in a list.




##25)create a list like ["p","y","t","h","o","n"] and print "python"

##a=["p","y","t","h","o","n"]
##print("".join(a))
##
####OR
##
##s=""
##for i in a:
##    s+=str(i)
##print(s)

##26)create a string "python" and print ["p","y","t","h","o","n"]

##a="python"
##b=list(a)
##print(b)
##
####    or
##x=[]
##
##for i in a:
##    x.append(i)
##print(x)
##
#### OR
##
##c=[i for i in a]
##print(c)

##27)create a string like"     python" and print "python"

##a="     python"
##print(a.strip())

##28)create a list [1,2,3,4] and print it like [1,2,3,4,5]

##a=[1,2,3,4]
##a.append(5)
##print(a)
##
####or
##b=a+[5]
##print(b)

##29)create a list [1,2,3,4] and print [1,2,3,4,1,2,3,4] using extend function

##a=[1,2,3,4]
##print(a*2)
##a.extend(a)
##print(a)


##30)create a list [1,2,3,4] and print [1,2,3,4,"p","y","t","h","o","n"] using extend function

##a=[1,2,3,4]
##b=['p','t','h','o','n']
##a.extend(b)
##print(a)
##
####or
##
##a.extend(['p','t','h','o','n'])
##print(a)

##31)create a list [1,2,3,4] and remove 2 using pop function

##a=[1,2,3,4]
##a.pop(1)
##print(a)

##    or

##for i in a:
##    if i==2:
##        pop(i)
##print(a)

##32)create a list [1,2,3,4] and print [1,5,3,4] using insert function

##a=[1,2,3,4]
##a.pop(1)
##a.insert(1,5)
##print(a)

##33)create a list [1,2,3,4] and print [1,5,3,4] using negative indexing in insert function

##a=[1,2,3,4]
##a.insert(-3,5)
##print(a)
##a.pop(-3)
##print(a)

##34)create a list [1,2,3,4] and print [4,3,2,1]

##a=[1,2,3,4]
##a.sort(reverse=True)
##print(a)
##
####or
##print(a[::-1])
##
####or
##a.reverse()
##print(a)




##35)create a list [1,4,3,2] and print [1,2,3,4] using function

##a=[1,4,3,2]
##a.sort()
##print(a)

##36)create a dict {"a":10,"b":12,"c":14} and clear it{}

##a={"a":10,"b":12,"c":14}
##a.clear()
##print(a)

##37)create a empty set{}

##a=set()
##print(a)

##38)create empty dict{}

##a={}
##print(a)
##print(type(a))

##39)create a dict{"a":10,"b":20,"c":30} and print {"b":20,"c":30}

##a={"a":10,"b":20,"c":30}
##a.pop('a')
##print(a)
 
##40)create a set {1,2,3,4} and remove 2

##a={1,2,3,4}
##a.remove(2)
##print(a)


#-------------------------------------------moderate question-------------------------------------------------------------

##1)create a string "hello" and print >> ll:2 times without using count method

##a='hello'
##print(((a[2:4])+' ')*2)
####or
##for i in a:
##    if i=='l':
##        print(i*2,end="")
##        print(" ",end="")


##2)create a string "hello" and sort it

##a='hello'
##b=list(a)
##b.sort()
##print(b)
##print("".join(b))

##3)Take input string from user and find vowels

##a=input("Enter your string : ")
##b=list(a)
##c=[]
##print(b)
##for i in a:
##    if i in 'aeiou':
##        c.append(i)
##print("".join(c))

##4) create a list [(1,2),{"A":10},"abc",[1,2,3,4]] and find the data type of each element

##a=[(1,2),{"A":10},"abc",[1,2,3,4]]
##
##for i in a:
##    print(type(i))

##5) print A to Z in sequence like A B C D E........XYZ.

##a=65
##for i in range(65,a+26):
##    print(chr(i),end="")
##print()
##
####or
##
##for i in range (ord('A'),ord('Z')+1):
##                print(chr(i),end="")

##6)print ten time "hii"

##a='hii'
##for i in range(1,11):
##    print(a,i)
##
####or
##
##print((a+' ')*10)

##7)print right angle triangle using while loop

##i=1
##while i<=5:
##    j=1
##    while j<=i:
##        print("*",end="")
##        j=j+1
##    print()
##    i=i+1

##8)print right angle triangle using for loop

##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end="")
##    print()

##9)take input from user and check its even or odd

##n=int(input("Enter the number "))
##if n%2==0:
##    print("the number is even")
##else:
##    print("the number is odd")

##10)take input from user and check the number is divisible by 5 or not

##n=int(input("Enter the number "))
##if n%5==0:
##    print("the number is divisible by 5")
##else:
##    print("The numbre is not divisible by 5")

##11)write a programme to check whether a person is eligible for voting or not(accept age from user)

##age=int(input("Enter your age "))
##
##if age >=18:
##    print("You can vote in election ")
##else:
##    print(f"sorry,you cant vote try after {18-age} years")

##12)print 1 to 10 using for loop

##for i in range(1,11):
##    print(i)

##13)write a programme to check whether a number is divisible by 7 or not

##n=int(input("Enter the number "))
##if n%7==0:
##    print("the number is divisible by 7")
##else:
##    print("The numbre is not divisible by 7")

##14)wap to display "hello" if number enterned by user is even , otherwise print "bye"

##n=int(input("Enter number"))
##
##if n%2==0:
##    print("hello")
##else:
##    print("bye")

##15)take input from user and check its data type

##n=input("Enter anything")
##print(type(n))

##16)create set like {1,2,3,4,5} and update it {1,2,3,4,5,6,7,8,9}

##a={1,2,3,4,5}
##a.update([6,7,8,9])
##print(a)

##17)create a set like {1,2,3,4,5} and add the element like {1,2,3,4,5,6,7,8,9}

##a={1,2,3,4,5}
##a|={6,7,8,9}
##print(a)

##18)take string from user like "python" and print ["p","y","t","h","o","n"]

##a='python'
##b=list(a)
##print(b)

##19)take input from user in int data type without using int() function

##def integer_value(a):
##    n=0
##    for char in a:
##        n=n*10+(ord(char)-ord('0'))  #n=2  54-48
##    return n
##
##user=input("Enter the number ")
##print(ord('0'))
##result=integer_value(user)
##print(f"The integer value is : {result}")
##print(type(result))

####or

##user=eval(input("Enter the number "))
##print("Type of user is :",type(user))



##20)create a string like " 7 apple 8 mango 9 banana" and print the int values only which dynamic state

##a="7 apple 8 mango 9 banana"
##b=[c for c in a.split() if c.isdigit()]
##print(b)
##
####or
##
##for i in a:
##    if i.isdigit():
##        print(i,end="")



##21)take input from user like 1234 and print the every second element 0 eg,1020
                                 # 2 4 6 8
##user=(input("Enter the value"))  #123456789
##for i,k in enumerate(user):                   #012345678
##    if user.index(i)%2!=0:
##        print(i,end="")
##        print(0,end="")

##22)take gmail from user like "abc@gmail.com" and print its name only "abc"

##user=input('Enter your gmail id ')
##
##a=user.index('@')
##name=user[:a]
##print(name)
##
####or
##
##a=user.split('@')
##print(a[0])

##23) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
##    Unit                          Price  
##  First 100 units                 no charge
##  Next 100 units                 Rs 5 per unit
##  After 200 units                Rs 10 per unit
##  (For example if input unit is 350 than total bill amount is Rs2000)

##units=int(input("Enter the units consumed by you"))
##
##if units <=100:
##    print("no charge , electricity is free till 100 units")
##elif units>100 and units <=200: 
##    print(f"your bill is 5 Rs per unit total bill is: {((units-100)*5)}")
##else:
##    print(f"your bill is 10 RS per unit total bill is : {(100*5)+(units-200)*10}")

##24) Write a program to check whether the last digit of a number
##   (entered by user ) is divisible by 3 or not.

##user=input("Enter the number")  
##
##for i in user:
##    if user.index(i)==len(user)-1:   # for 0th position value 1  index value is 0
##        if int(i)%3==0:              #for 1st position value 2 index value 1
##            print("yes")          # for 2nd position value 1 index value will give first occurance of number that is 0
##        else:                     #for 3rd position value 2 index value will give first occurance of number that is 1
##            print("no")           #in this code if user entered last digit value is repeted  in that case else part will not execute
            
##25) Write a program to determine whether a number (accepted from the user) 
##   is divisible by 2 and 3 both.

##user=int(input("Enter the value "))
##
##if user%2==0 and user%3==0:
##    print("value is divisible by 2 and 3 ")
##else:
##    print("value if not divisible by 2 and 3 both")

##26)Accept the age of 4 people and display the youngest one?

##a=int(input("enter age of first person"))
##b=int(input("enter age of second person"))
##c=int(input("enter age of third person"))
##d=int(input("enter age of fourth person"))
##
##youngest=min(a,b,c,d)
##print("youngest of all of them is :",youngest)
##
####       or
##
##young=a
##
##if b<a:
##    young=b
##if c<a:
##    young=c
##if d<a:
##    young=d
##
##print(f"The youngest one is {young} ")

##27) Accept the age of 4 people and display the oldest one?

##a=int(input("enter age of first person"))
##b=int(input("enter age of second person"))
##c=int(input("enter age of third person"))
##d=int(input("enter age of fourth person"))
##
##oldest=max(a,b,c,d)
##print("oldest of all of them is :",oldest)
##
####       or
##
##old=a
##
##if b>a:
##    old=b
##if c>a:
##    old=c
##if d>a:
##    old=d
##
##print(f"The oldest one is {old} ")


##28) Write a program to check whether an years is leap year or not

##year=int(input("Enter the year"))
##
##if year%4==0:
##    print("This year is a leap year")
##else:
##    print("This year is not a leap year")

##29) Write a program to check whether an years is leap year or not without using (or) keyword


##31)Write a program to check whether a number entered is three digit number or not.

##user=int(input("Enter the number "))
##a=str(user)
##if len(a)==3:
##    print("Entered number is 3 digit")
##else:
##    print("Entered number is not 3 digits")

##32) Write a program to check whether a person is senior citizen or not.

##age=int(input("Enter the age"))
##if age>=65:
##    print("you are senior citizen")
##else:
##    print("you are not senior citizen")

##33)wap which will add(sum) all the elements of list

##a=[201,56,39,12,56,48]
##def sum(x):
##    s=0
##    for i in x:
##        s=s+i
##    return s
##print("The sum of all list element is ",sum(a))
##
####                 or
##
##b=sum(a)
##print(b)

##34)wap to print maximum number without using max function

##a=[20,90,14,89,45,45,23]
##
##for i in range(0,len(a)):
##    for j in range (i+1,len(a)):
##        if a[i]>=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)
##print("maximum element is ",a[-1])

##35)wap to print minmum number without using min function 

##a=[25,65,78,23,10,2,1,56]
##
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]<=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)
##print("Minimum element is :",a[-1])
       
##36)wpa to square all the all elements of list note[1,5,3,9],>>[1,25,9,81]

##a=[1,5,3,9]
##sqrt=[]
##
##for i in a:
##    a=i*i
##    sqrt.append(a)
##print(sqrt)

##37)wpa to print all the elements in list which are divisible by 3

##a=[18,50,12,30,75,77]
##b=[]
##for i in a:
##    if i%3==0:
##        b.append(i)
##print(b)

##38)wpa to print all the elements which are greater then 100"""

##a=[12,10002,1523,85,2323,1001,45,23]
##b=[]
##
##for i in a:
##    if i >1000:
##        b.append(i)
##print(b)

##39)"""wap to find the total length of all string element in a list eg ["py","thon"],>>[2,4]

##a=["py","thon"]
##count=[]
##for i in a:
##    count.append(len(i))
##print(count)

##40)wap to print all elements in dict

##a={"name":"krushna","age":23,"city":"Ambernath"}
##print(a.items())

##----------------------------------------High level Question----------------------------------------------------------------

##1)take a list and sort it without using sort function

##a=[6,4,1,3,2,5]
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]>=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)

##2)tak a list and sort it in decending order without using sort function

##a=[6,4,1,3,2,5]
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]<=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)

##3)take a list and find the highest element without using max function

##a=[6,4,1,3,2,5]
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]>=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)
##print("Higest number in list is :",a[-1])

##4)take a list and find the second highest element

##a=[6,4,1,3,2,5]
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]>=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)
##print("second Higest number in list is :",a[-2])

##5)take a list and find the lowest element with using min function function

##a=[6,4,1,3,2,5]
##for i in range(0,len(a)):
##    for j in range(i+1,len(a)):
##        if a[i]<=a[j]:
##            a[i],a[j]=a[j],a[i]
##print(a)
##print("Lowest number in list is :",a[-1])

##6)take a dictionary and print the highest key value pair
                                 
##m = {'s1': 54, 's2': 78, 's3': 167, 's4': 97}
##k=list(m.keys())
##v=list(m.values())
##print(k)
##print('key :',k[v.index(max(v))],'value',max(v))

##7)take a dictionary and print the lowest key value pair

##m = {'s1': 54, 's2': 78, 's3': 167, 's4': 97}
##k=list(m.keys())
##v=list(m.values())
##print(k)
##print('key :',k[v.index(min(v))],'value',min(v))

##8)create a list like [1,2,3,4] and print the elements without using loop

a=[1,2,3,4]
print(*a)






    


        





     
    
    





        
        
    
    
        
    
    
        
    








  



    
    


        
        
    
        

        


































    





        










    











