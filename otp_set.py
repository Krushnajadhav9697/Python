otp={'0','1','2','3','4','5','6','7','8','9'}
print(otp)
n=0
for i in otp:
    if n<4:
        print(i,end="")
        n+=1

#OR

print() 

c=""
for i in otp:
    c=c+i
print(c[:4])
