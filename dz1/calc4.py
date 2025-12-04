import math


class Calculator:
    def __init__(self):
        self.num1 = float(input())
        self.num2 = float(input())

    def basic_operations(self, operation:str):
        if operation == '+':
            result = self.num1 + self.num2
        elif operation == '-':
            result = self.num1 - self.num2
        elif operation == '*':
            result = self.num1 * self.num2
        elif operation == '/':
            if self.num2 == 0:
                return "Ошибка: деление на ноль!"
            result = self.num1 / self.num2
        else:
            return "Неизвестная операция!"

        return f"{self.num1} {operation} {self.num2} = {result}"

    def trigonometric_operations(self, operation):
        if operation == 'sin':
            result1 = math.sin(self.num1)
            result2 = math.sin(self.num2)
            return f"sin({self.num1}) = {result1}, sin({self.num2}) = {result2}"
        elif operation == 'cos':
            result1 = math.cos(self.num1)
            result2 = math.cos(self.num2)
            return f"cos({self.num1}) = {result1}, cos({self.num2}) = {result2}"
        elif operation == 'tan':
            if math.cos(self.num1) == 0 or math.cos(self.num2) == 0:
                return "Ошибка: тангенс не определен для данного угла!"
            result1 = math.tan(self.num1)
            result2 = math.tan(self.num2)
            return f"tan({self.num1}) = {result1}, tan({self.num2}) = {result2}"
        else:
            return "Неизвестная тригонометрическая операция!"


calc = Calculator()

print(calc.basic_operations('+'))
print(calc.basic_operations('-'))
print(calc.basic_operations('*'))
print(calc.basic_operations('/'))

print(calc.trigonometric_operations('sin'))
print(calc.trigonometric_operations('cos'))
print(calc.trigonometric_operations('tan'))
