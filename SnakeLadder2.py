#22-1440738 M.Hamza Shahid
#23-10903 Muhammad Muzafar 
import random # For dice values each turn.
import snakeorladderfunc as s #importing module function.
dict1 = {}
import Board 
import boardp1 as bp1
import boardp2 as bp2
Board.my_board()
def main():
    # time complaxity O(n)
    
    print(Board.my_board())
    player1 = 0
    player2 = 0
    score = 0

    # When any of the player gets to 100 score game will end.
    while (score != 100):# time complaxity O(n)
        bp1.boardp1()
        user_input = input("\nPlayer 1, Press Y/y to roll the dice: " )
        if (user_input == "y" or user_input == "Y"):
            die = random.randint(1,6) #Rolling the dice, Value can be 1,2,3,4,5 and 6.
            print("\nPlayer 1 rolled the dice, Die value = " , die)

            a = player1 + die # Adding the score of player , with dice value.
            if a <= 100:
                player1 = player1 + die # If the score is below 100, player can move his gitti.
            else:
                player1 = player1 + 0 # If the score is going above 100, player is not allowed to move his gitti, hence staying in his current position.
            print("\nPlayer 1 Score = " ,player1)
            x = s.snakeorladderfunc(player1) #Check if player's is on ladder or snake.
            player1 = x #Update the score
            if dict1[player1] == "P2":
                dict1[player1] = "P1 , P2"
            else:
                dict1[player1] = "P1"
            print("\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t" % tuple(dict1.values()))
             


           

            #If player 1 's score is 100, then End the game, No need for player 2 to take his turn.
            if player1 == 100:
                score = player1
                break;
        user_input2 = input("\nPlayer 2, Press Y/y to roll the dice; " )
        if (user_input2 == "y" or user_input2 == "Y"):
            die2 = random.randint(1,6) #Rolling the dice, Value can be 1,2,3,4,5 and 6.
            print("\nPlayer 2 rolled the dice, Die Value = ", die2)
            b = player2 + die2 # Adding the score of player , with dice value.
            if b <= 100:
                player2 = player2 + die2 # If the score is below 100, player can move his gitti.
            else:
                player2 = player2 + 0 # If the score is going above 100, player is not allowed to move his gitti, hence staying in his current position.
            print("\nPlayer 2 Score = ", player2)
            y = s.snakeorladderfunc(player2) #Check if player's is on ladder or snake.
            player2 = y #Update the score
            bp2.boardp2()
            if dict1[player2] == "P1":
                dict1[player2] ="P1 , P2"
            else:
                dict1[player2] = "P2"
            print("\n\t|  %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t|  % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s | %s | %s | %s | %s | %s | %s | %s | %s | \n\t---------------------------------------------------\n\t| % s | %s  | %s  | %s  | %s | %s  | %s  | %s  | %s  | %s  | \n\t---------------------------------------------------\n\t " % tuple(dict1.values()))
            

            #If player 2 's score is 100, then End the game, No need for player 1 to take his turn.
            if player2 == 100:
                score = player2
                break;
    if player1 == score:
        print("\nPlayer 1 WINS !!!")
    elif player2 == score:
        print("\nPlayer 2 WINS !!!")
        
start = input("\n Start the game by pressing y: ") #Players will be asked to start the game
if start == "y":
    main()       
user_input3 = input("\nGAME OVER, Do you want to restart game? press y or n: ") #After the game is completed players can retart the game or exit it.
if user_input3 == "y":
    print("\n")
    print("\n")
    main()
if user_input3 == "n":
    exit()
    


