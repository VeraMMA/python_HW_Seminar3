# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

Amount = abs(int(input("Введите количество элементов массива А: ")))
FilledArray = input("Введите через пробел элементы массива А: ").split()
Digit = list(map(int, FilledArray))
if len(Digit) != Amount:
    print(" Количество введенных элементов не равно ранее объявленному количеству")
else:
    numberX = int(input("Введите число X, которое необходимо найти в массиве: "))
    count = 0
    for i in range(Amount):
        if Digit[i] == numberX:
            count += 1
    print(f"Число {numberX} встречается в массиве A {count} раз") 
    
    

    
