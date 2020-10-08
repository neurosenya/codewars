from itertools import cycle

def encode_rail_fence_cipher(string, n):
    if string == '':
        return ''
    m = n*2 - 2 # number of element to iterate once through all rails 
    encoded = string[0]
    rails = ['' for i in range(n)]
    rails[0] += string[0]
    for idx in range(m, len(string), m):
        rails[0] += string[idx]
        end = idx-1
        start = idx - (m-1)
        for rail in range(1, n):
            if start == end:
                rails[rail] += string[start]
            else:
                rails[rail] += string[start]
                rails[rail] += string[end]
            start += 1
            end -= 1
    print(rails)
    return ''.join(i for i in rails)

def decode_rail_fence_cipher(string, n):
    m = n*2 - 2
    r1 = sum([1 for i in range(0, len(string), m)])-1
    print(r1)
    rn = r1
    rb = r1 * 2
    print(rb)
    rails = ['' for i in range(n)]
    rails[0] = [i for i in string[0:r1+1]]
    rails[-1] = [i for i in string[-rn:]]
    start = r1+1
    for r in range(1, n-1):
        rails[r] = [i for i in string[start:start+rb]]
        start += rb
    print(rails)
    ping_pong = cycle([i for i in range(n)] + [i for i in range(n-2, 0, -1)])
    decoded = ''
    idx = None
    lst_fst = [0, n-1]
    idx = next(ping_pong)
    while len(decoded) < len(string):
        decoded += rails[idx][0]
        rails[idx] = rails[idx][1:]
        idx = next(ping_pong)
    return decoded
s = "Hooel,wrdl l"
#print(decode_rail_fence_cipher(s, 3))
s1 = "Hello, world"
print(encode_rail_fence_cipher(s1, 3))
