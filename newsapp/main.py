from flask import *
import requests
from googletrans import Translator
import timeago, datetime
import random
import os


translator = Translator()

API_KEY = os.environ.get('API_KEY')

endpoint = 'https://newsapi.org/v2/top-headlines'
app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(
        url=endpoint,
        params={
        "apikey": API_KEY,
        "country": 'ng',
        "language": 'en',
        'pageSize': 100
    })
    articles = response.json()['articles']
    if articles:
        for article in articles:
            date = datetime.datetime.now()
            print(date)
            article['timeago'] = timeago.format(date, article['publishedAt'].split('T')[0])
            article['views'] = random.randint(0, 1000)
            if article['content'] is not None and article['description'] is not None:
                try:
                    article['content'] = translator.translate(article['content'], dest='ha').text
                    article['description'] = translator.translate(article['description'], dest='ha').text
                except TypeError:
                    pass
            else:
                article['content'] = translator.translate("Empty", dest='ha').text
                article['description'] = translator.translate("Empty", dest='ha').text
    return render_template('index.html', articles=articles)



if __name__ == '__main__':
    app.run(debug=True)