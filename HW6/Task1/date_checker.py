# В модуль с проверкой даты!
# - добавьте возможность запуска в терминале с передачей даты на проверку.
import sys


def _leap_year (year):
    res = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        res = True
    return res


def my_date (date: str):
    check = False
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            check = True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            check = True
        elif month == 2:
            if _leap_year(year):
                if 1 <= day <= 29:
                    check = True
            else:
                if 1 <= day <= 28:
                    check = True
    res = f'Настоящий: {check}, високосный: {_leap_year(year)}'
    return res


if __name__ == '__main__':
    print(my_date(sys.argv[1]))
