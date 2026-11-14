import random 

option = ["Rock", "Paper", "Scissor"]

print("********ROCK PAPER SCISSOR***********")
  
player_score = 0
draws = 0
computer_score = 0


while True:
    computer_choice = random.choice(option)
    player_choice = input("Enter your choice: ").capitalize()
    
    print("Computer chose:", computer_choice)
    print("You chose: ",player_choice)
    
    
    if player_choice == computer_choice:
        draws += 1
        print("ITS DRAW!!")
        
    elif  player_choice == "Rock" and computer_choice == "Paper":
        computer_score += 1
        print("YOU LOST!!")
    elif player_choice == "Scissor" and computer_choice == "Rock":
        computer_score += 1
        print("YOU LOST!!")
    elif player_choice == "Paper"" and computer_choice == ""Scissor":
        computer_score += 1
        print("YOU LOST!!")
        
    else:
        player_score += 1
        print("YOU WON!!")
    print("Your wins: ", player_score)
    print("computer wins:", computer_score)
    print("draws: ", draws)
    play_again = input("Press enter to play again or Q to quit: ").lower()
    
    if play_again == "q":
        print("THANKS FOR PLAYING")
        break