import json
import os
import menu
import openfile
from colors import fg, bg, style
import cheking
import write_to_file

os.system('color')

text = ""
dic_en_rus = {}


# функия для выбора из меню. работает с статическими методами в модули menu
def select_action(value):
    global text
    lst = ['1', '2', '0', '3']
    while value not in lst:
        value = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

    if value == '1':
        lst_choose = ['2', '3', '0']
        print("""

                        [2] посмотреть записанные слова
                        [3] меню
                        [0] выход
                        """)
        if os.path.exists('dictionary.json'):
            text = input(fg.CYAN + "Введите слово для перевода"
                                   " или выбирайте из меню :-> " + style.RESET_ALL).lower().strip()
            while text.isdigit() and not text in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        else:
            print("новый файл создан")
            file = open('dictionary.json', 'a+', encoding='utf-8-sig')
            file.close()
            text = input('\033[32m' + '\033[1m' + "Введите слово для перевода"
                                                  " или выбирайте из меню :-> ").lower().strip()
            while text.isdigit() and not text in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        if text == "0":
            exit()

        elif text == "1":
            value = text
            select_action(value)

        elif text.isalpha():
            read = openfile.OpenFile()
            dic_en_rus = read.opening_json('dictionary.json')
            cheking.Cheking.checking(dic_en_rus, text)
            select_action("1")

        elif text == "2":
            value = text
            select_action(value)
    elif value == '2':

        lst_choose = ['1', '3', '0']
        print("""

                                [1] поиск в словаре
                                [3] меню
                                [0] выход
                                """)
        if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') != 0:
            read = openfile.OpenFile()

            dic_en_rus = read.opening_json('dictionary.json')
            c = 1
            for i, j in dic_en_rus.items():
                print(f' {str(c) + ". "}{i}' + style.RESET_ALL + '  -> ' + f' {j}  ')
                c += 1
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            while text.isdigit() and not text in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

            else:
                select_action(text)
            select_action(text)
        elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') == 0:
            print("Словарь пустой. выбирайте пункт [1] и создайте словарь")
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            select_action(text)

    elif value == '3':

        a = menu.Menus.show_menu()
        select_action(a)

    elif value == '0':

        exit()
    return text


a = menu.Menus.show_menu()
select_action(a)
