#variation in user defined function

#1.Function with no argumrnt no return value

def add():
    a=20
    b=20
    print(f"addition of {a} and {b} is", a+b)
add()


#2.Function with argumrnt no return value

def add(x,y):
    print(f"addition of {x} and {y} is", x+y)
a=10
b=20
add(a,b)


#3.Function with no argumrnt but return value

def add():
    a=100
    b=10
    return f"addition of {a} and {b} is ",a+b
sum=add()
print(sum)


#4.Function with argumrnt and return value

def add(a,b):
    return f'addition of {a} and {b} is',a+b
x=12
y=10
print(add(x,y))


