##Polymorphism :- Polymorphism means many form
##an entity can work in multiple role this capability is called polymorphism
##Types :- 1)Function overriding 2) Function Overloading

##1) In function overriding we can declare a function in base class  and derived class with same name and  same  parameter
##it occures when one class is inherit from another class

##class A:
##    def display(self):
##        print('python developer ')
##class B(A):
##    def display(self):
##        print('java developer ')
##object = B()
##object.display()   #this is overriding #to called the display of A class we need to create object for class A

##2) more then one function with same name difines in same class and call with different parameter
##this process is known as method overloading
##But python does not support method overloading

##class A:
##    def show(self):
##        print('hiiiii')
##    def show(self,x):
##        print('bye')              # this is not supported
##    def show(self,x,y):
##        print('Hello')
##a=A()
##a.show()
##a.show(10)         
##a.show(10,30)

# have alternate method to achive this 

##class A:
##    def overloding(self,a=None,b=None,c=None):
##        if a!=None and b!=None and c!=None :
##            print(a+b+c)
##        elif a!=None and b!=None:
##            print(a+b)
##        else :
##            print(a)
##x=A()
##x.overloding(10)
##x.overloding(10,20)
##x.overloding(10,20,30)


class A:
    def show(self):
        self.name= 'krukshna'
        print(self.name)
a=A()
print()
a.show()


        





