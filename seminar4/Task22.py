# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

def intersection(n, m):
    import random
    numbers_n = list(random.randint(0, 10) for i in range(n))
    numbers_m = list(random.randint(0, 10) for i in range(m))
    end_list = []
    print(numbers_n)
    print(numbers_m)

    for i in numbers_n:
        if i in end_list:
            continue
        for j in numbers_m:
            if i == j:
                end_list.append(i)
                end_list.sort()
                break

    # end_list = list(set(numbers_n) & set(numbers_m))
    if (len(end_list) > 0):
        print(end_list)
    else:
        print('Совпадений нет')


while True:
    try:
        num_n = int(input('Введите кол-во элементов первого набора: '))
        num_m = int(input('Введите кол-во элементов второго набора: '))
        intersection(num_n, num_m)
        break
    except:
        print('Неверный ввод! Попробуйте еще!')
