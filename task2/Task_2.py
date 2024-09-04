flag = 1
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('cirlce_data', type=str, help='Координаты круга')
parser.add_argument('list_of_dots', type=str, help='Координаты точек')
obj = parser.parse_args()
obj_dict = vars(obj)
file_circle_name = obj_dict['cirlce_data']
file_dots_name = obj_dict['list_of_dots']


file_circle = open(file_circle_name, 'r')
file_dots = open(file_dots_name, 'r')
BOT, TOP = (-10 ** 38, 10 ** 38)  # BOT-значение на данный момент зеркально отражает TOP-значение

circle_data = [i.split() for i in file_circle.read().strip().split('\n')]
x1, x2 = map(float, circle_data[0])  # x1, x2 - Координаты центра окружности, r - радиус окружности
r = float(circle_data[1][0])
if any([(x1 < BOT or x1 > TOP), (x2 < BOT or x2 > TOP), r < 0]):  # Проверка файла с кругом на вход в ОДЗ
    flag = 0

list_of_dots = [i.split() for i in file_dots.read().strip().split('\n')]  # Список с координатами точек
for i in range(len(list_of_dots)):
    list_of_dots[i] = [float(j) for j in list_of_dots[i]]
    for j in list_of_dots[i]:
        if j < BOT or j > TOP:
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


