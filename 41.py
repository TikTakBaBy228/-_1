#Полиморфизм
from classes import Person, Emplpoyee

person = Person('Katy', 30)
person.age = 35
person.print_info()

employee = Emplpoyee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)
