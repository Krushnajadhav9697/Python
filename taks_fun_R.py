#taks on funtion and variable(local and global variable  )
#1
B=30
def display(x):
    global a
    a=a+x
    return a
a=20
b=5
display(b)
print(a)

#2

a=10
y=5
def myfun():
    a=2
    y=a
    print(y,a)
myfun()
print(y,a)

#4
a=10
y=5
def myfun():
    global a
    y=a
    a=2
    print(y,a)
myfun()
print(y,a)

#5
a=10
y=5
def myfun():
    global a
    a=2
    y=a
    print(y,a)
myfun()
print(y,a)

#6
a=1
def display():
    return a
print(a)
print(display())
print(a)


#3
a=10
y=5
def myfun():
    y=a
    a=2
    print(y,a)
myfun()
print(y,a)
