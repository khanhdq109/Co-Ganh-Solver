# Co Ganh
A computer program that play Vietnam's traditional board game "CO GANH" using *Minimax* and *Monte Carlo Tree Search* algorithm.

## Project structure
* [main.py](./main.py) 		                              : the main code file to execute the program
* [game.py](./game.py) 		                              : source code for game "Co Ganh"
* [Minimax.py](./Mimimax.py) 		                        : source code for Minimax algorithm
* [MCTS.py](./MCTS.py) 		                              : source code for Monte Carlo Tree Search algorithm
* [input.txt](./input.txt), [output.txt](./output.txt)  : temporary file to read input and save output in each turn of players

## Execute
Running the program with command line syntax for playing with the bot:
```
python main.py <algorithm>
```
Example: 
```
python bloxorz.py mcts
```
When it's your turn, the program will ask you to enter the coordinates.<br /> 
For example, if you want to move from *(4, 4)* to *(3, 3)*, type: *4433*.
