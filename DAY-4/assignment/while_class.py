class while_class:
    def prt(self,n):
        i=1
        while(i<=n):
            print(i,end=" ")
            i=i+1
        print()
    def rev(self,n):
        i=n
        while(i>0):
            print(i,end=" ")
            i=i-1
        print()
    def while_table(self,n,t):
       i=1
       while(i<=t):
            y=n*i
            print(f"{n}x{i}={y}")
            i=i+1
    print()
    def wfactor(self,n):
        
        print('The factors are:')
        i=1
        while(i<=n):
            if n%i==0:
                print(i,end=" ")
            i=i+1
        print()
    def wprime(self,n):
        i=1
        flag=0
        while(i<=n):
            if n%i==0:
                flag=flag+1
            i=i+1
        if flag>2:
            print(f'{n} is a not prime number')
        else:
            print(f'{n} is a prime number')
        print()
    def wprime_factors(self,n):
        i=1
        print(1)

        while(i<=n):
            if n%i==0 :
                c=0
                j=1
                while(j<=i):
                    if i%j==0:
                        c=c+1
                    j=j+1
           
                if(c==2):
                    print(f"{i}")
            i=i+1

        
    def warm(self,num):
        c=0
        sum=0
        n1=num
        n2=num
        while(n1>0):
            n1=n1//10
            c=c+1
        print(c)
        while(n2>0):
             r=n2%10
             n2=n2//10
             sum=sum+r**c
        if sum==num:
            print("Armstrong number")
        else:
            print("not a Armstrong number")

    def wpalind(self,n):
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
obj=while_class()
# obj.prt(10)
# obj.rev(10)
# obj.while_table(2,10)
# obj.wfactor(25)
# obj.wprime(12)
# obj.warm(153)
# obj.wpalind(1221)
obj.wprime_factors(12)