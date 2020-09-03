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

board =[[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]]
print(valid_solution(board))

