#Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз)
# и после первого нуля выводит сумму всех ранее введенных чисел.
from decimal import Decimal


def set_list():
    numbers = list()
    numbers.append(0)
    x = Decimal(input("Введите число:"))
    while x != 0:
        numbers.append(x)
        x = Decimal(input("Введите число:"))
    get_sum(numbers)


def get_sum(numbers):
    print(sum(numbers))
    return sum(numbers)


set_list()
