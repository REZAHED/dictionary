import openfile
import write_to_file

dic_en={}
class Cheking:

    @staticmethod
    def checking(dic,text):


        if dic is not None and text in dic.keys():
            print('\n' + f'перевод слово на русский: -> ' + '\033[31m' + '\033[1m' + dic[text])
            return True

        elif dic is not None and text in dic.values():
            for i, j in dic.items():
                if j == text:
                    print('\n' + f'перевод слово на английский: -> ' + '\033[31m' + '\033[1m' + i)
            return True

        elif dic is not None and text not in dic.keys() and text not in dic.values() :


            write_to = write_to_file.Write_To_File()
            print('\033[32m' + '\033[1m' + "Данное слово не найдено!! ")
            print("вы правильно написали? \n [+]ДА  [-]НЕТ :  -> ",end="")
            check =input().lower().strip()
            check_lst=["+", "-"]

            while check not in check_lst:
                check = input("введите ' + ' или ' - '   :-> ").lower().strip()


            if check == '+':
                print("\nВведите его значение \n для записи в словарь: -> ",end="")
                text_translate = input().lower().strip()
                while not text_translate.isalpha():
                    print("Введите правильное значение: -> ", end="")
                    text_translate = input().lower().strip()
                print('\033[34m' + write_to.dic_to_file(text, text_translate))




            elif check =="-":
                Cheking.choose()

    @staticmethod
    def choose():

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