import check_input
from dictionary import words
from dictionary import alphabet
import random
'''
2/7/2024
5-Letter Hangman Game
'''


def main():
  '''The main function'''
  print("-Hangman-")
  keepGoing = True
  while keepGoing:
    #Start of game
    theWord = random.choice(words)
    win = False
    num_incorrect = 0
    incorrectLetters = []
    correctLetters = []
    while (win == False and num_incorrect != 6):
      #This will repeat every guess
      display_letters(incorrectLetters, "\nIncorrect selections:")
      displayGallows(num_incorrect)
      print()
      #The word
      display_letters(displayWord(theWord, correctLetters))
      print()
      remaining = get_letters_remaining(correctLetters, incorrectLetters)
      #Remaining letters
      display_letters(remaining, "Letters remaining:")
      guess = input("\nEnter a letter: ").strip().upper()

      #Filters guesses
      if guess not in alphabet:
        print('That is not a letter.')
      elif guess in correctLetters or guess in incorrectLetters:
        print('You have already used that letter.')
      elif guess in theWord:
        print("\nCorrect!")
        correctLetters.append(guess)
        #Check if correctLetters is the same as theWord
        if all(letter in correctLetters for letter in theWord):
          win = True
      else:
        print("\nIncorrect!")
        incorrectLetters.append(guess)
        num_incorrect += 1
        incorrectLetters.sort()
    if win:
      print()
      displayGallows(num_incorrect)
      print()
      display_letters(displayWord(theWord, correctLetters))
      print()
      print("You win!")
    else:
      print("You lose!")
      displayGallows(6)
      print("The word was " + theWord)
    play_again = check_input.get_yes_no("Play again (Y/N)? ")
    keepGoing = play_again


def displayGallows(num_incorrect: int):
  '''Displays the hangman figure
    stage determines how the gallows should be drawn'''
  gallows = ["========", "||/      |", "||      ", "||      ", "||      "]
  if num_incorrect == 0:
    gallows = ["========", "||/    |", "||      ", "||      ", "||      "]
  elif num_incorrect == 1:
    gallows = ["========", "||/    |", "||     o", "||      ", "||      "]
  elif num_incorrect == 2:
    gallows = ["========", "||/    |", "||     o", "||     |", "||      "]
  elif num_incorrect == 3:
    gallows = ["========", "||/    |", "||    \\o", "||     |", "||      "]
  elif num_incorrect == 4:
    gallows = ["========", "||/    |", "||    \\o/", "||     | ", "||       "]
  elif num_incorrect == 5:
    gallows = ["========", "||/    |", "||    \\o/", "||     |", "||    /  "]
  else:
    gallows = ["========", "||/    |", "||    \\o/", "||     |", "||    / \\"]

  for line in gallows:
    print(line)


def displayWord(word, correctGuesses):
  '''Displays the current state of the word
  Word is the word that should be displayed
  CorrectGuesses is a list of correct guesses
  '''
  #precondition
  if (len(correctGuesses) == 0):
    return ["_", "_", "_", "_", "_"]

  listWord = []
  for i in range(5):
    listWord.append(word[i])

  #Word is good, make gaps
  for i in range(0, 5):
    if listWord[i] not in correctGuesses:
      listWord[i] = "_"

  return listWord


def get_letters_remaining(correct, incorrect):
  '''Displays the remaining letters
  Correct is a list of the correctly guessed letters
  Incorrect is a list of the incorrectly guessed letters
  A list of the remaining letters will be returned'''
  #Creates a new list
  temp = []
  for i in range(26):
    temp.append(alphabet[i])

  #Removes the letters already used
  for letter in correct:
    temp.remove(letter)

  for letter in incorrect:
    temp.remove(letter)

  return temp


def display_letters(letters, prefix=""):  #Done
  '''Takes a string and displays each element with a space between
  Prefix is a statement that will be printed before the letters are displayed'''
  if (prefix != ""):
    print(prefix, end=" ")
  for let in letters:
    print(let, end=" ")
  #End with a new line
  print()


main()
