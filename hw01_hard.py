# Задание-1:
# Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу
def IsPrime(n):
    if n == 2 or n == 3 or n == 5: return True
    if n == 1 or n %2 == 0 or n % 3== 0 : return False

    i = 5
    while i*i <= n:
        if (n % i == 0 or n % (i+2) == 0):
            return False
        i = i+6
    
    return True

n = 2
while n > 1:
    n = int(input("Input any integer number (<=1 - Quit): "))
    print (f'{n} is prime = {IsPrime(n)}')

# test - 2 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# for i in range(100):
#    if IsPrime(i): print(f'{i}', end=' ')

# Задание-2
# Найдите n-ое число Фибоначчи
def NthFibonacciNumber(n):
    if (n <= 1): return n
    return NthFibonacciNumber(n-1) + NthFibonacciNumber(n-2)

#test - 1 1 2 3 5 8 13 21 34 55 89 144
for n in range(12): print(f'{NthFibonacciNumber(n+1)}', end = ' ')


# Задание-3
# Вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# (таких строк n, в каждой строке m троек AAA)
def AAABBBPrinter(n, m):
    for i in range(n):
        for j in range(m):
            if (i % 2 == 0): 
               print("AAABBB", end = "")    
            else:
               print("BBBAAA", end = "")
        print()

# test
# AAABBBPrinter(5,3)                
    
