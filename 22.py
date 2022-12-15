#множества
#не дублируется
#не поддерживает индексирование

# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = set('hello')
# s3 = {i for i in range(1, 11)}
# s4 = {5, 3, 10, 1, 9, 2}
# s5 = set()
# print(type(s))
# print(s)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

# nums = [1,2,3,3,1,2,4,5]
# nums2 = set(nums)
# print(nums2)

# a = set('abracadabra')
# b = set('alacazam')
# c = a - b #вычитание - убирает из а все буквы, которые есть в b
# d = a | b #объединение - буквы или в а или в b
# e = a & b #пересечение - буквы и в а и в b (дубликаты)
# f = a ^ b #множество из элементов - буквы в а или b, но не в обоих
# print(a, b, c, d, e, sep= '\n')

# set.copy() - возвращает копию множества
# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s.copy()
# print(s, id(s))
# print(s2, id(s2))

# set.add(elem) - добавляет элемент в множество
# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s.add('melon')
# print(s)

# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует
# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s.remove('apple')
# print(s)

# set.discard(elem) - удаляет элемент, если он находится в множестве
# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s.discard('apple2')
# print(s)


# set.pop() - возвращает и удаляет первый элемент из множнства.
# Так как множества не упорядочены, нельзя точно сказать, какой
# элемент будет первым
# set.clear() - очистка множества
# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s.clear()
# print(s)

# frozenset - изменить нельзя

# a = frozenset('hello')
# print(a)

a = frozenset('hello')

print(a)