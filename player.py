from board import *
import itertools

# a random player always randomly picks a move from the all valid moves list
class RandomPlayer:
    def __init__(self, board):
        self.board = board
       
    def toString(self):
      return "Random Player"

    def find_move(self):
        b = self.board
        turn = b.turn
        pos = b.get_all_position(turn)
        moves = {}
        for p in pos:
            moves[p] = b.get_all_valid_move(p)
        rem = []
        for key in moves:
            if len(moves[key]) == 0:
                rem.append(key)
        for key in rem:
            moves.pop(key)
        keys = list(moves.keys())
        chosen_pos = random.choice(keys)
        return chosen_pos, random.choice(moves[chosen_pos])
    
class ManualPlayer:
    def __init__(self, board):
        self.board = board

    def toString(self):
      return "Human Player"

    def find_move(self):
        pos = input("What piece do you want to move?\n")
        mv = input("Where do you want to move it?\n")
        return int(pos), int(mv)

# Minimax Player implementation, uses center-control as a logic for heuristic
class MiniMaxPlayer:
  def __init__(self, board):
    self.board = board
    self.md = 4

  p1_win = 1000
  tie = 0
  p2_win = -1000
  
  def toString(self):
    return "MiniMax Player"

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
    # initial weights for heuristic
    #return 12 * self.center_control(b) + 1 * self.movable_pieces(b)  + 1 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
    # genetic algorithm calculated weights for heuristic
    return 16 * self.center_control(b) + 92 * self.movable_pieces(b)  + 46 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
    
  def minimax(self, board, depth):
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
        score = self.minimax(board, depth-1)[1]
        board.undo_move()
        if best_move is None or (board.turn == 1 and score > best_score) or (board.turn == 2 and score < best_score):
          best_score = score
          best_move = current,move
    return best_move, best_score
  
  def find_move(self):
    board = self.board
    move, score = self.minimax(board, self.md)
    return move[0], move[1]
    

# Implementation of a AlphaBeta player, uses a more complicated heuristic which includes center control, moveable pieces and next_to_empty
class AlphaBetaPlayer:
  p1_win = 1000
  tie = 0
  p2_win = -1000
  def __init__(self, board):
    self.board = board
    self.max_depth = 4
  
  def toString(self):
    return "AlphaBeta Player"

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
    # initial weights for heuristic
    #return 12 * self.center_control(b) + 1 * self.movable_pieces(b)  + 1 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
    # genetic algorithm calculated weights for heuristic
    return 16 * self.center_control(b) + 92 * self.movable_pieces(b)  + 46 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
  
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

# function that returns a list of all indices matching given value
def indices_of(ls, val):
  res = []
  for i in range(len(ls)):
    if ls[i] == val:
      res.append(i)
  return res

# implementation for HillClimbing Player
class HillClimbingPlayer:
  def __init__(self, board):
    self.board = board
  
  def toString(self):
    return "Hill Climbing Player"
  
  def center_control(self, b):
    p1_s = 0
    p2_s = 0
    if b.board[8] == 1:
      p1_s += 1
    elif b.board[8] == 2:
      p2_s += 1
    return p1_s - p2_s
  # think about this one more:
  def spread_apart(self, b):
    p1_s = 0
    p2_s = 0
    p1_inds = indices_of(b.board, 1)
    p2_inds = indices_of(b.board, 2)
    for pr in itertools.combinations(p1_inds, 2):
      if 8 in pr:
        p1_s += 0
      if 0 in pr and 7 in pr:
        p1_s += 0
      else:
        p1_s += (abs(pr[0] - pr[1]) - 1)
    for pr in itertools.combinations(p2_inds, 2):
      if 8 in pr:
        p2_s += 0
      if 0 in pr and 7 in pr:
        p2_s += 0
      else:
        p2_s += (abs(pr[0] - pr[1]) - 1)
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
      p1_moves.append(b.get_all_valid_move(pos))
    for pos in p2_pos:
      p2_moves.append(b.get_all_valid_move(pos))
    return len(p1_moves) - len(p2_moves)

  def heuristic(self):
    b = self.board
    # initial weights for heuristic
    #return 12 * self.center_control(b) + 1 * self.movable_pieces(b) + 1 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)
    # genetic algorithm calculated weights for heuristic
    return 16 * self.center_control(b) + 92 * self.movable_pieces(b)  + 46 * self.next_to_empty(b)#+ 5 * self.spread_apart(b)

  def find_move(self):
    b = self.board
    p = self.board.turn
    bestmove = None
    bestscore = None
    if p == 1:
      bestscore = -math.inf
    else:
      bestscore = math.inf
    all_positions = b.get_all_position(b.turn)
    all_moves = []
    for i in all_positions:
          moves = b.get_all_valid_move(i)
          if(len(moves)>0):
                for j in moves:
                      all_moves.append((i,j)) # i is current, j is move
    
    for current, move in all_moves:
      b.make_move(current, move)
      if p == 1:
        if self.heuristic() > bestscore:
          bestmove = current, move
      else:
        if self.heuristic() < bestscore:
          bestmove = current, move
      b.undo_move()
      return bestmove





