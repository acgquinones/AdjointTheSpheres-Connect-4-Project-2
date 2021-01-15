"""
File:    proj2_test.py
Author:  Ara Carmel Quinones
Date:    4/28/20
Section: 35
E-mail:  aquinon1@umbc.edu
Description:
You have been chosen to create a version of connect 4.
In this version, there can be forbidden positions, or places that neither x nor o can play.
However, connecting four together is still the way to win, and this can be done vertically,
horizontally, diagonally (or anti-diagonally if you distinguish between the backward diagonal).
"""

from random import randint

PLAYER_ONE = "Player x"
PLAYER_X = 'x'
PLAYER_TWO = "Player o"
PLAYER_O = 'o'
PLAYER_COMPUTER = "Computer o"
SAVE_GAME = "save game"
LOAD_GAME = "load game"
FORBIDDEN_POSITION = '*'
EMPTY_SPACE = ' '
EMPTY_SPACE_PERIOD = '.'
DASH = '--'
EMPTY_LIST = []
PIPE = '|'
NUMBERS_OPTIONS = ['1', '2', '3']
OPTION_ONE = '1'
OPTION_TWO = '2'
OPTION_THREE = '3'
RANDOM_MINIMUM = 1
MAX_DIGIT_INPUT = 2

class AdjoinTheSpheres:

    def __init__(self, player, symbol, board):
        """
        initializes variables for the game

        :param player: the current player
        :param symbol: the symbol of the player
        :param board: an empty board
        """

        self.current_player = player
        self.symbol = symbol
        self.track_moves = []
        self.board = board

    def main_menu(self):
        """
        prints the main menu options
        :return: 1 if Player V Player, 2 for Player vs CPU, or 3 to quit the game
        """
        #prints the menu options to player
        print("AdjoinTheSpheres Main Menu")
        print("\t1) New Game (2 player)\n\t2) New Game (1 player vs computer)\n\t3) Exit Game")
        # asks how they want to play the game
        ask_option = input("Select Option from the Menu: ").strip()
        return ask_option

    def start_game(self):
        """
        asks what map/game/board the player wants to play
        :return: player's current board
        """
        map = input("What game/map do you want to load? ").lower()

        # opens file in read mode
        with open(map, "r") as f:
            board = f.readlines()

        # strips "\n" from each line and add the pipe in the string
        for i in range(len(board)):
            # strip the first element and split it to make list then append it to self.board
            if i == 0:
                self.board.append(board[i].strip("\n").split())
            # this updates what symbol to print on the board
            elif i == 1:
                self.board.append(self.symbol)
            # makes a list so you it can be joined by the | to make a string. This helps with printing the board
            else:
                row_to_list = list(board[i].strip("\n"))
                self.board.append("|".join(row_to_list))

        # prints board
        if self.current_player == PLAYER_ONE:
            game_one.print_board()
        else:
            game_two.print_board()

        return self.board

    def load_game(self):
        """
        asks player if they want to make a move, save the game, or load another game
        :return: 1 if player wins, 0 if player makes the same move, or self.board to keep the game going
        """
        # if current player is computer, this will make random integer
        if self.current_player == PLAYER_COMPUTER:
            move = [randint(RANDOM_MINIMUM, int(self.board[0][0])), randint(RANDOM_MINIMUM, int(self.board[0][1]))]

        # if current player is not computer, ask player what move they want to make
        else:
            move = input(self.current_player + " What move do you want to make? Answer as row (vertical) column (horizontal) or save game or load game? ")
            # check if the move has the correct format
            while len(move.split()) != MAX_DIGIT_INPUT:
                print("Invalid input. Must enter 2 numbers with space.")
                move = input(self.current_player + " What move do you want to make? Answer as row (vertical) column (horizontal) or save game or load game? ")

        # save game if player choose to save game
        if move == SAVE_GAME:
            # call player x save_game()
            if self.current_player == PLAYER_ONE:
                save = game_one.save_game()
                return save
            #call player o save_game()
            else:
                save = game_two.save_game()
                return save
        # asks what game player wants to load
        elif move == LOAD_GAME:
            # check if self.board is not empty, overwrite it by setting it to empty list
            if self.board:
                if self.current_player == PLAYER_ONE:
                    # this will set the board to empty to be able to load a new game
                    self.board = []
                    game_one.start_game()
                    return self.board
                else:
                    # this will set the board to empty to be able to load a new game
                    self.board = []
                    game_two.start_game()
                    return self.board

        else:  # the player chose to make a move

            # if the player is CPU, run this because it will return correct input format
            if self.current_player == PLAYER_COMPUTER:
                row = move[0] + 1
                col = move[1] - 1

            # if player is not CPU, split the move to make a list to be able to read input correctly
            else:
                move = move.split()
                # add 1 and subtract 1: program still starts at 0 even if the printed grid starts at 1
                row = int(move[0]) + 1
                col = int(move[1]) - 1
            # this splits row from string to list to remove the pipe and be able to use elements correctly
            board = self.board[row].split(PIPE)  # split the string to remove the '|'
            # tracks the moves player made
            if move not in self.track_moves:
                self.track_moves.append(move)
                # check if move is empty space or a period
                if board[col] == EMPTY_SPACE_PERIOD or board[col] == EMPTY_SPACE:
                    # this marks the board of the player's symbol
                    board[col] = self.symbol
                    # re-join the list again with | to print the board correctly later
                    self.board[row] = PIPE.join(board)

                # check if player wins
                if self.current_player == PLAYER_ONE:
                    check_one = game_one.check_victory()
                    # if player wins, return 1 to end game
                    if check_one == 1:
                        game_one.print_board()
                        self.board = []
                        self.track_moves = []
                        return 1
                    # if not, return self.board to keep the game going
                    else:
                        game_one.print_board()
                        return self.board

                else:
                    check_two = game_two.check_victory()
                    # if player wins, return 1 to end game
                    if check_two == 1:
                        #print board
                        game_two.print_board()
                        self.board = []
                        self.track_moves = []
                        return 1
                    else:
                        # if not, return self.board to keep the game going
                        game_two.print_board()
                        return self.board
            #when move is already is self.track_moves, ask the same user what they want to do again
            else:
                print("You cannot make the same move. Try again.")
                return 0

    def print_board(self):
        """
        this prints the board
        :return: none it's a print board
        """

        # prints 1|2|3|4|5|6|7
        for j in range(int(self.board[0][1]) + 1):
            # this makes the empty space before the first number is printed
            if j == 0:
                print(EMPTY_SPACE, end="")
            # prints the rest of the number with |
            else:
                print(j, end=PIPE)

        # prints dashes
        print("\n", DASH * int(self.board[0][1]))

        # prints grid
        for i in range(len(self.board)):
            if i >= 2:
                row = self.board[i]
                print(i - 1, row)
                print(EMPTY_SPACE, DASH * int(self.board[0][1]))

    def save_game(self):
        """
        You must implement a save game feature.
        Ask for the name that you wish to save to, and save the file to
        that name.
        :return:
        """
        converted_board = []

        name = input("What would you like to save the game as? ").lower()
        # this converts board to the same format it was initially loaded
        for i in range(len(self.board)):
            # makes the list into a string for the first line
            if i == 0:
                converted_board.append(" ".join(self.board[0]))
            # updates the board of the player that played the game or who saved the game
            elif i == 1:
                converted_board.append(self.board[i])
            # removes | from each element and joins then again without any space or character to make a string
            if i > 1:
                board = "".join(self.board[i].split(PIPE))
                converted_board.append(board)
        # this writes and save the current board to the chosen file name
        with open(name, 'w') as save_file:
            for i in range(len(converted_board)):
                # added \n to create a new line for every element written
                save_file.write(converted_board[i] + "\n")

        return self.board

    def check_victory(self):
        """
        a. Display a message with the winning player.
        b. End that game.
        c. Go back to the main menu.
        d. If the board is full, then that is a tie.
        :return: 1 if player wins else 0
        """
        board = []
        height = int(self.board[0][0])
        width = int(self.board[0][1])
        count = 0

        # this ignores element 0 and 1 and splits the self.board on "|" to create the 2D list
        for i in range(len(self.board)):
            if i > 1:
                board.append(self.board[i].split(PIPE))

        # check if the board is full
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == PLAYER_X or board[i][j] == PLAYER_O or board[i][j] == FORBIDDEN_POSITION:
                    count += 1
                    if count == height * width:
                        print("It's a tie! Good game!")
                        return 1

        # check if there's a winner in the row
        # the conditions makes sure that program only check within the board to avoid crashing
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.symbol:
                    if j + 1 <= width - 1:          # condition
                        if board[i][j + 1] == self.symbol:
                            if j + 2 <= width - 1:          # condition
                                if board[i][j + 2] == self.symbol:
                                    if j + 3 <= width - 1:         # condition
                                        if board[i][j + 3] == self.symbol:
                                            print("The winner is", self.current_player)
                                            return 1

        # check if there's a winner in the column
        # the conditions makes sure that program only check within the board to avoid crashing
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.symbol:
                    if i + 1 <= height - 1:     # condition
                        if board[i + 1][j] == self.symbol:
                            if i + 2 <= height - 1:     # condition
                                if board[i + 2][j] == self.symbol:
                                    if i + 3 <= height - 1:    # condition
                                        if board[i + 3][j] == self.symbol:
                                            print("The winner is", self.current_player)
                                            return 1

        # check if there's a winner in the diagonal
        # the conditions makes sure that program only check within the board to avoid crashing
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.symbol:
                    if i + 1 <= height - 1 and j + 1 <= width - 1:  # condition
                        if board[i + 1][j + 1] == self.symbol:
                            if i + 2 <= height - 1 and j + 2 <= width - 1:  # condition
                                if board[i + 2][j + 2] == self.symbol:
                                    if i + 3 <= height - 1 and j + 3 <= width - 1:  # condition
                                        if board[i + 3][j + 3] == self.symbol:
                                            print("The winner is", self.current_player)
                                            return 1

        # check if there's a winner in the anti diagonal
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.symbol:
                    if i + 1 <= height - 1 and j - 1 <= width - 1:  # condition
                        if board[i + 1][j - 1] == self.symbol:
                            if i + 2 <= height - 1 and j - 2 <= width - 1:  # condition
                                if board[i + 2][j - 2] == self.symbol:
                                    if i + 3 <= height - 1 and j - 3 <= width - 1:  # condition
                                        if board[i + 3][j - 3] == self.symbol:
                                            print("The winner is", self.current_player)
                                            return 1

        return 0


