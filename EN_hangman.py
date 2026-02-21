import random

word_list = ["aardvark", "baboon", "camel", "python", "developer"]
max_lives = 6

stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length
used_letters = []
lives = max_lives
game_over = False

print("🎮 Welcome to Hangman!")

while not game_over:

    print(stages[max_lives - lives])  # 👈 desenho da forca
    print(f"\nWord: {' '.join(display)}")
    print(f"Lives: {lives}")
    print(f"Used letters: {', '.join(used_letters)}")

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Type a single valid letter.")
        continue

    if guess in used_letters:
        print("🔁 You already tried that letter.")
        continue

    used_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct!")

        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print("❌ Wrong!")

        if lives == 0:
            game_over = True
            print(stages[max_lives])
            print("\n💀 You lost!")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("\n🏆 You win!")
        print(f"The word was: {chosen_word}")