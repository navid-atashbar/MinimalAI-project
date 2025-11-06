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
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move
        '''
        def minimax_search(game, state):
            player = game.to_move(state)
            value, move = max_value(game,state)
            return move
        def max_value(game,state):
            if game.is_terminal(state):
                return game.utility(state, game.to_move(state)), None
            v = float('-inf')
            best_move = None
            for a in game.actions(state):
                v2, _ = min_value(game, game.result(state,a))
                if v2 > v:
                    v, best_move = v2, a
            return v, best_move
        def min_value(game, state):
            if game.is_terminal(state):
                return game.utility(state,game.to_move(state)), None
            
            v = float('inf')
            best_move = None
            for a in game.actions(state):
                v2, _ = max_value(game,game.result(state,a))
                if v2 < v:
                    v, best_move = v2, a
            return v, best_move
                '''
