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
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        move = minimax_search(self.board, self.color)
        '''index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]'''
        self.board.make_move(move,self.color)
        return move

    def minimax_search(game, state):
        #player = game.to_move(state)
        value, move = max_value(game,state)
        return move
        
    def max_value(game,state):
        result = game.is_win(state)
        if result != 0:
            if result == -1:
                return 0, None
            elif result == player:
                return 100, None
            else:
                return -100, None
        v = float('-inf')
        best_move = None
        if state == 1:
            opponent = 2
        else:
            opponent = 1
        all_moves = game.get_all_possible_moves(state)
        for i in all_moves:
            for j in i:
                try:
                    game.make_move(j,state)
                    v2, _ = min_value(game, opponent)
                    game.undo()
                    if v2 > v:
                        v, best_move = v2, j
                except:
                    continue
        return v, best_move

    def min_value(game, state):
        player = game.to_move(state)
        result = game.is_win(state)
        if result != 0:
            if result == -1:
                return 0, None
            elif result == player:
                return 100, None
            else:
                return -100, None
        v = float('inf')
        best_move = None
        if state == 1:
            opponent = 2
        else:
            opponent = 1
        all_moves = game.get_all_possible_moves(state)
        for i in all_moves:
            for j in i:
                try:
                    game.make_move(j,state)
                    v2, _ = min_value(game, opponent)
                    game.undo()
                    if v2 > v:
                        v, best_move = v2, j
                except:
                    continue
        return v, best_move
