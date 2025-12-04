def calculator(x: float, y: float, operation: str) -> str:
    if operation == '+':
       return f"{num1} {operation} {num2} = {num1 + num2}"
    elif operation == '-':
        return f"{num1} {operation} {num2} = {num1 - num2}"
    elif operation == '*':
        return f"{num1} {operation} {num2} = {num1 * num2}"
    elif operation == '/':
        return f"{num1} {operation} {num2} = {num1 / num2}"
    return "неизвестная операция"


num1 = float(input())
num2 = float(input())
oper = input()

print(calculator(num1, num2, oper))
