from itertools import cycle


def encode_rail_fence_cipher(string, n):
    rails = ['' for i in range(n)]
    rails_cycle = cycle([i for i in range(n)] + [i for i in range(n-2, 0, -1)])
    while string:
        rail = next(rails_cycle)
        rails[rail] += string[0]
        string = string[1:]
    return ''.join(rails)


def decode_rail_fence_cipher(string, n):
    pass
string ="WEAREDISCOVEREDFLEEATONCE"
print( encode_rail_fence_cipher(string, 3) )
