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
# WEATHER_URL = ("http://api.openweathermap.org/data/2.5/weather?q={}\
#                &units=metric&APPID=%s" % os.environ['OWM_API_KEY'])
DEFAULTS = {'publication': 'hacker_news',
            'city': 'London,UK'}


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
    
    return render_template('home.html',
                           articles=articles,
                           weather=weather)

def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication = DEFAULTS["publication"]
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']

def get_weather(query):
    api_key = os.environ['OWM_API_KEY']
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

    query = urllib.parse.quote(query)
    url = api_url.format(query, api_key)
    data = urllib.request.urlopen(url).read()
    parsed = json.loads(data.decode('utf-8'))
    weather = None
    if parsed.get("weather"):
        weather = {"description": parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"],
                   'country': parsed['sys']['country']}
    return weather


if __name__ == '__main__':
    app.run(port=5000, debug=True)
