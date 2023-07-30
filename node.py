
class Node:

    MARKS = ["X","0"]

    def __init__(self,board,current_mark,computer_mark):
        self.score = 0
        self.board = board
        self.current_mark = current_mark
        self.computer_mark = computer_mark

        self.spaces_coordinates = self.__finding_spaces()
        self.number_of_spaces = len(self.spaces_coordinates)

        if self.number_of_spaces != 0 and not(self.check_if_winner()):
            self.next_nodes = self.__creating_next_nodes()
            self.score = self.__calculate_score()
        else:
            self.__set_score()

    def get_score(self):
        return self.score

    def get_board(self):
        return self.board
    
    def find_next_board(self,board):
        for node in self.next_nodes:
            if node.get_board() == board:
                return node

    def finding_best_board(self,currentMark):
        next_nodes_scores = []
        for index, node in enumerate(self.next_nodes):
            next_nodes_scores.append(node.get_score())
            if node.check_if_winner() and node.check_who_won() == currentMark:
                return self.next_nodes[index].get_board()
        max_score = max(next_nodes_scores)
        return self.next_nodes[next_nodes_scores.index(max_score)].get_board()
    
    def finding_next_node(self,currentMark):
        next_nodes_scores = []
        for index, node in enumerate(self.next_nodes):
            next_nodes_scores.append(node.get_score())
            if node.check_if_winner() and node.check_who_won() == currentMark:
                return self.next_nodes[index]
        max_score = max(next_nodes_scores)
        return self.next_nodes[next_nodes_scores.index(max_score)]

    def check_if_winner(self):
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

    def __set_score(self):
        if self.check_who_won() == self.computer_mark:
            self.score = 1
        elif self.check_who_won() is None:
            self.score = 0.8
        else:
            self.score = 0

    def __calculate_score(self):
        likelhood = 0
        for node in self.next_nodes:
            likelhood += node.get_score()
        return likelhood / self.number_of_spaces
            
    def __creating_next_nodes(self):
        child_nodes = []
        for move in self.spaces_coordinates:
            board_copy = [row[:] for row in self.board]
            y, x = move
            board_copy[y][x] = self.current_mark
            if not (self.check_if_winner()):
                #Recursive part of the program
                next_node = Node(board_copy, self.__set_mark(), self.computer_mark)
                child_nodes.append(next_node)
        return child_nodes
                
    def __set_mark(self):
        if self.current_mark == "X":
            return "0"
        else:
            return "X"

    def __finding_spaces(self):
        total = []
        for y_index, row in enumerate(self.board):
            for x_index, _ in enumerate(row):
                if self.board[y_index][x_index] == "-":
                    total.append((y_index, x_index))
        return total