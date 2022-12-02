from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "English"
PRACTICE_LANGUAGE = "French"
TIME_BETWEEN_FLIP = 3000

# Load user file of remaining words to learn. if it does not exist
# Load the file containing the complete list of words
try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
finally:
    words_to_learn = words.to_dict(orient="records")

current_word = {}


# Select a random word for user to guess and present it on the flashcard
# Update flashcard background and font
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(card_language, text=PRACTICE_LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_word[PRACTICE_LANGUAGE], fill="black")
    canvas.itemconfig(card_background, image=flash_card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# Updates background and font color for the flashcard and reveals answer
def flip_card():
    canvas.itemconfig(card_language, text=LANGUAGE, fill="white")
    canvas.itemconfig(card_word, text=current_word[LANGUAGE], fill="white")
    canvas.itemconfig(card_background, image=flash_card_back_img)


# When user knows a word remove it from the list of words to learn
# Updates words_to_learn.csv for next session
def is_known():
    words_to_learn.remove(current_word)
    save_words = pandas.DataFrame(words_to_learn)
    save_words.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------------Generate Display--------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIME_BETWEEN_FLIP, func=flip_card)

# Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                highlightthickness=0)
flash_card_front_img = PhotoImage(file="images/card_front.png")
flash_card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flash_card_front_img)
card_language = canvas.create_text(400, 150, text="", font=("Ariel", 40,
                                                            "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60,
                                                        "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
checkmark_image = PhotoImage(file="images/right.png")
correct_button = Button(image=checkmark_image, highlightthickness=0,
                        command=is_known)
correct_button.grid(row=1, column=0)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0,
                      command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
