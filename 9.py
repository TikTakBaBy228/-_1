# s = r'C:\d\new.txt'
# print(s)
#
# s = 'Py' 'thon'
# print(s)

# s1 = 'hello, '
# s2 = 'world!'
# s3 = s1 + s2
# print(s3)

# name = 'John'
# age = 20
#
# print('My name is '+ name + 'im' + age)
# print('my name is ' + name + "im " + str(age))

# print('hi ' * 5)

# s = "Hello world!"
# print(s[0])
# print(s[-1]) #последний символ строки
# #индексация
# s[0] = 'd' #нельзя.

#[X:Y:Z] X - начало среза Y - окончание среза Z - шаг среза

s = 'Hello world!'

print(s[0:12]) #нумерация по стандарту начинается с 0 = Hello world!
print(s[-1]) #!
print(s[0:5]) #Hello
print(s[:5]) #Hello
print(s[6:]) #world!
print(s[::2]) #опускается каждый второй символ
print(s[::-1]) #переворот строки
print(s[:5] + [6:]) #целая строка без пробела