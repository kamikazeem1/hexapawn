from random import randint as r
import sys
sys.setrecursionlimit(10**9)

class Game:

    def __init__(self, mode):
        self.mode = mode
        self.computer_score = 0
        self.player_score = 0
        self.white_pawns = 'O'
        self.black_pawns = 'X'
        self.board_state = {}
        self.move_dict = {}
        self.board = {"1": "O",    "2": "O",    "3": "O",
                      "4": " ",    "5": " ",    "6": " ",
                      "7": "X",    "8": "X",    "9": "X"}
        self.print_board()

    def reset(self):
        self.board = {"1": "O",    "2": "O",    "3": "O",
                      "4": " ",    "5": " ",    "6": " ",
                      "7": "X",    "8": "X",    "9": "X"}
        print(f"\nPLAYER SCORE: {self.player_score}\nCOMPUTER SCORE: {self.computer_score}")
        self.print_board()
        self.play()

    def play(self):
        move = input("Your move: ")
        x = move.split()
        try:
            self.pawn = x[0]
            self.moveval = x[1]
            if (len(x) == 2 and (int(self.pawn) >= 1 and int(self.pawn) <= 9) and
                    int(self.moveval) >= 1 and int(self.moveval) <= 9):
                self.bpawn_moves(x)
            elif int(self.pawn) < 1 or int(self.pawn) > 9:
                print("pawn index out of range, must be between 1-9")
                self.play()
            elif int(self.moveval) < 1 or int(self.moveval) > 9:
                print("move index out of range, must be between 1-9")
                self.play()
            elif ((int(self.pawn) < 1 or int(self.pawn) > 9) and
                    int(self.moveval) < 1 or int(self.moveval) > 9):
                print("pawn and move indeces out of range, must be between 1-9")
                self.play()
            else:
                print("input should be as following:")
                print("[pawn index], [move index]")
                self.play()
        except(ValueError):
            print("Numbers... my friend")
            self.play()
        except(IndexError):
            print("2 numbers are required")
            self.play()

    def bpawn_moves(self, move):
        self.bpawn_has_legal_move()
        if move in self.blackpmoves:
            self.board[self.moveval] = self.black_pawns
            self.board[self.pawn] = " "
            self.check_player_win()
            self.wpawn_moves()
            self.play()
        else:
            print("illegal move")
            self.play()

    def wpawn_moves(self):
        board = str(self.board)
        if board in self.board_state:
            possible = self.board_state[board]
            move = possible[r(0,len(possible)-1)]
            self.move_dict[board] = move
            spl_move = move.split()
            print("board_state:\n",self.board_state)
            print("move_dict:\n",self.move_dict)
            pawn = spl_move[0]
            moveval = spl_move[1]
            self.board[moveval] = self.white_pawns
            self.board[pawn] = " "
            self.check_computer_win()
        else:
            self.board_state[board] = self.whitepmoves
            self.wpawn_moves()

    def bpawn_has_legal_move(self):
        self.blackpmoves = []
        if self.board['4'] == self.black_pawns:
            if self.board['1'] == " ":
                self.blackpmoves.append(['4', '1'])
            if self.board['2'] == self.white_pawns:
                self.blackpmoves.append(['4', '2'])
        if self.board['5'] == self.black_pawns:
            if self.board['2'] == " ":
                self.blackpmoves.append(['5', '2'])
            if self.board['1'] == self.white_pawns:
                self.blackpmoves.append(['5', '1'])
            if self.board['3'] == self.white_pawns:
                self.blackpmoves.append(['5', '3'])
        if self.board['6'] == self.black_pawns:
            if self.board['3'] == " ":
                self.blackpmoves.append(['6', '3'])
            if self.board['2'] == self.white_pawns:
                self.blackpmoves.append(['6', '2'])
        if self.board['7'] == self.black_pawns:
            if self.board['4'] == " ":
                self.blackpmoves.append(['7', '4'])
            if self.board['5'] == self.white_pawns:
                self.blackpmoves.append(['7', '5'])
        if self.board['8'] == self.black_pawns:
            if self.board['5'] == " ":
                self.blackpmoves.append(['8', '5'])
            if self.board['4'] == self.white_pawns:
                self.blackpmoves.append(['8', '4'])
            if self.board['6'] == self.white_pawns:
                self.blackpmoves.append(['8', '6'])
        if self.board['9'] == self.black_pawns:
            if self.board['6'] == " ":
                self.blackpmoves.append(['9', '6'])
            if self.board['5'] == self.white_pawns:
                self.blackpmoves.append(['9', '5'])
        if len(self.blackpmoves) == 0:
            return False

    def wpawn_has_legal_move(self):
        self.whitepmoves = []
        if self.board['1'] == self.white_pawns:
            if self.board['4'] == " ":
                self.whitepmoves.append('1 4')
            if self.board['5'] == self.black_pawns:
                self.whitepmoves.append('1 5')
        if self.board['2'] == self.white_pawns:
            if self.board['5'] == " ":
                self.whitepmoves.append('2 5')
            if self.board['4'] == self.black_pawns:
                self.whitepmoves.append('2 4')
            if self.board['6'] == self.black_pawns:
                self.whitepmoves.append('2 6')
        if self.board['3'] == self.white_pawns:
            if self.board['6'] == " ":
                self.whitepmoves.append('3 6')
            if self.board['5'] == self.black_pawns:
                self.whitepmoves.append('3 5')
        if self.board['4'] == self.white_pawns:
            if self.board['7'] == " ":
                self.whitepmoves.append('4 7')
            if self.board['8'] == self.black_pawns:
                self.whitepmoves.append('4 8')
        if self.board['5'] == self.white_pawns:
            if self.board['8'] == " ":
                self.whitepmoves.append('5 8')
            if self.board['7'] == self.black_pawns:
                self.whitepmoves.append('5 7')
            if self.board['9'] == self.black_pawns:
                self.whitepmoves.append('5 9')
        if self.board['6'] == self.white_pawns:
            if self.board['9'] == " ":
                self.whitepmoves.append('6 9')
            if self.board['8'] == self.black_pawns:
                self.whitepmoves.append('6 8')
        if len(self.whitepmoves) == 0:
            return False

    def check_player_win(self):
        print("\nYOUR MOVE")
        self.print_board()
        white_pawn_count = []
        check = False
        for i in range(1,10):
            white_pawn_count.append(self.board[f'{i}'])
        if self.white_pawns in white_pawn_count:
            check = True
        if check is False:
            self.computer_learn(playerwins=1)
        elif (self.board['1'] == self.black_pawns or self.board['2'] ==
            self.black_pawns or self.board['3'] == self.black_pawns):
            self.computer_learn(playerwins=1)
        elif self.wpawn_has_legal_move() is False:
            self.computer_learn(playerwins=1)
        else:
            pass

    def check_computer_win(self):
        print("COMPUTER'S MOVE")
        self.print_board()
        black_pawn_count = []
        check = False
        for i in range(1,10):
            black_pawn_count.append(self.board[f'{i}'])
        if self.black_pawns in black_pawn_count:
            check = True
        if check is False:
            print("COMPUTER WINS (all your pawns were eliminated)")
            self.computer_learn()
        elif (self.board['7'] == self.white_pawns or self.board['8'] ==
            self.white_pawns or self.board['9'] == self.white_pawns):
            print("COMPUTER WINS (white pawn has made it to your side)")
            self.computer_learn()
        elif self.bpawn_has_legal_move() is False:
            print("COMPUTER WINS (you have no legal moves)")
            self.computer_learn()
        else: #continue game
            pass

    def computer_learn(self, playerwins=None):
        if self.mode == 1:
            if playerwins:
                self.cl_pwin()
            else:
                self.computer_score += 1
        if self.mode == 2:
            if playerwins:
                self.cl_pwin()
            else: #add winning move to board_state dictionary
                board_instance = list(self.move_dict)[-1] #board_instance is set to last key of move_dict dictionary
                ml_move = self.move_dict[board_instance] #ml_move is set to value of 'board_instance' in move_dict dictionary (is a list)
                bs_move = self.board_state[board_instance] #bs_move is set to value of 'board_instance' in board_state dictionary (is a list)
                bs_move.append(ml_move[0:3])
                self.board_state[board_instance] = bs_move #at board_state key 'board_instance', value is set to 'new_move'
                self.computer_score += 1

        self.move_dict = {}
        self.reset()

    def cl_pwin(self):
        print("PLAYER WINS")
        board_instance = list(self.move_dict)[-1] #board_instance is set to last key of move_dict dictionary
        ml_move = self.move_dict[board_instance] #ml_move is set to value of 'board_instance' in move_dict dictionary (is a list)
        bs_move = self.board_state[board_instance] #bs_move is set to value of 'board_instance' in board_state dictionary (is a list)
        new_move = [move for move in bs_move if move not in ml_move] #new_move is a new list that removes the losing move from bs_move
        self.board_state[board_instance] = new_move #at board_state key 'board_instance', value is set to 'new_move'
        self.player_score += 1

    def print_board(self):
        print(f"\n\n1: {self.board['1']}\t2: {self.board['2']}\t3: {self.board['3']}\n")
        print(f"4: {self.board['4']}\t5: {self.board['5']}\t6: {self.board['6']}\n")
        print(f"7: {self.board['7']}\t8: {self.board['8']}\t9: {self.board['9']}\n\n")

while True:
    try:
        mode = int(input("for mode 1, enter 1.\nfor mode 2, enter 2.\n> "))
        if mode == 1 or mode == 2:
            game = Game(mode)
            game.play()
        else:
            pass
    except(KeyboardInterrupt):
        print("\n\nexiting game\n")
        exit(0)
    except(ValueError):
        pass
