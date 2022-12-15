#Регулярные выражения - re
#Используется для поиска в строке некого соответсвия того или иного шаблона
#^ - начало строки
#$ - конец строки

import re
#
# s = 'Это просто строка текста. А это еще одна строка текста'
# pattern = 'строка'

# #Метод search ищет совпадения
#
# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No match')
#
# match = re.search(pattern, s)
# print(match)

#Метод match показывает совпадения
#
# print(re.match(pattern, s))

#Метод  findall ищет все совпадения
#
# print(re.findall(pattern, s))


#Метод split, maxsplit
#
# print(re.split('\.', s, 1))

s = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
А это строка с разными символами: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string'''

# pattern = r'\w+'
# pattern = r'[а-я0-9А-Яё]+'
# pattern = r'\d+'
# pattern = r'[\d-]+'
# pattern = r'a\\b\tc'
# pattern = r'\w+$'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

#mail@mail.com
#kudlay@bank
#mail@google.com.ua


def validate_email(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)
print(validate_email('mail@mail.com'))
print(validate_email('kudlay@bank'))
print(validate_email('mail@google.com.ua'))














