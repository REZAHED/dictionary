from fuzzywuzzy import process
import Levenshtein
lst = ["котенок", "цап", "пацр",'царь','а','пацан']
text = 'цар'
lst2=[]

for i in lst:
    if len(i) == len(text) or len(i) == len(text)+1:
        lst2.append(i)

Ratio = process.extract(text,lst2)
for e in Ratio:
    print(e[0])



# with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:


