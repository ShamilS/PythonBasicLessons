# Hard
#
# Задача-1: Пользователь вводит текст, необходимо разбить его по словам и 
#           выдать статистику по тексту
#
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?
#
import re
text = 'The, quick- Быстрая brown бурая : fox лиса ? jumps! over перепрыгивает the lazy? ленивую dog собаку.'
text = input("Введите текст: ") or text
print(f'Введенный текст: {text}')
words = re.findall('\w+', text)
print(f'Кол-во слов в тексте = {len(words)} - {words}')

englishChars = re.findall('[A-Za-z]', text)
print(f'Кол-во английских букв в тексте = {len(englishChars)} - {englishChars}')

# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
text1 = 'The, quick- Быстрая brown бурая : fox лиса ? jumps! over перепрыгивает the lazy? ленивую dog собаку.'.lower()
text2 = 'Brown fox and a lazy dog.'.lower()
text1 = input("Введите текст №1:" ) or text1
text2 = input("Введите текст №2:" ) or text2

print(f'Введенный текст №1: {text1}')
print(f'Введенный текст №2: {text2}')

wordsSet1 = set(re.findall('\w+', text1))
wordsSet2 = set(re.findall('\w+', text2))
commonWords = wordsSet1.intersection(wordsSet2)
print(f'Общие слова: {commonWords}')

# EXTRA
# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в холодильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь

def MakeShoppingList(recepy, fridgeContents):
    shoppingList = dict()
    for item in recepy:
        if item in fridgeContents:
            if recepy[item] > fridgeContents[item]: 
                shoppingList[item] = recepy[item] - fridgeContents[item]
        else:
            shoppingList[item] = recepy[item]
                        
    if len(shoppingList) == 0:
        print('Для приготовления блюда все есть');                         
    else:
        print('Список покупок:')
        print(shoppingList)    

#tests
recepy = {"meat": 500, "onion": 200, "carrot":250, "rice":150, "olive oil":50, "garlic":4 }
fridgeContents = {"meat": 500, "carrot":100, "rice":150, "garlic":4 }
MakeShoppingList(recepy, fridgeContents)

fridgeContents = {"meat": 500, "onion": 200, "carrot":250, "rice":150, "olive oil":50, "garlic":4 }
MakeShoppingList(recepy, fridgeContents)
