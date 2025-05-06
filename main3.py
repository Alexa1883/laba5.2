from enum import Enum

class MathOperation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

def calculate(firstNumber, secondNumber, operation):
    result = None

    if operation == MathOperation.ADD:
        result = firstNumber + secondNumber
    elif operation == MathOperation.SUBTRACT:
        result = firstNumber - secondNumber
    elif operation == MathOperation.MULTIPLY:
        result = firstNumber * secondNumber
    elif operation == MathOperation.DIVIDE:
        if secondNumber != 0:
            result = firstNumber / secondNumber
        else:
            raise ValueError("Делить на ноль нельзя!!")
    else:
        raise ValueError("Ошибка!!")

    return (firstNumber, secondNumber, operation.value, result)

firstNumber = 10
secondNumber = 5

#Сложение
operation = MathOperation.ADD
result = calculate(firstNumber, secondNumber, operation)
print(f"Первое число: {result[0]}, Второе число: {result[1]}, Операция: {result[2]}, Результат: {result[3]}")

#Вычитание
operation = MathOperation.SUBTRACT
result = calculate(firstNumber, secondNumber, operation)
print(f"Первое число: {result[0]}, Второе число: {result[1]}, Операция: {result[2]}, Результат: {result[3]}")

#Умножение
operation = MathOperation.MULTIPLY
result = calculate(firstNumber, secondNumber, operation)
print(f"Первое число: {result[0]}, Второе число: {result[1]}, Операция: {result[2]}, Результат: {result[3]}")

#Деление
operation = MathOperation.DIVIDE
result = calculate(firstNumber, secondNumber, operation)
print(f"Первое число: {result[0]}, Второе число: {result[1]}, Операция: {result[2]}, Результат: {result[3]}")

