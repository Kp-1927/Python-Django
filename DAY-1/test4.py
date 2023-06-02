n=int(input("enter the num: "))
c=0
sum=0
num1=n
num2=n

while num1>0:
    num1=num1//10
    c=c+1
print(c)
while(num2>0):
    r=num2%10
    num2=num2//10
    sum=sum+r**c
if(sum==n):
    print("armstrong number")
else:
    print("not a armstrong number")