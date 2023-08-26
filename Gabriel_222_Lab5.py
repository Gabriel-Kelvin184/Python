def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"


print(division(10, 2))
print(division(10, 0))
