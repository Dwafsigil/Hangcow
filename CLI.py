# hangcow by cat

import random


def display_word(word, guessed, attempts):
    if attempts == 6:
        hangman = " "
    elif attempts == 5:
        hangman = "𓃉"
    elif attempts == 4:
        hangman = "𓃿"
    elif attempts == 3:
        hangman = "𓃾"
    elif attempts == 2:
        hangman = "𓄀 "
    elif attempts == 1:
        hangman = "𓃒 "
    else:
        hangman = "🥩"

    # if a letter is GUESSED, reveal it, otherwise leave it blank
    return hangman + " || " + " ".join([letter if letter in guessed else "_" for letter in word])


def hangman():
    # word list
    words = ["cow", "cattle", "calf", "bull", "heifer", "ox", "steer", "bovine", "udder", "hoof",
             "horn", "muzzle", "hide", "leather", "herd", "pasture", "graze", "milk", "dairy", "flank",
             "beef", "veal", "rump", "brisket", "ribeye", "dairy", "grass", "cud", "sirloin", "salisbury",
             "tail", "barn", "stall", "feedlot", "slaughterhouse", "butchery", "branding", "farmer", "ranch",
             "livestock",
             "cream", "cheese", "hay", "manure", "steak", "flat iron", "prime rib", "medium rare", "well done",
             "barbecue"]

    word = random.choice(words)
    guessed = set()
    attempts = 6

    print("welcome to YIPPEE hangcow \ntry to guess the word and not get butchered!")

    while attempts > 0:
        print(display_word(word, guessed, attempts))

        guess = input("enter a letter: ").lower()

        # dont guess something twice
        if guess in guessed:
            print("\n\nyou already guessed that letter!")
            continue

        # dont guess something twice
        if len(guess) != 1 or not guess.isalpha():
            print("\n\nnot a valid letter!")
            continue

        # if ok, add it to the guessed letters list
        guessed.add(guess)

        # is it in the word?
        if guess in word:
            print("\n\n\nYIPPEE!")
            # did you guess everything?
            if set(word).issubset(guessed):
                print(display_word(word, guessed, attempts))
                print("well done! ...or maybe not?")
                break
        else:
            attempts -= 1
            print("\n\n\n[EXTREMELY LOUD INCORRECT BUZZER]")

        # ran out of attempts
        if attempts == 0:
            print(display_word(word, list(map(chr, range(97, 123))), attempts))
            print("a steak well done!")


# play
hangman()