import smtplib
import datetime as dt
from random import *
now = dt.datetime.now()
current_day = now.weekday()

if current_day == 1:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        random_quote = choice(quotes_list)
    my_email = "abc@gmail.com"
    pwd = "abcdefghijkl"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
                from_addr=my_email,
                to_addrs="xyz@yahoo.com",
                msg=f"Subject:Monday Motivation\n\n{random_quote}")
