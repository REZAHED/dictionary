import json
from tqdm import tqdm
import httpcore
from googletrans import Translator

with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file.readlines()]

dic_ru_fa = {}
c = 0
d = 1
# Updated Answer as of 2021 Sept
#
# pip uninstall googletrans==4.0.0-rc1
#
# pip install googletrans==3.1.0a0
# The 3.1.0a0 version works with bulk translation too!

translator = Translator()

try:
    # dt = translator.detect(text)
    TEST = translator.translate('hi', dest='fa')
    print("соединение с интерненом проведено успешно")

except:
    httpcore._exceptions.ConnectError()
    print("нет интернета")
else:

    for i in tqdm(range(89002, len(lines)), ncols=100):

        st = translator.translate(lines[i], src='ru', dest='en')
        dic_ru_fa[lines[i]] = st.text
        c += 1

        d += 1

        if c == 500:
            with open('translate_ru_en2.json', 'r+', encoding='utf-8-sig') as file:
                json.dump(dic_ru_fa, file, indent=2, ensure_ascii=False)
            c = 0

