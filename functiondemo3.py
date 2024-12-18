
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def dogInfo(self):
        print(self.name,"is",str(self.age),"year old")
d=Dog("puppy",5)

d.dogInfo()
d.bark()


        
