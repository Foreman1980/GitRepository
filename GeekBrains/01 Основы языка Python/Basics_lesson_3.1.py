#Отгадывание числа по алгоритму
print('Загадайте целое число из диапазона [1; 99], а я попробую отгадать')
print('Для подсказки вводите "<"-если ваше число больше, ">"-если меньше, "="-если я угадал')
minimum_value = 0
maximum_value = 100
pc_win = False
count = 0
while not pc_win:
    variant = minimum_value + ((maximum_value - minimum_value) // 2)
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