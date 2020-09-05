import numpy as np

def valid_solution(board):
    board = np.array(board)
    digits = set(np.array(range(1, 10))) # from 1 to 9
    n, m = np.shape(board)
    for i in range(n):
        if np.all(set(board[i,:]) != digits):
            return False
    for i in range(m):
        if np.all(set(board[:,i]) != digits):
            return False
    # checking blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(board[i:i+3, j:j+3])
            if np.all(set(board[i:i+3, j:j+3].flatten()) != digits):
                return False

    return True
board = [[6, 4, 5, 1, 9, 8, 2, 7, 3],
[1, 2, 7, 3, 4, 6, 5, 9, 8],
[8, 9, 3, 2, 7, 5, 4, 6, 1],
[5, 1, 4, 6, 2, 7, 3, 8, 9],
[2, 3, 8, 4, 1, 9, 6, 5, 7],
[7, 6, 9, 8, 5, 3, 1, 4, 2],
[4, 5, 1, 7, 8, 2, 9, 3, 6],
[9, 8, 6, 5, 3, 1, 7, 2, 4],
[3, 7, 2, 9, 6, 4, 1, 8, 5]]
print(valid_solution(board))

