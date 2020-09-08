'''
Source: codewars.com
Author: Blind4Basics
'''
import re

P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

def expand(expr):
    # a - is integer part of the first term
    # b - in integer part of the second term
    # v - is the str part of the first term
    # e - is the power of the exponent
    a, v, b, e = P.findall(expr)[0]

    # This is if power is equal to 0
    if e == '0':
        return '1'

    # o - is the list, which contains integer part of the first term `int(a)` and the second `int(b)`
    o = [int(a != '-' and a or a and '-1' or '1') , int(b)]

    # e - converted string power to the integer
    # p - is a copy of `o`
    e, p = int(e), o[:]

    for _ in range(e-1):
        p.append(0)
        p = [o[0] * coef + p[i-1]*o[1] for i, coef in enumerate(p)]
    res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef
            in enumerate(p) if coef)

    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
