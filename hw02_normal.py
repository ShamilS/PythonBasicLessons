# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

def CalcSQRTs(list):
    resultList = []
    for x in list:
        if x < 0: continue
        if int(math.sqrt(x)) != math.sqrt(x): continue    
        resultList.append(int(math.sqrt(x))) 
    return resultList 

#test
print(CalcSQRTs([2, -5, 8, 9, -25, 25, 4] ))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
def PrinFulltDate(date):
    onesAndTeens = \
       ["первое","второе","третье","четвертое","пятое","шестое","седьмое","восьмое","девятое", \
       "десятое", "одиннадцатое","двенадцатое","тринадцатое","четырнадцатое", \
       "пятнадцатое","шестнадцатое","семнадцатое","восемнадцатое","девятнадцатое"] 
    tens    = ["двадцать","тридцать"]
    months  = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
    dateParts = date.split('.')
    dayInWords = 0
    if int(dateParts[0]) < 20:
        dayInWords = onesAndTeens[int(dateParts[0])-1]
    else:
        dayInWords = tens[int(dateParts[0][0])-2] + ' ' + onesAndTeens[int(dateParts[0][1])-1]

    print (f'{dayInWords} {months[int(dateParts[1])-1]} {dateParts[2]} года')

PrinFulltDate("02.11.2013")
PrinFulltDate("12.03.2017")
PrinFulltDate("25.10.2014")
PrinFulltDate("31.05.2018")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
def randomNumbersList(n):
    randomNumbers = []
    for x in range(n):
        randomNumbers.append(random.randrange(-100, 100, 1))
    return randomNumbers    

#tests
print(randomNumbersList(10))
print(randomNumbersList(15))
print(randomNumbersList(20))

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
def GetUniqueNumbersSetFromList(list):
    return set(list)

#test
print(GetUniqueNumbersSetFromList([1, 2, 4, 5, 6, 2, 5, 2]))

# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
def GetNotRepeatableUniqueNumbersSetFromList(list):
    resultSet = set()
    for x in set(list):
        if list.count(x) == 1 : resultSet.add(x) 
    return resultSet

#test
print(GetNotRepeatableUniqueNumbersSetFromList([1, 2, 4, 5, 6, 2, 5, 2]))
