# Question6 Write a program for a matchstick game being played between the computer and a user. Your
#program should ensure that the computer always wins. Rules for the game are as follows:
#• There are 21 matchsticks.
#• The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
#• After the person picks, the computer does its picking.
#• Whoever is forced to pick up the last matchstick loses the game.

def matchstick_game():
    total_matchsticks = 21
    
    print("Welcome to the Matchstick Game!")
    print("Rules: There are 21 matchsticks. You can pick 1, 2, 3, or 4 matchsticks on your turn.")
    print("The player forced to pick the last matchstick loses the game.")

    while total_matchsticks > 1:
        # User's turn
        user_pick = int(input(f"\nThere are {total_matchsticks} matchsticks left. How many do you pick? (1-4): "))
        
        if user_pick < 1 or user_pick > 4:
            print("Invalid choice. Please pick between 1 and 4 matchsticks.")
            continue
        
        total_matchsticks -= user_pick
        
        if total_matchsticks == 1:
            print("\nYou picked the last matchstick. You lose!")
            break
        
        # Computer's turn
        computer_pick = 5 - user_pick
        total_matchsticks -= computer_pick
        print(f"Computer picks {computer_pick} matchstick(s). {total_matchsticks} matchstick(s) left.")

        if total_matchsticks == 1:
            print("\nComputer left you the last matchstick. You lose!")
            break

# Run the game
matchstick_game()