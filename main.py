from board import *
from player import *

def test_AlphaBetaPlayer(num_games):
    randomwins = 0
    abwins = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      b = board()
      p1 = RandomPlayer(b)
      p2 = AlphaBetaPlayer(b,4)
      #b.print_board()
      while not b.game_over():
        if b.turn == 1:
          pos, mv = p1.find_move()
        else:
          pos, mv = p2.find_move()
        b.make_move(pos, mv)
        num_moves += 1
      if b.turn == 1:
        abwins += 1
      else:
        randomwins += 1
      totalmoves += num_moves

    elapsed_time = time.time() - start_time

    print("Out of 1000 games, the AlphaBeta AI won " + str(abwins) + " of them.")
    print("The average number of moves was " + str(totalmoves/1000) + ".")
    print("The total amount of time to play the 1000 games is " + str(elapsed_time) + ".")


if __name__ == "__main__":
    b = board()
    p1 = RandomPlayer(b)
    p2 = MiniMaxPlayer(b, 3)
    while not b.game_over():
        if b.turn == 1:
          pos, mv = p1.find_move()
        else:
          pos, mv = p2.find_move()
        b.make_move(pos, mv)
        num_moves += 1
      if b.turn == 1:
        abwins += 1
      else:
        randomwins += 1
      totalmoves += num_moves

    # test_AlphaBetaPlayer(1000)
    # b.print_board()
      # time.sleep(1)
    #print("                   \\|||/")
    #print("                   (o o)")
    #print("****************ooO*(_)*Ooo*********************\n")
    #print("******** Game Over! Player " + str(b.turn) + " has lost. *********\n")
    #print("********** That game took " + str(num_moves) + " turns. ************\n")
    #print("************************************************\n")
