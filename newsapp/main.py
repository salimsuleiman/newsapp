from flask import *
import requests
from googletrans import Translator


translator = Translator()

API_KEY ='c630ff8e6d8543d9bcd43e080ad78b81'
'8468d3e24f614f959062cd9645b04e9d'
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
    for article in articles:
        if article['content'] != None:
            article['content'] = translator.translate(article['content'], dest='ha').text
            article['description'] = translator.translate(article['description'], dest='ha').text

    return render_template('index.html', articles=articles)



if __name__ == '__main__':
    app.run(debug=True)