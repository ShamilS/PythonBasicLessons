# https://github.com/GeekBrainsTutorial/Python_lessons_basic/pull/580

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
# https://pyformat.info/
def EnumerateFruits(fruits):
    maxlen = 0
    for fruit in fruits: 
        if len(fruit) > maxlen: maxlen = len(fruit)
    formatStr = '{}. {:>' + str(maxlen) + '}'
    i = 1
    for fruit in fruits:
        print (formatStr.format(i, fruit))
        i = i+1

#test
EnumerateFruits(["яблоко", "банан", "киви", "арбуз", "watermelon"])

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
def SubstractList(list1, list2):
    return set(list1) - set(list2)

#test    
print( \
     SubstractList ( \
        ["яблоко", "банан", "киви", "арбуз", "watermelon"], \
        ["яблоко", "киви", "watermelon", "orange"] \
    )\
)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
def ProcessList(list1):
    list2 = []
    for x in list1: 
        if x % 2 == 0:
            list2.append(x / 4)
        else:
            list2.append(x * 2)
    return list2

list1 = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
list2 = ProcessList(list1)
print(list2)
