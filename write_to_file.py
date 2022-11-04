import os

import colors
import openfile
import  json


class Write_To_File:
    os.system('cls')
    def __init__(self, a="" ,b=""):
        self.a=a
        self.b=b

    def dic_to_file(self,word, translate):
        self.a=word
        self.b=translate

        read = openfile.OpenFile()
        dic_en_rus = read.opening_json('dictionary.json')
        if dic_en_rus is not None:
            dic_en_rus.update({word: translate})
        else:
            dic_en_rus = {word: translate}
        with open('dictionary.json', 'r+', encoding='utf-8-sig') as file:
            json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
            os.system('cls')
        return colors.fg.YELLOW+ f'Слово --{word.upper()}-- и его значение --{translate.upper()}-- успешно сохранены.'