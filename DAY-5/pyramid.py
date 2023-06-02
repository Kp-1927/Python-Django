# def pyramid(x):
#     k=0
#     for i in range(1,x+1):
#         for j in range(1,(x-i)+1):
#             print(end=" ")
#         while(k!=(2*i-1)):
#             print("*",end="")
#             k=k+1
#         k=0
#         print()
# pyramid(5)

def prog1(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            
            print("* ",end="")
        print("\n")
prog1(5)