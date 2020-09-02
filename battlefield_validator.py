import numpy as np

def validate_battlefield(field):
    field = np.array(field)
    # Ensures that there is exactly 20 occuppied cells
    if np.sum(field) != 20:
       return False
    # Adding extra zero layer on the sides of the matrix
    for i in range(10):
        field_new = np.zeros((12, 12))
        field_new[1:11, 1:11] = field

    # Describing ships
    submarine = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    destroyer = np.array([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    battleship = np.array([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]])
    cruiser = np.array([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]])
    ships = [submarine, destroyer, battleship, cruiser]
    required_counts = [4, 3, 1, 2]

    # Function that will search for a ship in a field
    def count_ships(ship):
        c = 0
        n, m = np.shape(ship)
        for row in range(12 - (m-1)):
            for col in range(12 - (n-1)):
                if np.array_equal(field_new[row:row+m, col:col+n], ship.T):
                    c += 1
        if n != m: # submarine is a squre
            for row in range(12 - (n-1)):
                for col in range(12 - (m-1)):
                    if np.array_equal(field_new[row:row+n, col:col+m], ship):
                        c += 1
        return c
    counted_ships = [count_ships(ship) for ship in ships]
    if counted_ships == required_counts:
        return True
    else:
        return False

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))
