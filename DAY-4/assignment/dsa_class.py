class dsa_class():
    def diction(self):
        student={"name":"Khushi","age":20,"university":"SIT"}
        print(type(student))
        print(student)
        for i in student.keys():
            print(i,student[i])
    def list_class(self):
        a=[2,4,6,8,10,12]
        print(a)
        print(len(a))
        for i in range(len(a)):
            print(a[i],end=" ")
        print()
    def list_insert(self,n):
        a=[]
        n=int(input("enter the size of the list:"))
        for i in range(n):
            a.append(int(input("enter the items in the list:")))
        print(a)
        print()
    def list_insert_atbegin(self,n):
        a=[4,5,6,7,8]
        a.append(None)
        for i in range(len(a)-1,0,-1):
            a[i]=a[i-1]
        a[0]=3
        print(a)
    def slicing(self):
        a=[2,3,4,5,6,7]
        print(a[0:4])
    def prog1_sum(self):
        a=[[1,2,3],[4,5,6],[7,8,9]]
        sum=0
        for i in range (int(len(a))):
            for j in range(int(len(a[i]))):
                sum=sum+a[i][j]
        print(sum)
    def prog2(self):
        a=[[1,2,3],[4,5,6],[7,8,9]]
        for i in range(int(len(a))):
            for j in range(int(len(a[i]))):
                print(a[j][i],end="\t")
            print()
    def prog3_sum_diagonals(self):
        a=[[1,2,3],[4,5,6],[7,8,9]]
        s=0
        for i in range(int(len(a))):
            for j in range (int(len(a[i]))):
                if(i==j or i+j==len(a)-1):
                    s=s+a[i][j]
        print(s)
    def sum_of_arrays(self):
        a=[[1,2,3],[4,5,6],[7,8,9]]
        b=[[1,2,3],[4,5,6],[7,8,9]]
        c=[]
        for i in range(len(a)):
            for j in range(len(a[i])):
                c.append(a[i][j]+b[i][j])
        print(c)
    def mul_array(self):
        a=[[1,2,3],[4,5,6],[7,8,9]]
        b=[[1,2,3],[4,5,6],[7,8,9]]
        c=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range (len(a)):
            for j in range(len(a[i])):
                for k in range(len(b[j])):
                    c[i][j]=c[i][j]+(a[i][k]*b[k][j])
        print(c)
    def strrrr(self):
        x="Khushi Pradhan"
        print(x[5])
        print(x[::-1])
    def sets_cls(self):
        y={1,2,3,4,5,"yy"}   
        print(type(y))
        print(y)    
    def tuple_cls(self):
        z=(0,1,2,5,4)
        print(z.index(4))    
    

xyz=dsa_class()
# xyz.diction()
# xyz.list_class()
# xyz.list_insert(None)
# xyz.list_insert_atbegin(None)
# xyz.slicing()
# xyz.prog1_sum()
# xyz.prog2()
# xyz.prog3_sum_diagonals()
# xyz.sum_of_arrays()
# xyz.mul_array()
# xyz.strrrr()
# xyz.sets_cls()
# xyz.tuple_cls()