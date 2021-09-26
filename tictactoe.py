#TIC TAC TOE
#LAST UPDATED 26/09/2021

##1-Define the board
tttboard=[]
for i in range(3):                           #a for loop that creates 3 new lists inside the ttboardlist
    row = ["-" for i in range(3)]            #the print statement then creates a new line after every list
    tttboard.append(row)                     #giving the user a look of a board, the elements in the lists
print("Tic,Tac,Toe:",*tttboard,sep='\n')     #can then be used to update the game.
print("Player x goes first.")

#2-Define the Turn
player="x"
for turn in range(10):
    r= [int(input("Enter row: "))] #User input selecting the row and column from the lists
    c= [int(input("Enter column: "))]
    if tttboard[r][c] == '-': #comparing the element selected
        tttboard[r][c] = player #if element selected is - then change to value of player (either x or o depending on turn)
    else:
        print("You can't go there")
        continue
    if turn % 2 == 0:  #changes the players turns to either x or o
        player="o"
        print("It is", player, "'s turn")
    else:
        player="x"
    print(*tttboard,sep='\n')

#3-Define Win
#ACROSS TOP
    if tttboard[0][0] == "x" and tttboard[0][1] == "x" and tttboard[0][2] == "x":                        #Win statements, compares each "row" to see if values 
        print(*tttboard,"YOU WIN",sep='\n')                                                              # all equal x or o. If they are then print win statement.
    elif tttboard[0][0] == "o" and tttboard[0][1] == "o" and tttboard[0][2] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#ACROSS MIDDLE
    elif tttboard[1][0] == "x" and tttboard[1][1] == "x" and tttboard[1][2] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    if tttboard[1][0] == "o" and tttboard[1][1] == "o" and tttboard[1][2] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#ACROSS BOTTOM
    elif tttboard[2][0] == "x" and tttboard[2][1] == "x" and tttboard[2][2] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[2][0] == "o" and tttboard[2][1] == "o" and tttboard[2][2] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#DOWN LEFT SIDE
    elif tttboard[0][0] == "x" and tttboard[1][0] == "x" and tttboard[2][0] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[0][0] == "o" and tttboard[1][0] == "o" and tttboard[2][0] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#DOWN MIDDLE SIDE
    elif tttboard[0][1] == "x" and tttboard[1][1] == "x" and tttboard[2][1] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[0][1] == "o" and tttboard[1][1] == "o" and tttboard[2][1] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#DOWN RIGHT SIDE
    elif tttboard[0][2] == "x" and tttboard[1][2] == "x" and tttboard[2][2] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[0][2] == "o" and tttboard[1][2] == "o" and tttboard[2][2] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#DIAGONAL R2L
    elif tttboard[2][0] == "x" and tttboard[1][1] == "x" and tttboard[0][2] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[2][0] == "o" and tttboard[1][1] == "o" and tttboard[0][2] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#DIAGONAL L2R
    elif tttboard[2][2] == "x" and tttboard[1][1] == "x" and tttboard[0][0] == "x":
        print(*tttboard,"YOU WIN",sep='\n')
    elif tttboard[2][2] == "o" and tttboard[1][1] == "o" and tttboard[0][0] == "o":
        print(*tttboard,"YOU WIN",sep='\n')
#4-Define TIE
    if turn == 9:
        print(*tttboard,"ITS A TIE, GAME OVER",sep='\n') #if turn counter gets to 9 print IT'S A TIE, GAME OVER
