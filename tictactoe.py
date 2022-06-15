#Tic Tac Toe game, created by AJ Yballa
#created on 6/14/2022

#Variables
line = "----------------"
boxes = "   |   |   |   "
player_move = " x "
computer_move = " O "
win_con = False

#this game runs inside of a loop, checking to see if player wants to play.
while True:
    play = input("Would you like to play Tic Tac Toe? Y to play, Q to quit.")
    if play == 'y' or play == 'Y':
        print(boxes)
        print(line)
        print(boxes)
        print(line)
        print(boxes)



        while win_con == False:
            player_choice = input("Make your move! enter 1-9, 1 being the top left corner, 9 the bottom right.")
            #TODO use arrays/lists and put player choice into existing list, same with computer


        
    elif play == 'q' or play == 'Q':
        quit()
    else:
        print("player did not enter either, entered " + play + " instead")
