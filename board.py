class board:
    def __init__(self):
        self.board = [1,1,1,1,2,2,2,2,0] #initialization of the board
    
    # check if the spot is empty
    def spot_empty(self, spot):
        return self.board[spot] == 0

    # check if a move is valid
    def valid_move(self,current, move):
        # from kewai to kewai
        if(move!=8 and ((move == current+1) or (current == 7 or move == 0))):
            return self.spot_empty(move)
        # from kewai to putahi
        elif(move == 8 and (current >=0 and current <=7)):
            return self.spot_empty(move)
        # from putahi to kewai
        elif(current == 8 and (move >=0 and move <=7)):
            return self.spot_empty(move)
        else:
            return False

    # return a list of potential valid moves
    def get_all_valid_move(self, current):
        for i in range(len(self.board)+1):
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

    # function sto make a move, has to call valid move to check if the move is valid first!
    def make_move(self, current, move):
        temp = self.board[current]
        self.board[move] = self.board[current]
        self.board[current] = temp

    # print the board representation
    def print_board(self):
        indexes = [[-1,-1,0,-1,-1], [-1,7,-1,1,-1], [6,-1,8,-1,2], [-1,5,-1,3,-1], [-1,-1,4,-1,-1]]
        print("Position indexes are: ")
        for i in indexes:
            for j in i:
                if(j < 0):
                    print(" ", end = " ")
                else:
                    print(j, end = " ")
            print()

        print("The board is (0 represents empty spot, x is player 1, o is player 2): ")
        matrix = [[3,3,self.board[0],3,3],[3,self.board[7],3,self.board[1],3],[self.board[6],3,self.board[8], 3, self.board[2]],[3,self.board[5], 3,self.board[3],3], [3,3,self.board[4], 3,3]]
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
    b = board()
    b.print_board()