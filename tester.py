import game
import Minimax

def readBoard(file):
    count = 0
    board = []
    with open(file) as f:
        for line in f:
            board.append([int(x) for x in line.split()])
            count += 1
            if count == 5: break
    return board

def printBoard(board):
    for i in board:
        print(str(i) + '\n')

def test_chan(board):
    cg = game.CoGanh()
    cg.chan(board, -1)
    print("\nSECOND BOARD\n")
    printBoard(board)
    
def test_ganh(board):
    cg = game.CoGanh()
    cg.ganh(board, (2, 2))
    print("\nSECOND BOARD\n")
    printBoard(board)
    
def test_moveGen(board):
    node = game.Node(board)
    cg = game.CoGanh()
    result = cg.move_gen(node, (1, 1))
    print("\nGENERATED:\n")
    for gen in result:
        print(gen[1], ", score: ", str(sum(map(sum, gen[0].board))))
        print('\n')
    
board = readBoard('input.txt')

print("FIRST BOARD\n")
printBoard(board)

test_moveGen(board)