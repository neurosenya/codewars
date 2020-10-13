# Solution from codewars

from itertools import chain

def fencer(string, n):
    rails = [ [] for _ in range(n) ]
    rail, dx = 0, 1
    for c in string:
        rails[rail].append(c)
        if rail == n-1 and dx > 0 or rail == 0 and dx < 0:
            dx *= -1
        rail += dx
    return chain.from_iterable(rails)

def encode_rail_fence_cipher(s, n):
    return ''.join( fencer(s, n) )

def decode_rail_fence_cipher(s, n):
    lst = [''] * len(s)
    for c, i in zip( s, fencer(range(len(s), n)) ):
        lst[i] = c
    return ''.join(lst)
