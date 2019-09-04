# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
def max_number(n1, n2, n3):
    numbers_list = []
    for i in n1, n2, n3:
        numbers_list.append(i)
    return max(numbers_list)

print(max_number(5, 2, 3))

# Вывод вида - "5"