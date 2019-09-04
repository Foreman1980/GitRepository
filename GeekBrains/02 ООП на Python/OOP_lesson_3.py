# ООП на Python (урок № 3).
# 1. Напишите функцию получения IATA-кода города из его названия, используя API Aviasales для усовершенствования
# приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API (ссылка на значке
# «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

import requests, json

# Вариант № 1:

city_name = input('Введите название города - ')
# Вывод вида - "Введите название города - мурманск"

request_iata = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city_name}%20в%20{city_name}'
iata_dict = json.loads(requests.get(request_iata).text)
print(iata_dict)
# Вывод вида - "{'origin': {'iata': 'MMK', 'name': 'Мурманск'},  'destination': {'iata': 'MMK', 'name': 'Мурманск'}}"

if iata_dict:
    str1 = iata_dict['origin']['name']
    str2 = iata_dict['origin']['iata']
    print(f'Городу "{str1}" соответствует iata-код = "{str2}"')
else:
    print('Такого города нет в каталоге')
# Вывод вида - "Городу "Мурманск" соответствует iata-код = "MMK""

# Вариант № 2 (забераем весь справочник iata-кодов):

def get_actual_iata():
    html = requests.get('http://api.travelpayouts.com/data/ru/cities.json')
    iata_lists = json.loads(html.text)
    iata_codes = []
    for item in iata_lists:
        iata_codes.append({'name': item['name'], 'code': item['code']})
    with open(r'D:\PythonProjects\GeekBrains\02 ООП на Python\iata_cods_lesson_3.json', 'w') as f:
        json.dump(iata_codes, f, ensure_ascii=False)


def city_to_iata(cityname):
    with open(r'D:\PythonProjects\GeekBrains\02 ООП на Python\iata_cods_lesson_3.json', 'r') as f:
        iata_codes = json.load(f)
    for item in iata_codes:
        if item['name'] == cityname:
            return item['code']


get_actual_iata()
city_name = input('Введите название города - ').lower().title()
# Вывод вида - "Введите название города - мурманск"

city_code = city_to_iata(city_name)
if city_code:
    print(f'Городу "{city_name}" соответствует iata-код = "{city_code}"')
else:
    print('Такого города нет в каталоге')
# Вывод вида - "Городу "Мурманск" соответствует iata-код = "MMK""
