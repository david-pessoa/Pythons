from email.mime import image
from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("data/french_words.csv")
info = df.to_dict(orient= "records")


current_dict = {}

def choose_french_word():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)

    current_dict = choice(info)
    canvas.itemconfig(card_img, image= card_front_img)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_dict["French"], fill = "black")
    flip_timer = window.after(3000, show_english_translation)


def show_english_translation():
    global current_dict
    canvas.itemconfig(card_img, image= card_back_img)
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= current_dict["English"], fill = "white")


window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, show_english_translation)


canvas = Canvas(width= 800, height = 526)
card_front_img = PhotoImage(file= "images/card_front.png")
card_back_img = PhotoImage(file= "images/card_back.png")
card_img = canvas.create_image(400, 263, image= card_front_img)

canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0, column= 0, columnspan= 2)

card_title = canvas.create_text(400, 150, text= "Title", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font= ("Arial", 60, "bold"))

cross_image = PhotoImage(file= "images/wrong.png")
unknow_button = Button(image= cross_image, highlightthickness= 0, command= choose_french_word)
unknow_button.grid(row= 1, column= 0)

check_image = PhotoImage(file= "images/right.png")
check_button = Button(image= check_image, highlightthickness= 0, command= choose_french_word)
check_button.grid(row= 1, column= 1)

choose_french_word()


window.mainloop()
