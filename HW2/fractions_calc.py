from fractions import Fraction


def nod (a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def nok (a, b):
    return (a * b) // nod(a, b)


def summ (first_str, second_str):
    first = list(map(int, first_str.split('/')))
    second = list(map(int, second_str.split('/')))
    sub_first = first[:]
    sub_second = second[:]
    lcm = nok(first[1], second[1])
    first[0] = first[0] * (lcm // first[1])
    second[0] = second[0] * (lcm // second[1])
    res = f'{first[0] + second[0]}/{lcm}'
    print(f'{sub_first[0]}/{sub_first[1]} + {sub_second[0]}/{sub_second[1]} '
          f'= {first[0]}/{first[1]} + {second[0]}/{second[1]} = {res}')
    return res


def mult (first_str, second_str):
    first = list(map(int, first_str.split('/')))
    second = list(map(int, second_str.split('/')))
    sub_first = first[:]
    sub_second = second[:]
    res = f'{first[0] * second[0]}/{first[1] * second[1]}'
    print(f'{sub_first[0]}/{sub_first[1]} * {sub_second[0]}/{sub_second[1]} = {res}')
    return res


first_frac = input(f'Введите первую дробь в виде числитель/знаменатель\n')
second_frac = input(f'Введите вторую дробь в виде числитель/знаменатель\n')
f_frac = Fraction(first_frac)
s_frac = Fraction(second_frac)

summ(first_frac, second_frac)
mult(first_frac, second_frac)

print(f'Проверка\n'
      f'{f_frac + s_frac}\n'
      f'{f_frac * s_frac}')
