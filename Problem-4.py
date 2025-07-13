def find_counts(num_list):
    counts = {key: 0 for key in range(1, 10)} 

    for number in num_list:
        for divisor in range(1, 10):
            if number % divisor == 0:
                counts[divisor] += 1  

    return counts
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiple_counts = find_counts(numbers)
print(multiple_counts)
