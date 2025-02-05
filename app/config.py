import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URLS = [
  # "https://discord.com/api/webhooks/1336095023623831602/GwFASaUYNiEQa1T289ilhyItTimhF9wDohoCcb5tBchHsc-9R-T6puOEgB7xmaA7Yep_",
  "https://discord.com/api/webhooks/1336499018750103562/HK3idGyNQOo0wX_NDWjstBmcBsGM2cIwZofKDqeR-RSw80bJ9uQEtSGHmOEJB6yy54rC"
]

NEWS_SOURCES = {
  "nbc": "http://feeds.nbcnews.com/feeds/topstories",
  "cbs": "https://www.cbsnews.com/latest/rss/main",
  "abc": "http://abcnews.go.com/abcnews/topstories",
  "nypost": "https://nypost.com/feed/",
  "forbes": "https://www.forbes.com/real-time/feed2/",
  "bloomberg-tech": "https://feeds.bloomberg.com/technology/news.rss",
  "bloomberg-markets": "https://feeds.bloomberg.com/markets/news.rss",
  "bloomberg-politics": "https://feeds.bloomberg.com/politics/news.rss",
  "bloomberg-wealth": "https://feeds.bloomberg.com/wealth/news.rss",
  "apple": "https://www.apple.com/newsroom/rss-feed.rss",
  "google-news": "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en",
  "cnn": "http://rss.cnn.com/rss/cnn_topstories.rss",
  "cnbc": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
  "washington-post": "http://feeds.washingtonpost.com/rss/business",
  "fox": "https://moxie.foxnews.com/google-publisher/latest.xml",
  "time": "http://time.com/feed/",
  "usa-today": "http://rssfeeds.usatoday.com/usatoday-NewsTopStories",
  "huffpost": "https://chaski.huffpost.com/us/auto/vertical/us-news",
  "economist": "http://www.economist.com/sections/economics/rss.xml",
  "independent": "http://www.independent.co.uk/rss",
  "buzzfeed": "https://www.buzzfeed.com/politics.xml",
  "the-atlantic": "https://www.theatlantic.com/feed/all/",
  "national-geographic": "http://news.nationalgeographic.com/rss/index.rss"
}
