n=int(input("enter the number: "))
temp=n
rev=0

while temp!=0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if(rev==n):
    print(f"{n} palindrome number")
else:
    print(f"{n} not a palindrome number")
