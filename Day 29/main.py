from tkinter import *
from tkinter import messagebox
from random import randint, choice
import json
import tkinter

import json.scanner
# ---------------------------- UPDATE PASSWORDS ------------------------------- #
def update_all():
    new_data = {
        "": {
            "email": "",
            "password": ""  
        }
    }
    info = {}
    try:
        with open("Passwords.json", "r") as file:
            info = json.load(file)

    except FileNotFoundError:
            open("Passwords.json", "w")

    except json.decoder.JSONDecodeError:
        with open("Passwords.json", "w") as filew:
                json.dump(new_data, filew, indent= 4)

    with open("Passwords.json", "w") as new_file:
        info.update(info)
        json.dump(info, new_file, indent= 4)

# ---------------------------- DELETE ALL PASSWORDS ------------------------------- #
def delete_all():
    file = open("Passwords.json", "w")
    file.close()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    password = ''
    for _ in range(14):
        up_char = chr(randint(65, 90))
        low_char = chr(randint(97, 122))
        symbol = choice(["!", '@', "#", '$', '%', '&', '*'])
        chosen = randint(1, 3)
        if chosen == 1:
            password += up_char
        elif chosen == 2:
            password += low_char
        else:
            password += symbol
    entry_password.insert(END, password)  

# ---------------------------- FIND PASSWORD ------------------------------- #
def show_custom_message(title, message):
    # Create a new Toplevel window
    dialog = tkinter.Toplevel()
    dialog.title(title)
    
    # Add the message
    message_label = tkinter.Label(dialog, text=message)
    message_label.pack(pady=10, padx=10)
    
    # Add an OK button to close the dialog
    ok_button = tkinter.Button(dialog, text="OK", command=dialog.destroy)
    ok_button.pack(pady=10)

def find_password():
    website = entry_web.get()
    if website == "":
        warning.config(text = "Please, type the website's name")

    else:
        warning.config(text = "")
        try:
            with open("Passwords.json", "r") as file:
                data = json.load(file)
                email = data[website]["email"]
                password = data[website]["password"]
                show_custom_message(title = website, message =f"Email: {email}\nPassword: {password}")
        
        except FileNotFoundError:
            messagebox.showerror("", "No data file was found")
        
        except KeyError:
           messagebox.showwarning("", "No details for this website exists")

        except json.decoder.JSONDecodeError:
            messagebox.showerror("", "No data file was found")
        



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = entry_email.get()
    password = entry_password.get()
    website = entry_web.get()
    new_data = {
        website: {
            "email": email,
            "password": password  
        }
    }
    if email == "" or password == "" or website == "":
        warning.config(text = "Please, type your email, password and website")
    else:
        warning.config(text = "")
        data = {}
        try:
            with open("Passwords.json", "r") as file:
                data = json.load(file)
    
        except FileNotFoundError:
            open("Passwords.json", "w")
        
        except json.decoder.JSONDecodeError:
            with open("Passwords.json", "w") as filew:
                json.dump(new_data, filew, indent= 4)


        with open("Passwords.json", "w") as filew:
            data.update(new_data)
            json.dump(data, filew, indent= 4)


        entry_web.delete(0, END)
        entry_password.delete(0, END)

        messagebox.showinfo("Password added succesfully!", "Password added succesfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk() # Criação da janela
window.title("Password Manager") # Configuração do título da janela
window.config(padx = 20, pady = 20) # Define espaçamento de 20px das bordas

lock_image = PhotoImage(file= "logo.png") # Carrega a imagem do cadeado
canvas = Canvas(width= 200, height= 200) # Cria um canvas de 200px X 200px
canvas.create_image(100, 100, image = lock_image) # Coloca a imagem no canvas na posição (100, 100)
canvas.grid(row = 0, column = 1) # Posiciona o canvas na "grade"

label_web = Label(text= "Website:", font = ("Arial", 12))
label_web.grid(row = 1, column = 0)
label_email = Label(text= "Email/Username:", font = ("Arial", 12))
label_email.grid(row = 2, column = 0)
label_password = Label(text= "Password:", font = ("Arial", 12))
label_password.grid(row = 3, column = 0)

entry_web = Entry(width = 25)
entry_web.grid(row = 1, column = 1)
entry_web.focus()
entry_email = Entry(width = 40)
#entry_email.insert(END, "example@gmail.com")
entry_email.grid(row = 2, column = 1, columnspan = 2)
entry_password = Entry(width = 40)
entry_password.grid(row = 3, column = 1, columnspan= 2)

gen_password_button = Button(text= "Search", command = find_password, width= 10) 
gen_password_button.grid(row = 1, column = 2)

delete_button = Button(text= "Delete All Passwords",  command = delete_all) 
delete_button.grid(row = 4, column = 0)

add_button = Button(text= "Add Password", width = 10,  command = save_password) 
add_button.grid(row = 4, column = 1)

gen_password_button = Button(text= "Generate password",  command = create_password) 
gen_password_button.grid(row = 4, column = 2)

warning = Label(font = ("Arial", 12, "bold"), foreground= "#fc4103")
warning.grid(row = 5, column = 0, columnspan= 3)

window.mainloop()