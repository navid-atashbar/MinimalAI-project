from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2

    def get_move(self,move):
        # Just make it caputre the xlosest piecejjj
        # 
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves_that_capture_pieces = []
        moves = self.board.get_all_possible_moves(self.color)
        for elem in moves:
            for possible_move in elem:
                if len(possible_move.seq) >1:
                    moves_that_capture_pieces.append(possible_move)

        if len(moves_that_capture_pieces) > 0:
            picked_move = moves_that_capture_pieces[randint(0,len(moves_that_capture_pieces) -1)]
        else:
            index = randint(0,len(moves)-1)
            inner_index =  randint(0,len(moves[index])-1)
            move = moves[index][inner_index]
            
      
        self.board.make_move(picked_move,self.color)
        return picked_move
