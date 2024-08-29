import json

name_tests = input('Пожалуйста, введите полное имя файла со структурой построения отчета\n')
values_tests = input('Пожалуйста, введите полное имя файла с результатами прохождения тестов\n')
with open(name_tests) as json_test:
    tests = json_test.read()
with open(values_tests) as json_values:
    values = json_values.read()
dict_tests = json.loads(tests)
dict_values = json.loads(values)


def recursion(new_list):
    if isinstance(new_list, dict):
        for key, value in new_list.items():
            if key == 'values':
                return recursion(value)
            elif key == 'id':
                for z in dict_values.values():
                    for k in z:
                        if new_list['id'] == k['id']:
                            new_list['value'] = k['value']
                            break
    elif isinstance(new_list, list):
        return list(map(recursion, new_list))


test_list = dict_tests['tests']
recursion(test_list)

report_tests = input('Пожалуйста, введите полное имя файла с результатом\n')
with open(report_tests, "w", encoding="utf-8") as file:
    json.dump(test_list, file, indent=4)

'''Ниже куски кода, оставшиеся от мозгового штурма. Первоначальные попытки решить с помощью индексов провалились 
   из-за вложенности (работало только на первом уровне). Итоговым решением задачи с сохранением вложенности 
   стала рекурсия
for value in dict_tests.values():
    for j in range(len(value)):
        #print(dict_tests['tests'][j])
        #print(value[j], j)
        for y in value[j]:
            if y == 'values':
                recursion(y)
                #print(dict_tests['tests'][j]['values'][0])
        for z in dict_values.values():
            for k in z:
                #print(k['id'], k['value'])
                if value[j]['id'] == k['id']:
                    #print(value[j]['id'], k['id'])
                    #print(dict_tests['tests'][j]['id'], k['value'])
                    dict_tests['tests'][j]['value'] = k['value']
                    break

for key, value in dict_tests.items():
    for j in range(len(value)):
        for k in value[j]:
            if k == 'values':
                recurse

#print(dict_tests)'''
