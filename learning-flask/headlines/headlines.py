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
    first_article = feed['entries'][0]
    return render_template("home.html",
                            title=first_article.get("title"),
                            published=first_article.get("published"),
                            summary=first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
