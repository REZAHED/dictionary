from deep_translator import PonsTranslator
from deep_translator import LingueeTranslator
word = 'привет'
translated_word = PonsTranslator(source='ru', target='en').translate(word, return_all=True)
# print(translated_word)

from deep_translator import GoogleTranslator
translated= GoogleTranslator(source="ru", target="en").translate(text='привет',return_all=True)


