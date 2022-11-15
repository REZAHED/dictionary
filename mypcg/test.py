
from fuzzywuzzy import process

def suggest(text, lst):



    global ratio
    c = 0

    new_lst = []
    new_lst_choose=[]

    ratio = process.extract(text, lst, limit=75)

    for e in ratio:

        if e[1] > 85 and len(e[0]) == len(text):
            new_lst.append(e[0])


    for e in ratio:
        if e[1] > 66 and e[0][0] == text[0] and len(e[0]) == len(text) and e[0] not in new_lst:
            new_lst.append(e[0])
    for e in ratio:
        if e[1] > 66 and e[0] not in new_lst:
            new_lst.append(e[0])


    return new_lst
