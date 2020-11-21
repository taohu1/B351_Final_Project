# B351_Final_Project
## How to build this project?
No dependencies is required to build this project. You can run our test cases by simply running the main.py\

## Structure of the code
Board.py is the basis of this project. It provides a representation of the game board for Mu Torere. The board is a list of integers with each element represents one spot\
This class also contains basic operations of the game. Ex. find all valid moves, make move, and undo the previous move.\

Player.py contains different type of players: manual player, randomly player, minimax player, alphabeta player, and two versions of hillclimbing player. All players depend on the board class\
There is a simple version of heuristic which only takes center control into account (the player who has a piece at the center has a higher chance to win)\
There is also a more complicated heuristics using several other properties other than the center control, such as number of movable pieces, if any of the pieces is next to an empty pit, and if a player's piece spread the board apart.\ 

main.py is where the main function locates. It also has several methods to test different type of players.\
test_AI: this is a general testing methods that can test any types of 2 players and will let these 2 players play num_games times against each other and calculate the statistics\
Other three test method are for a specific type of player (as indicated in the method name). User can decide how many games to run by changing the input, and it will calculate the statistics in the end\








