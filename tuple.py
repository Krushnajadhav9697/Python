#tuple

a=(1,2,3,"abc","xyz")
print(a)
print(type(a))
print(len(a))
print(a[-1])

b=(1,2)
print(type(a+b))   # adding 2 tuple
s=(1)   # adding single value in tuple  wrong way
print(type(s))  # o/p -> int
p=(1,)    #if we want to add single value in tuple need to give coma ',' after value 
print(type(p))  #o/p -> tuple

#unpacking of tuple

data=('krushna',23,'ambernath',45,48,15,15)
(name,age,city,*x)=data
print(name)
print(x)

#tuple slicing
a=('krushna','ramrao','jadhav',45,78,15)
print(a[:3])

#tuple method

#1.count

a=(1,2,3,4,5,5,5)
print(a.count(5))

#2.index
b=(1,2,3,4,5,5,5)
print(b.index(1))

