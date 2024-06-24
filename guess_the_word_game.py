import random
words=['top','pot','anuj','anju','krushna','rushank','shalvi','vishal']
score=0
while True :
    for wr in range(3):
        letters = list(random.choice(words))
        print("guess the correct word by given word =>","".join(letters))
        user = input("Enter correct word or quit :")
        if user == 'quit':
            break
        if user != "".join(letters):
            valid =  True
            for letter in user:
                if letter in letters:
                    letters.remove(letter)
                else:
                    valid=False
                    break

            if valid and user in words:
                score= score+len(user)
                print(f"correct and your score is {score}")
            else:
                print("you have entered wrong word")
            if user !="".join(letters):
                break
        else:
            print("you enter the same name which we have provided....")
    else:
        score= score-len(user)
        print(f"we have reduce your score by {len(user)} points because you enter same word 3 time your total score is {score}")
print("Thank you for playing!")
            
            
