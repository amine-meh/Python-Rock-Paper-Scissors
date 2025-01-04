import random

user_wins = 0
computer_wins = 0
ties = 0
options = ["rock", "scissors", "paper"]

print("Welcome to the rock/scissors/paper game!\n")

while True:
  user_pick = input("Pick one of the following options (Rock/Scissors/Paper) or Q to quit the game\n").lower()

  if user_pick == 'q':
    break

  if user_pick not in options:
    print("Please pick a valid option (Rock/Scissors/Paper)")
    continue

  #computer_pick = random.choice(options)

  index = random.randint(0, 2)
  computer_pick = options[index]
  print("Computer picked : ", computer_pick) 

  if user_pick == "rock" and computer_pick == "Scissors" :
    print("You win!")
    user_wins += 1

  elif user_pick == "scissors" and computer_pick == "Paper" :
    print("You win!")
    user_wins += 1

  elif user_pick == "paper" and computer_pick == "Rock" :
    print("You win!")
    user_wins += 1

  elif user_pick == computer_pick :
    print("It's a tie!")
    ties += 1

  else :
    print("Computer wins!")
    computer_wins += 1

print("Computer wins : ", computer_wins)
print("User wins : ", user_wins)
print("Ties : ", ties)
print("Good By")