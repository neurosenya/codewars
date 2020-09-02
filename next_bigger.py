n = 236041
def next_bigger(n):
    left = list(str(n))[::-1]
    if left == sorted(left):
        return -1
    for i in range(len(left)-1):
        swap_idx = i
        print(left[i], left)
        if int(left[swap_idx]) > int(left[i+1]):
            for j in range(i):
                if int(left[j]) > int(left[i+1]) and int(left[j]) < int(left[swap_idx]):
                    if j < swap_idx:
                        swap_idx = j

            left[swap_idx], left[i+1] = left[i+1], left[swap_idx]
            pivot = i+1
            break
    print(sorted(left[0:pivot], key=lambda x: int(x) ))
    next_bigger = sorted(left[0:pivot], key=lambda x: int(x), reverse=True ) + left[pivot:]
    print(next_bigger)
    return int(''.join(next_bigger[::-1]))
print(n)
print(next_bigger(n))
