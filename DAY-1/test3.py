n=int(input("enter the number: "))
print("factors are:")

i=1
# for i in range (i,n+1):
#     if(n%i==0):
#         print(i,end=" ")
        

while(i<=n):
    if(n%i==0):
        print(i,end=" ")
    i=i+1
