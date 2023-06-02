# def rev_string_decorator(func):
#     def wrapper():
#         val=func()
#         return val[::-1]
#     return wrapper
# @rev_string_decorator
# def say_hello_world():
#     return "Hello,world"
# print(say_hello_world())

def arm_strong_decorator(func):
    def wrapper():
        val=func()
        c=0
        sum=0
        n1=val
        n2=val
        while(n1>0):
            n1=n1//10
            c=c+1
        
        while(n2>0):
             r=n2%10
             sum+=(r)**c
             n2=n2//10
        if sum==val:
            return "Armstrong number"
        else:
            return "Not an Armstrong number"
    return wrapper
            
@arm_strong_decorator
def function1():
    return 121
print(function1())
