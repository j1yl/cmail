import pandas as pd


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
      # do something
      # send_email(emails[i], first_names[i], last_names[i], companies[i])
        print(f"{first_names[i]} {last_names[i]}, {emails[i]}, {companies[i]}")
        i = i + 1


def send_email():
    return


def main():
    return
