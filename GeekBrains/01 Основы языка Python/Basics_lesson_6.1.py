# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016}, {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import json, pickle

my_favourite_group = {'name': 'Г.М.О.',
                      'tracks': ['Последний месяц осени', 'Шапито'],
                      'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}

my_favourite_group_json = json.dumps(my_favourite_group)
print(my_favourite_group_json)

# Вывод вида - "{"name": "\u0413.\u041c.\u041e.", "tracks": ["\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439..."

my_favourite_group_bytes = pickle.dumps(my_favourite_group)
print(my_favourite_group_bytes)

# Вывод вида - "b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\t\x00\x00\x00\xd0\x93....."

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)