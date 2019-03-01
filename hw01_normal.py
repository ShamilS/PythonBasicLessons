import math

__author__ = 'Salakhetdinov Shamil'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
#
# Task1. Solution 1
#
print("Task1. Solution 1:")
maxDigit = 0
x = 58375
print(f"Source value: ", x)
while x > 0:
    if x % 10 > maxDigit:
        maxDigit = x % 10
    x = x // 10
print(f"maxDigit = {maxDigit}")
print()
#
# Task1. Solution 2
#
print("Task1. Solution 2:")
maxDigit = 0
x = 58375
print(f"Source value: ", x)
for c in str(x):
    if (int(c) > maxDigit):
        maxDigit = int(c)
print(f"maxDigit = {maxDigit}")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a = input('Enter a value:')
b = input('Enter b value:')
a,b = b,a
print(f"a={a}, b={b}")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
def quandraticEquationSolver(a,b,c):
    x1 = None
    x2 = None

    d = math.pow(b,2) - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
    elif d == 0:
        x1 = x2 = -b / (2*a)


    print(f"a = {a}, b = {b}, c = {c}")
    print(f"Source equation: {a}x**2 + {b}x + {c} = 0")
    print(f"discriminant={d}")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print("----------")
    if (d >= 0):
        print(f"Test x1: {a*math.pow(x1,2)+b*x1+c} == 0 => {a*math.pow(x1,2)+b*x1+c == 0}") 
        print(f"Test x2: {round(a*math.pow(x2,2)+b*x2+c,3)} == 0 => {round(a*math.pow(x2,2)+b*x2+c,3) == 0} ") 
    else:    
        print(f"No real solution for negative discriminant = {d}")


a = 1
b = 3
c = 3
print("--- Test case #1 ---")
quandraticEquationSolver(a,b,c)
print()

a = -6
b = -5
c = -1
print("--- Test case #2 ---")
quandraticEquationSolver(a,b,c)
print()

a = 1
b = -6
c = 9
print("--- Test case #3 ---")
quandraticEquationSolver(a,b,c)
print()
