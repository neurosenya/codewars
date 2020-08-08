from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))

    res = []
    for c in set(list(c1.keys()) + list(c2.keys())):
        n1, n2 = c1.get(c), c2.get(c)
        if n1 > 1 or n2 > 1:
            if n1 > n2:
                res.append(('1', c, n1))
            elif n2 > n1:
                res.append(('2', c, n2))
            else:
                res.append(('=', c, n1))

    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))

s1 = "Are they here"
s2 = "Are they here"
print(mix(s1, s2))
