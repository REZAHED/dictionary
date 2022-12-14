import json

import httpcore
from flashtext.keyword import KeywordProcessor
from googletrans import Translator

import colors
import write_to_file

dic = {
    'посольство исламской республики Иран в республике Беларусь':['سفارت جمهوری اسلامی ایران در بلاروس'],
    'свидительвуя свое уважение': ['با ابراز تعارفات خود به'],
    'Министерство Внутренных Дел': ['وزارت کشور'],
    'в': ['در','به'],
    'Министерству Иностранных Дел': ['به وزارت امور خارجه'],
    'и ссылаясь на ': ['پیرو'],
    'в ответ на':['بازگشت'],
    'ноту': ['یادداشت'],
    'Посольство':['سفارت'],
    'Министерство Иностранных дел':['وزارت امور خارجه'],
    'и имеет честь сообщить следующее.': ['احتراماً اشعار می دارد','احتراماً اشعار می دارد:'],
    'посольство пользуется случаем,чтобы': ['موقع را مغتنم شمرده'],
    'возобновить уверения в своем высоком уважении.': ['احترامات فائقه را تجدید می نماید','احترامات فائقه را تجدید می نماید'],
    'принимая во внимание': ['با توجه به','با عنایت به'],
    'недавний визит': ['سفر اخیر'],
    'визит': ['سفر'],
    'Е.П. г-на Владимира Макей': ['جناب آقای ولادیمیر ماکی'],
    'Министр иностранных дел':['وزیر امور خارجه'],
    'Исламская Республика Иран':['جمهوری اسلامی ایران'],
    'Е.П. г-н Посол':['سفیر محترم'],
    'Республика Беларусь': ['جمهوری بلاروس'],
    'Минск':['مینسک'],



}
dic2={}
lst=[]



# for i in range(len(lines)):
#     lst.append(lines[i].split(":"))
# print(lst)
# for i in lst:
    # if ';' in i[1]:
    #
    #     dic2[i[0]] = [i[1][0:i[1].find(';')] + "'"]
    # else:
#         dic2[i[0]]=[i[1].replace("\"",'')]
# print(dic2)

# for i,j in dic2.items():
#
#     if ";" in str(j):
#       dic2[i]=[j[0][:2] +"'"+ j[0][2:5].replace(";",',') ]
#
# print(dic2)




keyword_processor = KeywordProcessor()
# keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword_from_file('dic_file.txt')
dic3 = keyword_processor.get_all_keywords()
# print(dic3)
keyword_processor.add_non_word_boundary(":.,:")


def online_translate(text):
    lst_record = []
    lst_lang = ['fa', 'en', 'ru']
    translator = Translator()

    st = translator.translate(text, src='fa', dest='ru')
    return st.text



# keyword_processor.add_keyword('New Delhi', 'NCR region')
while True:
    text = input(" ведите текст ---->").replace("ًً",'').replace('\n',"").strip()
    if text =="yes":
        print()
        break
    if text:

        lst.append(text)
new_sentence=''
lst2=[]
lenth=110

for i in lst:
    new_sentence = keyword_processor.replace_keywords(i)
    lst2.append(new_sentence.replace("ً", "").replace("،",","))
for i in lst2:
    if len(i)<110:
        print(i)
    else:
        for e in range(0, len(i), lenth):
            # if i[lenth] ==" ":
                print(i[e:e + lenth])
            # else:
            #     while i[lenth]!=" ":
            #         lenth+=1
            #
            #     print(i[e:e + lenth])
            #     lenth-=1
# print(lst2)
lst3=[]
lst4=[]
alpha_farsi = 'ئابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
c=0
for i in lst2:
    for e in alpha_farsi:
        if e in i:
            c+=1
    if c >=1:
        lst3=i.replace("،",' ').split(" ")
        c=0
c=0
d=0
new_text=""
for i in lst3:
    for e in alpha_farsi:
        if e in i:
            print(e + 'e ' + i)
            c+=1
    if c>=1:
        d+=1
        new_text+=i+" "

        c=0
    else:
        if d>0:
            print(new_text)
            lst4.append(online_translate(new_text))
            new_text=''
            d=0
            c=0
        else:
            c=0
        # print(i)
        lst4.append(i)
print(lst3)
print(lst4)
# print(online_translate('هیئت'))
#
# print()
# print(lst2)
# from Levenshtein import distance as lev
#
#
# t = 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران'.split(" ")
# lst = [['принимая во внимание','با توجه به'], ['недавный визит','سفر اخیر']]
#
# for i in lst:
#     for j in t:
#         print(j)
#         print(lev(i[1], j))

# import re

# text = "(лек)Название пары h.j. Петров А.А. ауд. 12 <-----> (пр)Название пары Рыбин О.А. ауд. 15"
# rx = re.compile(r'\w+\s+\w\.\w\.')
# print(rx.findall(text))
#
# result = re.match(r'با توجه به', 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران')
# print(result.group(0))
