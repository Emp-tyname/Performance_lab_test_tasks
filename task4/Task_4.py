import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input_data', type=str, help='Число n')
obj = parser.parse_args()
obj_dict = vars(obj)
nums = obj_dict['input_data']


with open(nums, 'r') as file:
    numbers = [int(i) for i in file.read().strip().split('\n')]
median = sorted(numbers)[len(numbers) // 2] # Рассчет медианы
moves_number = sum([abs(median - i) for i in numbers])  # Сумма разностей по модулю медианы и каждого значения
print(moves_number)
