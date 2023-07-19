def fib (reps):
    first_num, second_num = 1, 1
    res = 1
    for i in range(reps):
        yield first_num
        res = first_num + second_num
        first_num = second_num
        second_num = res



reps = int(input('Сколько чисел вывести?\n'))

for item in fib(reps):
    print(item, end=' ')