if __name__ == '__main__':

    end_program = False
    end_game = False
    grid = []

    while not end_program:
        game_one = AdjoinTheSpheres(PLAYER_ONE, PLAYER_X, grid)
        option = game_one.main_menu()
        # keep asking player how they want to play if they don't enter valid options
        while option not in NUMBERS_OPTIONS:
            print("Invalid choice, try again.")
            option = game_one.main_menu()
        # end the program
        if option == OPTION_THREE:
            end_program = True
        # start game as player vs player
        elif option == OPTION_ONE:
            start = game_one.start_game()
            while not end_game:
                load_one = game_one.load_game()
                # this keeps asking the same player for what move to make if she plays a move that is already made
                while load_one == 0:
                    load_one = game_one.load_game()
                # end the game because there's a winner
                if load_one == 1:
                    end_game = True
                # this is player two's turn
                else:
                    game_two = AdjoinTheSpheres(PLAYER_TWO, PLAYER_O, load_one)
                    load_two = game_two.load_game()
                    # end game, there's a winner
                    if load_two == 1:
                        end_game = True
                    # this keeps asking the same player for what move to make if she plays a move that is already made
                    while load_two == 0:
                        load_two = game_two.load_game()

        elif option == OPTION_TWO:
            start = game_one.start_game()
            while not end_game:
                load_one = game_one.load_game()
                # end game, there's a winner
                if load_one == 1:
                    end_game = True
                else:
                    # this keeps asking the same player for what move to make if she plays a move that is already made
                    while load_one == 0:
                        load_one = game_one.load_game()

                    game_two = AdjoinTheSpheres(PLAYER_COMPUTER, PLAYER_O, load_one)
                    load_two = game_two.load_game()
                    # end game, there's a winner
                    if load_two == 1:
                        end_game = True
                    else:
                        # this keeps asking the same player for what move to make if she plays a move that is already made
                        while load_two == 0:
                            load_two = game_two.load_game()
