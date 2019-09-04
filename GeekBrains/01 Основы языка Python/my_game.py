#Отгадывание числа случайным образом, тут интереснее))
import random
def my_game():
    print('Загадайте целое число из диапазона [1; 99], а я попробую отгадать')
    print('Для подсказки вводите "<"-если ваше число больше, ">"-если меньше, "="-если я угадал')
    minimum_value = 0
    maximum_value = 100
    pc_win = False
    count = 0
    while not pc_win:
        variant = random.randint(minimum_value + 1, maximum_value - 1)
        count += 1
        result = input(f'Мой {count} вариант - {variant} ')
        if result == '=':
            pc_win = True
            print('Ура! Я угадал)')
            break
        elif result == '<':
            minimum_value = variant
        else:
            maximum_value = variant