from collections import Counter
from math import sqrt


def primeFactors(number):
    L = []
    message = ''
    x = 3
    while number % 2 == 0:
        number /= 2
        L.append(2)
    # print(number)
    # This algo can also return largest prime factor
    for x in range(3, int(sqrt(number))+1):
        # print(x)
        while number % x == 0:
            number /= x
            # print(x)
            L.append(x)

    if number != 1:
        L.append(int(number))
    dic = dict(Counter(L))
    for k, v in dic.items():
        message += f'({k}**{v})' if v != 1 else f'({k})'
    return message
