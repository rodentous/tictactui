from tests import *
from board import *
from draw import *


# run tests, abort if any failed
run_tests()
print(term.clear)

# block text input and hide cursor
with term.cbreak(), term.hidden_cursor():

    def get_input():
        # read input
        input_key = term.inkey()

        # quit if 'q' is pressed
        if input_key == 'q':
            print(term.clear)
            exit(0)

        # restart if 'r' is pressed
        if input_key == 'r':
            print(term.clear)
            select_character()

        return input_key


    # selecting character phase
    def select_character():
        selected_option = 'x'

        # draw menu and selection screen
        print(term.clear)
        draw_menu()
        draw_character_selection(selected_option)

        while True:
            # get input
            input_key = get_input()

            # move selection
            if repr(input_key) == "KEY_UP":
                selected_option = 'x'

            if repr(input_key) == "KEY_DOWN":
                selected_option = 'o'

            # selected
            if repr(input_key) == "KEY_ENTER":
                # set player and computer
                player = selected_option

                # ask to fill board and start main game
                select_fill(player)

            # update selection text
            draw_character_selection(selected_option)


    # selecting whether to fill grid or start from zero
    def select_fill(player):
        selected_option = "no"

        # draw menu and selection screen
        print(term.clear)
        draw_menu()
        draw_fill_selection(selected_option)

        while True:
            # get input
            input_key = get_input()

            # move selection
            if repr(input_key) == "KEY_UP":
                selected_option = "no"

            if repr(input_key) == "KEY_DOWN":
                selected_option = "yes"

            # selected
            if repr(input_key) == "KEY_ENTER":
                # clear screen and fill grid if "yes" selected
                if selected_option == "yes":
                    grid = fill_grid()
                else:
                    grid = [['' for i in range(3)] for i in range(3)]

                # clear screen and start main game
                main(grid, player)

            # update selection text
            draw_fill_selection(selected_option)


    # fill grid with starting configuration
    def fill_grid():
        grid = [['' for i in range(3)] for i in range(3)]

        # selected cell
        (selected_x, selected_y) = 1, 1
        
        # draw controls and grid
        print(term.clear)
        draw_fill_controls()
        draw_grid(selected_x, selected_y, grid)

        while True:
            # get input
            input_key = get_input()

            # select cell
            if repr(input_key) == "KEY_LEFT" and selected_x != 0:
                selected_x -= 1
            if repr(input_key) == "KEY_RIGHT" and selected_x != 2:
                selected_x += 1
            if repr(input_key) == "KEY_UP" and selected_y != 0:
                selected_y -= 1
            if repr(input_key) == "KEY_DOWN" and selected_y != 2:
                selected_y += 1

            # fill cell with user input
            if input_key == 'x':
                grid[selected_x][selected_y] = 'x'
            elif input_key == 'o':
                grid[selected_x][selected_y] = 'o'
            elif input_key == ' ':
                grid[selected_x][selected_y] = ''
            elif repr(input_key) == "KEY_ENTER":
                break

            # draw grid with current cell selected
            draw_grid(selected_x, selected_y, grid)

        return grid


    # check if game is finished
    def check(grid, player):
        winner = check_win(grid)
        if winner != '':
            # mark winning characters red
            get_winner(grid)
            draw_grid(-1, -1, grid)

            # finish game
            win(winner, player)


    # main game loop
    def main(grid, player):
        # selected cell
        selected_x, selected_y = 1, 1

        # draw menu and grid
        print(term.clear)
        draw_menu()
        draw_grid(selected_x, selected_y, grid)

        # select character for computer
        if player == 'x':
            computer = 'o'
        else:
            computer = 'x'

        # check if game was already finished
        check(grid, player)

        # computer's first move
        if computer == 'x':
            x, y = predict(grid, computer)
            grid[x][y] = computer
            check(grid, player) # check if it won
            draw_grid(selected_x, selected_y, grid) # redraw grid

        while True:
            # get input
            input_key = get_input()

            # select cell
            if repr(input_key) == "KEY_LEFT" and selected_x != 0:
                selected_x -= 1
            if repr(input_key) == "KEY_RIGHT" and selected_x != 2:
                selected_x += 1
            if repr(input_key) == "KEY_UP" and selected_y != 0:
                selected_y -= 1
            if repr(input_key) == "KEY_DOWN" and selected_y != 2:
                selected_y += 1

            # player made a move
            if repr(input_key) == "KEY_ENTER" and grid[selected_x][selected_y] == '':
                # place a character
                grid[selected_x][selected_y] = player

                # check if game ended
                check(grid, player)

                # find best next move for computer
                x, y = predict(grid, computer)
                grid[x][y] = computer

                # check if game ended again
                check(grid, player)

            # update grid
            draw_grid(selected_x, selected_y, grid)


    # final screen
    def win(winner, player):
        # draw winner
        draw_winner(winner, player)

        while True:
            get_input()


    # start game
    select_character()
