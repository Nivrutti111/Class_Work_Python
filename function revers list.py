#Q.1)Write a function to reverse a list without using
#the built-in reverse() method.


def rev_list(l):
    return l[::-1]

l=[34,98,45,65,88]

ans=(rev_list(l))
print("The Revers of a given list is:",ans)
