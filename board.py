import random
class board:
    def __init__(self):
        self.board = [1,1,1,1,2,2,2,2,0] #initialization of the board
        self.turn = 1 # initially player 1's turn

    # check if the spot is empty
    def spot_empty(self, spot):
        return self.board[spot] == 0

    # returns list of adjacent kewai positions
    def adjacent_kewai(self, spot):
      res = []
      if spot == 7:
        res.append(0)
        res.append(6)
      if spot == 0:
        res.append(7)
        res.append(1)
      else:
        res.append(spot+1)
        res.append(spot-1)
      return res

    # check if the current position is adjacent to the other player's piece
    def adjacent_to_opponent(self, spot):
      adjacents = self.adjacent_kewai(spot)
      player = self.board[spot]
      for adj in adjacents:
        if self.board[adj] != 0 and self.board[adj] != player:
          return True
      return False

    # check if a move is valid
    def valid_move(self, current, move):
        # can't move something that isn't there
        # nor can you move to somewhere occupied
        if self.spot_empty(current) or not self.spot_empty(move):
          return False
        # you can't move the other player's piece
        if self.turn != self.board[current]:
          return False
        # from kewai to putahi
        if move == 8:
          return self.adjacent_to_opponent(current)
        # from kewai to kewai
        if current != 8:
          return move in self.adjacent_kewai(current)
        # from putahi to kewai
        else:
          return True # it's always valid to move from putahi to empty kewai

    # return a list of potential valid moves
    def get_all_valid_move(self, current):
        result = []
        for i in range(len(self.board)):
          if self.valid_move(current, i):
            result.append(i)
        return result

    # return the position of all player p's pits, valid inputs are 1 or 2ss
    def get_all_position(self,p):
        result = []
        for i in range(len(self.board)):
            if(self.board[i] == p):
                result.append(i)
        return result

    # check if the player is lost. Valid inputs are 1 or 2
    #example: lose_check(1) returns true when player 1 has no valid moves, then player 2 wins
    def lose_check(self,player):
        positions = self.get_all_position(player)
        for i in positions:
            valid_moves = self.get_all_valid_move(i)
            if(len(valid_moves)>0):
                return False # list is not empty, which means there exists at least one valid move
        return True

    # checks if the game is over
    def game_over(self):
      return self.lose_check(self.turn)
    
    # gives the other player the turn
    def flip_turn(self):
      if self.turn == 1:
        self.turn = 2
      else:
        self.turn = 1

    # function sto make a move, has to call valid move to check if the move is valid first!
    def make_move(self, current, move):
        if not self.valid_move(current, move):
          print("ope, invalid move there bud... try again\n")
        else:
          temp = self.board[move]
          self.board[move] = self.board[current]
          self.board[current] = temp
          self.flip_turn()

    # print the board representation
    def print_board(self):
        indexes = [[-1,-1,0,-1,-1], [-1,7,-1,1,-1], [6,-1,8,-1,2], [-1,5,-1,3,-1], [-1,-1,4,-1,-1]]
        print("Position indicies are: ")
        for i in indexes:
            for j in i:
                if(j < 0):
                    print(" ", end = " ")
                else:
                    print(j, end = " ")
            print()
        print("It is Player " + str(self.turn) + "'s turn.\n")
        print("The board is (0 represents empty spot, x is player 1, o is player 2): ")
        matrix = [[3,3,self.board[0],3,3],
                  [3,self.board[7],3,self.board[1],3],
                  [self.board[6],3,self.board[8], 3, self.board[2]],
                  [3,self.board[5], 3,self.board[3],3], 
                  [3,3,self.board[4], 3,3]]
        for i in matrix:
            for j in i:
                if(j == 3):
                    print(" ", end =" ")
                elif(j == 1):
                    print("x", end = " ")
                elif(j == 2):
                    print("o", end = " ")
                else:
                    print(j, end=" ")
            print()
if __name__ == "__main__":
    num_moves = 0
    b = board()
    b.print_board()
    while not b.game_over():
      pos = b.get_all_position(b.turn)
      moves = {}
      for p in pos:
        moves[p] = b.get_all_valid_move(p)
      for key in moves:
        if len(moves[key]) > 0:
          psn = key
          mv = moves[key]
          break
      b.make_move(psn, mv[0])
      num_moves += 1
      b.print_board()
    print("Game Over! Player " + str(b.turn) + " has lost.\n")
    print("That game took " + str(num_moves) + " turns.\n")

