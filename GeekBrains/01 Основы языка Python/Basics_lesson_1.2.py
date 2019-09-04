while True:
    number = int(input('Введите число из диапазона - [1;9]: '))
    if 0 < number < 10:
        print(number ** 2)
        break
    else:
        print('Число не верное!')