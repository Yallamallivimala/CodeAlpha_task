import random

def hangman():
    words = ["apple", "tiger", "india", "chair", "robot"]

    clues = {
        "apple": "A fruit that keeps the doctor away.",
        "tiger": "A wild animal with black stripes.",
        "india": "A country in South Asia.",
        "chair": "You sit on it.",
        "robot": "A machine that can act like a human."
    }

    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    incorrect_guesses = 0
    max_attempts = 6
    guessed_letters = []

    print("💡 Welcome to Hangman Game!")
    print("Guess the word:")
    print("🔍 CLUE:", clues[secret_word])    

    while incorrect_guesses < max_attempts and "_" in guessed_word:
        print("\nCurrent word: ", " ".join(guessed_word))
        print("Guessed letters:", guessed_letters)
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good job! Correct guess.")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print("❌ Wrong guess!")

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n💀 Game Over! You ran out of attempts.")
        print("The correct word was:", secret_word)

hangman()
