import os
from mypcg import select
import menu


# os.system('mode con: cols=60 lines=10')

os.system('color')

text = ""
# dic_en_rus = {}


# функия для выбора из меню. работает с статическими методами в модули menu

a = menu.Menus.show_menu()
if a =='3':
    select.select_action('4')
else:
    select.select_action(a)