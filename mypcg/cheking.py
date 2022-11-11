import os

import colors
import fonts
import openfile
import write_to_file
from mypcg import select, test
import arabic_reshaper
from bidi.algorithm import get_display
from arabic_reshaper import ArabicReshaper


class Cheking:

    @staticmethod
    def checking(dic, text):

        # lst_choose = ['1', '3', '2', '0']
        # write_to = write_to_file.Write_To_File()
        # print("из словаря " )
        # print('\033[32m' + '\033[1m' + "Данное слово не найдено!! ")
        # print("\nВведите его значение \n для записи в словарь: -> ", end="")
        # text_translate = input().lower().strip()
        # while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
        #     print("Введите правильное значение: -> ", end="")
        #     text_translate = input().lower().strip()
        #     os.system('cls')
        # if text_translate in lst_choose:
        #     os.system('cls')
        #     select.select_action(text_translate)
        # else:
        #     print('\033[34m' + write_to.dic_to_file(text, text_translate))
        #     select.select_action("1")

        if dic is not None and text in dic.keys():
            alpha_en = 'abcdefghijklmnopqrstuvwxyz'
            alpha_farsi = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            os.system('cls')
            # if text.lower() not in lst:
            #     print('+++ это слово есть в вашем словаре\nно мы не нашли его в словаре русского языка')
            #     print("+--проверьте, может вы неправильно написали--+")
            c = 0
            alph_text = ''
            for i in alpha_en:
                if i in dic[text]:
                    c += 1
            if c >= 1:
                alph_text = 'Английский'
                c = 0
            else:
                c = 0
                for i in alpha_farsi:
                    if i in dic[text]:
                        c += 1
                if c >= 1:
                    alph_text = 'Персидский'
                    c = 0
                else:
                    c = 0
                    alph_text = "Русский"
            #-----------чтобы можно было фарси писать и ситать в cmd
            #-------------------------------------------------------
            reshaped = arabic_reshaper.reshape(dic[text])
            bidi_tex = get_display(reshaped)
            #______________________________________________

            print('\n' + f'перевод слово на {alph_text}: -> ' + '\033[31m' + '\033[1m' + bidi_tex)





            # print(reshaped_text[::-1])




            for i, j in dic.items():
                if j == dic[text] and i != text:
                    for e in alpha_en:
                        if e in i:
                            c += 1
                    if c >= 1:
                        alph_text = 'Английский'
                        c = 0
                    else:
                        c = 0
                        for e in alpha_farsi:
                            if e in i:
                                c += 1
                        if c >= 1:
                            alph_text = 'Персидский'
                            c = 0
                        else:
                            c = 0
                            alph_text = "Русский"
                    print('\n' + f'перевод слово на {alph_text}: -> ' + '\033[31m' + '\033[1m' + i)

        elif dic is not None and text in dic.values():
            alpha_en = 'abcdefghijklmnopqrstuvwxyz'
            alpha_farsi = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            c = 0
            os.system('cls')
            for i, j in dic.items():
                if j == text:
                    for e in alpha_en:
                        if e in i:
                            c += 1
                    if c >= 1:
                        alph_text = 'Английский'
                        c = 0
                    else:
                        c = 0
                        for e in alpha_farsi:
                            if e in i:
                                c += 1
                        if c >= 1:
                            alph_text = 'Персидский'
                            c = 0
                        else:
                            c = 0
                            alph_text = "Русский"
                    reshaped = arabic_reshaper.reshape(i)
                    bidi_tex = get_display(reshaped)
                    print('\n' + f'перевод слово на {alph_text}: -> ' + '\033[31m' + '\033[1m' + bidi_tex)

        elif dic is not None and text not in dic.keys() and text not in dic.values():

            # lst = []
            #
            #
            # if not lst:
            # print(lst)

            with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
                if len(text) == 1:
                    lines = {line.rstrip() for line in file.readlines() if len(line.rstrip()) == 1}

                elif len(text) == 2:
                    lines = {line.rstrip() for line in file.readlines() if len(line.rstrip()) == 2}
                elif len(text) >= 3:
                    lines ={line.rstrip() for line in file.readlines()
                            if len(line.rstrip()) == len(text)+1
                            or len(line.rstrip())==len(text)}


            # print(lines)
            # for i in lines:
            #
            #     if i[0]:
            #         lst.append(i[0].lower())

            # print(lst)
            # lines.clear()
            # lst_to_set = set(lst)
            if text.lower() in lines:

                lst_choose = ['1', '3', '2', '0']
                write_to = write_to_file.Write_To_File()

                print('\033[32m' + '\033[1m' + "Данное слово не найдено!! ")
                print("\nВведите его значение \n для записи в словарь: -> ", end="")
                text_translate = input().lower().strip()
                while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
                    print("Введите правильное значение или :\n выберите [1][2][3][0] -> ", end="")
                    text_translate = input().lower().strip()
                    os.system('cls')
                if text_translate in lst_choose:
                    os.system('cls')
                    select.select_action(text_translate)
                else:
                    print('\033[34m' + write_to.dic_to_file(text, text_translate))
                    select.select_action("1")
            else:

                write_to = write_to_file.Write_To_File()
                print("этого слова нет в словаре русского языка")

                suggest_lst = test.suggest(text, lines)

                lines.clear()

                if suggest_lst:
                    print(colors.fg.YELLOW + 'предложения :', end="")

                    # c = 0
                    for i in range(len(suggest_lst)):
                        # for j in list(text):
                        #     if j in suggest_lst[i]:
                        #         c+=1
                        # if c== len(text)  :

                        #         or len(text) == len(suggest_lst[i]) + 1 :
                        #     c=0
                        #     print(suggest_lst[i])
                        #     print(list(text))
                        # else:
                        #     c=0
                        #     suggest_lst.pop(i)
                        print(f' {i + 1}.{suggest_lst[i]}', end='' + colors.style.RESET_ALL)

                        if i == 9:
                            break

                else:
                    suggest_lst.clear()
                    print(colors.fg.RED + "Данное слово не найдено!! ")
                print("\nвы правильно написали? \n[+]ДА  [-]НЕТ :  -> ", end="")

                check = input().lower().strip()

                check_lst = ["+", "-"]
                lst_choose = ['1', '3', '2', '0']
                # else:
                while check not in check_lst and check not in lst_choose:
                    check = input("введите ' + ' или ' - '   :-> ").lower().strip()
                if check in lst_choose:
                    select.select_action(check)
                if check == '+':
                    print("\nВведите его значение \n для записи в словарь: -> ", end="")
                    text_translate = input().lower().strip()

                    while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
                        print("Введите правильное значение: -> ", end="")
                        text_translate = input().lower().strip()
                        os.system('cls')
                    if text_translate in lst_choose:
                        os.system('cls')
                        select.select_action(text_translate)
                    else:
                        print('\033[34m' + write_to.dic_to_file(text, text_translate))

                elif check == "-":
                    Cheking.choose()
        elif dic is None:
            write_to = write_to_file.Write_To_File()
            lst_choose = ['1', '3', '2', '0']
            print(colors.style.RESET_ALL + "\n---Cловарь пустой---")
            print("\nВведите его значение \nдля записи в словарь: -> ", end="")
            text_translate = input().lower().strip()
            if text_translate in lst_choose:
                os.system('cls')
                select.select_action(text_translate)
            else:
                print('\033[34m' + write_to.dic_to_file(text, text_translate))
                select.select_action("1")

    @staticmethod
    def choose():
        lst_choose = ['1', '3', '2', '0']
        print("введите еще раз правильное слово:  -> ", end="")
        right_word = input().lower().strip()
        while right_word == "":
            print("введите еще раз правильное слово:  -> ", end="")
            right_word = input().lower().strip()
        if right_word in lst_choose:
            select.select_action(right_word)
        text = right_word
        read = openfile.OpenFile()
        dic = read.opening_json('dictionary.json')
        Cheking.checking(dic, text)
        # print("yyyyyyyyyyyyyy")
        # print("\nВведите его значение для записи в словарь: -> ", end="")
        # text_translate = input().lower().strip()
        # print('\033[34m' + write_to.dic_to_file(text, text_translate))
