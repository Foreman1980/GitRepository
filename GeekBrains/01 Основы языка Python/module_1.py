#1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys
def make_ten_new_dir(dir_name):
    for d in range(1, 10):
        os.mkdir(os.path.join(os.getcwd(), f'{dir_name}_{d}'))

def del_ten_new_dir(mask):
    for d in os.listdir():
        if mask in d:
            os.rmdir(os.path.join(os.getcwd(), d))

# Запишем условие для исполнения кода только при запуске непосредственно этого модуля, а не при его подключении
if __name__ == '__main__':
    # Зададим маску для имени каталогов
    name = 'dir'

    # Для удаления папок закоментировать функцию make_ten_new_dir() и раскомментировать del_ten_new_dir()
    make_ten_new_dir(name)
    #del_ten_new_dir(name)

    # Для проверки списка содержимого текущего каталога
    print(os.listdir())
