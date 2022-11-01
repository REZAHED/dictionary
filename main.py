import json
import os
import menu
import openfile



text=""
dic_en_rus = {}



# if __name__ == "__main__":




def dic_to_file(word, translate):
    dic_en_rus.update({word: translate})
    with open('dictionary.json', 'r+', encoding='utf-8') as file:
        json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
    return f'слово {word.upper()} и его значение {translate.upper()} успешно сохранены.'


def checking(dic):
    if text in dic.keys():
        print('\n' + f'перевод слово на русский: -> ' + '\033[31m' +'\033[1m' + dic[text])

    else:
        print('\033[32m'+"Данное слово не найдено!! \nВведите его значение для записи в словарь:")
        text_translate = input().lower().strip()
        print('\033[34m'+dic_to_file(text, text_translate))


if os.path.exists('dictionary.json'):
    meny=menu.Menus()
    meny.show_menu()
else:
    print("создал файл")
    file = open('dictionary.json', 'a+', encoding='utf-8-sig')
    file.close()
    menu.Menus.show_menu()


read = openfile.OpenFile()
print("я здесь")
if read.opening_read('dictionary.json'):
    dic_en_rus = read.opening_json('dictionary.json')
    checking(dic_en_rus)
else:
    print("словарь пустой\n" + f'Введите значение слово {text} для записи в словарь:')
    translate = input().lower().strip()
    print(menu.Menus().select_action())
    print(dic_to_file(menu.Menus().select_action(), translate))



    

# dic = {'hello': 'привет', 'bye': 'пока'}
#
#
#
# def getvalue(dic, value):
#     for i, j in dic.items():
#         if j == value:
#             return i
#
# print(getvalue(dic,'привет'))
