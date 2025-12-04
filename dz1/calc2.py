def summation(x: float, y: float) -> float:
    """ функция суммирования двух чисел
        входные данные: два действительных числа
        выходные данные: сумма этих чисел """
    return x + y


def difference(x: float, y: float) -> float:
    """ функция суммирования двух чисел
        входные данные: два действительных числа
        выходные данные: разность этих чисел """
    return x - y


def composition(x: float, y: float) -> float:
    """ функция суммирования двух чисел
        входные данные: два действительных числа
        выходные данные: произведение этих чисел """
    return x * y


def division(x: float, y: float) -> float:
    """ функция суммирования двух чисел
        входные данные: два действительных числа
        выходные данные: деление первого числа на второе """
    return x / y


num1 = float(input())
num2 = float(input())
oper = input()

if oper == '+':
    print(f"{num1} {oper} {num2} = {summation(num1, num2)}")
elif oper  == '-':
    print(f"{num1} {oper} {num2} = {difference(num1, num2)}")
elif oper  == '*':
    print(f"{num1} {oper} {num2} = {composition(num1, num2)}")
elif oper  == '/':
    print(f"{num1} {oper} {num2} = {division(num1, num2)}")
