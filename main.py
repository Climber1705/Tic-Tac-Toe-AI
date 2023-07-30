
from random import randint

from node import Node   

class Window:

    MARKS = ["X","0"]

    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]
        self.player_mark = self.__set_player_mark()
        self.computer_mark = self.__set_computer_mark()
        self.mark = self.MARKS[randint(0,1)]
        self.tree = Node([["-" for _ in range(3)] for _ in range(3)],self.mark,self.computer_mark)
        self.__info()
    
    def run(self):
        print("===============\nPlayer's mark:",self.player_mark +"\nComputer's mark:", self.computer_mark +"\n"+ self.mark,"starts")
        self.node = self.tree
        while True:
            if self.mark == self.player_mark:
                self.__player_move()
                self.node = self.node.find_next_board(self.board)
                print("===============")
            else:
                self.__computer_move(self.mark)
            self.__display_board()
            self.__set_mark()
            if self.__check_if_winner():
                print(self.check_who_won(), "wins")
                break
            elif self.__check_if_full_board():
                print("A Draw")
                break
        if self.__play_again():
            self.__reset()
            self.run()

    def __computer_move(self,mark):
        self.board = self.node.finding_best_board(mark)
        self.node = self.node.finding_next_node(mark)
        
    def __reset(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]
        self.player_mark = self.__set_player_mark()
        self.computer_mark = self.__set_computer_mark()
        self.mark = self.MARKS[randint(0,1)]

    def __play_again(self):
        continue_game = input("Play again: ")
        if continue_game.lower().startswith("y"):
            return True
        return False

    def __info(self):
        info = input("===============\nHow to play?: ")
        if info.lower().startswith("n"):
            print("A cross is a capital X and a dot is a zero 0\nUse the num pad as the location of each number equals location on the board e.g. 7 is top left")

    def __set_player_mark(self):
        index = randint(0,1)
        return self.MARKS[index]

    def __set_computer_mark(self):
        if self.player_mark == "X":
            return "0"
        else:
            return "X"
    
    def __display_board(self):
        for row in self.board:
            print(row)
        print("===============")

    def __player_move(self):
        try:
            move = int(input("Enter move(1/9): "))
            validMove = self.__valid_move(move)
            if validMove:
                if move == 1:
                    self.board[2][0] = self.mark
                if move == 2:
                    self.board[2][1] = self.mark
                if move == 3:
                    self.board[2][2] = self.mark
                if move == 4:
                    self.board[1][0] = self.mark
                if move == 5:
                    self.board[1][1] = self.mark
                if move == 6:
                    self.board[1][2] = self.mark
                if move == 7:
                    self.board[0][0] = self.mark
                if move == 8:
                    self.board[0][1] = self.mark
                if move == 9:
                    self.board[0][2] = self.mark
            else:
                self.__player_move()
        except ValueError:
            print("Invalid Input\n===============")
            self.__player_move()

    def __valid_move(self, move):
        if move == 1 and self.board[2][0] == "-":
            return True
        if move == 2 and self.board[2][1] == "-":
            return True
        if move == 3 and self.board[2][2] == "-":
            return True
        if move == 4 and self.board[1][0] == "-":
            return True
        if move == 5 and self.board[1][1] == "-":
            return True
        if move == 6 and self.board[1][2] == "-":
            return True
        if move == 7 and self.board[0][0] == "-":
            return True
        if move == 8 and self.board[0][1] == "-":
            return True
        if move == 9 and self.board[0][2] == "-":
            return True
        return False

    def __check_if_winner(self):
        for mark in self.MARKS:
            #Checks the diagonals
            if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark:
                return True
            if self.board[0][2] == mark and self.board[1][1] == mark and self.board[2][0] == mark:
                return True                
            for index in range(3):
                #Checks the rows
                if self.board[index][0] == mark and self.board[index][1] == mark and self.board[index][2] == mark:
                    return True
                #Checks the columns
                if self.board[0][index] == mark and self.board[1][index] == mark and self.board[2][index] == mark:
                    return True
        return False
    
    def check_who_won(self):
        for mark in self.MARKS:
            #Checks the diagonals
            if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark:
                return mark
            if self.board[0][2] == mark and self.board[1][1] == mark and self.board[2][0] == mark:
                return mark               
            for index in range(3):
                #Checks the rows
                if self.board[index][0] == mark and self.board[index][1] == mark and self.board[index][2] == mark:
                    return mark
                #Checks the columns
                if self.board[0][index] == mark and self.board[1][index] == mark and self.board[2][index] == mark:
                    return mark
        return None

    def __set_mark(self):
        if self.mark == "X":
            self.mark = "0"
        else:
            self.mark = "X"

    def __check_if_full_board(self):
        for y, row in enumerate(self.board):
            for x, _ in enumerate(row):
                if self.board[y][x] == "-":
                    return False
        return True

if __name__ == "__main__":
    print("    Tic Tac Toe AI\n.::Built by Climber::.")
    window = Window()
    window.run()
    print("===============\nThank you for playing my program")
    
