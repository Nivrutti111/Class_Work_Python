class Test:
    def add(self,a,b):
        res=a+b
        return res
    def sub(self,a,b):
        res=a-b
        print("The substraction is",res)
    def div(self,a,b):
        res=a/b
        print("The devision is",res)
    def mul(self,a,b):
        res=a*b
        print("The multiplication is",res)

a=int(input("Enter first Number"))
b=int(input("Enter second Number"))

T=Test()
answer=T.add(a,b)
print("The  addition of two numbers are",answer)

T.sub(a,b)

T.div(a,b)

T.mul(a,b)
