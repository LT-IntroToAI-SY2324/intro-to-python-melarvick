# We will write a rock paper scissors game in class - Complete it in this file

import random


player_choice= "rock"
computer_choice= "paper"

def get_choices():
    options=['rock', 'paper', 'scissors']
    player_choice= input("Enter a choice (rock, paper, scissors): ")
    computer_choice=random.choice(options)
    choices= {"player": player_choice, "computer": computer_choice}

    return choices

def check_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "It's a tie"
    elif player=="rock":
        if computer== "scissors":
            return "Rock smashes scissors. You win!"
        else:
            return "Paper covers rock. You lose."
    elif player=="scissors":
        if computer=="paper":
            return "Scissors cut paper. You win!"
        else:
            return "Rock smashes scissors. You lose."
    elif player=="paper":
        if computer=="scissors":
            return "Scissors cut paper. You lose."
        else:
            return "Paper covers rock. You win!"

    

choices= get_choices()
# print(choices)

result= check_winner(choices["player"], choices["computer"])
print(result)