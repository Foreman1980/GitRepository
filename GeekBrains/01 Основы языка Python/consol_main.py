import sys, os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from my_game import my_game

save_info('Старт')

if sys.argv[1] == 'list':
    try:
        get_list(sys.argv[2])
    except:
        get_list()
elif sys.argv[1] == 'create_file':
    try:
        create_file(sys.argv[2], sys.argv[3])
    except IndexError:
        print('Не указано имя нового файла')
elif sys.argv[1] == 'create_folder':
    try:
        create_folder(sys.argv[2])
    except IndexError:
        print('Не указано имя новой папки')
elif sys.argv[1] == 'delete':
    try:
        delete_file(sys.argv[2])
    except IndexError:
        print('Не указано имя удаляемого объекта')
elif sys.argv[1] == 'copy':
    try:
        name1 = sys.argv[2]
    except IndexError:
        print('Не указано имя копируемого объекта')
    else:
        try:
            name2 = sys.argv[3]
        except IndexError:
            print('Не указано имя нового объекта')
        else:
            copy_file(name1, name2)
elif sys.argv[1] == 'change':
    try:
        change_dir(os.path.join(os.getcwd(), sys.argv[2]))
    except IndexError:
            print('Не указано наименование новой рабочей папки')
    except FileNotFoundError:
        print('К сожалению такой папки не существует')

elif sys.argv[1] == 'game':
    my_game()

elif sys.argv[1] == 'help':
    print('"list" - спиок файлов и папок,\n    с доп. параметрами:\n    "files" - только файлы,\n    "folders" - только папки')
    print('"create_file" - создание файла')
    print('"create_folder" - создание папки')
    print('"delete" - удаление файла или папки')
    print('"copy" - копирование файла или папки')
    print('"change" - смена рабочей папки')
    print('"game" - игра - вы загадываете число, компьютер пытается его угадать')

save_info('Стоп')
