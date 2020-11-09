from board import *
from player import *
if __name__ == "__main__":
    num_moves = 0
    b = board()
    p1 = RandomPlayer(b)
    # p2 = ManualPlayer(b)
    #p2 = RandomPlayer(b)
    p2 = AlphaBetaPlayer(b,4)
    b.print_board()
    while not b.game_over():
      if b.turn == 1:
        pos, mv = p1.find_move()
      else:
        pos, mv = p2.find_move()
      b.make_move(pos, mv)
      num_moves += 1
      b.print_board()
      # time.sleep(1)
    print("                   \\|||/")
    print("                   (o o)")
    print("****************ooO*(_)*Ooo*********************\n")
    print("******** Game Over! Player " + str(b.turn) + " has lost. *********\n")
    print("********** That game took " + str(num_moves) + " turns. ************\n")
    print("************************************************\n")