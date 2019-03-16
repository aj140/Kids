from random import randint

theAnswer = randint(1, 100)
#print( "CHEAT MODE ON! The answer is %d\n" % theAnswer )
guessesRemaining = 6
totalGuesses = 0

while (guessesRemaining > 0):

  usersGuess = int( input("What do you think the secret number is?\n") )
  guessesRemaining = guessesRemaining - 1
  totalGuesses = totalGuesses + 1

  if (usersGuess == theAnswer):
    print("WOW! You got the answer!!\n")
    print("You got the answer in %d guesses!" % totalGuesses)
    guessesRemaining = 0
  elif (guessesRemaining == 0):
    print("Sorry, you did well but the game is over :(")
    print("The answer was %d" % theAnswer)
  else:
    if (usersGuess > theAnswer):
      print("Try again, the answer is less than your guess!")
    else:
      print("Try again, but the answer is higher than your guess!")
    if (guessesRemaining == 1):
      print("Oh dear, you only have one guess left!!")
    else :
      print("You have %d guesses left" % guessesRemaining)
