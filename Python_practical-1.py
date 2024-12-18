def count_even_odd_numbers(tup):
    even_count = 0
    odd_count = 0
    
    for num in tup:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

# Tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

# Call the function
even, odd = count_even_odd_numbers(numbers)

# Output 
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
