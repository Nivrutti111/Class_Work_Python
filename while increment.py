'''
syntax:
while(condition):
     block of statement
     increment/decrement
'''
'''
i=1
while(i<10):
    print("Hi World")
    i+=1   #i=i+1
'''
'''
#WAP to get table of givan number using while loop
n=int(input("Enter a number"))
i=1
while(i<=10):
    print(n*i)
    i+=1
'''
'''
n=int(input("Enter a number"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse is",rev)
'''
#WAP to check whether the number is palindrome or not.

n=int(input("Enter a number"))
temp=n;
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse is",rev)
if(temp==rev):
    print(" is a palindrome.",temp)
else:
    print(" is not a palindrome.")


