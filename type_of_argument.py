##Types of parameter/argument
##1.Positional argument
# during a function call,values passed through argument should be in the order of parameters in the function defination

def simple_intrest(p,r,t):
    print("principle is :",p)
    print("rate of intrest is :",r)
    print("time is :",t)
    si=(p*r*t)/100
    print(si)
p=5000
r=10
t=5
simple_intrest(p,r,t)



##2.default argument
#a default parameter is defined with a fallback value as a default
#argument. Such parameters are optional during a function call. If no
#argument is provided, the default value is used, and if an argument is
#provided, it will overwrite the default value.

def simple_intrest(p,r=12,t=6):
    print("principle is :",p)
    print("rate of intrest is :",r)
    print("time is :",t)
    si=(p*r*t)/100
    print(si)
p=5000
simple_intrest(p)

##if we pass the wrong argument in function they will take value from global 

def simple_intrest(p,r,t):
    print("principle is :",p)    # value of p taken from gobal same for r and t 
    print("rate of intrest is :",r)
    print("time is :",t)
    si=(p*r*t)/100
    print(si)
p=5000
r=10
t=5
##simple_intrest(x,y,z)

##3.keyword argument
#Keyword-only arguments mean whenever we pass the arguments(or value) by
#their parameter names at the time of calling the function in Python in
#...

def simple_intrest(r,t,p):   #order of parameter does not matter   
    print("principle is :",p)
    print("rate of intrest is :",r)
    print("time is :",t)
    si=(p*r*t)/100
    print(si)

simple_intrest(p=6000,r=6,t=10)

#scope :- scope is a part of program in which variable can be used
#1.local
#2.global
#1.local variable :-a variable can be declared inside the function is called as local function
#scope of local variable :-is inside the function only

def dis():
    a=10
    print(a)
##print(a)   # cant print a caz its a local variable in dis() function
dis()
#2.global Variable:- a variable can be declared outside the function is called as global variable
#scope of global variable :-is inside as wll as outside the function i.e throught out the program

A=10
def dis():
    a=15
    b=20
    print(a)
    print(A)
print(A)
dis()
print(A)


##takss
print("-----------------task-----------------------------")

A=20
def display():
    A=25
    print(A)  #25
print(A)#20
display()
print(A)#20

A=20
def display():
    global A
    A=25
    print(A)  
print(A)
display()
print(A)





##4.variable length argument
