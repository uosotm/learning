import feedparser
import json
import os
import urllib

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

RSS_FEEDS = {'hacker_news': 'https://news.ycombinator.com/rss',
             'mozilla': 'https://blog.mozilla.org/feed/',
             'make': 'https://makezine.com/feed/'}
DEFAULTS = {'publication': 'hacker_news',
            'city': 'London,UK',
            'currency_from':'GBP',
            'currency_to':'USD'}
WEATHER_API = os.environ['OWM_API_KEY']
CURRENCY_API = os.environ['OER_API_KEY']
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
CURRENCY_URL = "https://openexchangerates.org//api/latest.json?app_id={}"


@app.route('/')
def home():
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)

    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)

    currency_from = request.args.get('currency_from')
    if not currency_from:
        currency_from = DEFAULTS['currency_from']
    currency_to = request.args.get('currency_to')
    if not currency_to:
        currency_to = DEFAULTS['currency_to']
    rate = get_rate(currency_from, currency_to)
    
    return render_template('home.html',
                           articles=articles,
                           weather=weather,
                           currency_from=currency_from,
                           currency_to=currency_to,
                           rate=rate)

def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']

def get_weather(query):
    query = urllib.parse.quote(query)
    url = WEATHER_URL.format(query, WEATHER_API)
    data = urllib.request.urlopen(url).read()
    parsed = json.loads(data.decode('utf-8'))
    weather = None
    if parsed.get("weather"):
        weather = {"description": parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   'country': parsed['sys']['country']}
    return weather

def get_rate(frm, to):
    url = CURRENCY_URL.format(CURRENCY_API)
    all_currency = urllib.request.urlopen(url).read()

    parsed = json.loads(all_currency.decode('utf-8')).get('rates')
    frm_rate = parsed.get(frm.upper())
    to_rate = parsed.get(to.upper())
    return to_rate/frm_rate


if __name__ == '__main__':
    app.run(port=5000, debug=True)
