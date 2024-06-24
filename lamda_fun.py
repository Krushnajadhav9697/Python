#lambda function:- a function without name is lambda function its also known as anonymous function (take single expression )

#lambda function always start with lamda keyword

#syntax

#lamda arg_list : expression

##a=lambda x : print(x)
##a(4)

##a= lambda x: print(x**2)
##a(4)

##a=lambda x: x**2  #lambda funtion have default return coz its take single expresion
##print(a(3))

##add=lambda x,y: print(x+y)
##add(3,4)

##result = lambda x,y :(x+y,x-y)
##print(result(3,4))

##result=lambda x,y:(x+y,x-y) 
##
##add,sub=result(5,3)
##print(add)
##print(sub)

##default argument

##add=lambda x,y=5:x+y
##print(add(3))

##keywowrd argument

add = lambda a=5,b=3:a+b
print(add())


