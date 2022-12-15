#Ошибки бывают двух типов: синтаксические, исключения

# print(100 / 10  #синтаксическая

# print(100 / 0) #исключение ZeroDivisionError
# print(1 + '2') #исключение TypeError
# print(int('test')) #исключение ValueError
# print('hellolololololololololo')

# try:
#     num = 100 / 2
# except ZeroDivisionError:
#     num = 0
# print(num)
# print('Hi')

# try:
#     num = 100 / 0
# except ZeroDivisionError:
#     num = 0
# except TypeError:
#     num = 1
# print(num)

# try:
#     num = 100 / 0
# except Exception:
#     num = 0
# try:
#     num = 100 / '2'
# except Exception:
#     num = 0
# else:
#     print('Else')
# finally:
#     print('Finally')
#
# print(num)

# while True:
#     try:
#         num = int(input('Enter your number: '))
#         print(f'100 / {num} = {100 / num}')
#         break
#     except ZeroDivisionError:
#         print('The number must be greater than zero')
#     except ValueError:
#         print('Must be a number')


