# lst = []


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

    c = 0

    new_lst = []
    new_lst.clear()

    for i in lst:
        if 8 <= len(text) <= len(i) < 11:
            for j in list(text):
                if j in i:
                    c += 1
            if (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
                    and text[0] == i[0] and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
                    and text[5] == i[5]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
                    and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
                    and text[5] == i[6] and text[6] == i[6]:
                c = 0
                new_lst.append(i)

            else:
                c = 0

        if 8 <= len(text) == len(i):
            for j in list(text):
                if j in i:
                    c += 1
            if (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
                    and text[5] == i[5]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
                    and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
                    and text[5] == i[5] and text[6] == i[6]:
                c = 0
                new_lst.append(i)

            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4] \
                    and text[5] == i[5] and text[6] == i[6]:
                c = 0
                new_lst.append(i)

            else:
                c = 0
        elif 5 <= len(text) <= len(i) < 8:
            for j in list(text):
                if j in i:
                    c += 1
            if (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] \
                    and text[2] == i[2] and text[3] == i[3]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[1] == i[1] \
                    and text[2] == i[2] and text[3] == i[3] and text[4] == i[4]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] \
                    and text[1] == i[1] and text[3] == i[3] and text[4] == i[4]:
                c = 0
                new_lst.append(i)

            elif (c == len(text) or c == len(text) - 1 or c == len(text) - 2) \
                    and text[0] == i[0] and text[1] == i[1] \
                    and text[2] == i[2] and text[4] == i[4]:
                c = 0
                new_lst.append(i)

            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1] \
                    and text[-1] == i[-1]:
                c = 0
                new_lst.append(i)

            else:
                c = 0
        elif 3 <= len(text) == len(i):
            for j in list(text):
                if j in i:
                    c += 1
            if (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[1] == i[1] and text[2] == i[2]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[2] == i[2]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1] and text[2] == i[2]:
                c = 0
                new_lst.append(i)
            elif (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0] and text[1] == i[1] and text[2] == i[2]:
                c = 0
                new_lst.append(i)
            else:
                c = 0
        elif 3 <= len(text) == len(i) - 1:
            for j in list(text):
                if j in i:
                    c += 1
            if c == len(text) \
                    and text[0] == i[0] and text[1] == i[1]:
                c = 0
                new_lst.append(i)
            elif c == len(text) \
                    and text[1] == i[1] and text[2] == i[2]:
                c = 0
                new_lst.append(i)
            else:
                c = 0

        elif 3 <= len(text) == len(i) + 1:
            for j in list(text):
                if j in i:
                    c += 1
            if c == len(text) - 1 \
                    and text[0] == i[0] and text[1] == i[1]:
                c = 0
                new_lst.append(i)
            else:
                c = 0

        elif len(i) >= len(text) < 3:
            for j in list(text):
                if j in i:
                    c += 1
            if (c == len(text) or c == len(text) - 1) \
                    and text[0] == i[0]:
                c = 0
                new_lst.append(i)
            else:
                c = 0
    return set(new_lst)
