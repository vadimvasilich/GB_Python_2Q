# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# ________________________________________________________________
# 5.Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

# показывает справочник целиком
# def show_data(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             print(line.strip())
    

# #  добавляет новую строку
# def add_data(file_path):
#     with open(file_path, 'a', encoding='utf-8') as f:
#         f.write(input('Введите новую строку: '+ '\n'))
    

# # поиск информации в справочнике
# def find_data():
#     with open(file_path, 'r', encoding='utf-8') as f:
#         find_info = input('Введите данные для поиска: ')
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 print(line)

# # удаляет данные
# def delete_data(name):
#     persons = add_data()
#     with open(file_path, "w", encoding="utf8" ) as f:
#         for person in persons:
#             if name != person:
#                 f.write(person)

# # изменяет данные
# def change_data(new_name, old_name):
#     persons = add_data()
#     with open(file_path, "w", encoding="utf8" ) as f:
#         for person in persons:
#             if  old_name != person:
#                 f.write(person)
#             else:
#                 f.write(new_name + "\n")

# def find_char():
#     print('Выберите характеристику:')
#     print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
#     char = input()
#     while char not in ('0', '1', '2', '3', '4', 'q'):
#         print('Введены неверные данные')
#         print('Выберите характеристику:')
#         print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
#         char = input()
#     if char != 'q':
#         inp = input('Введите значение\n')
#         return char, inp
#     else:
#         return 'q', 'q'
    
#     # def find_records(file_name: str, char, condition):
#     #     if condition != 'q':
#     #         printed = False
#     #         with open(file_name, 'r', encoding='utf-8') as data:
#     #             for line in data:
#     #                 if condition == line.split(';')[int(char)]:
#     #                     print(*line.split(';'))
#     #                     printed = True
#     #         if not printed:
#     #             print("Не найдено")
#     #         return printed

# file_path = r'/Users/vadim/Desktop/Python_2Q/ДЗ семинар 8/phonebook.txt'


# actions = {'1': 'чтение',
#            '2': 'запись',
#            '3': 'поиск',
#            '4': 'изменение',
#            '5': 'удаление',
#            'q': 'выход'
#            }

# action = None
# while action != 'q':
#     print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
#     action = input()
#     while action not in actions:
#         print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
#         action = input()
#         if action not in actions:
#             print('Введены неверные данные')
#     if action != 'q':
#         if action == '1':
#             show_data(file_path)
#         elif action == '2':
#             add_data(file_path)
#         elif action == '3':
#             find_data(file_path, *find_char())
#         elif action == '4':
#             change_data(file_path)
#         elif action == '5':
#             delete_data(file_path)
#             break
#     else:
#         print('No mode')

def show_data(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(' '), end='')


def add_data(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите фамилию, имя, отчество, номер телефона через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('добавление записи')
        if confirm == 'y':
            data.write(line)


def find_char():
    print('Выберите характеристику:')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'


def find_data(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed


def check_id_data(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_data(path, *find_char())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        while not find_data(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision


def confirmation(text: str):
    confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    return confirm


def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_data(file_name: str):
    record_id = check_id_data(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите фамилию, имя, отчество, номер телефона через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def delete_data(file_name: str):
    record_id = check_id_data(file_name, 'удалить')
    if record_id != 'q':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')


path = 'phone_book.txt'

try:                        
    file = open(path, 'r')  
except IOError:             
    print('Создан новый справочник -> phone_book.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'показать',
           '2': 'добавить',
           '3': 'поиск',
           '4': 'изменение',
           '5': 'удаление',
           'q': 'выход'}

action = None
while action != 'q':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            show_data(path)
        elif action == '2':
            add_data(path)
        elif action == '3':
            find_data(path, *find_char())
        elif action == '4':
            change_data(path)
        elif action == '5':
            delete_data(path)