#super method  
class A :
    def __init__(self,name,age):
        print('python developer ')
        print(name,age)
    def show(self):
        print('hii')
class B(A):
    def __init__(self,name,age):
        super().__init__('raj',10)
        print('java developer')
        print(name,age)
    def display(self):
        print('hello')

b=B('rajesh',31)
