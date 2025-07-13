class Calculator:
    def __init__(self, a, b):
        self.a = a 
        self.b = b  

    def calculate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'sub':
            return self.a - self.b
        elif operation == 'mul':
            return self.a * self.b
        elif operation == 'div':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Can not divide by zero"
        else:
            return "invalid operation"

a = float(input("enter 1st number: "))
b = float(input("enter 2nd number: "))
operation = input("enter operation (add, sub, mul, div): ").lower()

calc = Calculator(a, b)
res = calc.calculate(operation)
print("result:", res)
