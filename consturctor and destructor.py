#constructors => __init__ method runs automatically when object is created which is used to initialize the instance object

##class A:
##    def __init__(s):
##        print("krush")
##        s.id=101
##        s.name='kru'
##        s.salary=25025
##
##    def display(s):
##        print('id is',s.id)
##        print('name is',s.name)
##        print('salary is ',s.salary)
##        
##a=A()    #consturctor runs automatically when object is created
##a.display()


class A:
    def __init__(s):
        s.id=int(input('enter the id '))
        s.name=input('enter the name ')
        s.salary=int(input('enter the salary '))
    def display(s):
        print(f'id is {s.id}, name is {s.name} and salary is {s.salary}')
a=A( )

a.display()



#__str__ method runs when object gets printed

##class A:
##    def __init__(s,name,age,salary):
##        s.name=name
##        s.age=age
##        s.salary=salary
##    def display(s):
##        print(s.name,s.age,s.salary)
##    def __str__(s):
##        return s.name + " " + str(s.age) +" " + str(s.salary)
##a=A('kru',23,151515)
##a.display()
##print(a)

##class A:
##    def display(s,name,age):
##        s.email='kru@gmail.com'
##        print(name,age,s.email)
##        print('python dev')
##
##    def show(s):
##        print(s.email)
##        s.display('KJ',22)
##        print('java dev')
##
##    def demo(k):
##        print(k.email)
##        print(a.email)
##
##a=A()
##a.display('kru',211)
##a.show()
##a.demo()

#destructor => is a member method of calss it delete the memory of object
#it can b called with object :-  __del__

#garbage collector:
#a progra, to delete reference
#it runs automatically
#it does mamory management

##class A:
##    def __init__(j):
##        j.name='KJ'
##        print('python debv')
##    def show(k):
##        print("java dev")
##    def __del__(k):
##        print("Object deleted ")
##a=A()
##a.show()
##del a
#####a.show()  # it will not execute coz objejct a deleted by destructor method





        
