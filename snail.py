import numpy as np

def snail(snail_map):
    snail_map = np.array(snail_map)
    _, n = np.shape(snail_map)
    snail_path = []
    def snail_goes(start=0, end=n):
        if start == end-1:
            snail_path.append(snail_map[start, end-1])
            return snail_path
        for i in range(start, end):
            snail_path.append(snail_map[start, i])
        for i in range(start+1, end):
            snail_path.append(snail_map[i, end-1])
        for i in range(end-2, start-1, -1):
            snail_path.append(snail_map[end-1, i])
        for i in range(end-2, start, -1):
            snail_path.append(snail_map[i, start])
        return snail_goes(start=start+1, end =end - 1 )

    return snail_goes()
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))
