import openfile


class Menus:

    def __init__(self,text=""):
        self.text = text

    def select_action(self,te:str):



        lst = ['1', '2', '0']
        self.text = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
        while self.text not in lst:
            self.text = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()

        if self.text == '1':
            text_sel = input('\033[32m' + '\033[1m' + "Введите слово для перевода:-> ").lower().strip()
            return text_sel
        elif self.text == '2':
            read = openfile.OpenFile()
            print('\033[32m' + '\033[1m' + str(read.opening_json('dictionary.json')))
        elif self.text == '0':
            Menus.show_menu()
        print(self.text)

    def show_menu(self,te=""):
        self.text=""

        print('\033[33m' + '\033[1m' + "Welcome to my firt Dictionary")
        print("выбирайте из списка:")
        print("""
        [1] поиск в словаре
        [2] посмотреть записанные слова
        [0] меню
        """)
        self.select = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()

        return self.select

    def secound_menu(self=None):

        print("Файл пустой!")
        print("выбирайте из списка:")
        print("""
                [0] вернуться в меню

                    """)



if __name__ == "__main__":
    a = Menus()
    a.select_action(a.show_menu())


