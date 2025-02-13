'''
Вариант 23.
Натуральные четные числа, начинающиеся с нечетной цифры и содержащие не более 3 нечетных цифр.
Для каждого числа через тире вывести прописью первую цифру и нечетные цифры.
'''
#Словарь с цифрами
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
#Нечетные цифры
odd = '13579'
#Баффер
gived_num = '1'
#Выбор файла
file_name = "text.txt"
try:
    open(file_name, 'r')
except:
    print('Файл отсутствует в директории проекта')
    exit()

k0 = False
with open(file_name, 'r') as file:
    while 1:
        gived_num = file.readline().replace('\n', '')
        if not gived_num:
            #print('Файл закончился')
            break
        if not gived_num.isdigit():
            continue
        if (int(gived_num) % 2 == 0) and (gived_num[0] in odd) and (sum([gived_num.count('1'), gived_num.count('3'), gived_num.count('5'), gived_num.count('7'), gived_num.count('9')]) <= 3):
            print(gived_num, end=' - ')
            for i in gived_num:
                if (i in odd): print(dc_cifr[i], end= ' ')
            print()


#*1
'''
lambda - вложенная функция, которая выполняет след действие:
Получает на вход некий х, возвращает х not in k (х не содержится в k)

map - на входе в скобках получает два аргумента - функция и лист
возвращает массив, где каждым элементом является итог функции от соответствующего элемента листа

list - преобразует итог работы map в лист 

all - возвращает True, если все элементы поданного на вход листа являютсяя True, иначе - False
'''