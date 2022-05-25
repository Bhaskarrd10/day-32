import datetime as dt
import smtplib
import random


my_email = "varmard10@gmail.com"
password = "3214@varma"
#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)
#
#date_of_birth = dt.datetime(year=1985, month=3, day=10)
#print(date_of_birth)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open ("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addr = my_email,
                            msg=f"Subject:monday motivation\n\n{quote}"
                            )