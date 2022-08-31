import os
import random
import sys

print('Hello World')

name = 'Wesley'

print(name)

# Numbers Strings Lists Tuples Dictionaries

print('5 + 2 = ', 5 + 2)
print('5 - 2 = ', 5 - 2)
print('5 * 2 = ', 5 * 2)
print('5 / 2 = ', 5 / 2)
print('5 % 2 = ', 5 % 2)
print('5 ** 2 = ', 5**2)
print('5 // 2 = ', 5 // 2)

quote = '\'Always remember you are unique'

multi_line_quote = ''' just like everyone else'''

print('%s %s %s' % ('I like the quote', quote, multi_line_quote))

print('I don\'t like ', end='')
print('newlines')

# Lists
grocery_List = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item:', grocery_List[0])

grocery_List[0] = 'green juice'
print(grocery_List[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_List]
print(to_do_list)
print(to_do_list[1][1])

grocery_List.append('Onions')

grocery_List.insert(1, 'Pickle')
grocery_List.remove('Pickle')
grocery_List.sort()
grocery_List.reverse()
del grocery_List[4]
print(grocery_List)

to_do_list2 = other_events + grocery_List
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

# Tuples
pi_tuple = (3, 1, 4, 1, 5, 9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

# Dictionaries
super_villains = {
    'Fiddler': 'Isaac Bowin',
    'Captain Cold': 'Leonard Snart',
    'Weather Wizard': 'Mark Mardon',
    'Mirror Master': 'Sam Scudder',
    'Pied Piper': 'Thomas Peterson'
}
print(super_villains['Captain Cold'])
del super_villains['Fiddler']
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get('Pied Piper'))
print(super_villains.keys())
print(super_villains.values())

# Conditionals
age = 21
if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')

if ((age >= 1) and (age <= 18)):
    print('You get a birthday')
elif ((age == 21) or (age >= 65)):
    print('You get a birthday')
elif age != 30:
    print('You don\'t get a birthday')
else:
    print('You get a birthday party')

# Loops
for x in range(0, 10):
    print(x, ' ', end='')
print('\n')

for y in grocery_List:
    print(y)

for x in [2, 4, 5, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

# While Loops
random_num = random.randrange(0, 100)
while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 100)

i = 0
while i < 10:
    if (i % 2) == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue
    i += 1


# Functions
def add_number(fnum, snum):
    sumnum = fnum + snum
    return sumnum


print('What is your name')
name = sys.stdin.readline()
print('Hello', name)

long_string = 'I\'m a long string and I need to be wrapped up in a function'
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:4] + ' is a cool function')
print('%c is %s letter and my number is %d' % ('a', 'first', 1))
print(long_string.capitalize())
print(long_string.find('Floor'))
print(long_string.isalpha())
print(long_string.isalnum())
print(long_string.strip())

test_file = open('test.txt', 'wb')
test_file.write(b'Write me to the file\n', 'UTF-8')
test_file.close()

test_file = open('test.txt', 'r+', encoding='UTF-8')
text_in_file = test_file.read()
print(text_in_file)
test_file.close()

os.remove('test.txt')


# OOP
class Animal:
    '''an animal class'''
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print('Animal')

    def to_string(self):
        return '{} is {} cm tall and {} kilograms and says {}'.format(
            self.__name, self.__height, self.__weight, self.__sound)


cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())


# inheritance
class Dog(Animal):
    ''' an inheritance for Dog'''
    __ownr = ''

    def __init__(self, name, height, weight, sound, owner):
        self.__ownr = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__ownr = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print('Dog')

    def to_string(self):
        return '{} is {} cm tall and {} kilograms and says {}. His owner is {}'.format(
            self.__name, self.__height, self.__weight, self.__sound,
            self.__owner)


# method overloading
def multiple_sounds(self, how_many=None):
    if how_many is None:
        print(self.get_sound())
    else:
        print(self.get_sound() * how_many)


spot = Dog('Spot', 53, 27, 'Ruff', 'Derek')
print(spot.to_string())


# Polymorphism
class AnimalTesting:
    ''' a polymorphism class'''

    def get_type(self, animal):
        animal.get_type()


test_animal = AnimalTesting()
test_animal.get_type(cat)
test_animal.get_type(spot)

spot.multiple_sounds(3)
