def LCM(denoms):
    denoms.sort()
    denoms_product = 1
    for i in denoms:
        denoms_product *= i
    for i in range(denoms[-1], denoms_product+1, denoms[-1]):
        if all([True if i % denom == 0 else False for denom in denoms]):
            return i
print(LCM([6,9]))
