import random
def hangman():
  words=["apple", "tiger", "python", "banana", "school"]
  word= random.choice(words)

  guessed=[]
  attempts=6
  print("Welcome to Hangman Game!")
  print("Guess the word one letter at a time.")

  while attempts > 0:

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

    guessed.append(guess)

    print("Attempts left:", attempts)

    if attempts == 0:
      print("Game Over!")
      print("Correct word was:", word)
hangman()

