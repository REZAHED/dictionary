import os

import colors
import openfile
import write_to_file
from mypcg import select


class Cheking:

    @staticmethod
    def checking(dic, text):
        lst=[]

        with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
            lines = [line.replace(" ","").strip().split("\n") for line in file]

        for i in lines:

            if i[0]:
                lst.append(i[0].lower().replace("1", "").replace('2', '').replace('3', '').replace(":",""))

        # print(lst)

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

            os.system('cls')
            if text.lower() not in lst:
                print('+++ это слово есть в вашем словаре\nно мы не нашли его в словаре русского языка')
                print("+--проверьте, может вы неправильно написали--+")

            print('\n' + f'перевод слово на русский: -> ' + '\033[31m' + '\033[1m' + dic[text])


        elif dic is not None and text in dic.values():

            os.system('cls')
            for i, j in dic.items():
                if j == text:
                    print('\n' + f'перевод слово на английский: -> ' + '\033[31m' + '\033[1m' + i)


        elif dic is not None and text not in dic.keys() and text not in dic.values():
            if text.lower() in lst:

                lst_choose = ['1', '3', '2', '0']
                write_to = write_to_file.Write_To_File()
                print("из словаря ")
                print('\033[32m' + '\033[1m' + "Данное слово не найдено!! ")
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
                    select.select_action("1")
            else:


                write_to = write_to_file.Write_To_File()
                print('\033[32m' + '\033[1m' + "Данное слово не найдено!! ")
                print("вы правильно написали? \n [+]ДА  [-]НЕТ :  -> ", end="")

                check = input().lower().strip()

                check_lst = ["+", "-"]
                lst_choose=['1','3' ,'2','0']
                # else:
                while check not in check_lst:
                    check = input("введите ' + ' или ' - '   :-> ").lower().strip()

                if check == '+':
                    print("\nВведите его значение \n для записи в словарь: -> ", end="")
                    text_translate = input().lower().strip()

                    while not text_translate.replace(" ",'').isalpha() and text_translate not in lst_choose:

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
            print(colors.style.RESET_ALL+"\n---Cловарь пустой---")
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

        print("введите еще раз правильное слово:  -> ", end="")
        right_word = input().lower().strip()
        while right_word =="":
            print("введите еще раз правильное слово:  -> ", end="")
            right_word = input().lower().strip()
        text = right_word
        read = openfile.OpenFile()
        dic = read.opening_json('dictionary.json')
        Cheking.checking(dic, text)
        # print("yyyyyyyyyyyyyy")
        # print("\nВведите его значение для записи в словарь: -> ", end="")
        # text_translate = input().lower().strip()
        # print('\033[34m' + write_to.dic_to_file(text, text_translate))

