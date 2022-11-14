import json
import sys
import os
from time import sleep

import write_to_file
from tabulate import tabulate
import colors
import menu
import openfile
from mypcg import cheking
from colors import fg, style

text = ""


def select_action(value, arg=''):
    global text
    lst = ['1', '2', '0', '3', '4', '\\', '/', "-"]
    while value not in lst:
        value = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        #########################################################
        #########################################################

    if value == '1' or value == '\\':
        os.system('cls')
        lst_choose = ['1', '2', '3', '4', '0']
        lst_menu = [["""
[1] искать в словаре        
[2] посмотреть слова  
[3] меню
[4] онлайн поиск
[0] выход
        """]]
        print(style.RESET_ALL + fg.YELLOW + tabulate(lst_menu, tablefmt="grid", )
              + style.RESET_ALL)

        lst_input = [["Введите слово для перевода  \nили выбирайте из меню :   "]]
        print(style.RESET_ALL + fg.CYAN + tabulate(lst_input, tablefmt="grid", )
              + style.RESET_ALL + '\n')
        if arg:
            print(style.RESET_ALL + fg.RED + arg + style.RESET_ALL + '\n')
        text = input("---> ").lower().strip()
        while text.isdigit() and text not in lst_choose or text == "":
            os.system('cls')
            select_action("1", "**введите правильный номер** ")

        # sign = ['-', '+', '_', '.', '?']
        if not text.replace(" ", "").replace("-", "").replace(",", "").isalpha() \
                and text.replace(" ", "").replace("-", "") not in lst_choose:
            os.system("cls")
            select_action("1", "**введите правильно**")

        elif text.replace(" ", "").replace("-", "").replace(",", "").replace(".", '').isdigit() \
                and text.replace(" ", "").replace("-", "").replace(",", "").replace(".", '') in lst_choose:
            value = text
            select_action(value)

        elif text.replace(" ", "").replace("-", "").replace(",", "").isalpha():

            read = openfile.OpenFile()
            dic_ = read.opening_json('dictionary.json')
            cheking.Cheking.checking(dic_, text)

            select_action("1")

            #########################################################
            #########################################################
            #########################################################
            #########################################################

    elif value == '2':

        os.system('cls')
        lst_choose = ['1', '3', '2', '\\', '/']

        read = openfile.OpenFile()
        dic_ = read.opening_json('dictionary.json')

        if dic_ is not None:

            read = openfile.OpenFile()
            dic_ = read.opening_json('dictionary.json')
            c = 1
            head = ["№", "Слово ", "Перевод  "]
            lst_dic = []
            lst_dicbig = []

            for i, j in dic_.items():
                lst_dic.append(str(c))
                lst_dic.append(i)
                lst_dic.append(j)
                lst_copy = lst_dic.copy()
                lst_dicbig.append(lst_copy)
                lst_dic.clear()
                c += 1

            print(style.RESET_ALL + fg.YELLOW +
                  tabulate(lst_dicbig, headers=head, tablefmt="grid", )
                  + style.RESET_ALL + '\n')

            lst_info = [["-------всего" + style.RESET_ALL + fg.YELLOW + f" {len(dic_)} "
                         + style.RESET_ALL + fg.WHITE + "слов------\n"],
                        [style.RESET_ALL + fg.RED + f"+--Для изменение/удаление--+\n"],
                        [style.RESET_ALL + fg.WHITE + f"+--выберите номер слова--+"]]

            print(style.RESET_ALL + fg.WHITE +
                  tabulate(lst_info, tablefmt="grid", )
                  + style.RESET_ALL)

            lst_menu = [["""
            
[\\] поиск в словаре         
[/] меню
[-] удалить словарь
[0] выход
                                """]]
            print(style.RESET_ALL + fg.YELLOW + tabulate(lst_menu, tablefmt="grid", )
                  + style.RESET_ALL)

            if arg:
                print(style.RESET_ALL + fg.RED + arg + style.RESET_ALL + '\n')

            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            while text == "" or text.isalpha():
                os.system("cls")
                select_action("2", "**введите правильное значение**")

            if text == '\\' or text == '/':
                os.system('cls')
                select_action(text)
            elif text == "0":
                select_action(text)

            elif text == "-":
                print("вы действительно хотите удалить словарь?\n"
                      "[да][нет] ваш выбор ->", end="")

                delete_dic = input()
                if delete_dic.lower() == "да":
                    dic_.clear()
                    with open('dictionary.json', 'w+', encoding='utf-8-sig') as file:
                        json.dump(dic_, file, indent=2, ensure_ascii=False)
                        os.system('cls')
                    # print(f'Слово --{i[1]}-- и его значение --{i[2]}-- успешно удалены.')
                    select_action("2", f'Словарь успешно удален')
                elif delete_dic.lower() == "нет":
                    select_action("2", f'удаление отменено')
                else:
                    select_action("2", f'вы не правильно выбрали.\nпопробуйте еще раз')

            elif text.isdigit():
                if int(text) <= len(dic_):
                    for i in lst_dicbig:
                        if str(text) in i:
                            print(style.RESET_ALL + fg.YELLOW + f'[1] изменить {i[1].upper()} ')
                            print(f'[2] изменить {i[2].upper()}')

                            print(
                                style.RESET_ALL + fg.YELLOW + f'[3] удалить запись'
                                                              f' #{text}.  {i[1]}'.upper() + f' : {i[2].upper()}')
                            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
                            while text == "" and not text.isdigit() and text not in lst_choose:
                                text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
                            if text == '/' or text == '\\':
                                os.system('cls')
                                select_action(text)
                            if text == '1':

                                new_word = input('\033[32m' + '\033[1m' + "введите новый вариант:-> ").lower().strip()

                                while new_word == "" and new_word not in lst_choose:
                                    new_word = input(
                                        '\033[32m' + '\033[1m' + "введите новый вариант:-> ").lower().strip()
                                if new_word in lst_choose:
                                    select_action(new_word)
                                for word in lst_dicbig:

                                    if new_word == word[1]:
                                        select_action("2", f" слово {new_word.upper()} уже"
                                                           f" существует в словаре № {word[0]}"
                                                           f" \n со значением {word[2].upper()}")
                                        break

                                else:
                                    del dic_[i[1]]

                                dic_.update({new_word: i[2]})
                                lst_dicbig.clear()
                                write_to_file.Write_To_File().updat(dic_)
                                os.system('cls')
                                select_action("2", f'запись  {i[1]}'.upper() + f' изменена на {new_word.upper()}')

                            elif text == '2':

                                new_word = input('\033[32m' + '\033[1m' + "введите новый вариант:-> ").lower().strip()
                                dic_.update({i[1]: new_word})
                                write_to_file.Write_To_File().updat(dic_)
                                os.system('cls')
                                select_action("2", f'запись  {i[2]}'.upper() + f' изменена на {new_word.upper()}')

                            elif text == '3':
                                del dic_[i[1]]
                                write_to_file.Write_To_File().updat(dic_)
                                os.system('cls')
                                select_action("2", f'запись  {i[1]}'.upper() + f' : {i[2].upper()} удалена')

                            elif text not in lst_choose:
                                select_action('2', 'такого номера нет!')

                else:

                    select_action('2', 'такого номера нет!')

        elif dic_ is None:
            print("Словарь пустой. выбирайте  [1]\n и создайте словарь")
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> " + colors.style.RESET_ALL).lower().strip()
            select_action(text)

            #########################################################
            #########################################################

    elif value == '3' or value == '/':

        os.system('cls')
        b = menu.Menus.show_menu()
        if b == '3':
            select_action('4')
        else:
            select_action(b)


            #########################################################
            #########################################################
    elif value == '4':

        lst_menu = [["Здесь можете искать слова\nв гугле переводчике"],
                    ["""
[1] поиск в словаре
[2] посмотреть слова
[3] меню
[0] выход
                """]
                    ]

        print(style.RESET_ALL + fg.YELLOW + tabulate(lst_menu, tablefmt="grid", )
              + style.RESET_ALL)
        lst_choose = ['1', '2', '3', '0', '4']

        text = input("введите слово ->: ")
        while not text.replace(" ", "").isalpha() and text not in lst_choose:
            text = input("введите правильное слово ->: ")
        if text in lst_choose:
            if text == '0':
                select_action(text)
            else:
                os.system('cls')
                select_action(text)
        elif text.replace(" ", "").replace("-", "").isalpha():

            read = openfile.OpenFile()
            dic_ = read.opening_json('dictionary.json')
            cheking.Cheking.checking(dic_, text, online=1)
            select_action("4")

            #########################################################
            #########################################################

    elif value == '0':

        lst = [['___ ДО СВИДАНИЯ___']]
        input("enter to exit")
        print("подождите.....")
        sleep(1)
        print("сохраняем данные....")
        sleep(1)
        print("------", end="")
        print("-----------------")
        sleep(1)
        print(style.RESET_ALL + fg.YELLOW + tabulate(lst, tablefmt="grid", ) + style.RESET_ALL)
        sys.exit()
    return text
