https://github.com/adeosunvictor/Building-a-Simple-Hangman-Game-in-Python.git

Building a Simple Hangman Game in Python

Building a Simple Hangman Game in Python
The Hangman game is a classic word-guessing game that provides an excellent opportunity to practice fundamental programming concepts. In this article, we'll explore a Python implementation of Hangman, which covers basic operations such as list manipulation, user input, loops, and conditionals.

The Hangman Code
Here is the complete code for our simple Hangman game:

      import random  # Import the random module to use its functions
      
      print("Welcome to Hangman!!!")  # Print a welcome message
      words = ["gate", "cow", "it", "Ibadan", "Sango"]  # List of possible words to guess you are free to change thw words
      
      incorrect_guess = 0  # Initialize the counter for incorrect guesses
      max_attempt = 4  # Set the maximum number of incorrect guesses allowed
      
      guessed_letter = []  # List to store guessed letters
      
      guessed_word = random.choice(words)  # Randomly choose a word from the list of words
      
      # Start a while loop that runs until the number of incorrect guesses reaches the maximum allowed
      while incorrect_guess < max_attempt:
          # Create a display list with correctly guessed letters or underscores for unguessed letters
          display = [letter if letter in guessed_letter else "_" for letter in guessed_word]
          print(" ".join(display))  # Print the current state of the guessed word
          guess = input("Guess a letter: ")  # Prompt the user to guess a letter
          guessed_letter.append(guess)  # Add the guessed letter to the list of guessed letters
          if guess in guessed_word:  # Check if the guessed letter is in the chosen word
              print("Correct")  # Inform the user that the guess was correct
          else:
              incorrect_guess += 1  # Increment the incorrect guess counter
              print(f"Incorrect!!!!!!, you have {max_attempt - incorrect_guess} guesses left")  # Inform the user of incorrect guess and remaining attempts
      
          # Check if all letters in the chosen word have been guessed
          if all(letter in guessed_letter for letter in guessed_word):
              print("Congratulations!!! The correct answer was", guessed_word)  # Congratulate the user for guessing the word correctly
              break  # Exit the loop as the word has been guessed
explanation of each line of code are as follows:

Importing Libraries

      import random
  The random module is imported to allow the selection of a random word from a predefined list.


Introduction and Word List

    print("Welcome to Hangman!!!")
    words = [""]//make a list of words you want in the dictionary 

Game Initialization

        incorrect_guess = 0
        max_attempt = 4
        guessed_letter = []
        guessed_word = random.choice(words)
        Several variables are initialized:
      
  incorrect_guess: Counts the number of incorrect guesses.
  max_attempt: Maximum number of incorrect guesses allowed.
  guessed_letter: A list to keep track of the letters guessed by the player.
  guessed_word: A random word selected from the words list.


  Main Game Loop
    
      while incorrect_guess < max_attempt:
   The game runs in a loop that continues until the number of incorrect guesses reaches the maximum allowed.


Displaying the Word

    display = [letter if letter in guessed_letter else "_" for letter in guessed_word]
    print(" ".join(display))
 The current state of the guessed word is displayed. Correctly guessed letters are shown, while the rest are represented by underscores.
  

Guess Input

            guess = input("Guess a letter: ")
            guessed_letter.append(guess)
  The player is prompted to guess a letter. The guessed letter is added to the guessed_letter list.


Checking the Guess

    
    if guess in guessed_word:
        print("Correct")
    else:
        incorrect_guess += 1
        print(f"Incorrect!!!!!!, you have {max_attempt - incorrect_guess} guesses left")
    The code checks if the guessed letter is in the word:
  
  If correct, a confirmation message is printed.
  If incorrect, the incorrect_guess counter is incremented and a message indicating the remaining attempts is displayed.

Winning Condition

      if all(letter in guessed_letter for letter in guessed_word):
          print("Congratulations!!! The correct answer was", guessed_word)
          break
If the player has guessed all the letters in the word, a congratulatory message is displayed, and the loop breaks, ending the game.
