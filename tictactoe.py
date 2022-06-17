#Tic Tac Toe game, created by AJ Yballa
#created on 6/14/2022

#Variables
line =  "-----------"
boxes = "   |   |   "
player_move = " x "
computer_move = " O "
win_con = False

clear_row = ["   |   |   "]
row_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#1 2 3
#4 5 6
#7 8 9

#this game runs inside of a loop, checking to see if player wants to play.
while True:
    play = input("Would you like to play Tic Tac Toe? Y to play, Q to quit.")
    if play == 'y' or play == 'Y':
        print(boxes)
        print(line)
        print(boxes)
        print(line)
        print(boxes)


        #Loop to check if anyone has won yet, if not, keep playing.
        while win_con == False:
            player_choice = int(input("Make your move! enter 1-9, 1 being the top left corner, 9 the bottom right. "))
            #TODO use arrays/lists and put player choice into existing list, same with computer
            if player_choice in row_list:



                #debug command to check if player chose a valid number
                print("Player chose " + str(player_choice) + " at index " + str(row_list.index(player_choice)))
            
                continue
            #debug command to check if player chose a valid number
            elif player_choice not in row_list:
                print("Whoops! Choose a number 1-9.")
                continue

        
    elif play == 'q' or play == 'Q':
        quit()
    else:
        print("player did not enter either, entered " + play + " instead")
