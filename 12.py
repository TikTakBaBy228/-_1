#if - оператор условия

# True
# False #обязательно с большой

#операторы сравнения
# = - оператор присваивания
# == - оператор сравнения

# != - проверка неравенства

# > - больше
# >= - больше или равно
# < - меньше
# <= - меньше или равно

# print(2>3) #false
# print(2<3) #true
# print(2<=3) #true
# print(2>=3) #false
# print(2==2) #true

'''
if выражение 1:
    блок кода1
elif выражение 2:
    блок кода2
else: 
    блок кода 3
'''
'''
if - выражение условия которое вернет условие True. 
Если будет False то будет проверка остальных блоков 
условия
'''

# x = 0
# if x:
#     print('переменная х вернула ИСТИНУ')
# else:
#     print('переменная х вернула ЛОЖЬ') # ложь

# if 1:
#     print('выражение истина')
# else:
#     print('выражение ложно') #истина ибо 1

# light = 'red'
#
# if light == 'red':
#     print('stop')
# elif light == 'yellow':
#     print('wait')
# elif light == 'green':
#     print('go')
# else:
#     print('what?')
#
# light = 'yellow'
#
# if light == 'red':
#     print('stop')
# elif light == 'yellow':
#     print('wait')
# elif light == 'green':
#     print('go')
# else:
#     print('what?')
#
# light = 'green'
#
# if light == 'red':
#     print('stop')
# elif light == 'yellow':
#     print('wait')
# elif light == 'green':
#     print('go')
# else:
#     print('what?')
#
# light = 'blue'
#
# if light == 'red':
#     print('stop')
# elif light == 'yellow':
#     print('wait')
# elif light == 'green':
#     print('go')
# else:
#     print('what?')

#запрос у пользователя

# age = int( input('сколько вам лет? '))
# if age >= 18:
#     print('добро пожаловать')
# else:
#     print('вам еще рано')

# age = int(input('сколько вам лет?'))
# if age >= 18:
#     print('добро пожаловать')
# else:
#     print(f'вам {age} лет. вам еще рано. не хватает еще {18 - age} лет. возвращайтесь позже.')

# and - помогает проверить еще чтото

# or - помогает задать еще одно условие

# time = 11
# if time < 12 or time > 13:
#     print('open')
# else:
#     print('close')

# time = 8
# day = 'st'
# if time >= 8 and day != 'su':
#     print('close')
# else:
#     print('open')

#not - не (для инверсии условия)

# x = 1
# if not x:
#     print('OK')
# else:
#     print('NO')

# тернарный оператор - сокращенное выражение

# x = 1
# res = 'ok' if x else 'NO'
# print(res)

# x = 1
# print('OK' if x else 'NO')

