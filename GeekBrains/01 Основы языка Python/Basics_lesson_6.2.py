# 2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import json, pickle

with open('group.json', 'r', encoding='utf-8') as f:
	my_favourite_group = json.load(f)
print(my_favourite_group)

# Вывод вида - "{'name': 'Г.М.О.',
#				 'tracks': ['Последний месяц осени', 'Шапито'],
# 				 'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
#  				 {'name': 'Шапито', 'year': 2014}]}"

print(type(my_favourite_group))

# Вывод вида - "dict"

with open('group.pickle', 'rb') as f:
	my_favourite_group = pickle.load(f)
print(my_favourite_group)

# Вывод вида - "{'name': 'Г.М.О.',
#				 'tracks': ['Последний месяц осени', 'Шапито'],
# 				 'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
#  				 {'name': 'Шапито', 'year': 2014}]}"

print(type(my_favourite_group))

# Вывод вида - "dict"
