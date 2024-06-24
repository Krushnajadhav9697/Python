##print ur name 10 time without using loop and manually

##import sys
##sys.setrecursionlimit(1)
##def name():
##    print('krushna')
##    name()
##name()

####    or

##def name(c):
##    if c==0:
##        return
##    print('krushhh')
##    count(c-1)
##name(10)
    
##wap for factorial using recursion

##fact=1
##def factorial(c):
##    if c==0:
##        return 
##    global fact
##    fact=fact*c
##    factorial(c-1)
##factorial(6)
##print(fact)

##find power of number using recursion

##def power(n,expo):
##    if expo==0:
##        return 1
##    return n * power(n,expo-1)
##    
##result = power(2,4)
##print(result)

##find prime number using recursion

##def prime(n,b):
##    if n==0:
##        prine("0 is neither prime nor composite number ")
##    if n==1:
##        prine("1 is not prime number ")
##    if n%b==0:
##        return false
##
##    return prime(n,b-1)
##    
##    
##    
##a=int(input("enter number"))
##if prime(a,a-1):
##    print("number is prime")
##else:
##    print("number is not prime")

##wap of counting number of digit in givenn number  ie1212=4

##nos=0
##def count(b):
##    c=str(b)
##    print('number is :',c)
##    for i in range (len(c)):
##        global nos
##        nos=nos+1
##    
##        
##a=int(input("enter number"))
##count(a)
##print('no of digit in number is :',nos)

##wap for printing n to 1 seqence

##def seq(a):
##    if a==0:
##        return
##    print(a)
##    seq(a-1)
##    
##x=int(input("Enter the number "))
##seq(x)

##sum of 1st n number using recursion

def sum(a):
    global c
    c=a+sum(a-1)
    return c
    
    
    


c=0   
sum(2)    
    

x=int(input("Enter the number "))
sum(x)




















    

    
