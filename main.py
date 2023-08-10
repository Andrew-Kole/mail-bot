import yagmail
from dotenv import load_dotenv
import typing
import os
import pandas as pd
from news import NewsFeed
import datetime
import time


load_dotenv()
MAIL_LOGIN: typing.Final = os.getenv("MAIL_LOGIN")
MAIL_PASS: typing.Final = os.getenv("MAIL_PASSWORD")

df = pd.read_excel('files/people.xlsx')


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    receiver = row['email']
    topic = row['interest']
    receiver_name = row['name']
    receiver_surname = row['surname']
    news_feed = NewsFeed(topic=topic, from_date=yesterday, to_date=today)
    subject_body = f'Your {topic} news for today!'
    message_body = f"Hi, {receiver_name} {receiver_surname}\n " \
                   f"See what's about {topic} today." \
                   f"\n{news_feed.build_mail_body()}\nAndrew"
    email = yagmail.SMTP(user=MAIL_LOGIN, password=MAIL_PASS)
    email.send(to=receiver,
               subject=subject_body,
               contents=message_body)


while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 35:
        for index, row in df.iterrows():
            send_email()
    time.sleep(60)