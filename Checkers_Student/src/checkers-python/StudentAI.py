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
        self.max_depth_search = 5
        self.alpha = float('-inf')
        self.beta = float('inf')
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        legal_moves = []
        for group in moves:
            for m in group:
                if m is not None:
                    legal_moves.append(m)
        if not moves or all(len(m) == 0 for m in moves):
            return Move([])
        move = self.minimax_search(self.board, self.color, self.max_depth_search, self.alpha, self.beta)
        '''index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]'''
        if move is not None and move in legal_moves:
            self.board.make_move(move,self.color)
            return move
        else:
            print("random move")
            index = randint(0, len(moves)-1)
            inner_index = randint(0, len(moves[index])-1)
            move = moves[index][inner_index]
            self.board.make_move(move, self.color)
            return move 

    def minimax_search(self, game, state, depth, alpha, beta):
        #player = game.to_move(state)
        value, move = self.max_value(game,state, depth, alpha, beta)
        return move
        
    def max_value(self, game,state, depth, alpha, beta):
        #Tawann add the if statement to check if we went over the depth here
        if depth <= 0:
            return self.get_score(game, state), None
        #If we did then return 0,None
        result = game.is_win(state)
        if result != 0:
            if result == state:
                return 100, None
            elif result ==-1:
                return 100, None
            else:
                return -100, None
        all_moves = game.get_all_possible_moves(state)
        if not all_moves or self.len_checker(all_moves):
            return -100, None

        v = float('-inf')
        best_move = None
        opponent = self.opponent[state]
        all_moves = game.get_all_possible_moves(state)
        for i in all_moves:
            for j in i:
                try:
                    try:
                        game.make_move(j,state)
                    except:
                        continue
                    v2, _ = self.min_value(game, opponent, depth -1, alpha, beta)
                    game.undo()
                    if v2 > v:
                        v = v2
                        best_move = j
                    if v >= beta:
                        return v, best_move
                    alpha = max(alpha, v)
                except:
                    continue
        return v, best_move

    def min_value(self, game, state, depth, alpha, beta):
        #Tawann add the if statement to check if we went over the depth here
        #If we did then return 0,None
        if depth <= 0:
            return self.get_score(game, state), None
        result = game.is_win(state)
        if result != 0:
            if result == state:
                return 100, None
            elif  result == -1:
                return 100, None
            else:
                return -100, None
        all_moves = game.get_all_possible_moves(state)
        if not all_moves or self.len_checker(all_moves):
            return self.get_score(game, state), None
        v = float('inf')
        best_move = None        
        opponent = self.opponent[state]
        for i in all_moves:
            for j in i:
                try:
                    try:
                        game.make_move(j,state)
                    except:
                        continue
                    v2, _ = self.max_value(game, opponent, depth -1, alpha, beta)
                    game.undo()
                    if v2 < v:
                        v = v2
                        best_move = j
                    if v <= alpha:
                        return v, best_move
                    beta = min(beta, v)
                except:
                    continue
        return v, best_move
    def get_score(self, game, state):
        score = 0
        board = game.board
        color_map = {1: "B", 2: "W"} 
        my_color = color_map[state]
        opp_color = color_map[self.opponent[state]]
        center_row = range(2, len(board)-2)
        center_col = range(2,len(board[0])-2)
        for i in range(len(board)):
            for j in range(len(board[i])):
                piece = board[i][j]
                if piece is None:
                    continue
                if piece.color == my_color:
                    score += 2
                    if piece.is_king:
                        score += 4
                    if i in center_row and j in center_col:
                        score +=1
                elif piece.color == opp_color:
                    score -= 2
                    if piece.is_king:
                        score -= 4
                    if i in center_row and j in center_col:
                        score -= 1
        return score
    def len_checker(self, iterablee):
        for x in iterablee:
            if len(x) != 0:
                return False
        return True