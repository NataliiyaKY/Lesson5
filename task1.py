'''Задание максимум на 80 баллов:
Вывести треугольник #1 с шириной N с помощью цикла while
***
**
*
'''

a = int(input())
while a >= 1:
    print('*' * a)
    a -= 1
