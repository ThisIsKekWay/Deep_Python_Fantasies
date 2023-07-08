# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_to (number):
    digits = '0123456789abcdef'
    result = ''
    while number > 0:
        result = digits[number % 16] + result
        number //= 16
    return '0x' + result


number = int(input('Введите число для преобразования\n'))
hex_number = convert_to(number)
print(hex_number, hex(number), sep='\n')
