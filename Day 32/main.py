from calendar import weekday
import smtplib
import datetime as dt
from random import choices

#outlook.office365.com

MY_EMAIL = "email"
PASSWORD = "App password"
DESTINY = "email destination"

today = dt.datetime(2024, 6, 20)
week_day = today.weekday()

if week_day == 3:
    quotes = []
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()

    motivational_quote = choices(quotes)[0].rstrip()
    subject = "Subject: Email Title\n\n"
    msg = subject + motivational_quote
    msg = msg.encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs= DESTINY, msg= msg)


