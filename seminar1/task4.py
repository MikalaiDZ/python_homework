# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

print('Введите общее число журавликов ')
s = int(input())

knum = int(s // 3 * 2)
pnum = int((s - knum) // 2)
snum = pnum
if s % 2 == 0:
    print(f'Петя сделал {pnum}, Катя сделала {knum}, Сережа сделал {snum}.')
else:
    print(f'Петя сделал {pnum}, Катя сделала {knum}, Сережа сделал {snum}, 1 журавлик лишний.')