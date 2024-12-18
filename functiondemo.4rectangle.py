class rectangle:
        def __init__(self,length,breadth):
            self.length = length
            self.breadth = breadth

        def area(self):
            return self.length * self.breadth
# Taking input from user      
length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the  breadth of the rectangle"))

# Creating an object of the rectangle class
rect = rectangle(length, breadth)

# Calling area method using rect object
print("The Area of Rectangle is:",rect.area())
    
