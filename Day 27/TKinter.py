import tkinter as tk
# Create a window

window = tk.Tk()
window.title("My first window!")
window.minsize(500,500)
window.config(padx = 100, pady = 100)

# Create a label

label = tk.Label(text= "Label", font= ("Arial", 24, "bold"))
# label.pack(side = "top") # Printa a label na tela
label.grid(column= 0, row= 0)
# Create a button

def button_clicked():
    label.config(text = input.get())
button = tk.Button(text = "Button", command = button_clicked)
button.grid(column= 1, row= 1)

new_button = tk.Button(text = "New button", command = button_clicked)
new_button.grid(column= 2, row= 0)


# Create an Input

input = tk.Entry(width = 10)
input.grid(column= 3, row= 2)
# input.get() # Returns the input text


window.mainloop()