import json
import os
import menu
import openfile



text=""
dic_en_rus = {}



# if __name__ == "__main__":



#
def dic_to_file(word, translate):

    read = openfile.OpenFile()
    dic_en_rus = read.opening_json('dictionary.json')
    print("уже здесь")
    print(dic_en_rus)
    if dic_en_rus is not None:
        dic_en_rus.update({word: translate})
    else:
        dic_en_rus={word: translate}
    with open('dictionary.json', 'r+', encoding='utf-8') as file:
        json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
    return f'слово {word.upper()} и его значение {translate.upper()} успешно сохранены.'

#

def checking(dic):

    if dic is not None and text in dic.keys():
        print('\n' + f'перевод слово на русский: -> ' + '\033[31m' +'\033[1m' + dic[text])
        select_action("1")
    elif dic is not None and text  in dic.values():
        for i, j in dic.items():
            if j == text:
                print('\n' + f'перевод слово на русский: -> ' + '\033[31m' +'\033[1m' + i)
                select_action("1")

    else :
        print('\033[32m'+"Данное слово не найдено!! \nВведите его значение для записи в словарь:")
        text_translate = input().lower().strip()
        print('\033[34m'+dic_to_file(text,text_translate))
        select_action("1")

    # elif dic is not None and text not in dic.items():
    #     print('\033[32m'+"Данное слово не найдено!! \nВведите его значение для записи в словарь:")
    #     text_translate = input().lower().strip()
    #     print('\033[34m'+dic_to_file(text,text_translate))
#
#
# if os.path.exists('dictionary.json'):
#     meny=menu.Menus()
#     meny.show_menu()
# else:
#     print("создал файл")
#     file = open('dictionary.json', 'a+', encoding='utf-8-sig')
#     file.close()
#     menu.Menus.show_menu()
#
#
# read = openfile.OpenFile()
# print("я здесь")
# if read.opening_read('dictionary.json'):
#     dic_en_rus = read.opening_json('dictionary.json')
#     checking(dic_en_rus)
# else:
#     print("словарь пустой\n" + f'Введите значение слово {text} для записи в словарь:')
#     translate = input().lower().strip()
#     print(menu.Menus().select_action())
#     print(dic_to_file(menu.Menus().select_action(), translate))


# функия для выбора из меню. работает с статическими методами в модули menu
def select_action(value):
    global text
    lst = ['1', '2', '0','3']
    while value not in lst:
        value = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()
    if value == '1':
        print("""

                        [2] посмотреть записанные слова
                        [3] меню
                        [0] выход
                        """)
        if os.path.exists('dictionary.json'):
             text = input('\033[32m' + '\033[1m' + "Введите слово для перевода"
                                                  " или выбирайте из меню :-> ").lower().strip()
        else:
            print("новый файл создан")
            file = open('dictionary.json', 'a+', encoding='utf-8-sig')
            file.close()
            print("Файл пустой!")
            text = input('\033[32m' + '\033[1m' + "Введите слово для перевода"
                                                      " или выбирайте из меню :-> ").lower().strip()

        if text == "0":
            exit()
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
        pass
        # read = openfile.OpenFile()
        # print('\033[32m' + '\033[1m' + str(read.opening_json('dictionary.json')))
    elif value == '3':
        a= menu.Menus.show_menu()
        select_action(a)

    elif value  == '0':

        exit()
    return text
a = menu.Menus.show_menu()
select_action(a)




    

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
