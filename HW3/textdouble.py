with open('text.txt', 'r') as fw:
    my_string = fw.read()

my_string = my_string.lower()
for chr in my_string:
    if chr in '!@#$%^&*()_+=-`~:;[]{},—.<>?/\|\n"':
        my_string = my_string.replace(chr, '')

my_list = my_string.split(' ')
my_list = list(filter(None, my_list))
for item in my_list:
    if item == ' ':
        my_list.remove(item)

my_dict = dict()
for item in my_list:
    my_dict[item] = my_list.count(item)

my_other_dict = {k: v for k, v in sorted(my_dict.items(), key = lambda item: item[1], reverse=True)}

count = 0
for key in my_other_dict:
    if count < 10:
        print(f'{key}:{my_other_dict[key]}')
        count += 1
    else:
        break
