import pandas as pd
import datetime
import smtplib
import os
 

#authentication details
GMAIL_ID = 'birthdaywish02@gmail.com'
GMAIL_PSWD = 'Kuchbhi@32'


def sendEmail(to, sub, msg): 
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")

    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue']) 
            

     