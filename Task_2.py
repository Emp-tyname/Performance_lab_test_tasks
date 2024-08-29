flag = 1
file_circle_name = input('Пожалуйста, введите полное имя файла с координатами круга\n')
file_dots_name = input('Пожалуйста, введите полное имя файла с координатами точек\n')
file_circle = open(file_circle_name, 'r')
file_dots = open(file_dots_name, 'r')
BOT, TOP = (1 / (10 ** 38), 10 ** 38) ''' ОДЗ BOT ошибочно по тестовым условиям. т.к. точка 0 0 входит в ОДЗ, то есть
                                          минимальное допустимое значение равно нулю'''

circle_data = [i.split() for i in file_circle.read().strip().split('\n')]
x1, x2 = map(float, circle_data[0])  # x1, x2 - Координаты центра окружности, r - радиус окружности
r = float(circle_data[1][0])
if any([(x1 < 0 or x1 > TOP), (x2 < 0 or x2 > TOP), r < 0]):  # Проверка файла с кругом на вход в ОДЗ
    flag = 0

list_of_dots = [i.split() for i in file_dots.read().strip().split('\n')] # Список с координатами точек
for i in range(len(list_of_dots)):
    list_of_dots[i] = [float(j) for j in list_of_dots[i]]
    for j in list_of_dots[i]:
        if j < 0 or j > TOP:
            flag = 0

if len(list_of_dots) > 100:
    flag = 0
    print('Количество точек больше 100')

if flag:
    for i in range(len(list_of_dots)):
        if (list_of_dots[i][0] - x1) ** 2 + (list_of_dots[i][1] - x2) ** 2 < r * r:
            print(1)
        elif (list_of_dots[i][0] - x1) ** 2 + (list_of_dots[i][1] - x2) ** 2 > r * r:
            print(2)
        else:
            print(0)
else:
    print('Недопустимые входные данные')
file_circle.close()
file_dots.close()
