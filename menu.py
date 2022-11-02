import openfile
import colors

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
    def show_menu(value=""):
        # print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
        print(colors.fg.YELLOW + "Welcome to my firt Dictionary")
        print("выбирайте из списка:")
        print( colors.style.RESET_ALL+""" 
        [1] поиск в словаре
        [2] посмотреть записанные слова
        [0] выход
        """)
        if not value:
            select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
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


    @staticmethod
    def third_menu():



        select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()

        return select



# if __name__ == "__main__":
#     a = Menus()
#     a.select_action(a.show_menu())


