import requests
from dotenv import load_dotenv
import os
import typing


class NewsFeed:
    """This class represents news that are for sending on e-mail"""

    load_dotenv()
    API_KEY: typing.Final = os.getenv("API_KEY")
    base_url = 'https://newsapi.org/v2/everything'

    def __init__(self, topic, from_date, to_date, language='en'):
        self.topic = topic
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get_news(self):
        """converts json from request into formatted string for sending email"""
        params = {'qInTitle': self.topic,
                  'from': self.from_date,
                  'to': self.to_date,
                  'language': self.language,
                  'apiKey': self.API_KEY}
        response = requests.get(self.base_url, params=params)
        content = response.json()
        articles = content['articles']
        email_body = ''
        for article in articles:
            email_body = email_body + f"{article['title']}\n{article['url']}\n\n"
        return email_body

# test
# news_feed = NewsFeed(topic='Nasa', from_date='2023-08-07', to_date='2023-08-08', language='en')
# print(news_feed.get_news())

