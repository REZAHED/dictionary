import json
import os
import menu
import openfile
import colors
os.system('color')

text=""
dic_en_rus = {}

#
def dic_to_file(word, translate):

    read = openfile.OpenFile()
    dic_en_rus = read.opening_json('dictionary.json')
    if dic_en_rus is not None:
        dic_en_rus.update({word: translate})
    else:
        dic_en_rus={word: translate}
    with open('dictionary.json', 'r+', encoding='utf-8-sig') as file:
        json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
    return f'Слово --{word.upper()}-- и его значение --{translate.upper()}-- успешно сохранены.'

#

def checking(dic):

    if dic is not None and text in dic.keys():
        print('\n' + f'перевод слово на русский: -> ' + '\033[31m' +'\033[1m' + dic[text])
        select_action("1")
    elif dic is not None and text  in dic.values():
        for i, j in dic.items():
            if j == text:
                print('\n' + f'перевод слово на фарси: -> ' + '\033[31m' +'\033[1m' + i)
                select_action("1")

    else :
        print('\033[32m' + '\033[1m'+"Данное слово не найдено!! \nВведите его значение для записи в словарь:")
        text_translate = input().lower().strip()
        print('\033[34m'+dic_to_file(text,text_translate))
        select_action("1")


# функия для выбора из меню. работает с статическими методами в модули menu
def select_action(value):
    global text
    lst = ['1', '2', '0','3']
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
             text = input(colors.fg.CYAN + "Введите слово для перевода"
                                                  " или выбирайте из меню :-> " + colors.style.RESET_ALL).lower().strip()
             while not text in lst_choose:
                 text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        else:
            print("новый файл создан")
            file = open('dictionary.json', 'a+', encoding='utf-8-sig')
            file.close()
            text = input('\033[32m' + '\033[1m' + "Введите слово для перевода"
                                                      " или выбирайте из меню :-> ").lower().strip()
            while not text in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        if text == "0":
            exit()
        elif text == "2":
            lst_choose=['1','3','0']
            print("""

                                            [1] поиск в словаре
                                            [3] меню
                                            [0] выход
                                            """)
            if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') != 0:
                read = openfile.OpenFile()
                dic_en_rus = read.opening_json('dictionary.json')
                for i, j in dic_en_rus.items():
                    print(colors.fg.GREEN+f' {i}' + colors.style.RESET_ALL + ' -> ' + f' {j}  ')

                text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
                while not text in lst_choose:
                    text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

                else:
                    select_action(text)
            elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') == 0:
                print("Словарь пустой. выбирайте пункт [1] и создайте словарь")
                text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
                select_action(text)


        elif text == "1":
            lst_choose = ['2', '3', '0']
            print("""

                                    [2] посмотреть записанные слова
                                    [3] меню
                                    [0] выход
                                    """)
            text = input(colors.fg.CYAN + "Введите слово для перевода"
                                          " или выбирайте из меню :-> " + colors.style.RESET_ALL).lower().strip()
            while not text in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

            else:
                select_action(text)
            select_action(text)
        elif text != "0" and text in lst:
            a = menu.Menus.show_menu()
            select_action(a)
        elif text.isalpha():
            read=openfile.OpenFile()
            dic_en_rus = read.opening_json('dictionary.json')
            checking(dic_en_rus)


        elif text not in lst:
            a = menu.Menus.show_menu()
            select_action(a)
        # select_action(menu.Menus.show_menu())
    elif value == '2':
        lst_choose = ['1', '3', '0']
        print("""

                                [1] поиск в словаре
                                [3] меню
                                [0] выход
                                """)
        if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') !=0:
            read = openfile.OpenFile()

            dic_en_rus = read.opening_json('dictionary.json')
            for i,j in dic_en_rus.items():
                print(f' {i}' +  colors.style.RESET_ALL+' -> '+  f' {j}  ')
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            while not text  in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

            else:
                select_action(text)

        elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') ==0:
            print("Словарь пустой. выбирайте пункт [1] и создайте словарь")
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            select_action(text)

    elif value == '3':
        a= menu.Menus.show_menu()
        select_action(a)

    elif value  == '0':

        exit()
    return text
a = menu.Menus.show_menu()
select_action(a)




    

