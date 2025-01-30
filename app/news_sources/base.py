import feedparser
import logging
from abc import ABC, abstractmethod

# Base class for all news sources
class NewsSource(ABC):

  def __init__(self, url, rss_url):
    self.url = url
    self.rss_url = rss_url
    self.last_article_id = None

  # Parses a single article
  @abstractmethod
  def parse_article(self, article):
    pass

  # Fetches latest news articles from source and detects new articles
  def fetch_news(self):
    logging.info(f"Fetching news from {self.url}")

    feed = feedparser.parse(self.rss_url)
    if not feed.entries:
      logging.info("No new articles found")
      return

    latest_article = feed.entries[0]
    article_id = latest_article.id

    if self.last_article_id is None:
      self.last_article_id = article_id
      return

    if article_id != self.last_article_id:
      self.last_article_id = article_id
      return self.parse_article(latest_article)

    return None
