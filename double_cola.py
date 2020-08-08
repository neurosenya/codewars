import math


def who_is_next(names, r):
    N_names = len(names)
    if r > N_names:
        n = math.floor(math.log(r*2/N_names, 2))
        S_current = N_names*2**(n) - N_names
        S_previous = N_names*2**(n-1) - N_names
        dS = S_current - S_previous
        if S_current < r:
            n += 1
            S_current = N_names*2**(n) - N_names
            S_previous = N_names*2**(n-1) - N_names
            dS = S_current - S_previous
        l = dS/N_names
        for i in range(1, N_names+1):
            if r <= S_previous + i*l:
                return names[i-1]
    if r <= N_names:
        return names[r-1]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]



