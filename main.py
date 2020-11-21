from board import *
from player import *
from genetic import *
import random

def randomize_weights(p):
  p.c1 = random.randint(0,10)
  p.c2 = random.randint(0,10)
  p.c3 = random.randint(0,10)

def generate_population(N):
  pop = []
  for i in range(N):
    c1 = random.randint(0,100)
    c2 = random.randint(0,100)
    c3 = random.randint(0,100)
    pop.append([c1,c2,c3])
  return pop

def fitness(pop, num_sims):
  fit_list = []
  for ls in pop:
    b = board()
    player = GAPlayer(b, ls[0], ls[1], ls[2])
    opp = RandomPlayer(b)
    ls_wr, opp_wr, avg_moves = test_GA(num_sims, player, opp)
    fitness_of_ls = 1000 * ls_wr + (-1 * avg_moves + 500)
    fit_list.append(fitness_of_ls)
  return fit_list

def next_generation(pop, fit_list):
  # using top two
  N = len(pop)
  max_fitness = max(fit_list)
  max_ind = fit_list.index(max_fitness)
  father = pop.pop(max_ind)
  fit_list.pop(max_ind)
  max_fitness = max(fit_list)
  max_ind = fit_list.index(max_fitness)
  mother = pop.pop(max_ind)
  fit_list.pop(max_ind)
  new_pop = []
  for ind in range(N):
    rep_code = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]
    # ensure there is genetic material from both mom and dad
    if 0 not in rep_code:
      rand_ind = random.randint(0,2)
      rep_code[rand_ind] = 0
    if 1 not in rep_code:
      rand_ind = random.randint(0,2)
      rep_code[rand_ind] = 1
    child = [-1, -1, -1]
    if rep_code[0] == 0:
      child[0] = father[0]
    else:
      child[0] = mother[0]
    if rep_code[1] == 0:
      child[1] = father[1]
    else:
      child[1] = mother[1]
    if rep_code[2] == 0:
      child[2] = father[2]
    else:
      child[2] = mother[2]
    # mutation with rate of 1%
    for i in range(len(child)):
      rand_num = random.randint(1,100)
      if (rand_num == 1):
        child[i] = random.randint(0,10)
    new_pop.append(child)
  return new_pop

def genetic_algorithm(num_gens, N, num_sims):
  pop = generate_population(N)
  fit_list = fitness(pop, num_sims)
  for i in range(num_gens):
    pop = next_generation(pop, fit_list)
    fit_list = fitness(pop, num_sims)
  max_fitness = max(fit_list)
  max_ind = fit_list.index(max_fitness)
  weights = pop[max_ind]
  print("The weights found with a population size of " + str(N) + ", " + str(num_sims) + " simulations per element of population, and " + str(num_gens) + " generations are " + str(weights))
  return weights

def TournamentOfChampions(p1, p2, sims):
  print("Welcome to the Tournament of Champions!")
  bestc1 = None
  bestc2 = None
  bestc3 = None
  max_wr = 0
  bestmoves = None
  for i in range(sims):
    if isinstance(p1, GAPlayer):
      randomize_weights(p1)
    if isinstance(p2, GAPlayer):
      randomize_weights(p2)
    p1wr, p2wr, num_moves = test_GA(1000, p1, p2)
    
    if p1wr > p2wr:
      print("Player 1 is better.")
      if p1wr > max_wr or (p1wr == max_wr and num_moves < bestmoves):
        max_wr = p1wr
        bestc1 = p1.c1
        bestc2 = p1.c2
        bestc3 = p1.c3
        bestmoves = num_moves

    elif p2wr > p1wr:
      print("Player 2 is better.")
      if p2wr > max_wr or (p2wr == max_wr and num_moves < bestmoves):  
        max_wr = p2wr
        bestc1 = p2.c1
        bestc2 = p2.c2
        bestc3 = p2.c3

  print("The best win rate came from the GAPlayer with weights " + str(bestc1) + ", " + str(bestc2) + ", " + str(bestc3))
  print("The win rate for this player was " + str(max_wr))
  print("The average number of moves for this player is " + str(bestmoves))
  
  return bestc1, bestc2, bestc3, max_wr, bestmoves


def test_GA(num_games, p1, p2):
  if isinstance(p1, GAPlayer):
    print("For P1 weights " + str(p1.c1) + ", " + str(p1.c2) + ", and " + str(p1.c3) + ", the results are: ")
  if isinstance(p2, GAPlayer):
    print("For P2 weights " + str(p2.c1) + ", " + str(p2.c2) + ", and " + str(p2.c3) + ", the results are: ")
  p1wr, p2wr, num_moves = test_AI(num_games, p1, p2)
  return p1wr, p2wr, num_moves

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
      if isinstance(p1, GAPlayer):
        p1.__init__(b, p1.c1, p1.c2, p1.c3)
      else:
        p1.__init__(b)
      if isinstance(p2, GAPlayer):
        p2.__init__(b, p2.c1, p2.c2, p2.c3)
      else:
        p2.__init__(b)
      #b.print_board()
      while not b.game_over():
        #b.print_board()
        #time.sleep(2)
        if num_moves == 500:
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
    print(str(num_ties) + " of the games ended in a tie (reached 500 moves without a winner).")
    print("The average number of moves was " + str(totalmoves/num_games) + ".")
    print("The total amount of time to play the " + str(num_games) + " games is " + str(elapsed_time) + ".")

    p1_winrate = p1wins/num_games
    p2_winrate = p2wins/num_games
    return p1_winrate, p2_winrate, totalmoves/num_games

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
    #test_AI(1000, p1, p2)
    c1 = random.randint(0,10)
    c2 = random.randint(0,10)
    c3 = random.randint(0,10)
    ga = GAPlayer(b, c1, c2, c3)
    ga_opp = RandomPlayer(b)
    genetic_algorithm(10, 10, 10)
    #TournamentOfChampions(ga, ga_opp, 10)
    #test_GA(100, ga, ga_opp)
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
