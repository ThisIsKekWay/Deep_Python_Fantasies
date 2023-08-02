import json
import random as r
from functools import wraps
from pathlib import Path
from typing import Callable
import csv


def coef_reader (func: Callable):
    @wraps(func)
    def wrapper_a ():
        with open('coefs.csv', 'r', encoding='utf-8') as file:
            fr = csv.reader(file)
            for i, line in enumerate(fr):
                if i % 2 != 0:
                    continue
                else:
                    params = line
                    res = func(params)
        return res

    return wrapper_a


def result_writer (func: Callable):
    file = Path(f"{func.__name__}.json")
    data = []
    def wrapper_b (*args):
        res = func(*args)
        d = {f'{args}': res, }
        data.append(d)

        with open(file, 'w', encoding='utf-8') as fw:
            json.dump(data, fw, ensure_ascii=False, indent=2)
        return res

    return wrapper_b


@coef_reader
@result_writer
def quadratic_equation (list_of_coefs: list[float]) -> tuple[float]:
    a, b, c = float(list_of_coefs[0]), float(list_of_coefs[1]), float(list_of_coefs[2])
    d = b ** 2 - 4 * a * c
    if d < 0:
        res = "COMPLEX RESULT, JSON CAN'T AFFORD IT!"
    else:
        res = tuple({(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)})
    return res


def coef_generator ():
    file_len = r.randint(100, 1000)
    res = [(
        r.uniform(-1000, 1000).__round__(2),
        r.uniform(-1000, 1000).__round__(2),
        r.uniform(-1000, 1000).__round__(2)
    ) for _ in range(file_len)]
    with open('coefs.csv', 'w', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(res)


if __name__ == '__main__':
    coef_generator()
    quadratic_equation()
