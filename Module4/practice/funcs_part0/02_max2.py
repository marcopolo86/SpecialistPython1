# Напишите функцию, возвращающую наибольшее из двух чисел

def max2(n1, n2):
    # TODO: your code here
    pass


def max2(a, b):
    if a < b:
        return b
    return a

# Тестируем функцию
print(max2(5, 6))
print(max2(-10, -12))
print(max2(2.5, 2.6))
print(max2(-2.5, 0))
print(max2(0, -2.5))
