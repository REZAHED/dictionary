from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dic = {
    'Министерству Внутренных Дел': 'به وزارت کشور ',
    'возобновить уверения в своем высоком уважении.': 'احترامات فائقه را تجدید می نماید.',
    'посольство пользуется случаем,чтобы': 'موقع را مغتنم شمرده،',
    'Министерству Иностранных Дел': 'وزارت امور خارجه',
    'свидительвуя свое уважение': 'با ابراز تعارفات خود به',
    'имеет честь сообщить следующее.': 'احتراماً اشعار می دارد:',
    'посольство исламской республики Иран в республике Беларусь': 'سفارت جمهوری اسلامی ایران در مینسک'
}
lst =[]
test = 'سفارت جمهوری اسلامی ایران در مینسک، با ابراز تعارفات خود به وزارت امورخارجه جمهوری بلاروس، احتراماً اشعار می دارد:'

text = input("Введите текст: ---->>>>>> ")

ratio = process.extract(text,dic)
print(ratio)
for i in range(len(ratio)):
    # test.split(ratio[0][0])
    lst.append((ratio[i][0]))

# print(test)
# print(lst)
for i in lst:
    for a, b in dic.items():
        if i == b:

            print("".join(a),end='')

# print(ratio[0][0])
# text = input("введите : ").split(" ")
# print(text)
# print(test)


# for i , j in dic.items():
#     if text ==i.rstrip().lower():
#         print(j)
#     if text == j.rstrip().lower():
#         print(i)