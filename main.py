import smtplib
import datetime as dt
import random


my_email = "richardronith@gmail.com"
password = "pkajnfssisqcaydi"

#testing
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="richardronith@yahoo.com",
                            msg=f"subject:Quotes for Motivation\n\n{quote}")

#this sends mail using my mail.


