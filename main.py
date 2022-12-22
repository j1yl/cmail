import pandas as pd
import yagmail
import random
import time

user_email = "YOUREMAILHERE"
app_pass = "APP_PASSWORD"
SUBJECT_HERE = "YOUREMAILSUBJECTHERE"
ATTACHMENT_NAME = "resume.txt"
# EDIT EMAIL MESSAGE ON LINE 34


def read_csv(filename: str):
    df = pd.read_csv(filename)
    return df


def process_csv(df: object):
    emails = df["EMAIL"].array
    last_names = df["LNAME"].array
    first_names = df["FNAME"].array
    companies = df["COMPANY"].array

    i = 0
    while i < len(emails):
        send_email(emails[i], first_names[i], last_names[i], companies[i])
        i = i + 1


def send_email(email: str, first_name: str, last_name: str, company: str):
    time.sleep(random.randint(1, 5))
    subject = SUBJECT_HERE
    content = [f"""
    Dear {first_name} {last_name} from {company},
    """, ATTACHMENT_NAME]

    with yagmail.SMTP(user_email, app_pass) as yag:
        yag.send(email, subject, content)

    print(f"Email sent to {email}, {first_name} {last_name} from {company}")


def main():
    data = read_csv("data.csv")
    process_csv(data)


main()
