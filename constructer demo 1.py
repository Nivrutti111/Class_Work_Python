class Person:
    age=34     #instance variable
    def display(self):
        c=23+67  #inside method variable is local
        print(c)
        print("The age is",self.age)
    def getdeta(self):
        print(c) #scope of local variable is restricted within a block

p=Person()
p.display()
p.getdeta()

    
