
# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

from random import randint

n = int(input('n: '))
num = []
for i in range(n):
    num.append(randint(-100, 100))
print(num)
# num = [-29, -90, -53, 91, -20, -20, -27, -76, 8]
summ = 0
count = 0
for summ in num:
    if int(summ) > 0 and int(summ) % 2 == 0:
        count += summ
print(count)
