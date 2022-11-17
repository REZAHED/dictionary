
from flashtext.keyword import KeywordProcessor

dic = {
    'посольство исламской республики Иран в республике Беларусь':['سفارت جمهوری اسلامی ایران در بلاروس'],
    'свидительвуя свое уважение': ['با ابراز تعارفات خود به'],
    'Министерство Внутренных Дел': ['وزارت کشور'],
    'в': ['به']

}

keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keywords_from_dict(dic)
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords(input())
print(new_sentence)
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
