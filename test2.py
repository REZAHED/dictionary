import json
from tqdm import tqdm
import httpcore
from googletrans import Translator

with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file.readlines()]

dic_ru_fa = {}
c = 0
d = 1
# Updated Answer as of 2021 Sept
#
# pip uninstall googletrans==4.0.0-rc1
#
# pip install googletrans==3.1.0a0
# The 3.1.0a0 version works with bulk translation too!

translator = Translator()

try:
    # dt = translator.detect(text)
    TEST = translator.translate('hi',dest='fa')
    print("соединение с интерненом проведено успешно")

except:
    httpcore._exceptions.ConnectError()
    print("нет интернета")
else:

    for i in tqdm(range(len(lines)),ncols=100):

        st = translator.translate(lines[i],src='ru', dest='en')
        dic_ru_fa[lines[i]] = st.text
        c += 1

        d += 1


        if c == 500:
            with open('translate_ru_en.json', 'r+', encoding='utf-8-sig') as file:
                json.dump(dic_ru_fa, file, indent=2, ensure_ascii=False)
            c = 0






# with open("ENRUS.TXT" , 'r' , encoding='utf-8') as file:
#
#         lines =[line.rstrip() for line in file]
# lst = []
# for i in range(0,len(lines)-1):
#     lst.append([lines[i],lines[i+1]])
#
# text = input("веддите: ")
# for i in lst:
#     if text.lower() == i[0]:
#         print(i[1])
#     elif  text.lower() == i[1]:
#         print(i[0])


# lines=[]
# c=0
# d=0
#
# while c<50:
#     with open("engwords.txt", 'r', encoding='utf-8') as file:
#         for line in file:
#             c+=1
#             lines.append(file.readline().rstrip())
#             if c == 50:
#                 with open(f"newdic{d}.txt", 'w+', encoding='utf-8') as file:
#                     for i in lines:
#                         file.write(i + '\n')
#
#                 lines.clear()
#                 c=0
#                 d+=1
                #



# print(len(lines))
# print(lines)
# import tkinter as tk
# from tkinter.tix import Tk
# from tkinter.ttk import Label
#
# root = Tk()
#
# # specify size of window.
# root.geometry("250x170")
#
# # Create text widget and specify size.
# T = tk.Text(root, height = 5, width = 52)
#
# # Create label
# l = Label(root, text = "Fact of the Day")
# l.config(font =("Courier", 14))
#
# Fact = """سلام خوبی؟"""
# Faxt_2 ="مرسی خوبم تو چطوری"
#
# # Create button for next text.
# b1 = tk.Button(root, text ="Next", command=lambda:  T.delete(tk.HIDDEN) )
#
# # Create an Exit button.
# b2 = tk.Button(root, text ="Exit",
#                command = root.destroy)
#
# l.pack()
# T.pack()
# b1.pack()
# b2.pack()
#
# # Insert The Fact.
# T.insert(tk.END, Fact)
#
# tk.mainloop()


# from fuzzywuzzy import process
#
# lst = ["котенок", "цап", "пацр",'царь','а','пацан','пайка', 'пока','пачка','палка','папка','парк','паек','паша','паук']
# text = 'search'
# lst2=[]
#
# for i in lst:
#     if len(i) == len(text) or len(i) == len(text) +1:
#         lst2.append(i)
#
# Ratio = process.extractOne(text,lst2)
# print(Ratio[0])
# print(Ratio[1])
#
# Ratio2 = process.extract(text,lst2)
# for e in Ratio2:
#     print(e[0])
#     print(e[1])
#
# new = "-"
# if new.isspace():
#     print("yes")




# with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:


