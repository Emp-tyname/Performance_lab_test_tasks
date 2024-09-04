import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, help='Число n')
parser.add_argument('m', type=int, help='Число n')
obj = parser.parse_args()
obj_dict = vars(obj)
n = obj_dict['n']
m = obj_dict['m']


i = 1
crit_path = []
list_of_arrays = []
new_list = [i for i in range(1, n + 1)]
'''print("Круговой массив: ", *new_list,sep='', end='.\n') Изначальный круговой массив'''
while True:
    crit_path.append(i)
    '''list_of_arrays.append(new_list[:m])                Прибавление интервалов к общему списку
    new_list = new_list[m - 1:] + new_list[:m - 1]'''
    i = 1 + (i + m - 2) % n
    if i == 1:
        break

'''print(f"При длине обхода {m} получаем интервалы: ", *list_of_arrays) Найденные интервалы'''
print(*crit_path, sep='', end='\n')
