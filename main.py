from board import *
from player import *

def test_HillClimber(num_games):
    randomwins = 0
    abwins = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      b = board()
      p1 = RandomPlayer(b)
      p2 = HillClimbingPlayer(b)
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

    print("Out of " + str(num_games) + " games, the Hill Climbing AI won " + str(abwins) + " of them.")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

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
      b.print_board()
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

    print("Out of " + str(num_games) + " games, the AlphaBeta AI won " + str(abwins) + " of them.")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

def test_MinimaxPlayer(num_games):
    randomwins = 0
    abwins = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      b = board()
      p2 = RandomPlayer(b)
      p1 = MiniMaxPlayer(b,4)
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

    print("Out of " + str(num_games) + " games, the Minimax AI won " + str(abwins) + " of them.")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

if __name__ == "__main__":
    test_HillClimber(10000)
    #test_AlphaBetaPlayer(1)
    #test_MinimaxPlayer(10000)
    # b.print_board()
      # time.sleep(1)
    #print("                   \\|||/")
    #print("                   (o o)")
    #print("****************ooO*(_)*Ooo*********************\n")
    #print("******** Game Over! Player " + str(b.turn) + " has lost. *********\n")
    #print("********** That game took " + str(num_moves) + " turns. ************\n")
    #print("************************************************\n")
