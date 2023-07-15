import random


def transpon (list):
    res = []
    for i in range(len(list)):
        pre_res = []
        for j in range(len(list[i])):
            pre_res.append(list[j][i])
        res.append(pre_res)
    return res


def print_mat (list, word):
    print(word)
    for row in list:
        print(*row)


matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print_mat(matrix, 'Созданная матрица:')
trans_mat = transpon(matrix)
print_mat(trans_mat, 'Транспонированная матрица:')
