##OOP-Object oriented programming

## Class is a blueprint that defines some properties and behaviors. An
## object is an instance of a class that has those properties and
## behaviours attached. A class is not allocated memory when it is defined.
## An object is allocated memory when it is created. Class is a logical
## entity whereas objects are physical entities.3 Apr 2024

##class student:
##    name='krushna'
##    age=23
##    email='kru@gmsil.com'
##
##    def demo(s):
##        name='krushna';
##        print(name)
##
##k=student()
##k.demo()
##
##
##class student:
##    name='krushna'
##    age=23
##    email='kru@gmsil.com'
##
##    def demo(s,a,c):  #s is self a default parameter that represents instance of class
##        name='krushna';
##        print('i am',a)
##        print("My mail is ",a,c)
##
##k=student()
####k.demo(k.age)
##k.demo(k.email,k.age)


##class A :
##    def demo(self,depart):
##        print(depart)
##        print(self)
##        name='krushna'
##        age=23
##        roll_no=45
##        print(name,age,roll_no)
##
##    def display(self):
##        email='kru45@gmail.com'
##        add='thane'
##        print(email,add)
##a=A()
####a.demo('mech')
##print(a)
##
####a.display()
##A.demo('k')
####a.demo('mech')


##class student:
##    def show(self,name,roll_no):
##        print('my name is ',name)
##        print('roll_no is ',roll_no)
##        print("I am a python developer")
##
##    def display(self):
##        print('Java Devloper')
##
##s=student()
##s.show('krushna',122)
##s.display()


##scope of static variable

##class student:
##    name='krushna'     #static variable-> name and email
##    email='kru45@gmai.com'
##    def show(self):
####        print(name) #will not print 
##        print(self.name,self.email)
##        print("python devloper")
##    def display(self):
##        print(self.name)
##        print("java developer")
##
##a=student()
##a.show()
##
##a.display()

#local variable = present inside the method
#scoope = scope is inside method only

##class A :
##    def show(self,roll_no,dept_name):
##        print(roll_no,dept_name)
##        name='krushna'
##        age=23
##        print(name,age)
##
##    def display(self):
##        email='kru@gmail.com'
##        branch='EEE'
####        print(name)     #cant access in this method coz its belongs to show method
##        print(email,branch)
##
##a=A()
##a.show(123,'Electrical')
##a.display()

##instance variable= this varibale declared with self keyword and scope of this varible in all method

##class A :
##    def show (self,name,age,salary):
##        self.name1=name
##        self.age1=age
##        self.salary1=salary
##        print(self.name1,self.age1,self.salary1)
##    def display(self):
##        print(self.name1,self.age1,self.salary1)
##a=A()
##a.show('krushna',23,101010)
##a.display()


### taking self with another name 
##class A :
##    def show (kru,name,age,salary):
##        kru.name1=name
##        kru.age1=age
##        kru.salary1=salary
##        print(kru.name1,kru.age1,kru.salary1)
##    def display(self):
##        print(self.name1,self.age1,self.salary1)
##a=A()
##a.show('krushna',23,101010)
##a.display()

##class person:
##    name = 'kru'
##    age=29
##    add='thane'
##    def detail(self):
##        print(name)
##a=person()
##a.detail()

##class A:
##    def show(self,name,address):
##        self.name1=name
##        print('python dev')
##    def display(self):
##        self.show('kru','amb') #can called method inside method
##        a.show('krush','bad')
##        print("java dev")
##        print(self.name1)
##a=A()
##a.show('kJ','kal') 
##a.display()

class A:
    a=10
    b=20
    def demo(s):
        s.a=s.a+1 # this will not affect at og variable 
        A.b=A.b+1 # when we modify static variable using class name its afftet og varibale
        print(s.a,A.b)
x=A()
x.demo()  #11 21

y=A()
y.demo()  #11 22

z=A()
z.demo()   #11 23


        
    


        











             
