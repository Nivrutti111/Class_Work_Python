#Q.4)WAP to do intersection of two list


def intersection(lst1, list2):
    return list(set(lst1) & set(list2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("Intersection of the lists:", intersection(list1,list2))

