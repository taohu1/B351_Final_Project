from board import *
class RandomPlayer:
    def __init__(self, board):
        self.board = board
        
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

    def find_move(self):
        pos = input("What piece do you want to move?\n")
        mv = input("Where do you want to move it?\n")
        return int(pos), int(mv)

# TODO: implement minimax AI player

class MiniMaxPlayer:
  def __init__(self, board, max_depth):
    self.board = board
    self.md = max_depth

  p1_win = 10
  tie = 0
  p2_win = -10

  def heuristic(self):
    p1_s = 0
    p2_s = 0
    b = self.board
    if b.board[8] == 1:
      p1_s += 5
    elif b.board[8] == 2:
      p2_s += 5
    return p1_s - p2_s

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
    


class AlphaBetaPlayer:
  p1_win = 10
  tie = 0
  p2_win = -10
  def __init__(self, board, max_depth):
    self.board = board
    self.max_depth = max_depth

  def center_control(self, b):
    p1_s = 0
    p2_s = 0
    if b.board[8] == 1:
      p1_s += 5
    elif b.board[8] == 2:
      p2_s += 5
    return p1_s - p2_s
  

  def heuristic(self):
    b = self.board
    return self.center_control(b)

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
