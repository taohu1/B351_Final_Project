from board import *
from player import *

# simulate num_games rounds of the game between two player
def test_AI(num_games, p1, p2):
    p1wins = 0
    p2wins = 0
    num_ties = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      tie = False
      b = board()
      p1.__init__(b)
      p2.__init__(b)
      #b.print_board()
      while not b.game_over():
        #b.print_board()
        #time.sleep(2)
        if num_moves == 1000:
          tie = True
          break
        #print("Move #" + str(num_moves))
        if b.turn == 1:
          pos, mv = p1.find_move()
        else:
          pos, mv = p2.find_move()
        b.make_move(pos, mv)
        num_moves += 1
      if tie:
        num_ties += 1
        tie = False
      elif b.turn == 1:
        p2wins += 1
      else:
        p1wins += 1
      totalmoves += num_moves

    elapsed_time = time.time() - start_time

    print("Out of " + str(num_games) + " games, the " + p1.toString() +  " won " + str(p1wins) + " of them.")
    print("Out of " + str(num_games) + " games, the " + p2.toString() +  " won " + str(p2wins) + " of them.")
    print(str(num_ties) + " of the games ended in a tie (reached 1000 moves without a winner).")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

# run the game num_games times among a hill climning player and a simple hill climbing player
def test_HillClimber(num_games):
    randomwins = 0
    abwins = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      b = board()
      p1 = HillClimbingPlayer(b)
      p2 = HillClimbingPlayer_simple(b)
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

    print("Out of " + str(num_games) + " games, the dumb Hill Climbing AI won " + str(abwins) + " of them.")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

# testing function for alphabeta player, will run the game num_games times.
def test_AlphaBetaPlayer(num_games):
    randomwins = 0
    abwins = 0
    num_ties = 0
    totalmoves = 0
    start_time = time.time()
    for i in range(num_games): 
      num_moves = 0
      tie = False
      b = board()
      p1 = RandomPlayer(b)
      p2 = AlphaBetaPlayer(b,4)
      #b.print_board()
      while not b.game_over():
        b.print_board()
        time.sleep(2)
        if num_moves == 1000:
          tie = True
          break
        #print("Move #" + str(num_moves))
        if b.turn == 1:
          pos, mv = p1.find_move()
        else:
          pos, mv = p2.find_move()
        b.make_move(pos, mv)
        num_moves += 1
      if tie:
        num_ties += 1
        tie = False
      elif b.turn == 1:
        abwins += 1
      else:
        randomwins += 1
      totalmoves += num_moves

    elapsed_time = time.time() - start_time

    print("Out of " + str(num_games) + " games, the AlphaBeta AI won " + str(abwins) + " of them.")
    print(str(num_ties) + " of the games ended in a tie (reached 1000 moves without a winner).")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

# testing function for minimax player
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
    # initial board
    b = board()
    # uncomment ONLY ONE for each of p1 and p2
    p1 = AlphaBetaPlayer(b)
    #p1 = MiniMaxPlayer(b)
    #p1 = RandomPlayer(b)
    #p1 = ManualPlayer(b)
    #p1 = HillClimbingPlayer_simple(b)
    #p1 = HillClimbingPlayer(b)
    p2 = RandomPlayer(b)
    #p2 = AlphaBetaPlayer(b)
    #p2 = MiniMaxPlayer(b)
    #p2 = ManualPlayer(b)
    #p2 = HillClimbingPlayer_simple(b)
    #p2 = HillClimbingPlayer(b)
    # you can replace the first argument with the number of games you want to play 
    test_AI(10, p1, p2)
    #test_HillClimber(10000)
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
