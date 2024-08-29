nums = input('Пожалуйста, введите имя файла, содержащего массив целых чисел\n')
with open(nums, 'r') as file:
    numbers = [int(i) for i in file.read().strip().split('\n')]
median = sum(numbers) // len(numbers)  # Поиск медианы для ряда
moves_number = sum([abs(median - i) for i in numbers])  # Сумма разностей по модулю медианы и каждого значения
print(moves_number)
