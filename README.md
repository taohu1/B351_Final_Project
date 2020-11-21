# B351_Final_Project
## Building the Project
No dependencies are required to build this project. You can run our test cases by simply running main.py with
```
python3 main.py
```
You can try out different combinations of AIs/Manual Playing by editing the main.py file and uncommenting the right p1 and p2 assignment statements.

## Structure of the code
Board.py is the basis of this project. It provides a representation of the game board for Mu Torere. The board is a list of integers with each element representing a spot on the board and what is contained there.

This class also contains basic operations of the game. Ex. find all valid moves, make move, and undo the previous move.

Player.py contains different type of players: manual player, random player, minimax player, alphabeta player, and a hillclimbing player. All players depend on the board class.

For the AIs, we used a heuristic that takes into account 3 properties of a given board. We initially weighted the first property much higher than the other two, but came to find out this was incorrect after running the genetic algorithm (mentioned below).

genetic.py just contains a class that is exactly an AlphaBeta player, but with input weights for the three properties. This is used in our implementation of the genetic algorithm.

main.py is where the main function is located. It also contains the code implementing the genetic algorithm.





