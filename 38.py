#Инкапсуляция

from classes import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Katy')
# # person2.__age = 30
# person2.print_info()
# # print(person2._Person__age)
# print(person2.get_age())
# person2.set_age(40)
print(person2.age)
person2.age = 35
person2.print_info()
#Если распечатать то геттер, а если чтото менять то сеттер
