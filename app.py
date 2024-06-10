# Write "hello world" to the console
print("Hello World")

# Create a multiplayer game in the console where two players can play against each other
# Path: app.py
# Write "Player 1" to the console
print("Player 1")
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# Path: app.py
# Write "Choose rock, paper, or scissors" to the console
print("Choose rock, paper, or scissors")
# Read the input from the console
user1_input = input()
# If the input is not rock, paper, or scissors, write "Invalid option" to the console
if user1_input not in ["rock", "paper", "scissors"]:
    print("Invalid option")
# Write "Player 2" to the console   
print("Player 2")
# Write "Choose rock, paper, or scissors" to the console
print("Choose rock, paper, or scissors")
# Read the input from the console
user2_input = input()
# If the input is not rock, paper, or scissors, write "Invalid option" to the console
if user2_input not in ["rock", "paper", "scissors"]:
    print("Invalid option")

# If both players choose the same option, write "It's a tie" to the console
if user1_input == user2_input:
    print("It's a tie")
# If player 1 chooses rock and player 2 chooses scissors, write "Player 1 wins" to the console
elif user1_input == "rock" and user2_input == "scissors":
    print("Player 1 wins")
# If player 1 chooses rock and player 2 chooses paper, write "Player 2 wins" to the console
elif user1_input == "rock" and user2_input == "paper":
    print("Player 2 wins")
# If player 1 chooses paper and player 2 chooses rock, write "Player 1 wins" to the console
elif user1_input == "paper" and user2_input == "rock":
    print("Player 1 wins")
# If player 1 chooses paper and player 2 chooses scissors, write "Player 2 wins" to the console
elif user1_input == "paper" and user2_input == "scissors":
    print("Player 2 wins")  
# If player 1 chooses scissors and player 2 chooses paper, write "Player 1 wins" to the console
elif user1_input == "scissors" and user2_input == "paper":
    print("Player 1 wins")
# If player 1 chooses scissors and player 2 chooses rock, write "Player 2 wins" to the console
elif user1_input == "scissors" and user2_input == "rock":
    print("Player 2 wins")
# If player 1 chooses an invalid option, write "Player 2 wins" to the console
elif user1_input == "Invalid option":
    print("Player 2 wins")
# If player 2 chooses an invalid option, write "Player 1 wins" to the console
elif user2_input == "Invalid option":
    print("Player 1 wins")
# If player 1 and player 2 choose an invalid option, write "It's a tie" to the console
else:
    print("It's a tie")
    

