import yagmail
from dotenv import load_dotenv
import typing
import os
import pandas as pd
from news import NewsFeed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 27

        load_dotenv()
        MAIL_LOGIN: typing.Final = os.getenv("MAIL_LOGIN")
        MAIL_PASS: typing.Final = os.getenv("MAIL_PASSWORD")

        df = pd.read_excel('files/people.xlsx')

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        for index, row in df.iterrows():
            receiver = row['email']
            topic = row['interest']
            receiver_name = row['name']
            receiver_surname = row['surname']
            news_feed = NewsFeed(topic=topic, from_date=yesterday, to_date=today)

            subject_body = f'Your {topic} news for today!'
            message_body = f"Hi, {receiver_name} {receiver_surname}\n see what's about {topic} today." \
                           f"\n{news_feed.get_news()}\nAndrew"

            email = yagmail.SMTP(user=MAIL_LOGIN, password=MAIL_PASS)
            email.send(to=receiver,
                       subject=subject_body,
                       contents=message_body)
    time.sleep(60)