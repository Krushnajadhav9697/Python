##Exceptional handling as exception is an event which occurs during the execution of a program that interrupt the normal
##flow of the programs instructions
##
##the try block which is used to test a block of code for errors
##the except block used to handle the errors

##print('java dev')
##a=int(input("Enter the number "))
##b=int(input("Enter the number "))
##try:
##    print(a/b)
##except:
##    print('Error occured')  #this is user defined message
##print('python dev')
##print('django dev')

##we can get message from python also

##print('java dev')
##a=int(input("Enter the number "))
##b=int(input("Enter the number "))
##try:
##    print(a/b)
##except Exception as a:
##    print(a)    #system defined message   #Exception can handled all types of exceptions
##print('python dev')
##print('django dev')

##default exception must be last

##print('java dev')
##a=int(input("Enter the number "))
##b=int(input("Enter the number "))
##try:
##    print(a/b)
##    print('thene')
##    print(int('hwllo'))
##
##except ZeroDivisionError as a:
##    print(a)
##except Exception as a:
##    print(a)
##except:
##    print('Error occured')
##print('python dev')
##print('django dev')

##nested try except block

##k=[]
##try:
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##except:
##    print('outer execution handled')
##print('outer except didnot run meaning error donest occured in outer try except block')

##try...except.... else
##else part :-it will execute only when execution is not occured

##k=[]
##try:
##    print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##except:
##    print('outer execution handled')
##else :
##    print('it will execute only when execution is not occured in outer try ')


##finally keyword

##k=[]
##try:
##    print(k[2])
##    print('thane')
##    try:
##        print(9/0)
##    except Exception as e:
##        print(e)
##    print('mumbai')
##    try:
##        print(abc)
##    except Exception as e:
##        print(e)
##except:
##    print('outer execution handled')
##else :
##    print('it will execute only when execution is not occured')
##finally:
##    print('it always be executed ')

##user defined error


#15/7/2024

##print('thane')
##try:
##    raise invalidAgeError()
##except:
##    print('exception handled')
##print('mumbai')
##

##class invalidAgeError(Exception):
##    pass
##
##print('thane')
##try:
##    raise invalidAgeError()
##except invalidAgeError as e:
##    print('exception handled')
##print('mumbai')

##class invalidAgeError(Exception):
##    def __str__(self):
##        return 'invalid age error detected'
##
##print('thane')
##try:
##    raise invalidAgeError()
##except invalidAgeError as e:
##    print(e)
##print('mumbai')

class invalidAgeError(Exception):
    def __str__(self):
        return 'invalid age detected'

age = int(input("Enter the age : "))
if age>=18 :
    print("you can vote")
else :
    try:
        raise invalidAgeError()
    except invalidAgeError as e:
        print(e)









    









