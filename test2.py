
# lst = []
# lst2=[]
# alph = 'abcdefghijklmnopqrstuvwxyz'
# # lines = [['hello'], ['мама'],['find'],[],[],[],['imigrate'], ['абажур'], ['email'], ['пока'], ['bye'], ['name']]
# # lines2 = copy.deepcopy(lines)
# # with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.replace(" ", "").strip().split("\n") for line in file]
#
#
# with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip().lower().split("\n") for line in file]
# print(len(lines))
# # print(lines)
# for i in range(len(lines)):
#
#
#   if lines[i][0]:
#         lst.append(lines[i][0].lower().strip().replace("1", "").replace('2', '').replace('3', '')
#                    .replace(":", "").replace("ё", "е").replace(".",""))
# print(len(lst))
# #
# #
# #
# # #
# # #
# a = set(lst)
# b = sorted(list(a))
# print(len(b))
# # c = 0
# # for i in range(len(b)):
# #     if b[i][0]:
# #         for j in alph:
# #             if  j in b[i][0]:
# #                 c += 1
# #
# #         if c == 0:
# #             lst2.append(b[i][0])
# #         else:
# #
# #             c = 0
# # print(len(lst2))
# # #
# # #
# with open('all_dic.txt', 'w+', encoding='utf-8') as file:
#     for i in b:
#         file.write(i.replace('ё', 'е')+"\n")
