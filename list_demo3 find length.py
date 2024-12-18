# WAP find the length of a list in python

l=[45,5,67,3,24]

length = len(l)
print(length)

#WAP finde Maximum of two numbers in python

maximum_val=max(l)
print("The maximum value of list is",maximum_val)

minimum_val=min(l)
print("The minimum value of list is",minimum_val)

#WAP to find 2nd largest number in list

#second largest
for i in range(0,5):
    for j in range(i+1,5):
        if l[j]>l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)
print("second largest ",l[1])



