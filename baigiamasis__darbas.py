import os
import time
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

emailFrom = os.getenv('EMAIL_FROM')
emailPassword = os.getenv('EMAIL_PASSWORD')
emailTo = os.getenv('EMAIL_TO')
birthdayFile = os.getenv('BIRTHDAY_FILE')

def checkTodaysBirthdays():
    with open(birthdayFile, 'r') as file:
        today = time.strftime('%m%d')
        flag = False
        for line in file:
            if today in line:
                firstName, lastName = line.split()[1:3]
                flag = True
                sendNotificationEmail(firstName, lastName)
                displayNotificationMessage(f"Šiandien gimtadieniaujantis(-a): {firstName} {lastName}")
        if not flag:
            sendNotificationEmail("", "")
            displayNotificationMessage("Šiandien niekas negimtadieniauja!")

def sendNotificationEmail(firstName, lastName):
    if firstName and lastName:
        message = f"Šiandien gimtadieniauja: {firstName} {lastName}!"
    else:
        message = "Šiandien niekas negimtadieniauja."
    msg = MIMEText(message)
    msg['From'] = emailFrom
    msg['To'] = emailTo
    msg['Subject'] = 'Gimtadienio pranešimas'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailFrom, emailPassword)
    server.sendmail(emailFrom, emailTo, msg.as_string())
    server.quit()

def displayNotificationMessage(message):
    root = tk.Tk()
    root.title("Gimtadienio pranešimas")
    label = tk.Label(root, text=message, font=('Arial', 16))
    label.pack(padx=20, pady=20)
    root.mainloop()

if __name__ == '__main__':
    load_dotenv()
    checkTodaysBirthdays()

# kadangi ikelem dotenv biblioteka galime naudoti "os getenv" funkcija kad pasiektume jautrius duomenys kurie yra ,saugomi env file

emailFrom = os.getenv('EMAIL_FROM')
emailPassword = os.getenv('EMAIL_PASSWORD')
emailTo = os.getenv('EMAIL_TO')
birthdayFile = os.getenv('BIRTHDAY_FILE')
