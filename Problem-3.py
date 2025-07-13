def generate_series(a):
    series = []
    count = 0
    num = 1

    limit = a if a % 2 != 0 else a - 1
    
    while count < limit:
        series.append(num)
        num += 2  
        count += 1
    return series

a = int(input("Enter the value of a: "))
if a <= 0:
    print("Please enter a positive integer.")
else:
    result = generate_series(a)
    print("Output:", ', '.join(map(str, result)))
