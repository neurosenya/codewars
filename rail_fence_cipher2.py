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
    rails = [ '' for i in range(n) ]
    # no. of symbols in the first rail
    NoSymbols = len(string)
    rail1 = sum([1 for i in range(0, len(string), (n*2 - 2))])
    LeftOverSymbols = NoSymbols - ((rail1 - 1) * 2 * (n - 2)  # no. of symbols in the (2,..,n-2)
                    + rail1 + (rail1 - 1 )) # no. of symbols in the first and last rail
    # filling 1st and last rail
    rails[0] += string[:rail1]
    # filling the rails (2, ..., n-1) with symbols
    start = rail1
    finish = rail1 + 2*(rail1-1)
    if LeftOverSymbols:
        NoOfDoubleSymbols = LeftOverSymbols - (n-1)
        StartDoubles = (n-1) - NoOfDoubleSymbols
    #print('StartDoubles: %s, LeftOverSymbols: %s' % (StartDoubles, LeftOverSymbols))
    for i in range(1, n-1):
        rails[i] += string[start:finish]
        if LeftOverSymbols > 0:
            if i < StartDoubles and StartDoubles > 0:
                rails[i] += string[finish]
                finish += 1
                start = finish
                finish += 2 * (rail1 - 1)
                LeftOverSymbols -= 1
            elif i >= StartDoubles and StartDoubles > 0:
                #print(i)
                rails[i] += string[finish:finish+2]
                finish += 2
                start = finish
                finish += 2 * (rail1 - 1)
                LeftOverSymbols -= 2
        else:
            start = finish
            finish += 2 * (rail1 - 1)
        print(rails)
    if LeftOverSymbols == 1:
        LastRail = rail1
        rails[-1] += string[-LastRail:]
        LeftOverSymbols -= 1
    else:
        rails[-1] = string[-(rail1 - 1):]
    decoded = ''
    rails_cycle = cycle([i for i in range(n)] + [i for i in range(n-2, 0, -1)])
    while len(decoded) < NoSymbols:
        rail = next(rails_cycle)
        decoded += rails[rail][0]
        rails[rail] = rails[rail][1:]
    return ''.join(decoded)



string = "WVOEOETNACRACRSEEEEIDLDF"
print(len(string))
print( decode_rail_fence_cipher(string, 6) )
