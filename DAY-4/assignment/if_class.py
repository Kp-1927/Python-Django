class if_class:
    def neg_pos_num(self,num):
        if num>=0:
            print(f"{num} is positive")
        else:
            print(f"{num} is negative")

    def even_odd(self,num):
        if num%2==0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    
    def leap_year(self,num):
        if num%100==0:
            if num%400==0:
                print(f"{num} is a leap year")
            else:
                print(f"{num} is not a leap year")
        else:
            if num%4==0:
                print(f"{num} is a leap year")
            else:
                print(f"{num} is not a leap year")





            
ifobj=if_class()

ifobj.neg_pos_num(-4)
ifobj.even_odd(5)
ifobj.leap_year(1700)
