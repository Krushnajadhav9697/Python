#random

import random
#print name randomly form list 
name=['abc','krushna','ramrao','jadhav','kishsn','pritii']
print(random.choice(name))
print(random.sample(name,k=3))
print(name)
random.shuffle(name) # shuffle the list
print(name)

pin=[1,2,6,4,5,3,7,8,9,0]

print(random.randint(1,10)) # give random value form 1 to 9
print("".join(random.sample('1234567890',k=4)))
for i in range(1,5,1):
    print(random.choice(pin),end="")


##cororpati game 
##import random
##Question=['What is 1+1','What is 2*9','What comes after 5','what is 3+4']
##Answer=['2','18','6','7']
##rs=[0,100,200,400,800]
##seq_Q=['first','second','third','fourth']
##x=0
##correct_ans=0
##while True:
##    print("Welcome to KBC")
##    a=input("To proceed type 'next' or 'quit' :")
##    if a=='next':
##        print('''Rules to play game
##        1.Answer the Qustion correctly
##        2.One wrong ans and u lose the game
##        3.prise money will double for every question''')
##    elif a=='quit':
##        print("Khelke to dekh bhidu ")
##        break
##    else:
##        break
##
##    while True:
##        if len(Question)==0:
##                print("Congratulation you Won The game ")
##                print(f"You won {rs[correct_ans]} Rs")
##        b=input(f"Ready for the {seq_Q[x] } Question yes/no :")
##        if b=='yes':    
##            first_Q=random.choice(Question)
##            Question.remove(first_Q)
##            print(first_Q)
##            ans=input("Enter your Answer :")
##            w=ans
##            y=w.lower()
##            if ans.lower() in Answer:
##                Answer.remove(y)
##                print("Correct answer ")
##                correct_ans=correct_ans+1
##                x=x+1
##                print(correct_ans)
##            elif ans not in Answer:
##                print("Wrong Answer ")
##                print(f"You won {rs[correct_ans]} Rs")
##                print("thank U for playing,you can start again")
##                break
##            
##        
##
##        elif b=='no':
##            print(f"ok, You won {rs[correct_ans]} Rs")
##            break

   
        
    

    
    

