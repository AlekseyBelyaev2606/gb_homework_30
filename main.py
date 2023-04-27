# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

firstElement = int(input("Введите значение первого элемента"))
differenceElement = int(input("Введите разность элементов"))
maxElement = int(input("Введите количество элементов в массиве"))

listResult = []
for i in range(1,maxElement+1):
    temp = firstElement + (i - 1) * differenceElement
    listResult.append(temp)

print(listResult)