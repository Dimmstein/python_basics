"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
n = int(input('Введите целое положительное число n: '))
nn = n + n
nnn = n + n + n
print(f"n + nn + nnn = {str(n) + str(nn) + str(nnn)}")
