import pandas as pd
import smtplib
from random import randint
import datetime as dt

MY_EMAIL = "My email"
PASSWORD = "App password"
DESTINY = "email_destination"
today = dt.datetime.now()

df = pd.read_csv("birthdays.csv")
contacts = df.to_dict(orient= 'records')
chosen_letter = f"./letter_templates/letter_{randint(1, 3)}.txt"

for row in contacts:
    letter = ""
    if today.month == row["month"] and today.day == row["day"]:
        with open(chosen_letter, 'r') as file:
            letter = file.readlines()
            letter = "\n".join(letter)
            letter = letter.replace("[NAME]", row["name"])
        
        with smtplib.SMTP(host= "smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= PASSWORD)
            connection.sendmail(from_addr= MY_EMAIL, to_addrs= DESTINY, msg= f"Subject:Happy Birthday, {row['name']}\n\n{letter}")





