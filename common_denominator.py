from math import sqrt
import numpy as np
import time
start = time.time()


def find_primes(lst):
    divs = []
    for num in lst:
        for i in range(2, num+1):
            if num % i == 0:
                if num == i:
                    divs.append(num)
                    break
                else:
                    divs.append(int(i))
                    divs.append(int(num / i))
                    break
    if len(divs) == len(lst):
        return lst
    else:
        return find_primes(divs)

def convertFracts(r):
    if len(r) < 2:
        return r
    denoms = sorted([i[1] for i in r])
    denoms_primes = []
    for i in denoms:
        denoms_primes.append(find_primes([i]))

    required_primes = dict()
    for i in denoms_primes:
        for j in i:
            if j not in required_primes:
                required_primes[j] = i.count(j)
            else:
                c = i.count(j)
                if c > required_primes[j]:
                    required_primes[j] = c
    common_denominator = 1
    for k,v in required_primes.items():
        common_denominator *= k**v
    for i in r:
        i[0] = int((common_denominator * i[0]) / i[1])
        i[1] = int(common_denominator)
    return r




print(convertFracts([[27115, 5262], [87546, 1111111], [43216, 255689]]))
print("\n_____Execution time is %s s______\n" % (time.time() -start))
