print('Заполните анкету:')
first_name = input('Ваше имя - ')
second_name = input('Ваша фамилия - ')
age = int(input('Ваш возраст (полных лет) - '))
weight = int(input('Ваш вес (округлите до целого) - '))
if 5 <= age <= 40:
    if 50 < weight <= 120:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - хорошее состояние.')
    elif 25 <= weight <= 50 or 120 < weight <= 150:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - следует заняться собой.')
    else:
        print('Некорректные данные')
elif 40 < age <= 70:
    if 50 < weight <= 85:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - хорошее состояние.')
    elif 40 < weight <= 50 or 85 < weight <= 100:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - следует заняться собой.')
    elif 25 <= weight <= 40 or 100 < weight <= 120:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - следует обратиться к врачу!')
    else:
        print('Некорректные данные')
elif 70 < age <= 100:
    if 50 < weight <= 75:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - хорошее состояние.')
    elif 40 < weight <= 50 or 75 < weight <= 85:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - следует заняться собой.')
    elif 25 <= weight <= 40 or 85 < weight <= 100:
        print(first_name + ' ' + second_name + ', ' + str(age) + ' год, вес ' + str(weight) + ' кг - следует обратиться к врачу!')
    else:
        print('Некорректные данные')
else:
    print('Некорректные данные')