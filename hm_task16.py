# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве из случайных чисел. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. Последняя строка
# содержит число X

from random import randint
n=int(input("Введите количество элементов списка чисел: "))
list1=[randint(1,10) for item in range(n)]
print(list1)
x=int(input("Введите число, которое ищем: "))
count=0
for i in list1:
    if i==x:
        count+=1
print(f"Число {x} встречается {count} раз")

