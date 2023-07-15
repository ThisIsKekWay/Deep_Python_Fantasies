# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

items = {
    'котелок': 6, 'спички': 1, 'вода': 2, 'мясо': 5, 'аптечка': 3, 'паталка': 9, 'топор': 4, 'посуда': 1,
    'антикомарин': 1
}

max_weight = int(input('Введите максимальный вес для рюкзака:\n'))
max_length = int(input('Сколько вещей надо взять?\n'))


def find_combo (items, max_weight, max_length):
    for k, v in items.items():
        combinations = []
        for i in range(1, len(items)):
            for combo in itertools.combinations(items.keys(), max_length):
                sum = 0
                for name in combo:
                    sum += items[name]
                if max_weight >= sum:
                    combinations.append(combo)
    return combinations


def print_combo (list):
    for item in list:
        print(*item, end=' ')
        sum = 0
        for i in range(len(item)):
            sum += items[item[i]]
        print(sum)
    print()


combo = find_combo(items, max_weight, max_length)
print_combo(combo)
