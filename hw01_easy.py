
__author__ = 'Salakhetdinov Shamil'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

#
# Task1. Solution 1
#
x = 1234567890
z = x
while (z > 0):
    print (z % 10)
    z = z // 10

#
# Task1. Solution 2
#
x = 1234567890
for c in str(x):
    print(c)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = int(input('Enter a value:'))
b = int(input('Enter b value:'))
#using variable
print('Solution using a temp variable:')
print(f"Before: a={a}, b={b}")
x = a
a = b
b = x
print(f"After: a={a}, b={b}")

#no variables
print('Solution without using a temp variable:')
print(f"Before: a={a}, b={b}")
a = a + b
b = a - b
a = a - b
print(f"After: a={a}, b={b}")

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input('Input your age:'))
if age >= 18:
    print ("Доступ разрешен")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет")    
