# 1
# a=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(int(len(a))):
#     for j in range(int(len(a[i]))):
#         sum=sum+a[i][j]
# print(sum)

#  2
# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[j][i],end="\t")
#     print()

# 3
# a=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if(i==j or i+j==len(a)-1):
#             sum=sum+a[i][j]
# print(sum)

# # 4
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[1,2,3],[4,5,6],[7,8,9]]
# c=[]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         c.append(a[i][j]+b[i][j])
# print(c)

# 5
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[1,2,3],[4,5,6],[7,8,9]]
# c=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum=0
#         for k in range(len(b[i])):
#             c[i][j]+=a[i][k]*b[k][j]
#         # print(sum,end=" ")
# print(c)