import yagmail
from dotenv import load_dotenv
import typing
import os
import pandas as pd
from news import NewsFeed

load_dotenv()
MAIL_LOGIN: typing.Final = os.getenv("MAIL_LOGIN")
MAIL_PASS: typing.Final = os.getenv("MAIL_PASSWORD")

df = pd.read_excel('files/people.xlsx')

for index, row in df.iterrows():
    receiver = row['email']
    topic = row['interest']
    receiver_name = row['name']
    receiver_surname = row['surname']
    news_feed = NewsFeed(topic=topic, from_date='2023-8-9', to_date='2023-8-10')

    subject_body = f'Your {topic} news for today!'
    message_body = f"Hi, {receiver_name} {receiver_surname}\n see what's about {topic} today." \
                   f"\n{news_feed.get_news()}\nAndrew"

    email = yagmail.SMTP(user=MAIL_LOGIN, password=MAIL_PASS)
    email.send(to=receiver,
               subject=subject_body,
               contents=message_body)
