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
        #1 handle opps move if they made one
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        #2 get all legal moves for curr player
        #if none return empty move
        #call mcts
        #take the best move on board and return it
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move



    def monty_search(self,legal_moves):
        #dictinoary to store stats for each of the moves wins and simulatiobs
        # all moves start with 0 wins and 0 simulation
        #loop number of simulations
            #select move using uct
            #simulate randome game from the move
            #get result
            #update stats

        #pick the move with the highest win rate
        #return that move

    def pick_move(self,move_dictionary, legal_moves):
        #calc total sims across all moves
        #check each move if any have 0 sims return it to explore
        #for each move get the UCT
            #get wins and somulations for this move
            #calc the wins/simulation
            #calc explorations  
            #UCT = wins/sims + explorations
        #return the move with the highest UCT value

    def game_simulator(self,start_move):
        #make a copy of the curr board
        #make the start move
        #set curr player to opponent
        #loop until games end
            #check if games won return winner 
            #get legal moves for curr player
            #if no moves return opp as the winner
            # pick a random move from legal moves
            #make the random move
            #switch to other player
        #if max moves reached evalute board and return likely winner