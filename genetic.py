from board import *
from player import *

# idea: make a new player that uses AlphaBeta but contains attributes for the weights
# then, generate 100 of these players randomly (that is, random weights)

class GAPlayer:
  p1_win = 1000
  tie = 0
  p2_win = -1000
  def __init__(self, board, c1, c2, c3):
    self.board = board
    self.max_depth = 4
    self.c1 = c1
    self.c2 = c2
    self.c3 = c3
  
  def toString(self):
    return "Genetic Algorithm Alpha Beta Player"

  def center_control(self, b):
    p1_s = 0
    p2_s = 0
    if b.board[8] == 1:
      p1_s += 1
    elif b.board[8] == 2:
      p2_s += 1
    return p1_s - p2_s
  
  def next_to_empty(self, b):
    p1_s = 0
    p2_s = 0
    pos_of_zero = b.board.index(0)
    if pos_of_zero != 8:
      next_to = b.adjacent_kewai(pos_of_zero)
      for pos in next_to:
        if b.board[pos] == 1:
          p1_s += 1
        else:
          p2_s += 1
    return p1_s - p2_s

  def movable_pieces(self, b):
    p1_pos = b.get_all_position(1)
    p2_pos = b.get_all_position(2)
    p1_moves = []
    p2_moves = []
    for pos in p1_pos:
      for move in b.get_all_valid_move(pos):
        p1_moves.append(move)
    for pos in p2_pos:
      for move in b.get_all_valid_move(pos):
        p2_moves.append(move)
    return len(p1_moves) - len(p2_moves)

  def heuristic(self):
    b = self.board
    #return self.center_control(b)
    return self.c1 * self.center_control(b) + self.c2 * self.movable_pieces(b)  + self.c3 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
  
  def alphaBeta(self, board, depth, alpha, beta):
    if board.lose_check(board.turn):
            if(board.turn == 1):
                return None, self.p2_win
            else:
                return None, self.p1_win
        
    if(depth == 0):
        return None, self.heuristic()
    
    best_move = None
    best_score = None
    all_positions = board.get_all_position(board.turn)
    all_moves = []
    for i in all_positions:
          moves = board.get_all_valid_move(i)
          if(len(moves)>0):
                for j in moves:
                      all_moves.append((i,j)) # i is current, j is move
    for current, move in all_moves:
        board.make_move(current, move)
        score = self.alphaBeta(board, depth-1, alpha, beta)[1]
        board.undo_move()

        if board.turn == 1:
            if best_move is None or score > best_score:
                best_score = score
                best_move = (current,move)
                
                if score > alpha:
                    alpha = score
                    if alpha >=beta:
                        return None, score
        
        if board.turn == 2:
            if best_move is None or score < best_score:
                best_score = score
                best_move = (current, move)

                if score < beta:
                    beta = score
                    if alpha >= beta:
                        return None, score
    return best_move, best_score

  def find_move(self):
        board = self.board
        move, score = self.alphaBeta(board, self.max_depth, -math.inf, math.inf)
        return move[0], move[1]

