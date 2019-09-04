# 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
#     Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import random

# Формируем список из случайных целых чисел от -50 до 50

random_list = [random.randint(-50, 50) for i in range(20)] # тут генератор списков
print(random_list)

# Вывод вида - "[2, 10, 35, 21, 4, 11, -49, -9, -5, -15, -26, -28, -27, 26, -27, 26, 25, -1, 3, 29]"

result_list = [item for item in random_list if item > 0 and item % 3 == 0 and item % 4 != 0] # тут генератор списков
print(result_list)

# Вывод вида - "[21, 3]"