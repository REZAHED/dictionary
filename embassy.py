from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dic = {
    'посольство исламской республики Иран в республике Беларусь': 'سفارت جمهوری اسلامی ایران در بلاروس',
    'посольство исламской республики Иран ': 'سفارت جمهوری اسلامی ایران',
    'свидительвуя свое уважение': 'با ابراز تعارفات خود به',
    'Министерству Внутренных Дел': 'به وزارت کشور',
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
    'в Исламскую Республику Иран ':'به جمهوری اسلامی ایران',
    'в Исламской Республике Иран ':'در جمهوری اسلامی ایران',
    'Е.П. г-н Посол':'سفیر محترم',

}
lst_big = []
t = 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران'

for i,j in dic.items():
    lst_big.append([i.strip(),j.strip()])

# print(lst_big)

lst =[]
lst_text = []
test = 'سفارت جمهوری اسلامی ایران در مینسک، با ابراز تعارفات خود به وزارت امور خارجه جمهوری بلاروس، احتراماً اشعار می دارد:'
test2= 'پیرو یادداشت سفارت'
while True:
    text = input("Введите текст: ---->>>>>> ").split(" ")
    if text =='exit':
        break
    # sp = text.split(" ")
    # print(sp)

    # ratio = process.extract(text,lst_big)
    # print(ratio)
    c=0
    for i in text:
       lst_text.append([c,i])
       c+=1
    # print(lst_text)
    for e in lst_text:
        print(e[0])
    for i in lst_big:


            ratio2 = fuzz.token_set_ratio(lst_text,i[1])
            ratio3 = fuzz.ratio(text, i[1])
            ratio4 = fuzz.partial_ratio(lst_text, i[1])
            ratio5 = fuzz.WRatio(text,i[1])
            ratio6 = process.extract(i[1], text)
#پیرو یادداشت وزارت امور خارجه
            #با توجه به سفر اخیر وزیر امور خارجه



            # print(['T'+str(ratio2) , ratio3,ratio4,ratio5,ratio6,i[1]])

            if ratio2 >99 and ratio4 >21  :
                for e in lst_text:
                    print(e[0])
                    if i[1] in e:

                        lst.insert(e[0],[i[0]])
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
    for i in lst:
        text_last +=" ".join(i)+" "
    print(text_last)
    lst.clear()


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

