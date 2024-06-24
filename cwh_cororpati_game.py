import random
Question=['What is 1+1','What is 2*9','What comes after 5','Who is PM of india','Capital of India','Birth place of Chatrapati Shivaji Maharaj','The mother of Chatrtapati Shivaji Maharaj jijbai bhosle also known as','First PM of independent India','who was the killer of Mahatma Gandhi','How many side triangle have','Area of circle']
Answer=['2','18','6','narendra modi','delhi','shivnery fort','swarajya janani','jawaharlal nehru','nathuram godse','3','pi*r*r']
rs=[0,100,200,400,800,1600,3200,6400,12800,25600,51200,102400]
seq_Q=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','kru']
x=0
correct_ans=0
while True:
    print("Welcome to KBC")
    a=input("To proceed type 'next' or 'quit' :")
    if a=='next':
        print('''Rules to play game
        1.Answer the Qustion correctly
        2.One wrong ans and u lose the game
        3.prise money will double for every question''')
    elif a=='quit':
        print("Khelke to dekh bhidu ")
        break
    else:
        break

    while True:
        if len(Question)==0:
                print("Congratulation you Won The game ")
                print(f"You won {rs[correct_ans]} Rs")
        b=input(f"Ready for the {seq_Q[x] } Question yes/no :")
        if b=='yes':    
            first_Q=random.choice(Question)
            Question.remove(first_Q)
            print(first_Q)
            ans=input("Enter your Answer :")
            w=ans
            y=w.lower()
            if ans.lower() in Answer:
                Answer.remove(y)
                print("Correct answer ")
                correct_ans=correct_ans+1
                x=x+1
                print(correct_ans)
            elif ans not in Answer:
                print("Wrong Answer ")
                print(f"You won {rs[correct_ans]} Rs")
                print("thank U for playing,you can start again")
                break
            
        

        elif b=='no':
            print(f"ok, You won {rs[correct_ans]} Rs")
            break

   
        
    

    
    
