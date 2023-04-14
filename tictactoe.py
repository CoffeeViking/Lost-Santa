theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
           'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
           'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def checkForWin(turn):
    # Top Row
    if theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit() 
    # Middle Row
    if theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Bottom Row
    if theBoard['bot-L'] == turn and theBoard['bot-M'] == turn and theBoard['bot-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Left Column
    if theBoard['top-L'] == turn and theBoard['mid-L'] == turn and theBoard['bot-L'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Middle Column
    if theBoard['top-M'] == turn and theBoard['mid-M'] == turn and theBoard['bot-M'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Right Column
    if theBoard['top-R'] == turn and theBoard['mid-R'] == turn and theBoard['bot-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Top Left to Bottom Right
    if theBoard['top-L'] == turn and theBoard['mid-M'] == turn and theBoard['bot-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    # Top Right to Bottom Left
    if theBoard['bot-L'] == turn and theBoard['mid-M'] == turn and theBoard['top-R'] == turn:
        printBoard(theBoard)
        print(turn + ' is the winner! WHOO!')
        quit()
    
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    # Quits the game
    if move == 'quit':
        print('Baiiiiii')
        quit()
    # Checks for correct input
    while move not in theBoard:
        move = input('Please try again!')
    # Check for empty space
    if theBoard[move] != ' ':
        print("That's already taken!")
    # Updates the game board with the current turn's piece
    theBoard[move] = turn
    # Checks for Winner
    checkForWin(turn)
    # Changes Turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
print('Oops! No Winner!')
