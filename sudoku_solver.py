import numpy as np

def sudoku_solver(puzzle):
    puzzle3d = np.zeros((9, 9, 10))
    puzzle3d[:, :, 0] = np.array(puzzle)
    digits = set(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def sudoku(puzzle3d):
        for row in range(9):
            for col in range(9):
                if puzzle3d[row, col, 0] == 0:
                    # finding possible digits by looking at the row and column
                    possible_digits = digits - set(puzzle3d[:, col, 0]) - set(puzzle3d[row, :, 0])
                    # by looking at the block of the cell
                    upper_row = ((row // 3) + 1) * 3
                    upper_col = ((col // 3) + 1) * 3
                    lower_row = upper_row - 3
                    lower_col = upper_col - 3
                    possible_digits -= set(puzzle3d[lower_row:upper_row, lower_col:upper_col, 0].flatten())
                    no_digits = len(possible_digits)
                    if no_digits == 1:
                        puzzle3d[row, col, 0] = list(possible_digits)[0]
                    else:
                        puzzle3d[row, col, 1:no_digits + 1] = np.array(list(possible_digits))
                    #print(row, col)
        if np.any(puzzle3d[:, :, 0] == 0):
            #print(puzzle3d[:,:,0])
            return sudoku(puzzle3d)
        return puzzle3d
    return sudoku(puzzle3d)[:, :, 0]



puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
print(sudoku_solver(puzzle))
