from fuzzywuzzy import fuzz


text = 'Исламская Республика Иран'
text2= 'в Исламскую Республику Иран'
text3=  'в Исламской Республике Иран'

ratio = fuzz.UWRatio('Исламская Республика Иран','в Исламскую Республику Иран')
print(ratio)