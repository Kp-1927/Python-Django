"""
# Matrix Multiplication
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0,],[0,0,0],[0,0,0]]
def mat_mul(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            sum=0
            for k in range(len(b[i])):
                c[i][j]+=a[i][k]*b[k][j]
    print(c)

mat_mul(a,b)

# Sum of arrays or list
a=[[1,2,3],[4,5,6],[7,8,9]]
def sum_array(a,b):
    sum=0
    for i in range(int(len(a))):
        for j in range(int(len(a[i]))):
            sum=sum+a[i][j]
    print(sum)
sum_array(a,b)

# Sum of 2-D array
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
def sum_2d(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j]+b[i][j],end=" ")
sum_2d(a,b)

# Sum of Diagonals
a=[[1,2,3],[4,5,6],[7,8,9]]
def sum_diagonals(a):
    sum=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(i==j or i+j==len(a)-1):
                sum=sum+a[i][j]
    print(sum)
sum_diagonals(a)

# Transpose of a matrix
a=[[1,2,3],[4,5,6],[7,8,9]]
def transpose(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[j][i],end="\t")
        print()
transpose(a)

"""
"""----------------------------------------------------------------------"""
"""BUILT IN FUNCTIONS"""
# List
"""
a=[1,2,3]
a.append(4)
print(a)

b=a.copy()
print(b)

print(a.count(5))

d=[5,6,7,8]
a.extend(d)
print(a)

print(a.index(3))

a.insert(9,2)
print(a)

a.pop(2)
print(a)

a.remove(1)
print(a)

a.reverse()
print(a)

e=[8,4,6,5,9,3,1,7,2]
e.sort()
print(e)

a.clear()
print(a)

"""
# String
"""
a="My Name is Shouvik Maharana"
b="                 djsohfoewsk           "
print(a.isupper())

print(a.islower())

print(a.isdigit())

print(a.isnumeric())

print(a.replace("Shouvik","Shuvik"))


print(a.split("is"))

print(b.strip())

"""
# Own Count Function
"""
a=[1,2,5,3,4,5,6,7,8,5,9]
b="Shouvik Maharana"
n=(input("Enter for the count: "))
def count(a,n):
    c=0
    for i in range(len(a)):
        if(a[i]==n):
            c+=1
    print(c)

count(a,n)

"""

# Filter out the duplicates
"""
a=[1,2,3,5,6,4,5,8,7,9,8,4,6,1,2,3]
b=[]
def dup(a):
    for i in range(len(a)):
        if(a[i] not in b):
            b.append(a[i])
    print(b)
dup(a)

"""
# Dictionary
"""
d={1:"jfiewajfu",2:"edfwu",3:5,4:622}
dic={}
keys=[1,2,3]
values=["abc","def","ghi"]

# d.clear()
# print(d)

a=d.copy()
print(a)

dic=d.fromkeys(keys,values)
print(dic)

print(d.get(4))

print(dic.items())

print(dic.keys())

d.pop(1)
print(d)

dic.popitem()
print(dic)

print(dic.setdefault(3))

d.update({"5":"qwerty"})
print(d)

print(dic.values())

"""
# iterate the keys(),items()
"""
dict={1:"Shovuik",2:"Maharana",3:"qwerty"}

for i in dict.keys():
    print(f"{i}:{dict[i]}")

for i in dict.items():
    print(f"{i[0]}:{i[1]}")

for i,j in dict.items():
    print(f"{i}:{j}")

"""
# Key -> Value
"""
list_dict=[{
    "name":"Shouvik",
    "age":"20"
},
{
    "name":"Sam",
    "age":"20"
},
{
    "name":"Priyanshu",
    "age":"20"
},
{
    "name":"Kalinga",
    "age":"20"
}]

for i in list_dict:
    for j,k in i.items():
        print(f"{j} -> {k}",end="\n")

"""
