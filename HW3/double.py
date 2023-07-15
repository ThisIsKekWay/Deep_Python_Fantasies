# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint as rng

print('Я немножк затупил и не понял, надо вывести: все повторяющиеся элементы или только те, '
      'что повторяются только дважды, поэтому наваял оба варианта.')


lst = [rng(1,10) for _ in range(20)]
print(f'Созданный список:\n{lst}')

sub_list = []
for number in lst:
    if lst.count(number) > 1:
        sub_list.append(number)

print('Список элементов, повторяющихся более одного раза:')
print(*set(sub_list))

sub_list = []
for number in lst:
    if lst.count(number) == 2:
        sub_list.append(number)

print('Список элементов, повторяющихся РОВНО ДВА раза (дублирующихся прям вот дублирующихся):')
print(*set(sub_list))