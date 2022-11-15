import string
from random import sample

SYMBOLS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def get_random_password(n=8) -> str:
    if not isinstance(n, int):
        raise TypeError(f'''Функция принимает только целые числа, {type(n)} 
        не подходит для ввода''')
    if n < 0:
        raise TypeError('Функция принимает только положительные числа')

    symbols_for_pass = sample(SYMBOLS, n)
    password = ''.join(symbols_for_pass)
    return password


print(get_random_password())
