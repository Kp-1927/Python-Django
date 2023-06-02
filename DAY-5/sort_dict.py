# student=[
#     {
#         "name":"John",
#         "age":22
#     },
#     {
#         "name":"Mark",
#         "age":25
#     },
#     {
#         "name":"Mosh",
#         "age":21
#     },
#     {
#         "name":"Marry",
#         "age":23
#     },{
#         "name":"Cris",
#         "age":24
#     }
# ]
# for i in student.keys():
    
#     if student[i]>=student[i+1]:
#         temp=student[i]
#         student[i]=student[i+1]
#         student[i+1]=temp
# print(i,student[i])

a=[7,4,8,9,7,2]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>=a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            
print(a)