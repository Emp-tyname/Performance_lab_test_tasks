n, m = map(int, input('Введите m и n \n').split())
i = 1
crit_path = []
list_of_arrays = []
new_list = [i for i in range(1, n + 1)]
# print("Круговой массив: ", *new_list,sep='', end='.\n') Изначальный круговой массив
while True:
    crit_path.append(i)
    # list_of_arrays.append(new_list[:m])                Прибавление интервалов к общему списку
    # new_list = new_list[m - 1:] + new_list[:m - 1]
    i = 1 + (i + m - 2) % n
    if i == 1:
        break

# print(f"При длине обхода {m} получаем интервалы: ", *list_of_arrays) Найденные интервалы
print("Полученный путь: ", *crit_path, sep='', end='.\n')
