#!/usr/bin/python3
# 102-magic_calculation.py
# Adeboye Victor Oyekanmi <adeboyevictor18@gmail.com>


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)