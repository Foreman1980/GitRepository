#Ввод пользователем произвольного списка с клавиатуры
n = int(input('Введите длину списка (целое число) - '))
lst = []
for i in range(n):
	lst.append(input('\nВедите {} элемент списка № 1 - '.format(i+1)))
result_list = []
#Сортируем список по порядку
lst.sort()
while lst != []:
    last_value = lst.pop()
#Если последнее значение списка не равно предпоследнему, значит оно уникально
    if lst == [] or last_value != lst[-1]:
	    result_list.append(last_value)
    else:
#Иначе удаляем все вхождения в исходный список неуникального значения
	    del lst[lst.index(last_value):]
print('\n', result_list)