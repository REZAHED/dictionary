# lst = []
# lst_suggest=[]
# def add_to_lst(value):
#     for i in lst_suggest:
#         if value not  in
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

def suggest(text, lst):



    # with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
    #     lines = [line.replace(" ", "").strip().split("\n") for line in file]
    #
    # for I in lines:
    #
    #     if i[0]:
    #         lst.append(i[0].lower().strip().replace("1", "").replace('2', '').replace('3', '')
    #                    .replace(":", "").replace("ё","е"))
    # text = input("введите: ").lower().strip()

    global ratio
    c = 0

    new_lst = []
    new_lst_choose=[]

    # for i in lst:
    #     if len(text) == len(i) :
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if c == len(text) or c == len(text) - 1:
    #             c = 0
    #
    #             new_lst.append(i)

    # for i in lst:
    #     if len(i) == len(text) :
    #         new_lst_choose.append(i)

    ratio = process.extract(text, lst, limit=20)
    for e in ratio:
        if e[1] > 50 and e[0][0] == text[0] and e[0][0] not in new_lst :
            new_lst.append(e[0])
    for e in ratio:
        if e[1] > 50 and e[0] not in new_lst:
            new_lst.append(e[0])
    new_lst_choose.clear()

    last_lst =[]
    # new_lst.clear()

    # for i in lst:
    #     if 8 <= len(text) == len(i) :
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3]  \
    #                 and text[5] == i[5]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
    #                 and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
    #                 and text[5] == i[6] and text[6] == i[6]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         else:
    #             c = 0
    #
    #     if 8 <= len(text) == len(i):
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
    #                 and text[5] == i[5]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
    #                 and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
    #                 and text[5] == i[5] and text[6] == i[6]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] \
    #                 and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
    #                 and text[5] == i[5] and text[6] == i[6]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         else:
    #             c = 0
    #     elif 5 <= len(text) <= len(i) < 8:
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if (c == len(text) or c == len(text) - 1) and len(i)==len(text) \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         if (c == len(text) or c == len(text) - 1) and len(i)==len(text)+1 \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] \
    #                 and text[2] == i[2] and text[3] == i[3]:
    #             c = 0
    #             new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[1] == i[1] \
    #                 and text[2] == i[2] and text[3] == i[3] and text[4] == i[4]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] \
    #                 and text[1] == i[1] and text[3] == i[3] and text[4] == i[4]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         elif c == len(text) or c == (len(text) - 1) or c == (len(text) - 2) \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[2] == i[2] and text[4] == i[4]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[1] == i[1] \
    #                 and text[-1] == i[-1]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #
    #         else:
    #             c = 0
    #     elif 3 <= len(text) == len(i):
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[1] == i[1]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[1] == i[1] and text[2] == i[2]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[2] == i[2]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[1] == i[1] and text[2] == i[2]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0] and text[1] == i[1] and text[2] == i[2]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         else:
    #             c = 0
    #     elif 3 <= len(text) == len(i) - 1:
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if c == len(text) \
    #                 and text[0] == i[0] and text[1] == i[1]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         elif c == len(text) \
    #                 and text[1] == i[1] and text[2] == i[2]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         else:
    #             c = 0
    #
    #     elif 3 <= len(text) == len(i) + 1:
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if c == len(text) - 1 \
    #                 and text[0] == i[0] and text[1] == i[1]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         else:
    #             c = 0
    #
    #     elif len(i) >= len(text) < 3:
    #         for j in list(text):
    #             if j in i:
    #                 c += 1
    #         if (c == len(text) or c == len(text) - 1) \
    #                 and text[0] == i[0]:
    #             c = 0
    #             if i not in new_lst:
    #                 new_lst.append(i)
    #         else:
    #             c = 0
    # count = 0
    #
    #     # ------------------------
    # for i in new_lst:
    #     for j in list(text):
    #         if len(text) >= 3 and j in i   :
    #             count += 1
    #     if (count == len(text)  or count== len(text)-1) and len(i) == len(text)\
    #             and i[0]==text[0] and i[-1] == text[-1] :
    #         last_lst.append(i)
    #         count=0
    #     else:
    #         count=0


    return new_lst
