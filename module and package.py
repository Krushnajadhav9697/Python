#module and package
#module is a file containing python defination ,funtion and variable
#its a collection of function and classes
#types of modules :- 1.built-it module  2.user defined module
#before using built-in or user defined module in a python file we need to import that module in the python file

#syntax
#import module_name

#accessing a function inside module
#module_name.fun_name()

import math as m
print(m.sqrt(4))

print(m.factorial(5))
print(m.pow(2,3))
print(m.floor(15.2))   #round down the number
print(m.floor(-15.2))
##
print(m.ceil(15.6))    #round up the number
print(m.ceil(-15.6))
##
##import random as r
##
##print(r.random())  # -> given random value(float) between 0 to 1 [0,1)
##
##print(r.randrange(1,4)) # gives random value(int) form given range [1,4)
##
##print(r.randrange(2,8))
##print(r.randrange(20))
##
##print(r.randint(1,5)) # its include both value  and its  dont have step value
##
##print(r.uniform(2,5)) #return float value from given range 
##
##l=[1,2,3,4,5,'krushna']
##print(r.choice(l)) # given random value from list
##
##k=['karan','bb','katilsaya','3idiots']
##r.shuffle(k)  #shuffle the list 
##print(k)
##
##s='python_programming'
####print(s[-15:-16])
####print(s[2:3:-1])
##
## 
##    
