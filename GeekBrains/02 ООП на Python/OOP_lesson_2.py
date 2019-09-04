# Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта geekbrains.ru.
# Решите задачу двумя способами:
# a) используя регулярные выражения (библиотеку re),
# b) используя библиотеку BeautifulSoup.
# Примечание: Чтобы увидеть количество учеников, вам надо зайти на главную страницу сайта без залогинивания (нажмите 3
# точки в правом верхнем углу экрана рядом с вашей фотографией и выберите пункт меню «Выход»). Вы окажетесь на главной
# странице, где вверху увидите логотип, количество человек (то, что нам нужно) и кнопку «Войти».

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as BS

html = urlopen('https://geekbrains.ru/')
html_text = html.read().decode('utf-8')
with open('text_auto.html', 'w', encoding='utf-8') as f:
    f.write(html_text)

# СПОСОБ № 1:
# Вариант № 1:

search_text = re.findall('Нас уже 3 8\d\d \d\d\d человек', html_text)
print(search_text)
# Вывод вида - "['Нас уже 3 844 818 человек']"

# Вариант № 2:

search_text_list = re.findall('<span class="total-users">(.+)</span>', html_text)
print(search_text_list)
# Вывод вида - "['Нас уже 3 844 818 человек']"

# СПОСОБ № 2:

bs_object = BS(html_text, 'html.parser')

# Вариант № 1:

print(len(bs_object.find_all('div')))
# Вывод вида - "68"

print(bs_object.find_all('div')[5])
# Вывод вида - "<div class="col"><span class="total-users">Нас уже 3 844 818 человек</span><a class="btn sign-in" href=
#               "/login">Войти</a></div>"

print(bs_object.find_all('div')[5].span.string)
# Вывод вида - "Нас уже 3 844 818 человек"

# Вариант № 2:

print(len(bs_object.find_all('span')))
# Вывод вида - "13"

print(bs_object.find_all('span')[0])
# Вывод вида - "<span class="total-users">Нас уже 3 844 818 человек</span>"

print(bs_object.find_all('span')[0].string)
# Вывод вида - "Нас уже 3 844 818 человек"
