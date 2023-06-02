class for_class:
    def xyz(self,n):
        for i in range(1,n+1):
            print(i,end=" ")
        print()
    def rev_xyz(self,n):
        for i in range(n,0,-1):
            print(i,end=" ")
        print()
    def for_table(self,n,t):
        i=1
        for i in range(1,t+1):
            y=n*i
            print(f"{n}x{i}={y}")
            i=i+1
    def factor(self,n):
        i=1
        print('The factors are:')
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")
        print()
    def prime(self,n):
        flag=0
        for i in range(1,n+1):
            if n%i==0:
                flag=flag+1
        if flag>2:
            print(f'{n} is a not prime number')
        else:
            print(f'{n} is a prime number')
        print()

    def primefactor(self,num):
        i=1
        for i in range(1,num+1):
            j=1
            c=0
            if num%i==0:
                for j in range(1,i+1):
                    c=c+1
                if(c==2):
                    print(f"{i}")
                

    def arm(self,num):
        c=0
        sum=0
        n1=num
        n2=num
        for i in str(n1):
            n1=n1//10
            c=c+1
        print(c)
        for i in str(n2):
             r=n2%10
             n2=n2//10
             sum=sum+r**c
        if sum==num:
            print("Armstrong number")
        else:
            print("not a Armstrong number")
            
    def palindrome(self,num):
        temp=num
        rev=0
        
        for i in str(num):
            dig=temp%10
            rev=rev*10+dig
            temp=temp//10

        if rev==num:
            print(f"{num} is a palindrome number")
        else:
            print(f"{num} is not a palindrome number")

            
                

classobj=for_class()
classobj.xyz(10)
classobj.rev_xyz(10)
classobj.for_table(2,10)
classobj.factor(12)
classobj.prime(25)
classobj.palindrome(1221)
classobj.primefactor(25)
classobj.arm(121)