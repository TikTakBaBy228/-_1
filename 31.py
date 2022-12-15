            #Угадай число 2.0
import random
x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100 - угадай его:'))
    cnt += 1 # cnt = cnt + 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        if input('Сыграем еще? "y | n":') == 'y':
            x = random.randint(1, 100)
            cnt = 0
        else:
            print('Спасибо за игру')
            break
    elif user_num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше')

#Модуль Datetime
#Управление датой и временем

#datetime

# from datetime import date, datetime, timedelta
# import locale

#class date
# today = date.today()
# print(today) #2022-12-05
# print(today.day) #5
# print(today.month) #12
# print(today.year) #2022
# print(today.weekday()) #0 - понедельник

#class datetime
# now = datetime.now()
# now2 = datetime.today()
# print(now) #2022-12-05 10:50:10.306753
# print(now.day) #5
# print(now.month) #12
# print(now.year) #2022
# print(now.weekday()) #0 - понедельник
# print(now.hour) #10
# print(now.minute) #55
# print(now.second) #11
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()]) # понедельник

# now = datetime.now()
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# print(now)
# print(now.strftime('%a')) #Mon
# print(now.strftime('%A')) #Monday
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

# now = datetime.today()
# print(now.strftime('%c'))
# d1 = now + timedelta(days=1, hours=2, minutes=10)
# print(d1.strftime('%c'))

