from Levenshtein import distance as lev


t = 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران'.split(" ")
lst = [['принимая во внимание','با توجه به'], ['недавный визит','سفر اخیر']]

for i in lst:
    for j in t:
        print(j)
        print(lev(i[1], j))

# import re

# text = "(лек)Название пары h.j. Петров А.А. ауд. 12 <-----> (пр)Название пары Рыбин О.А. ауд. 15"
# rx = re.compile(r'\w+\s+\w\.\w\.')
# print(rx.findall(text))
#
# result = re.match(r'با توجه به', 'با توجه به سفر اخیر جناب آقای ولادیمیر ماکی وزیر امور خارجه به جمهوری اسلامی ایران')
# print(result.group(0))
