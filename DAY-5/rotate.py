a=[1,2,3,4,5]
# ord=str(input("enter the order:"))
# l=int(input())

def rotate_left(a):
    temp=a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=temp
    return a
def rotate_right(a):
    temp=a[0]
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[len(a)-1]=temp
    return a
def rotate(ord,t,a):
    while t>0:
        if ord=='l':
            rotate_left(a)

        if ord=='r':
            rotate_right(a)
        t=t-1
    return a 
ord=str(input("Ente the order of the rotation(r/l):"))
t=int(input('Enter the times array should rotate:'))
print(rotate(ord,t,a))