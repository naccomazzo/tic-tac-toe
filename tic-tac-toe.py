class Player:
    def __init__(self, num, name):
        self.order = num
        self.name = name
        
#Converts any format of 2 integers to a list [a,b]
def coordinates():
    some_list = list(input('Enter 2 coordinates: '))
    coord = []
    not_coord = []
    for element in some_list:
        try:
            value=int(element)
            coord.append(value)
        except ValueError:
            not_coord.append(element)
    return coord
   
#Checks that the given coordinates make sense     
def check_coord():
    coord = coordinates()
    #check we are passing 2 coordinates
    if len(coord) != 2: 
        print('2 coordinates needed, try again!')
        return check_coord()
    
    #check integers are no bigger than 2   
    if coord[0]> n-1 or coord[1]>n-1:
        print('Coordinate cannot be bigger than '+ str(n-1)+', try again!')
        return check_coord()
    
    #checks for free space
    if board[coord[0]][coord[1]]!=0:
        print('Space is already taken, try again!')
        return check_coord()
    
    return coord

#Makes the board nicer to look at 
def print_board(mylist):
    row = '|'
    for element in mylist:
        if element == 0:
            row = row+'   '
        if element == 1:
            row = row + ' X '
        if element == 2:
            row = row + ' O '
    return print(row + '|')

#Players turns:
def player1_turn():
    print(player_1.name + "'s turn to play:")
    coord = check_coord()
    board[coord[0]][coord[1]] = 1
    winning_conf = [board[i] for i in range(n)]+[[board[i][j] for i in range(n)] for j in range(n)] + [[board[i][n-1-i] for i in range(n)]]+ [[board[i][i] for i in range(n)]]
    for i in range(n):
        print_board(board[i])
    if any(element == [1]*n for element in winning_conf):
       return print(player_1.name + " wins!")
    if any(board[i][j] == 0 for i in range(n) for j in range(n)):
        return player2_turn()
    return print("It's a tie!")

def player2_turn():
    print(player_2.name + "'s turn to play:")
    coord = check_coord()
    board[coord[0]][coord[1]] = 2
    winning_conf = [board[i] for i in range(n)]+[[board[i][j] for i in range(n)] for j in range(n)] + [[board[i][n-1-i] for i in range(n)]]+ [[board[i][i] for i in range(n)]]
    for i in range(n):
        print_board(board[i])
    if any(element == [2]*n for element in winning_conf):
        return print(player_2.name + " wins!")
    if any(board[i][j] == 0 for i in range(n) for j in range(n)):
        return player1_turn()
    return print("It's a tie!")
    
def board_size():
    n = int(input('Enter board size: '))
    if 1<= n <= 9:
        return n
    else:
        print('Size outside of parameters, try again.')
        return board_size()
    

## THE GAME
print('Welcome to tic-tac-toe! Please choose a number between 1 and 9 to determine the size of the board.')
#set up the board
n = board_size() 
board = [[0 for column in range(n)] for row in range(n)]

#Instructions
print('You are playing on a ' + str(n) + 'x' + str(n)+' rectangular board. Player 1 will use X and Player 2 will use O to mark their points.')
print('Enter the names for the players and on each turn enter a pair of coordinates between 0 and ' + str(n-1)+' to place your marker down.')
print('Good luck!')

#set up the players
player_1 = Player(0, str(input('Enter name for player 1: ')))
player_2 = Player(1, str(input('Enter name for player 2: ')))

#start with player1's turn
player1_turn()    