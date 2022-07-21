import random

class Game:
    def __init__(self) -> None:
    
        self.user = self.get_user_item
        self.comp = self.get_computer_item
    
    def get_user_item():
        user = input("Choose rock paper or scissors: ")
        choices = ["rock","paper","scissors"]    
        while user not in choices:
            user = ("select a valid letter")
        return user


    def get_computer_item():
        choices = ["rock","paper","scissors"] 
        rando = random.choice(choices)
        print(rando)
        return rando

    def get_game_result(self):
        if self.user == self.comp :
            print("Tie")
        elif self.user == "rock":
            if self.comp == "paper":
                print("You lose!")
            if self.comp == "scissors":
                print("You win!")
        elif self.user == "paper":
            if self.comp == "scissors":
                print("You lose!")
            if self.comp == "rock":
                print("You win!")
        elif self.user == "scissors":
            if self.comp == "rock":
                print("You lose!")
            if self.comp == "paper":
                print("You win!")
    get_user_item()
    get_computer_item()
    get_game_result()
    



# from random import randint

# class Game:
#     def
#     t = ["Rock", "Paper", "Scissors"]


#     computer = t[randint(0,2)]


#     player = False

#     while player == False:

#         player = input("Rock, Paper, Scissors?")
#         if player == computer:
#             print("Tie!")
#         elif player == "Rock":
#             if computer == "Paper":
#                 print("You lose!", computer, "covers", player)
#             else:
#                 print("You win!", player, "smashes", computer)
#         elif player == "Paper":
#             if computer == "Scissors":
#                 print("You lose!", computer, "cut", player)
#             else:
#                 print("You win!", player, "covers", computer)
#         elif player == "Scissors":
#             if computer == "Rock":
#                 print("You lose...", computer, "smashes", player)
#             else:
#                 print("You win!", player, "cut", computer)
#         else:
#             print("That's not a valid play. Check your spelling!")
    
#         player = False
#         computer = t[randint(0,2)]



            