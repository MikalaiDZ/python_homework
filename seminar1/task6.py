# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

print('Введите номер билета')
numbers = list(input())

if 5 < len(numbers) < 7:
    first_sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    last_sum = int(numbers[len(numbers) - 1]) + int(numbers[len(numbers) - 2]) + int(numbers[len(numbers) - 3])
    
    if first_sum == last_sum:
        print('Yes')
        
    else:
        print('No')
        
else:
    print('Номер билета не шестизначный')