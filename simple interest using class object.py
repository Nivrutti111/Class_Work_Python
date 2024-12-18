class Test:
    def Int(self,a,r,t):
        res=(a*r*t)/100
        return res

a=int(input("Enter a Amount"))
r=int(input("Enter a rate_of_interest"))
t=int(input("Enter a Time"))

T=Test()
answer=T.Int(a,r,t)
print("The Interest is: ",answer)
