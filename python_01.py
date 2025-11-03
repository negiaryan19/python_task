import random

words = ["apple", "banana", "orange", "grape", "mango","BMW","SWIFT","JAVASCRIPT","PYTHON","FULL STACK"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

display_word = []
for letter in secret_word:
    display_word.append("_")

print("Let's play Hangman!")
print("Try to guess the word - it could be a fruit, car, or programming language!")
print(f"You can have {max_wrong_guesses} wrong guesses.")

while wrong_guesses < max_wrong_guesses and "_" in display_word:
    
    print("\nCurrent word: ", " ".join(display_word))
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    print(f"Letters you tried: {', '.join(guessed_letters)}")
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1:
        print("Please type only one letter!")
        continue
    
    if not guess.isalpha():
        print("Please type a letter from A to Z!")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
  
    if guess in secret_word.lower():
        print(f"Good! '{guess}' is in the word!")
        
        for i in range(len(secret_word)):
            if secret_word[i].lower() == guess:
                display_word[i] = secret_word[i]  # Keep original case
    else:
        wrong_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

print("\n" + "="*30)
if "_" not in display_word:
    print(f"🎉 You won! The word was: {secret_word}")
else:
    print(f"💀 Game over! The word was: {secret_word}")
print("Thanks for playing!")