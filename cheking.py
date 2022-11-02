
import write_to_file


class Cheking:

    @staticmethod
    def checking(dic,text):

        if dic is not None and text in dic.keys():
            print('\n' + f'перевод слово на русский: -> ' + '\033[31m' + '\033[1m' + dic[text])

        elif dic is not None and text in dic.values():
            for i, j in dic.items():
                if j == text:
                    print('\n' + f'перевод слово на английский: -> ' + '\033[31m' + '\033[1m' + i)


        else:
            write_to = write_to_file.Write_To_File()
            print('\033[32m' + '\033[1m' + "Данное слово не найдено!! "
                                           "\nВведите его значение для записи в словарь: -> ",end="")
            text_translate = input().lower().strip()
            print('\033[34m' + write_to.dic_to_file(text, text_translate))

