import feedparser
from flask import Flask
from flask import render_template


app = Flask(__name__)
RSS_FEEDS = {'hacker_news': 'https://news.ycombinator.com/rss',
             'mozilla': 'https://blog.mozilla.org/feed/',
             'make': 'https://makezine.com/feed/'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='hacker_news'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
