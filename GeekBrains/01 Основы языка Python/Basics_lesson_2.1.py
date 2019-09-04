n, m = input('Введите длины списков (целые числа, через пробел) - ').split()
print()
n, m = int(n), int(m)
lst_1 = []
lst_2 = []
for i in range(n):
	lst_1.append(input('Ведите {} элемент списка № 1 - '.format(i+1)))
print()
for i in range(m):
	lst_2.append(input('Ведите {} элемент списка № 2 - '.format(i+1)))

for i in range(m):
    if lst_2[i] in lst_1:
        for j in range(lst_1.count(lst_2[i])):
            lst_1.remove(lst_2[i])
print()
print('Итоговый список № 1 -', lst_1)