##recursion :when a function call itself then that function is called as recursive function and the process is called as recursion
#advantage :
#1.clean code /less number of code
#2.complex problem can be solved

#disadvantage :
#1.hard to debug
#2.not memory efficient


##def demo():
##    print('krushna')  # it will go infinite 
##    demo()
##demo()


import sys
##print(sys.getrecursionlimit())

##sys.setrecursionlimit(100)
##print(sys.getrecursionlimit()) 

##i=0
##def demo():
##    global i
##    i=i+1
##    print('krushna',i)  
##    demo()
##demo()

#WAP for fibbonacci series using recursion

##fibo(1)=0
##fibo(2)=1
##fibo(3)=fibo(1)+fibo(2)
##fibo(3)=fibo(3-2)+fibo(3-1)
##fibo(n)=fibo(n-2)+fibo(n-1)

##def fibo(n):
##    if n==1:
##        return 0
##    if n==2:
##        return 1
##    return fibo(n-2)+fibo(n-1)
##n=int(input("Enter the number of turm"))
##print(fibo(n))

##task
##print ur name 10 time without using loop and manually
##wap for factorial using recursion
##find power of number
##find prime number using recursion
##wap of ciunting number of digit in givenn number  ie1212=4
##sum of 1st n number using recursion
##wap for printing n to 1 seqence
##

#package = its a collection of module






