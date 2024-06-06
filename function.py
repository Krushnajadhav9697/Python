#normal function
def data():
    a=1+3
    print(a)

data()

#positioanal argument function

def data(name,age,city):
    return f"my name is {name} and age is {age} and i live in {city}"
print(data('krush',23,'amb'))

#keyword argument function

def data(name,age,city):
    return f"my name is {name} and age is {age} and i live in {city}"
print(data(age=23,city='amb',name='krush'))


    
