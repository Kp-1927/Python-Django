class MathFunction:
    # a=None
    # b=None
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class MathFormula(MathFunction):
    def method1(self,a,b):
        return self.mul(self.sum(a,b),self.sum(a,b))

obj=MathFormula()
print(obj.method1(2,3))
    
    
# obj=MathFunction(5,2)
# print(obj.sum())
# print(obj.sub())
