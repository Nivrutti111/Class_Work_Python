def count_age_groups(ages):
    # Initialize counters for ages
    group_26_35 = 0
    group_36_45 = 0
    group_46_55 = 0
    
    for age in ages:
        if 26 <= age <= 35:
            group_26_35 += 1
        elif 36 <= age <= 45:
            group_36_45 += 1
        elif 46 <= age <= 55:
            group_46_55 += 1
            
    return group_26_35, group_36_45, group_46_55

# Input: Number of employees
n = int(input("Enter the number of employees: "))

# Input: Ages of employees
ages = []
for i in range(n):
    age = int(input(f"Enter age of employee {i+1}: "))
    ages.append(age)

# Get the count of people in each age group
group_26_35, group_36_45, group_46_55 = count_age_groups(ages)

# Output the result
print(f"Number of employees in age group 26-35: {group_26_35}")
print(f"Number of employees in age group 36-45: {group_36_45}")
print(f"Number of employees in age group 46-55: {group_46_55}")

