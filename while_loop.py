n=82081
sum=0
l=len(str(n))
n1=n
while n!=0:
    a=n%10
    sum=sum+a**l
    n=n//10
    
if n1==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")

