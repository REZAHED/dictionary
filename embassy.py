from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dic = {
    'посольство исламской республики Иран в республике Беларусь': 'سفارت جمهوری اسلامی ایران در بلاروس',
    'свидительвуя свое уважение': 'با ابراز تعارفات خود به',
    'Министерству Внутренных Дел': 'به وزارت کشور',
    'Министерство Внутренных Дел':'وزارت کشور',
    'Министерству Иностранных Дел': 'به وزارت امور خارجه',
    'и ссылаясь на ': 'پیرو',
    'в ответ на':'بازگشت',
    'ноту': 'یادداشت',
    'Посольство':'سفارت',
    'Министерство Иностранных дел':'وزارت امور خارجه',
    'и имеет честь сообщить следующее.': 'احتراماً اشعار می دارد:',
    'посольство пользуется случаем,чтобы': 'موقع را مغتنم شمرده،',
    'возобновить уверения в своем высоком уважении.': 'احترامات فائقه را تجدید می نماید.',
    'принимая во внимание': 'با عنایت به',
    'недавний визит': 'سفر اخیر',
    'Е.П. г-на Владимира Макей': 'جناب آقای ولادیمیر ماکی',
    'Министр иностранных дел':'وزیر امور خارجه',
    'Исламская Республика Иран':'جمهوری اسلامی ایران',
    'Е.П. г-н Посол':'سفیر محترم',

}
lst_big = []
t = 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران'

for i,j in dic.items():
    lst_big.append([i.strip().lower(),j.strip().lower()])

# print(lst_big)

lst =[]
lst_text = []
test = 'سفارت جمهوری اسلامی ایران در مینسک، با ابراز تعارفات خود به وزارت امور خارجه جمهوری بلاروس، احتراماً اشعار می دارد:'
test2= 'پیرو یادداشت سفارت'
text=""
while True:
    text = input("Введите текст: ---->>>>>> ")

    if text =='exit':
        break
    # sp = text.split(" ")
    # print(sp)

    # ratio = process.extract(text,lst_big)
    # print(ratio)
    c=0
    text_split = text.split(" ")
    for i in text_split:
       lst_text.append([c,i])
       c+=1
    # print(lst_text)
    # for i,j in dic.items():
    #     if j==text:
    #         print("dic")
    #         lst.append(i)
    for e in lst_text:
        # print(e[0])
        for i in lst_big:


            ratio2 = fuzz.token_set_ratio(e[1],i[1])
            ratio3 = fuzz.ratio(e[1], i[1])
            ratio4 = fuzz.partial_ratio(e[1], i[1])
            ratio5 = fuzz.WRatio(e[1],i[1])
            ratio6= fuzz.partial_token_set_ratio(e[1],i[1])
#پیرو یادداشت وزارت امور خارجه
            #با توجه به سفر اخیر وزیر امور خارجه

            print([ratio2,'rat 4^: '+ str(ratio4), 'rat 5^: '+ str(ratio5)],ratio6, i[1])

            # print(['T'+str(ratio2) , ratio3,ratio4,ratio5,ratio6,i[1]])
            d=0
            if ratio2 ==100 and ratio4 == 100 and ratio5 ==100:
                if lst:
                    for word in range(len(lst)):
                        d += len(lst[word])
                    print([d, 'D'])
                    print([len(text), 'text'])
                    print([i[0],'_1_IO'])
                    print([len(text), 'lentext'])
                    print([len(i[0]) , 'leni[0]'])
                    print(len(lst), 'leni[0]')
                    if len(text) + 20 >= d + len(i[0]) :
                        # print('yes')
                        lst.insert(e[0], i[0])
                        d = 0
                    else:
                        d = 0
                        continue

                else:
                    print([i[0], 'else_1 IO'])

                    if len(text) + 20 >= len(i[0]) :
                        # print("oooo")
                        lst.insert(e[0], i[0])

            elif ratio2 >=90 and ratio4 >=90 and ratio5 >= 90 :


                # print([ratio2,'rat 4^: '+ str(ratio4),'rat 5^: '+ str(ratio5),i[1]])
                #     if i[1] in e:
                # print([e[0]],i[0])
                 if lst:
                    for word in range(len(lst)):
                        d += len(lst[word])
                    print([d,'D'])
                    print([len(text),'text'])
                    print([i[0], '2_IO'])
                    print([len(i[0]), 'leni[0]'])
                    if  len(text)+20 >= d+len(i[0]) :
                        # print('yes')
                        lst.insert(e[0],i[0])
                        d=0
                    else:
                        d=0
                        continue

                 else:
                    print([i[0], 'else_2 IO'])

                    if len(text) + 20 >=  len(i[0]) :
                        # print("oooo")
                        lst.insert(e[0], i[0])
# if not lst:
    #     for i in lst_big:
    #
    #         ratio2 = fuzz.token_set_ratio(text, i[1])
    #         ratio3 = fuzz.ratio(text, i[1])
    #         # print(['T' + str(ratio2), ratio3, i[1]])
    #
    #         if ratio2 > 99 :
    #             lst.append([i[0]])
    # if not lst:
    #     for i in lst_big:
    #
    #         ratio2 = fuzz.token_set_ratio(text, i[1])
    #         ratio3 = fuzz.ratio(text, i[1])
    #         # print(['T' + str(ratio2), ratio3, i[1]])
    #
    #         if ratio2 > 70 :
    #             lst.append([i[0]])
    text_last=''
    lst2 = []
    if lst:
        for i in range(len(lst)-1):

          if  lst[i+1] != lst[i] :

             lst2.append(lst[i])
        lst2.append(lst[-1])
    else:
        print("ничего не найдено")

    for i in lst2:

        text_last +=" ".join(i)+" "
    # print(text_last)
    print(lst)
    print(lst2)
    lst.clear()
    lst_text.clear()
    lst2.clear()



# pip install fuzzywuzzy[speedup]

# for i in lst:
#
#
#     # print(i[1].split(" ")[0])
#
#     if i[1].split(" ")[0]==sp[0]:
#         lst.insert(0, lst.pop(lst.index(i)))
#
# #
#        # print(i[1])
#
# print(*lst)




# ld = [['1', '2'], ['3','4']]
# for i in ld:
#     if '3' in i:
#         ld.insert(0,ld.pop(ld.index(i)))
#
# print(ld)




# for i in range(len(ratio)):
#
#     lst.append((ratio[i][0]))
#
# for i in lst:
#     for a, b in dic.items():
#         if i == b:

            # print(a)

