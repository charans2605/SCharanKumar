def calci(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Can not divide by the zero"
    elif oper == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Can not perform the modulus operation with zero"
    else:
        return "invalid operation"
    
number1 = float(input("enter 1st number: "))
number2 = float(input("enter 2nd number: "))
op = input("enter operation (+, -, *, /, %): ")
res = calci(number1, number2, op)
print("result:", res)
