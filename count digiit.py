#Write a while loop that counts the number of digits in a given number.

# Input: a number
num = int(input("Enter a number: "))

# Initialize count
count = 0

# Use absolute value to handle negative numbers
num = abs(num)

# Count digits using a while loop
while num > 0:
    num //= 10  
    count += 1    

# If the input number is 0, we need to account for that case
if count == 0:
    count = 1

print("The number of digits is:", count)
