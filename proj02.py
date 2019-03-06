# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:05:37 2018

@author: arthu
"""

#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")
computer_count = 0
player_count = 0
while int(play_str) != 0:
#Initialize the two piles to have 5 stones
    pile_1 = 5
    pile_2 = 5
    #Print out the amounts in the pile
    pile_1_str = str(pile_1)
    pile_2_str = str(pile_2)
    print("start --> Pile 1: "+pile_1_str+" ;Pile 2: "+pile_2_str )
    while pile_1 > 0 or pile_2 >0:
        #Initialize player. Use %, if result is 0, then player turn, if anything else, computer turn
        player = True
        while player == True:
            pile_chosen = input("Choose a pile(1 or 2):")
            pile_chosen_int = int(pile_chosen)
            stone_amount = input("Choose stones to remove from pile:")
            stone_amount_int = int(stone_amount)
            if stone_amount_int > 3 or stone_amount_int < 1:
                print("That is not a valid move")
                continue
            if pile_chosen_int == 1:
                pile_1 = pile_1 - stone_amount_int
                pile_1_str = str(pile_1)
                pile_2_str = str(pile_2)
                print ("Player -> removed "+stone_amount+" stones from pile "+pile_chosen)
                print ("Pile 1: "+pile_1_str+"  Pile 2: "+pile_2_str)
            if pile_chosen_int == 2:
                pile_2 = pile_2 - stone_amount_int
                pile_1_str = str(pile_1)
                pile_2_str = str(pile_2)
                print ("Player -> removed "+stone_amount+" stones from pile "+pile_chosen)
                print ("Pile 1: "+pile_1_str+"  Pile 2: "+pile_2_str)
            if pile_1 == 0 and pile_2 == 0:
                print ("Player wins!")
                player_count += 1
            player = False
        while player == False:
            #choose the opposit one that the player chose
            if pile_chosen_int == 1:
                pile_2 = pile_2 -1
                pile_1_str = str(pile_1)
                pile_2_str = str(pile_2)
                print ("Computer -> removed 1 stone from pile 2")
                print ("Pile 1: "+pile_1_str+"  Pile 2: "+pile_2_str)
            if pile_chosen_int == 2:
                pile_1 = pile_1 - 1
                pile_1_str = str(pile_1)
                pile_2_str = str(pile_2)
                print ("Computer -> removed 1 stone from pile 1")
                print ("Pile 1: "+pile_1_str+"  Pile 2: "+pile_2_str)
            player = True
            if pile_1 == 0 and pile_2 == 0:
                print ("Computer wins!")
                computer_count += 1
    player_count_str = str(player_count)
    computer_count_str = str(computer_count)
    print ("Score: -> Human: "+player_count_str+" Computer: "+computer_count_str)
    
    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")

else:
   print("\nThanks for playing! See you again soon!")