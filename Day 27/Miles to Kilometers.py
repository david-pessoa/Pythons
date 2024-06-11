from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx= 20, pady= 20)
window.minsize(200, 200)

input = Entry()
input.insert(END, string = "0")
input.config(width= 10)
input.grid(column=1, row = 0)

mile_text = Label(text= "Miles")
mile_text.grid(column=2, row=0)
km_text = Label(text= "Km")
km_text.grid(column=2, row=1)
is_esqual_text = Label(text= "is equal to")
is_esqual_text.grid(column=0, row=1)
km_label = Label(text= "0")
km_label.grid(column=1, row=1)
def click_button():
    kilometers = float(input.get()) * 1.609
    km_label["text"] = str(kilometers)

button = Button(text= "Calculate", command= click_button)
button.grid(column= 1, row = 2)

window.mainloop()