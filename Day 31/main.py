from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

info = df.to_dict(orient= "records")
to_learn = []
current_dict = {}

def config_card_front(word):
    canvas.itemconfig(card_img, image= card_front_img)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= word, fill = "black")

def choose_french_word_right():
    global current_dict, flip_timer
    try:
        current_dict = choice(info)
    except IndexError:
        return
    window.after_cancel(flip_timer)
    to_learn.append(current_dict)
    info.remove(current_dict)

    try:
        current_dict = choice(info)
        config_card_front(current_dict["French"])
        flip_timer = window.after(3000, show_english_translation)
    except IndexError:
        config_card_front("No more cards")

def choose_french_word_wrong():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_dict = choice(info)
        config_card_front(current_dict["French"])
        flip_timer = window.after(3000, show_english_translation)
    except IndexError:
        config_card_front("No more cards")


def show_english_translation():
    global current_dict
    for dictionary in to_learn:
        if(dictionary["English"] == current_dict["English"]):
            to_learn.remove(dictionary)
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
unknow_button = Button(image= cross_image, highlightthickness= 0, command= choose_french_word_wrong)
unknow_button.grid(row= 1, column= 0)

check_image = PhotoImage(file= "images/right.png")
check_button = Button(image= check_image, highlightthickness= 0, command= choose_french_word_right)
check_button.grid(row= 1, column= 1)

choose_french_word_wrong()

window.mainloop()

newdf = pd.DataFrame(to_learn)

newdf.to_csv("data/words_to_learn.csv", index= False)

