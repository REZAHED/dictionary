import os

from tabulate import tabulate

from colors import fg,bg,style

 # class bcolors:
 #    HEADER = '\033[95m'
 #    OKBLUE = '\033[94m'
 #    OKCYAN = '\033[96m'
 #    OKGREEN = '\033[92m'
 #    WARNING = '\033[93m'
 #    FAIL = '\033[91m'
 #    ENDC = '\033[0m'
 #    BOLD = '\033[1m'
 #    UNDERLINE = '\033[4m'

class Menus:


    @staticmethod
    def show_menu(value=None):
        lst_choose=['1','2','3','0']
        lst_welcom = [["---- Welcome to my first Dictionary -----         "]]
        print(style.RESET_ALL + fg.WHITE + tabulate(lst_welcom, tablefmt="grid", ) + style.RESET_ALL)


        lst = [[" выбирайте из списка: "],[""" 
[1] поиск в словаре
[2] посмотреть слова\\изменить или удалить
[3] онлайн поиск
[0] выход
"""]]
        print(style.RESET_ALL + fg.YELLOW + tabulate(lst, tablefmt="grid", ) + style.RESET_ALL)

        # print(style.RESET_ALL+)
        if not value:
            text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            while text not in lst_choose:
                text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()
            if text =='0':
                return text
            else:
                os.system('cls')

                return text

        os.system('cls')
        return value


    # @staticmethod
    # def secound_menu():
    #
    #     print("Файл пустой!")
    #     print("выбирайте из списка:")
    #     print("""
    #             [2] посмотреть записанные слова
    #             [3] вернуться в меню
    #             [0] выход
    #                 """)
    #     select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
    #
    #     return select

    #
    # @staticmethod
    # def third_menu():
    #
    #
    #
    #     select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
    #
    #     return select



# if __name__ == "__main__":
#     a = Menus()
#     a.select_action(a.show_menu())


