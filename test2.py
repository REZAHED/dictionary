from fuzzywuzzy import process

lst = ["котенок", "цап", "пацр",'царь','а','пацан','пайка', 'пока','пачка','палка','папка','парк','паек','паша','паук']
text = 'search'
lst2=[]

for i in lst:
    if len(i) == len(text) or len(i) == len(text) +1:
        lst2.append(i)

Ratio = process.extractOne(text,lst2)
print(Ratio[0])
print(Ratio[1])

Ratio2 = process.extract(text,lst2)
for e in Ratio2:
    print(e[0])
    print(e[1])

new = "-"
if new.isspace():
    print("yes")




# with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:


