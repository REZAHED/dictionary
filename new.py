from fuzzywuzzy import process
lst = ['пока']
ratio = process.extract("пава", lst, limit=20)
print(ratio)