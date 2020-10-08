import numpy as np

start = 0
def spiral(size):
    spiral = np.zeros((size, size))
    s  = 0
    e = size-1
    def move(spiral, s, e):
        while e-s >= 4:
            spiral[s, s:e+1] = np.ones((e+1-s))
            spiral[s:e+1, e] = np.ones((e+1-s))
            spiral[e, s:e+1] = np.ones((e+1-s))
            spiral[s+2:e+1, s] = np.ones((e+1-2-s))
            spiral[s+2, s+1] = 1
            s += 2
            e -= 2
        if spiral[s, e] != 1:
            spiral[s, s:e+1] = np.ones((e+1-s))
        if spiral[e, e] != 1:
            spiral[s:e+1, e] = np.ones((e+1-s))
        if spiral[e, s] != 1 and spiral[e-1, s] != 1:
            spiral[e, s:e+1] = np.ones((e+1-s))
        if spiral[s+2, s] != 1:
            spiral[s+2:e+1, s] = np.ones((e+1-2-s))
        return spiral
        spiral[s, s-1] = 0
    return move(spiral, s, e)
#array =
#[[1,1,1,1,1,1,1,1],
# [0,0,0,0,0,0,0,1],
# [1,1,1,1,1,1,0,1],
# [1,0,0,0,0,1,0,1],
# [1,0,1,0,0,1,0,1],
# [1,0,1,1,1,1,0,1],
# [1,0,0,0,0,0,0,1],
# [1,1,1,1,1,1,1,1]]

print(spiral(6))
