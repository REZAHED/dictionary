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
        lst_choose=['1','2','0','4']
        print(fg.YELLOW + "Welcome to my first Dictionary")
        print("выбирайте из списка:")
        print(style.RESET_ALL+""" 
[1] поиск в словаре
[2] посмотреть слова
[4] изменение
[0] выход
""")
        if not value:
            select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
            while select.isdigit() and select not in lst_choose:
                select = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()
            return select

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


