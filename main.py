import tkinter as tk
import random
#from playsound import playsound
import pygame
import time
#from PIL import Image, ImageTk

# Testing that github is working and stuff

# Setting up sound effects and assigning them to variables
pygame.mixer.init()
wrong_answer = pygame.mixer.Sound("roblox-oof-sound.mp3")
game_lost = pygame.mixer.Sound("thepriceisright-loserhorns.mp3")
right_answer = pygame.mixer.Sound("ding-sound-effect_1.mp3")
game_won = pygame.mixer.Sound("yippee-sound-effect.mp3")

class HangcowGUI:
    # Setting up the main window of the GUI
    def __init__(self, root):
        root.title("Hangcow") # Title of the app
        root.geometry("800x500") # Setting dimensions of window

        # Creating the Variables
        # Word List (Note: Every word is cow-related) Could up complexity by adding more words and set easy, normal, and hard difficulty
        self.words = ["cow", "cattle", "calf", "bull", "heifer", "ox", "steer", "bovine", "udder", "hoof",
             "horn", "muzzle", "hide", "leather", "herd", "pasture", "graze", "milk", "dairy", "flank",
             "beef", "veal", "rump", "brisket", "ribeye", "grass", "cud", "sirloin", "salisbury",
             "tail", "barn", "stall", "feedlot", "slaughterhouse", "butchery", "branding", "farmer", "ranch", "livestock",
             "cream", "cheese", "hay", "manure", "steak", "flat iron", "prime rib", "medium rare", "well done", "barbecue"]

        self.secret_word = random.choice(self.words) # Chooses a random word from the words list
        self.guessed_letters = set() # Keeps track of letters guessed so far
        self.attempts_left = 6 # The number of attempts the player has left
        self.hangcow_graphics = ["🥩", "𓃒", "𓄀", "𓃾", "𓃿", "𓃉", " "] # These are the graphics corresponding to the current attempt. Attempts = 0 would show steak, 1 would show cow, etc.

        # GUI Components
        # Displays the hangcow_graphics corresponding to current player attempt
        self.hangcow_graphics_label = tk.Label(root, text=self.hangcow_graphics[self.attempts_left], font=("Arial", 60))
        self.hangcow_graphics_label.pack(pady=10) # Adding a bit of y distance between the UI elements

        # Displays the randomly chosen word. Parts of the word will be "_" to show that the letter hasn't been guessed yet
        self.word_label = tk.Label(root, text=self.display_word(), font =("Arial",60)) #display_word is the method that has the logic for the letter and underscores
        self.word_label.pack(pady=15)

        # Entry box to make your guesses
        self.player_entry = tk.Entry(root, font=("Arial", 40), justify="center")
        self.player_entry.pack(pady=10)
        self.player_entry.bind("<Return>", self.player_guess) # When you hit the enter key, you submit the letter as your guess and it runs through the make_guess method to update game state

        # Message box to update the game state for the players the see
        self.message_label = tk.Label(root, text="Hurry up and guess.", font=("Arial", 36))
        self.message_label.pack(pady=10)

    # This is the working part of the game
    # This method is responsible for updating the word displayed specifically the letters that were correctly guessed and the underscores
    def display_word(self):
       word_state_list = []  # Creating an empty list to store the letters and underscores

       # Looping through each letter in the word
       for letter in self.secret_word:
           if letter in self.guessed_letters: # Checking if the letter in the word was guessed already
                word_state_list.append(letter) # Adding the letter to the word_state_list
           else:
               word_state_list.append("_") # If the letter wasn't guessed already then replace with an underscore in the word_state_list
       return " ".join(word_state_list) # Join the elements of the list and ensure that there's a space in between for readability

    # This method is the logic for the game
    def player_guess(self, event=None):

        guess = self.player_entry.get().lower() # The entries are input into the guess variable in lowercase
        self.player_entry.delete(0, tk.END) # Clean the previous guess_entry so it doesn't get in the way

        # This part of the logic ensures that the guess is a valid guess
        # Ensures that you already haven't guessed a certain letter
        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter man.") # Update the message_label
            return

        # Ensures that your guess is not longer than a letter and that the guess is in fact a letter
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Do you even know what a letter is?")
            return

        self.guessed_letters.add(guess) # If everything is correct, the letter is added into the "guessed" letter set

        # If the letter is actually in the word
        if guess in self.secret_word:
            self.message_label.config(text="Yippee!")
            self.word_label.config(text=self.display_word())
            right_answer.play() # Plays the audio clip
            #playsound("ding-sound-effect_1.mp3")
            # If all the letters are guessed
            if set(self.secret_word).issubset(self.guessed_letters): # Checks if the letters in the word are in the guessed set
                self.word_label.config(text=self.secret_word) # Updates the word_label to word
                self.message_label.config(text="Well done!... or maybe not?")
                #time.sleep(1)
                game_won.play()
                self.end_Game() # Ends the game

        # If the letter that was guessed wasn't in the word
        else:
            self.attempts_left -= 1 # Decrement the attempts
            self.hangcow_graphics_label.config(text=self.hangcow_graphics[self.attempts_left]) # Update the cow graphic
            self.message_label.config(text="Womp womp")
            #playsound("roblox-death-sound_1.mp3")
            wrong_answer.play()

            # If the player runs out of attempts
            if self.attempts_left == 0:
                self.word_label.config(text=self.secret_word) # Reveal the actual word
                self.message_label.config(text="Game over! A steak well done!")
                time.sleep(1) # delay the wrong_answer audio clip so it doesn't overlap with the game_lost audio clip
                game_lost.play()
                self.end_Game()

    # This method is responsible for "ending the game" or disallowing the users from entering anymore inputs.
    def end_Game(self):
        self.player_entry.config(state="disabled") # Makes it where you can't type in the entry
        self.player_entry.unbind("<Return>") # There was an issue with being able to hit enter, so I disabled the ability to hit enter

# Creates the application window, creates an instance of the HangcowGUI class, then runs the event loop.
root = tk.Tk()
HangcowGUI(root)
root.mainloop()
