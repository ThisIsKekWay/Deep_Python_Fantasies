# Deep python. Homework 1.
# Task 2.
# Напишите код, который запрашивает число и сообщает является
# ли оно простым или составным. Используйте правило для 
# проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод 
# отрицательных чисел и чисел больше 100 тысяч.
def is_simple (number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k += 1

    if k < 1:
        res = 'The number is simple'
    else:
        res = "The number isn't so simple"
    return res


while True:
    try:
        number = int(input('Enter number. For exit enter 0\n'))
        if number == 0:
            print('Exiting...')
            break
        if 0 > number > 100_000:
            raise Exception
        ans = is_simple(number)
        print(ans)
    except Exception:
        print('Data is corrupted or over 100 000 or below zero')
