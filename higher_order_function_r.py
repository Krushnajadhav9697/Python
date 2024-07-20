#higher order function:
# a function which takes another functoin is called as higher order function

#built-in Higher order function
#1.Filter function
#2.map function
#3.reduce  function

#1.filter Function:
#   filter function filter out element of iterable
#   filter function return filter object

#syntax:

# filter (function_name,iterable)
#1.function name= function that test every element of iterable
#2.iterable:sequence which need to be filtered

##num=[11,22,33,44,55,66]
##
##def even(x):
##    if x%2==0:
##        return True
##
##filter_obj=filter(even,num)  # can stored in list directly like  list(filter(even,num))
##print(filter_obj)
##print(list(filter_obj))

n=[5,2,13,9,15,19,23,40,47,45,97]
def prime(a):
    for i in range (2,a,1):
        if a%i==0:
            return False
##            break
    else :
        return True
            
    

filter_obj = list(filter(prime,n))
print(filter_obj)


#2.map function: its also built in higher order function. It apply specific function on each element of iterable
##and perhaps change element

##n=[1,2,3,4,5,6]
##
##def square(a):
##    return a*a
##x=list(map(square,n))
##print(x)

##n=[1,2,3,4,5,6]
##
##def factorial(a):
##    
##    for i in range (1,a):
##         a=a*i
##    return a
##
##x=list(map(factorial,n))
##print(x)

 

 
