# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
def CalcEquation(equation, x):
    return eval(equation.replace('x', f'*{x}').replace('y = ',''))

#test
print('y = ' + str(CalcEquation('y = 2x + 10', 2.5)))
print('y = ' + str(CalcEquation('y = -12x + 11111140.2121', 2.5)))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
def IsNumber(x):
    try:
        val = int(x)
        return True
    except ValueError:
        return False     

def IsCorrectDate(dateStr):
    dateParts = dateStr.split('.')
    if len(dateParts) != 3: return False
    for x in dateParts:
        if not IsNumber(x): return False
    if len(dateParts[0]) != 2 : return False
    if len(dateParts[1]) != 2 : return False
    if len(dateParts[2]) != 4 : return False
    if int(dateParts[0]) < 1 or  int(dateParts[0]) > 31: return False     
    elif int(dateParts[1]) < 1 or  int(dateParts[1]) > 12: return False     
    elif int(dateParts[2]) < 1 or  int(dateParts[2]) > 9999: return False 
    elif int(dateParts[1]) not in [1,3,5,7,8,10,12] and int(dateParts[0]) == 31: return False    
    return True

# tests
# Пример корректной даты
date = '01.11.1985'
print(f'{date} is correct date = {IsCorrectDate(date)}')

# Примеры некорректных дат
dates = [ \
    '01.22.1001', '1.12.1001', '-2.10.3001', \
    '31.04.1001', 'z1.12.1001', '02.10.301' \
    ]
for date in dates:
    print(f'{date} is correct date = {IsCorrectDate(date)}')



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
def CaclFloorAndRoomSequentialNumber(roomNumber):
    n = 1
    floorsGroupFirstRoomNumber = 1
    floorsGroupFirstFloorNumber = 1

    while floorsGroupFirstRoomNumber + n ** 2 < roomNumber :
        floorsGroupFirstRoomNumber  = floorsGroupFirstRoomNumber + n ** 2
        floorsGroupFirstFloorNumber = floorsGroupFirstFloorNumber + n
        n = n + 1

    roomNumberInFoundGroup = roomNumber - floorsGroupFirstRoomNumber + 1
    floorNumber = floorsGroupFirstFloorNumber + (roomNumberInFoundGroup // n)
    if (roomNumberInFoundGroup  % n == 0) : floorNumber = floorNumber -1
    sequentialRoomNumberOnItsFloor = roomNumberInFoundGroup % n
    if (sequentialRoomNumberOnItsFloor == 0) : sequentialRoomNumberOnItsFloor = n
    return (floorNumber, sequentialRoomNumberOnItsFloor)

#tests
targetTestResults = {5:(3,2), 59:(16,4), 24:(9,2), 13:(6,2), 11:(5,3)}
for roomNumber in [5, 59, 24, 13, 11, 59] :
   result = CaclFloorAndRoomSequentialNumber(roomNumber)
   print(f'room#={roomNumber} => {result} = {result==targetTestResults[roomNumber]}')

print(CaclFloorAndRoomSequentialNumber(1000000))
print(CaclFloorAndRoomSequentialNumber(2000000000))
# test data
# 16   56 57 58 59 60
# 15   51 52 53 54 55
# 14   46 47 48 49 50
# 13   41 42 43 44 45
# 12   36 37 38 39 40
# 11   31 32 33 34 35

# 10   27 28 29 30 
# 9    23 24 25 26
# 8    19 20 21 22
# 7    15 16 17 18 

# 6    12  13  14
# 5     9   10  11
# 4     6   7   8

# 3       4   5
# 2       2   3

# 1         1
