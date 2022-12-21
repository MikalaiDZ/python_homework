# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


def coins(N):
    coins = []
    import random
    for _ in range(N):
        coins.append(random.randint(0, 1))
    print(coins)

    count = 0
    for item in coins:
        if item == 0: count += 1                                # Вычисляем количество монет повернутых одной стороной
    other_side = N - count                                       # Находим количество повернутых другой стороной
    
    if count > other_side:                                       
        print(f'минимум перевернуть {other_side} монет(ы)')     # если количество разное
    elif other_side > count:
        print(f'минимум перевернуть {count} монет(ы)')          # если количество разное
    elif count == N or other_side == N :
        print('Все монеты повернуты одной стороной')            # Если все повернуты одной стороной
    else:
        print(f'минимум перевернуть {count} монет(ы)')          # Если count = other_side
    return 
          

while True:
    try:
        num = int(input('Введите число монет: '))
        print(coins(num))
        break     
    except:
        print('Неверный ввод! Попробуйте еще!')