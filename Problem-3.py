def gen_series(a):
    series = []
    num = 1
    for _ in range(a):
        series.append(num)
        num += 2  
    return series

a = int(input("enter the value of a: "))

if a <= 0:
    print("enter a positive integer.")
else:
    res = gen_series(a)
    print("output:", ', '.join(map(str, res)))
