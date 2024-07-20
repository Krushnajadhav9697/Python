##inheritance :- one class can inherit the propertoies and method of another class this process is known as inheritance

##class A:
##    a=10
##    def show(self):
##        print("python devloper ")
##class B(A):
##    b=20
##    def display(s):
##        print(s.b,s.a,A.a)
##        print("java developer ")
####a=A()
####a.show()
##c=B()
##c.display()

#types of inheritance :-



##2.Multilevel inheritance :- The multiple inheritance in which a class derived form another derived classis known as multilevel inheritance

##class A:
##    a=10
##    def show(s):
##        print("Grand parents class called ")
##class B(A):
##    b=20
##    def display(s):
##        print(C.a)
##        print("parents calss called ")
##class C(B):
##    c=30
##    def data(s):
##        print(s.a+s.b+s.c)
##        print("child method called ")
##x=C()
##x.data()
##x.show()
##x.display()


##3.hirarchical inheritance :-

##class A:
##    a=20
##    def A1(s):
##        print('java')
##class B(A):
##    b=20
##    def B1(s):
##        print('python')
##class C(A):
##    c=20
##    def C1(s):
##        print("C lan")
##
##x=C()
##x.A1()


##4.Multilevel inheritance

class A:
    a=10
    def show(s):
        print('show the number ')
class B:
    b=10
    def display(s):
        print('display the number ')
class C(A,B):
    c=10
    print()
    def data(s):
        print('hello!')
x=C()
x.data()
x.show()
