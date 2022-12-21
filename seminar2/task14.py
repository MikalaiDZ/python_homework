# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4
# 17
# 1 2 4 8 16

def degree(N):
    degree = [2 ** k for k in range(N) if 2 ** k <=  N ]   # генерирует список сразу с условием.
    print(degree)
    

while True:
    try:
        num = int(input('Введите число: '))
        print(degree(num))
        break     
    except:
        print('Неверный ввод! Попробуйте еще!')