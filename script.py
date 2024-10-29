import feedparser
from datetime import datetime, timedelta
from time import mktime

news_feed = feedparser.parse("https://news.google.com/rss/search?q=consejo-insular-de-aguas-de-gran-canaria&hl=es&gl=ES&ceid=ES:es")

fecha_desde = datetime.today() - timedelta(days=14)

for entry in news_feed.entries:
    fecha_publicacion = datetime.fromtimestamp(mktime(entry.published_parsed))
    if fecha_publicacion > fecha_desde:
        print(" - " + entry.title)

