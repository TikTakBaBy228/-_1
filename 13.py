#циклы For и While

# while - универсальный цикл в питоне, но медленее For

# while True:
#     print('hello')
# простейший бесконечный цикл

# i = 1
# while i <= 10:
#     print(i)
# #еще одно бесконечное условие

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print('hello', 'world')
#
# print('hello', 'world2')

#sep - задает значение разделение строк.
# по умолчанию стоит обычный пробел

# print('hello', 'world' sep ='1')

# end - конец строки

# print('hello', 'world' sep ='1', end=' ')

# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1

#также end может выстроить все в одну строку с любым нужным разделителем

#For - менее универсальный но быстрее while
#используется для последовательности

# s = 'hello world'
# for l in s:
#     print(l, end=' ')
# отделение букв строки друг от друга

#continue - продолжение

# s = 'hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(l, end=' ')
# удаление пробела

# break - завершить цикл

# for i in 'hello world':
#     if i == ' ':
#         break
#     print(i, end=' ')
# else:
#     print('\nNo spaces')

     # Домашняя работа

year = 1900
while year <= 2022:
    print(year)
    year += 1