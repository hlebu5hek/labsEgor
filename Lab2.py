'''
Вариант 23.
Натуральные четные числа, начинающиеся с нечетной цифры и содержащие не более 3 нечетных цифр.
Для каждого числа через тире вывести прописью первую цифру и нечетные цифры.
'''
import re
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'} #Словарь с цифрами
file_name = "text.txt" #Выбор файла
with open(file_name, 'r') as file:
    f = file.readlines()
    for i, gived_num in enumerate(f):
        gived_num = gived_num.replace('\n', '')
        if re.match(r'^([13579]{1})(\d)*([24680])$', gived_num) and len(''.join(re.findall(r'[13579]*', gived_num))) <= 3:
            print(gived_num, end=' - ')
            for i in gived_num:
                if (i in '13579'): print(dc_cifr[i], end=' ')
            print()