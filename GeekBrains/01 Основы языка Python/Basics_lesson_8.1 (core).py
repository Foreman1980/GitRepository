# Консольный файловый менеджер
import os, shutil, datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')


def print_list_in_column(lst):
    for item in sorted(lst):
        print(item)


def get_list(value=None):
    if value == 'folders':
        print_list_in_column([item for item in os.listdir(os.getcwd()) if os.path.isdir(item)])
    elif value == 'files':
        print_list_in_column([item for item in os.listdir(os.getcwd()) if not os.path.isdir(item)])
    else:
        print_list_in_column(os.listdir(os.getcwd()))
    print('-' * 100)


def delete_file(name):
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)


def copy_file(file, new_file):
    try:
        shutil.copytree(file, new_file) if os.path.isdir(file) else shutil.copyfile(file, new_file)
    except FileExistsError:
        print('Такая папка уже существует')


def save_info(message):
    with open('lof_file.txt', 'a', encoding='utf-8') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')


if __name__ == '__main__':
    create_file('new3.txt', 'Hello world!')
    create_folder('new_f')
    create_folder('new_f2')
    get_list()
    delete_file('new_f')
    delete_file('new3.txt')
    get_list('folders')
    copy_file('new_f2', 'new_f3')
    copy_file('main.py', 'main2.py')
    save_info('test')
    pass
