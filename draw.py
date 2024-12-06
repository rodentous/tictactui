from blessed import Terminal


# characters foe drawing boxes
horizontal_corner = '━'
vertical_corner = '┃'
left_up_corner = '┏'
right_up_corner = '┓'
left_down_corner = '┗'
right_down_corner = '┛'


# initialize terminal
term = Terminal()
print(term.home + term.clear) # clear screen and reset cursor


# draw box
def draw_box(x, y, size_x, size_y):
    # draw corners
    for i in range(x, x + size_x):
        print(term.move_xy(i, y), end='')

        # draw left corner
        if i == x:
            # upper and bottom turns
            print(left_up_corner, end='')
            print(term.move_xy(i, y + size_y - 1) + left_down_corner, end='')

            # left corners
            for j in range(y + 1, y + size_y - 1):
                print(term.move_xy(i, j) + vertical_corner, end='')

        # draw right corner
        elif i == x + size_x - 1:
            # upper and bottom turn
            print(right_up_corner, end='')
            print(term.move_xy(i, y + size_y - 1) + right_down_corner, end='')

            # right corner
            for j in range(y + 1, y + size_y - 1):
                print(term.move_xy(i, j) + vertical_corner, end='')

        # draw upper and bottom corners
        else:
            print(horizontal_corner + term.move_xy(i, y + size_y - 1) + horizontal_corner)


# draw character selection options
def draw_character_selection(selected_option):
    # check which option is selected and color it yellow
    if selected_option == 'x':
        print(term.move_xy(25, 15) + term.yellow + "Play as X" + term.normal)
        print(term.move_xy(25, 16) + "Play as O")
    else:
        print(term.move_xy(25, 15) + "Play as X")
        print(term.move_xy(25, 16) + term.yellow + "Play as O" + term.normal)


# draw fill options
def draw_fill_selection(selected_option):
    # check which option is selected and color it yellow
    if selected_option == "no":
        print(term.move_xy(20, 15) + term.yellow + "Start with empty grid" + term.normal)
        print(term.move_xy(25, 16) + "Fill grid")
    else:
        print(term.move_xy(20, 15) + "Start with empty grid")
        print(term.move_xy(25, 16) + term.yellow + "Fill grid" + term.normal)


# draw title and controls
def draw_menu():
    print(term.home + term.blue + """

            _______ _   _______      _______    _ 
           |__   __(_) |__   __|    |__   __|  (_)
              | |   _  ___| | __ _  ___| |_   _ _ 
              | |  | |/ __| |/ _` |/ __| | | | | |
              | |  | | (__| | (_| | (__| | |_| | |
              |_|  |_|\___|_|\__,_|\___|_|\__,_|_|
    """ + term.normal)

    # print controls
    print(term.move_xy(60, 11) + "Q                  - quit")
    print(term.move_xy(60, 12) + "R                  - restart")
    print(term.move_xy(60, 13) + "<ARROWS>           - select")
    print(term.move_xy(60, 14) + "<ENTER>            - confirm")

    # draw surrounding box
    draw_box(0, 0, 100, 30)


# print controls for filling the board
def draw_fill_controls():
    print(term.home + term.yellow + """

    ______ _ _ _   _______ _            ____                      _ _ 
   |  ____(_) | | |__   __| |          |  _ \                    | | |
   | |__   _| | |    | |  | |__   ___  | |_) | ___   __ _ _ __ __| | |
   |  __| | | | |    | |  | '_ \ / _ \ |  _ < / _ \ / _` | '__/ _` | |
   | |    | | | |    | |  | | | |  __/ | |_) | (_) | (_| | | | (_| |_|
   |_|    |_|_|_|    |_|  |_| |_|\___| |____/ \___/ \__,_|_|  \__,_(_)
    """ + term.normal)

    # print controls
    print(term.move_xy(60, 11) + "Q                  - quit")
    print(term.move_xy(60, 12) + "R                  - restart")
    print(term.move_xy(60, 13) + "<ARROWS>           - select")
    print(term.move_xy(60, 14) + "X/O/<SPACE>        - place")
    print(term.move_xy(60, 15) + "<ENTER>            - confirm")

    # draw surrounding box
    draw_box(0, 0, 100, 30)


# draw winner text over title
def draw_winner(winner, player):
    # self explanatory
    if winner == "draw":
        print(term.home + term.yellow + """

             _____                     _ _ _ _ _ _ 
            |  __ \                   | | | | | | |
            | |  | |_ __ __ ___      _| | | | | | |
            | |  | | '__/ _` \ \ /\ / / | | | | | |
            | |__| | | | (_| |\ V  V /|_|_|_|_|_|_|
            |_____/|_|  \__,_| \_/\_/ (_|_|_|_|_|_)
        """ + term.normal)

    elif winner == player:
        print(term.home + term.green + """

        __     __          __          __        ___  _ 
        \ \   / /          \ \        / /       |__ \| |
         \ \_/ /__  _   _   \ \  /\  / /__  _ __   ) | |
          \   / _ \| | | |   \ \/  \/ / _ \| '_ \ / /| |
           | | (_) | |_| |    \  /\  / (_) | | | |_| |_|
           |_|\___/ \__,_|     \/  \/ \___/|_| |_(_) (_)
        """ + term.normal)

    else:
        print(term.home + term.red + """

          __     __           _               _   _ _ 
          \ \   / /          | |             | | | | |
           \ \_/ /__  _   _  | |     ___  ___| |_| | |
            \   / _ \| | | | | |    / _ \/ __| __| | |
             | | (_) | |_| | | |___| (_) \__ \ |_|_|_|
             |_|\___/ \__,_| |______\___/|___/\__(_|_)
        """ + term.normal)

    # draw surrounding box
    draw_box(0, 0, 100, 30)



# draw X/O/' ' at (x, y)
def draw_x(x, y):
    print(term.move_xy(x + 3, y + 1) + "▚  ▞")
    print(term.move_xy(x + 3, y + 2) + " ▞▗ ")
    print(term.move_xy(x + 3, y + 3) + "▞  ▚")

def draw_o(x, y):
    print(term.move_xy(x + 3, y + 1) + "▞▀▀▚")
    print(term.move_xy(x + 3, y + 2) + "▌  ▐")
    print(term.move_xy(x + 3, y + 3) + "▚▄▄▞")

def draw_space(x, y):
    print(term.move_xy(x + 3, y + 1) + "    ")
    print(term.move_xy(x + 3, y + 2) + "    ")
    print(term.move_xy(x + 3, y + 3) + "    ")


# draw a single square cell in the grid with 'x', 'o' or '' inside
def draw_cell(x, y, character=''):
    # draw a cell
    draw_box(x, y, 10, 5)

    # upper character means that its in a winning row / column
    # color it red
    if character.isupper():
        print(term.red)

    # draw X/O/' ' if cell is filled
    if character == 'x' or character == 'X':
        draw_x(x, y)
        print(term.normal) # reset color

    elif character == 'o' or character == 'O':
        draw_o(x, y)
        print(term.normal) # reset color

    elif character == '':
        draw_space(x, y)


# draw 3x3 grid of cells and mark currently selected cell
def draw_grid(current_x, current_y, grid):
    # grid left-up corner position
    x, y = 15, 10

    for i in range(3):
        for j in range(3):
            # color currently selected cell yellow
            if i == current_x and j == current_y:
                print(term.yellow)

            # draw (i, j) cell
            draw_cell(x + i * 11, y + j * 5, grid[i][j])
            print(term.normal) # reset color
