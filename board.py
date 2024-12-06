import sys

# make winning row of characters uppercase
def get_winner(grid):
    # check lines and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '':
            grid[i][0] = grid[i][1] = grid[i][2] = grid[i][0].upper()
            return

        elif grid[0][i] == grid[1][i] == grid[2][i] != '':
            grid[0][i] = grid[1][i] = grid[2][i] = grid[0][i].upper()
            return

    # check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        grid[0][0] = grid[1][1] = grid[2][2] = grid[0][0].upper()
        return

    elif grid[2][0] == grid[1][1] == grid[0][2] != '':
        grid[2][0] = grid[1][1] = grid[0][2] = grid[2][0].upper()
        return


# return 'x', 'o' or "draw" if game ended and '' otherwise
def check_win(grid):
    draw = True

    # check lines and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '':
            return grid[i][0]

        elif grid[0][i] == grid[1][i] == grid[2][i] != '':
            return grid[0][i]

        # check if there is at least one empty cell
        if grid[i][0] == '' or grid[i][1] == '' or grid[i][2] == '':
            draw = False

    # check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        return grid[0][0]

    elif grid[2][0] == grid[1][1] == grid[0][2] != '':
        return grid[2][0]

    # no winning row
    if draw:
        return "draw"
    else:
        return ''


# find how good last move was for {character} -10 being the worst and 10 the best
def evaluate(grid, character):
    winner = check_win(grid)

    # the best move is the one that wins, worst is the one that loses, draw is just 0
    if winner == character:
        return 10
    elif winner == "draw":
        return 0
    elif winner != '':
        return -10

    # find best move
    best = -11 # -inf by default
    for i in range(3):
        for j in range(3):
            # skip if cell is not empty
            if grid[i][j] != '':
                continue

            # try placing a character in cell
            grid[i][j] = character

            # find how good this move will be for the opponent and take a negative of it
            # (to find how good this move is for {character})
            if character == 'x':
                cost = -evaluate(grid, 'o')
            else:
                cost = -evaluate(grid, 'x')

            # reset cell
            grid[i][j] = ''
            
            # subtract (or add if negative) 1 for how far this move is from the win
            # (the closer to one the farther win is, and the worse this move is)
            if cost < 0:
                cost += 1
            elif cost > 0:
                cost -= 1

            # new best move found
            if cost > best:
                best = cost

    # return how good this move is
    return best


def predict(grid, character):
    # Pu-Pu-Pu-...-Pu-Pu
    sys.setrecursionlimit(50_000)

    # check if grid is empty
    empty = True
    for i in range(3):
        for j in range(3):
            if grid[i][j] != '':
                empty = False

    # if grid is empty place {character} at center
    if empty:
        return 1, 1

    # x and y of the best move
    best_x, best_y = -1, -1

    # find best move
    best = -11
    for i in range(3):
        for j in range(3):
            # skip if cell is not empty
            if grid[i][j] != '':
                continue

            # try placing a character in cell
            grid[i][j] = character

            # find how good this move will be for the opponent and take a negative of it
            # (to find how good this move is for {character})
            if character == 'x':
                cost = -evaluate(grid, 'o')
            else:
                cost = -evaluate(grid, 'x')

            # reset cell
            grid[i][j] = ''

            # new best move found
            if cost > best:
                best = cost
                best_x, best_y = (i, j)

    # return best move
    return best_x, best_y
