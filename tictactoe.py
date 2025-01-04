# This program assumes PROPER USER INPUT! No error checking is provided. Remember, garbage in garbage out.

class Tic_tac_toe():
    def __init__(self, board, player1, player2):
        self.game_board = board
        self.player1 = player1
        self.player2 = player2
        print("Welcome to the classic game Tic Tac Toe!")
        print(board)

    def start_game(self):
        self.player1.x_or_o()
        if player1.game_char == "X":
            player2.game_char = "O"
        else:
            player2.game_char = "X"
        self.game_board.display_board()

    def put_move_on_board(self, move, game_char):
        if move == 1:
            self.game_board.rows[0][0] = game_char
        elif move == 2:
            self.game_board.rows[0][1] = game_char
        elif move == 3:
            self.game_board.rows[0][2] = game_char
        elif move == 4:
            self.game_board.rows[1][0] = game_char
        elif move == 5:
            self.game_board.rows[1][1] = game_char
        elif move == 6:
            self.game_board.rows[1][2] = game_char
        elif move == 7:
            self.game_board.rows[2][0] = game_char
        elif move == 8:
            self.game_board.rows[2][1] = game_char
        elif move == 9:
            self.game_board.rows[2][2] = game_char
        else:
            print("Error")

    def play_game(self):
        winner = False
        p1_move_count = 0
        self.start_game()
        while winner == False:
            p1_input = int(input("Choose a square {}: ".format(player1.name)))
            self.put_move_on_board(p1_input, player1.game_char)
            self.game_board.display_board()
            p1_move_count += 1
            if self.game_board.has_winner():
                print("{} Wins!".format(player1.name))
                break
            if p1_move_count == 5:
                print("Draw")
                break
            p2_input = int(input("Choose a square {}: ".format(player2.name)))
            self.put_move_on_board(p2_input, player2.game_char)
            self.game_board.display_board()
            if self.game_board.has_winner():
                print("{} Wins!".format(player2.name))
                break


class Board():
    def __init__(self):
        self.rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def new_board(self):
        print('| 1 | 2 | 3 |\n+---+---+---+\n| 4 | 5 | 6 |\n+---+---+---+\n| 7 | 8 | 9 |')

    def __repr__(self):
        return '| T | I | C |\n+---+---+---+\n| T | A | C |\n+---+---+---+\n| T | O | E |'

    def has_winner(self):
        # each list within move_list represents a row or column or diagonal
        move_list = [[self.rows[0][0], self.rows[0][1], self.rows[0][2]],
                     [self.rows[1][0], self.rows[1][1], self.rows[1][2]],
                     [self.rows[2][0], self.rows[2][1], self.rows[2][2]],
                     [self.rows[0][0], self.rows[1][0], self.rows[2][0]],
                     [self.rows[0][1], self.rows[1][1], self.rows[2][1]],
                     [self.rows[0][2], self.rows[1][2], self.rows[2][2]],
                     [self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                     [self.rows[2][0], self.rows[1][1], self.rows[0][2]]]

        for row in move_list:
            if all(x == row[0] for x in row):
                return True
        return False

    def display_board(self):
        print(
            "| {} | {} | {} |\n+---+---+---+\n| {} | {} | {} |\n+---+---+---+\n| {} | {} | {} |".format(self.rows[0][0],
                                                                                                        self.rows[0][1],
                                                                                                        self.rows[0][2],
                                                                                                        self.rows[1][0],
                                                                                                        self.rows[1][1],
                                                                                                        self.rows[1][2],
                                                                                                        self.rows[2][0],
                                                                                                        self.rows[2][1],
                                                                                                        self.rows[2][
                                                                                                            2]))


class Player():
    def __init__(self, name):
        self.game_char = ""
        self.name = name

    def x_or_o(self):
        self.game_char += (input("Hello {}! Choose X or O: ".format(self.name)))

    def __repr__(self):
        return "Player name: {}\nPlayer game_character: {}".format(self.name, self.game_char)


board1 = Board()
player1 = Player("Bob")
player2 = Player("John")
game1 = Tic_tac_toe(board1, player1, player2)
game1.play_game()
