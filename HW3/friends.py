# HW3. Task 1. Friends

friends = {
    'Kolya': ('knife', 'lighter', 'rope', 'axe', 'cup', 'spoon'),
    'Tolya': ('lighter', 'fishing rod', 'cup'),
    'Petya': ('knife', 'rope', 'cup', 'fork')
}

res = list()
list_of_names = list(friends.keys())

list_for_all = [set(friends[name]) for name in list_of_names]

all_items_set = set() | list_for_all[0]

for i in range(1, len(list_for_all)):
    all_items_set.intersection_update(list_for_all[i])
res.append(all_items_set)

all_set = list_for_all[1] | list_for_all[2]
unique_for_all = list(all_set ^ list_for_all[0])

def distribution(mode):
    res = dict()
    if mode == 1:
        for name in list_of_names:
            help_list = []
            for item in unique_for_all:
                if item in friends[name]:
                    help_list.append(item)
            res[name] = tuple(help_list)
    else:
        for name in list_of_names:
            help_list = []
            for item in all_but_not:
                if item not in friends[name]:
                    help_list.append(item)
            res[name] = tuple(help_list)
    return  res


all_list = list()
for st in list_for_all:
    all_list.extend(list(st))

all_but_not = list()
for item in all_list:
    if all_list.count(item) == len(friends.keys()) - 1 and item not in all_but_not:
        all_but_not.append(item)

res.append(distribution(1))
res.append(distribution(2))
print(f'Все друзья взяли: {res[0]}\n'
      f'Только один друг взял: {res[1]}\n'
      f'Единственный не взял: {res[2]}')
