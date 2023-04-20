# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

Amount = abs(int(input("Введите количество элементов массива А: ")))
FilledArray = input("Введите через пробел элементы массива: ").split()
Digit = list(map(int, FilledArray))
if len(Digit) != Amount or Amount == 0:
    print(" Количество введенных элементов не равно ранее объявленному количеству")
else:
    numberX = int(input("Введите число X"))
    min = abs(numberX - Digit[0])
    index = 0
    for i in range(1, Amount):
        count = abs(numberX - Digit[i])
        if count < min:
            min = count
            index = i
    print(f"Число {Digit[index]} в массиве A наиболее близко по величине к числу {numberX}")
    