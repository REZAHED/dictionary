import os

import menu
import select
# os.system('mode con: cols=60 lines=10')

os.system('color')

text = ""
# dic_en_rus = {}


# функия для выбора из меню. работает с статическими методами в модули menu

a=menu.Menus.show_menu()
b=select.select_action(a)


