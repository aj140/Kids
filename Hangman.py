from random import randint

easyArray = ["blue", "red", "cow", "the", "dog", "cat", "tree", "hello", "moon", "father"]
mediumArray = ["kitchen", "computer", "basketball", "soccer", "circus", "volcano", "explanation", "underwater", "clothing", "flower", "headphones", "rabbit"]
hardArray = ["accommodation", "archaeologist","psychology", "palaeontologist", "uncharacteristically", "dendrochronological",  "assistant"]
mothersDayArray = ["celebration","love","mother","happiness","gift","card","flowers"]

wordSetsArray = [easyArray, mediumArray, hardArray, mothersDayArray]

print("############ WELCOME TO AKASH & DADDY'S SUPER HANGMAN GAME! ############")
print("Which word set do you want to use:")
print("[0] Easy")
print("[1] Medium")
print("[2] Hard")
print("[3] Special Surprise for Mama!")

whichWordSet = int(input("Please enter the number\n"))

if (whichWordSet == 3):
  print("\n\n\n********** Happy Mother's Day Mama! We love you!!  **********\n\n\n")
  print("                              ,....                         ")     
  print("                           ,,''    \"\"-.                     ")        
  print("                      .--,,'           \"\",                  ")             
  print("                    ,.  ,'     .-, ...    `                 ")                
  print("                   ,'  ,'   .-\"   P  ``.  : .,.             ")                   
  print("               ,'\".'   :   ,   ,--;-,   `.,\"   `.           ")               
  print("              ,'  :    :  '    :  :  `    '-,   `.          ")              
  print("              ,  ,     :  :    :  t. ',   :  `   `          ")           
  print("             ,'  :     `. :    :   `\"'`.  :  :   :          ")          
  print("             :   :       :`.   `.     ,'  :  :    :         ")                 
  print("             `.  `       : `.   `-,...( .,'  ,   ,'         ")        
  print("              :   :      :   `.      ' \"    ,'   :          ")         
  print("              `. ,\",     `.    \"----'      ,'    ,          ")          
  print("               `\", `,.    `,             .'      :          ")               
  print("                 :   `,     \"-,.,.    ,,'       ,           ")         
  print("                 `     `,.      :'---\"'       ,'            ")     
  print("                  t      `-....-td           ,'             ")          
  print("                   \"-.            \"-,,....,-\"               ")         
  print("       ,,-,.  ..      `..            :   ,.''\"----\"\",...    ")      
  print("   ,'\"\"'    \"\" `-. .    `T-..    ..-`).,,'             `.   ")       
  print(" ,\"'             `\" t    ,( `\"\"\"\"   ,' '    '    ,      `\"` ")         
  print(" : --. ,   `         `.  ::       ,.       :     : ,''   .' ")           
  print(" (   `\"),  `.   -.    `. `,      .'   ,    ,   ,'`\"\"-    :  ")          
  print(" : ,...t,`,.'    `     `,:`,.   '    ,'   ,\",--t       ,'   ")       
  print("  `         `.   `.  ,  `\", '   :,   :  ,.''    \"--   ,'    ")      
  print("  `,          :  ,'  `, `,` t   ::   : ,.:           .'     ")   
  print("   `  -,..---\"`'\"''.  : ,'`,`.  ::   ,\"'`\"-,...    ,,'      ")    
  print("    `,              :`'\"'  `,t  :`.,\",         '  ,'        ") 
  print("      t          ,.-`---,.. : t )' '-`-.....    -''         ")        
  print("       `. ,\"\"\"\"\"\"'      : ``.  `,\",           .'            ")      
  print("        `\"`-.          '    `,   :`,..,.,'\"\"\"\"              ")                                
  print("            `-,...-,.,'       \", `,   '                     ")         
  print("                                \", `,.                      ")         
  print("                                 :   `,.. ,.                ")           
  print("                                  \"\"\"-t.``'`-..    ,...,    ")     

wordArray = wordSetsArray[whichWordSet]
randomIndex = randint(0, (len(wordArray) - 1))
answerWord = wordArray[randomIndex]
#print( "CHEAT MODE ON! The answer is %s\n" % answerWord )
guessesRemaining = 6

usersGuesses = []

while (guessesRemaining > 0):

  wordToShow = ""
  guessesSoFar = ""
  wonTheGame = True
  
  for c in answerWord:
    
    inUsersGuesses = False

    for prevGuess in usersGuesses:
      if (prevGuess == c):
        inUsersGuesses = True
    
    if (inUsersGuesses == True):
      wordToShow = wordToShow + c + " "
    else:
      wordToShow = wordToShow + "_ "
      wonTheGame = False

  print ("\n" + wordToShow)

  if (wonTheGame == True):
    print ("\nHooray! You got the correct word! :) :) :)")
    break

  if (guessesRemaining == 1):
    print("\nOh dear, you only have one guess left!!")
  else :
    print("\nYou have %d guesses left" % guessesRemaining)

  for letter in usersGuesses:
    guessesSoFar = guessesSoFar + letter + " "

  print ("So far you have guessed these letters: %s" % guessesSoFar)
  usersGuess = input("Please guess a letter you think is in the secret word.\n")
  usersGuesses.append(usersGuess)

  if (usersGuess in answerWord):
    print("\nYes! There is at least one '%s'" % usersGuess)
    
  else:
    print("\nSorry, but there is no '%s' in the secret word  :(" % usersGuess)
    guessesRemaining = guessesRemaining - 1
    if (guessesRemaining == 0):
      print("\nSorry, but you have lost the game :( :( :(")
      print("The correct answer was '%s'" % answerWord)
      break
