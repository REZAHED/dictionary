import openfile

class Menus:


    @staticmethod
    def show_menu():


        print('\033[33m' + '\033[1m' + "Welcome to my firt Dictionary")
        print("выбирайте из списка:")
        print("""
        [1] поиск в словаре
        [2] посмотреть записанные слова
        [3] меню
        [0] выход
        """)

        select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()


        return select


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


