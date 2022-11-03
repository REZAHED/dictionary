import json
import os
import menu
import openfile
from colors import fg, style
import cheking
from tabulate import tabulate
# os.system('mode con: cols=60 lines=10')

os.system('color')

text = ""
# dic_en_rus = {}


# функия для выбора из меню. работает с статическими методами в модули menu
def select_action(value):

    global text
    lst = ['1', '2', '0', '3','4','\\','/','%']
    while value not in lst:
        value = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

    if value == '1' or value == '\\':
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

        elif text == "1" or text =='\\':
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

        elif text == "3" or text == '/':
            os.system('cls')
            value = text
            select_action(value)

        elif text == "4":
            os.system('cls')
            value = text
            select_action(value)




    elif value == '2':
        os.system('cls')
        lst_choose = ['1', '3', '0','4','\\','/']

        if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') != 0:
            read = openfile.OpenFile()

            dic_ = read.opening_json('dictionary.json')

            c = 1
            m = 1
            d= 1
            head = ["№","Слово", "Перевод"]
            lst_dic=[]
            lst_copy=[]
            lst_dicbig=[]
            # for i in range(len(dic_)):

            for i, j in dic_.items():
                lst_dic.append(str(c))
                lst_dic.append(i)
                lst_dic.append(j)
                lst_copy=lst_dic.copy()
                lst_dicbig.append(lst_copy)
                lst_dic.clear()
                # print(style.RESET_ALL+ fg.YELLOW+f'{str(c) + ". "}{i}' + style.RESET_ALL + '->' + f'{j}  '.rjust(20))
                c += 1

            # for i in lst_dicbig:



            print(style.RESET_ALL+fg.YELLOW +tabulate(lst_dicbig,tablefmt="grid",)+style.RESET_ALL)
                # m += 1
                # d += 1
            #     m += 1
            #     if m==20:
            #
            #         print(f"---------------всего {len(dic_)} слов--------------------")
            #         print("нажмите на ENTER чтобы увидеть остальные ")
            #         #
            #         enter = input( )
            #         m=1
            print(f"---------------всего {len(dic_)} слов--------------------")

            print(f"-------Для изменение/удаление выберите номер слова-------")
            print("""

[\] поиск в словаре
[/] меню
[0] выход
                                """)
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            if text =='\\' or text== '/' or text == '0':
                os.system('cls')
                select_action(text)
            elif text.isdigit():
                for i in lst_dicbig:
                    if str(text) in i:
                        print(style.RESET_ALL+ fg.YELLOW+f'[1] изменить {i[1].upper()} ')
                        print(f'[2] изменить {i[2].upper()}')

                        print(style.RESET_ALL+ fg.YELLOW+f'[3] удалить запись #{text}.  {i[1]}'.upper()+ f' : {i[2].upper()}')
                        text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
                        if text == '1':
                            print("pass")
                        elif text =='2':
                            pass
                        elif text == '3':
                             del dic_[i[1]]
                             print(dic_)
                             with open('dictionary.json', 'w+', encoding='utf-8-sig') as file:
                                json.dump(dic_, file, indent=2, ensure_ascii=False)
                                os.system('cls')
                             # print(f'Слово --{i[1]}-- и его значение --{i[2]}-- успешно удалены.')
                             select_action("2")


            # while text.isdigit() and text not in lst_choose:
            #     text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()



            # else:
            #     select_action(text)


        elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') == 0:
            print("Словарь пустой. выбирайте  [1]\n и создайте словарь")
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            select_action(text)

    elif value == '3' or value == '/':
        os.system('cls')
        b = menu.Menus.show_menu()
        select_action(b)

    elif value == '4':
        os.system('cls')
        lst_choose = ['1','2', '3', '0']
        print("здесь вы можете изменить/удалить слова")


        select_action("2")
        print("""
[+] изменить
[-] удалить

                        """)

        print("""
[1] поиск в словаре
[2] посмотреть слова
[3] меню
[0] выход
                """)



    elif value == '0':
        print("""
         ___ ДО СВИДАНИЯ___
                        """)
        exit()
    return text


a = menu.Menus.show_menu()
select_action(a)
