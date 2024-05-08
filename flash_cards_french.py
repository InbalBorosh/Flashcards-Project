import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
   data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
   data = pd.read_csv("data/french_words.csv.csv")
   data_new_format = data.to_dict(orient="records")
else:
   data_new_format = data.to_dict(orient="records")

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_new_format)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(front_card, image=card_front_img)
    timer = window.after(3000, flipping_card)

def flipping_card():
    canvas.itemconfig(front_card, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def v_button():
    global current_card
    data_new_format.remove(current_card)
    df = pd.DataFrame(data_new_format)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flipping_card)
canvas = Canvas(height=400, width=400)
card_front_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
front_card = canvas.create_image(100, 100, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(180, 80, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(180, 220, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# V and X buttons
the_x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=the_x_image,highlightthickness=0, height=100, width=100, command=next_card)
x_button.grid(row=1, column=0)
the_v_image = PhotoImage(file="images/right.png")
v_button = Button(image=the_v_image, highlightthickness=0, height=100, width=100, command=v_button)
v_button.grid(row=1, column=1)

fr_word = next_card()
window.mainloop()