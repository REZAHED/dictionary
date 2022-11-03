import os
import menu
import openfile
from colors import fg, style
import cheking

os.system('color')

text = ""
# dic_en_rus = {}


# функия для выбора из меню. работает с статическими методами в модули menu
def select_action(value):

    global text
    lst = ['1', '2', '0', '3','4']
    while value not in lst:
        value = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

    if value == '1':
        lst_choose = ['2', '3', '0']

        print("""

[2] посмотреть слова
[3] меню
[0] выход
        """)
        if os.path.exists('dictionary.json'):
            text = input(fg.CYAN + "Введите слово для перевода\n"
                                   " или выбирайте из меню :-> " + style.RESET_ALL).lower().strip()
            while text.isdigit() and text not in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        else:
            print("новый файл создан")
            file = open('dictionary.json', 'a+', encoding='utf-8-sig')
            file.close()
            text = input('\033[32m' + '\033[1m' + "Введите слово для перевода\n"
                                                  " или выбирайте из меню :-> ").lower().strip()
            while text.isdigit() and text not in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()
        sign = ['-', '+', '_', '.', '?']
        if text == "0":
            print("""
     ___ ДО СВИДАНИЯ___
                                    """)
            exit()

        elif text == "1":
            os.system('cls')
            value = text
            select_action(value)
        elif text in sign:
            value = "1"


            select_action(value)
        elif text.replace(" ", "").replace("-", "").isalpha() :

            read = openfile.OpenFile()
            dic_ = read.opening_json('dictionary.json')
            cheking.Cheking.checking(dic_, text)

            select_action("1")

        elif text == "2":
            os.system('cls')
            value = text
            select_action(value)

        elif text == "3":
            os.system('cls')
            value = text
            select_action(value)

        elif text == "4":
            os.system('cls')
            value = text
            select_action(value)




    elif value == '2':
        os.system('cls')
        lst_choose = ['1', '3', '0','4']

        if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') != 0:
            read = openfile.OpenFile()

            dic_ = read.opening_json('dictionary.json')
            c = 1
            for i, j in dic_.items():
                print(f' {str(c) + ". "}{i}' + style.RESET_ALL + '  -> ' + f' {j}  ')
                c += 1
            print("""

[1] поиск в словаре
[3] меню
[4] изменение 
[0] выход
                                """)
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()

            while text.isdigit() and text not in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()



            # else:
            #     select_action(text)

            select_action(text)
        elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') == 0:
            print("Словарь пустой. выбирайте  [1]\n и создайте словарь")
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            select_action(text)

    elif value == '3':
        os.system('cls')
        b = menu.Menus.show_menu()
        select_action(b)

    elif value == '4':
        os.system('cls')
        lst_choose = ['2', '3', '0']

        print("""
[1] поиск в словаре
[2] посмотреть слова
[3] меню
[0] выход
                """)
        print("здесь вы можете изменить/удалить слова")


    elif value == '0':
        print("""
         ___ ДО СВИДАНИЯ___
                        """)
        exit()
    return text


a = menu.Menus.show_menu()
select_action(a)
