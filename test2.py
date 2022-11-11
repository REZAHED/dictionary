import tkinter as tk
from tkinter.tix import Tk
from tkinter.ttk import Label

root = Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """سلام خوبی؟"""
Faxt_2 ="مرسی خوبم تو چطوری"

# Create button for next text.
b1 = tk.Button(root, text ="Next", command=lambda:  T.delete(tk.HIDDEN) )

# Create an Exit button.
b2 = tk.Button(root, text ="Exit",
               command = root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()


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


