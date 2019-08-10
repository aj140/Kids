# This is a game to play paper, rock, scissors
from random import randint

# Start the game here
print ("Welcome to our lovely paper, rock, scissors game!\n")

playerName = input("What is your name?\n")

print ("Hello %s, it's nice to meet you!\n" % playerName)

possibleChoices = ["paper", "rock", "scissors"]

choiceUnderstood = False

# This while loop goes on until the player puts in a proper choice
while choiceUnderstood != True:
  playerChoice = input (playerName + " choose paper, rock, or scissors\n")
  playerChoice = playerChoice.lower()

  if playerChoice in possibleChoices:
    print ("Ok! You have chosen %s" % playerChoice)
    choiceUnderstood = True
  else:
    print ("Please type in either paper, rock, or scissors - not %s" % playerChoice)

# Now, let's have the computer make a choice also using randint
randomNum = int(randint(1,3))
if randomNum == 1:
  computerChoice = "paper"
elif randomNum == 2:
  computerChoice = "rock"
else:
  computerChoice = "scissors"

print ("The computer has chosen %s" % computerChoice)

if playerChoice == "paper":
  if computerChoice == "scissors":
    winLoseTie = "lose"
  elif computerChoice == "rock":
    winLoseTie = "win"
  else:
    winLoseTie = "tie"
elif playerChoice == "rock":
  if computerChoice == "paper":
    winLoseTie = "lose"
  elif computerChoice == "scissors":
    winLoseTie = "win"
  else:
    winLoseTie = "tie"
else:
  if computerChoice == "rock":
    winLoseTie = "lose"
  elif computerChoice == "paper":
    winLoseTie = "win"
  else:
    winLoseTie = "tie"

print ("That means you %s" % winLoseTie)
