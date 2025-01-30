import feedparser
import logging
from abc import ABC, abstractmethod

# Base class for all news sources
class NewsSource(ABC):

  def __init__(self, name, rss_url):
    self.name = name
    self.rss_url = rss_url
    self.last_article_id = None

  # Parses a single article
  @abstractmethod
  def parse_article(self, article):
    pass

  # Fetches latest news articles from source and detects new articles
  def fetch_news(self):
    logging.info(f"Fetching news from {self.name}")

    feed = feedparser.parse(self.rss_url)
    if not feed.entries:
      logging.info("No new articles found 1")
      return

    latest_article = feed.entries[0]
    article_id = latest_article.get("id", latest_article.get("link"))

    if not article_id:
      logging.info("No article id found")
      return None

    if self.last_article_id is None:
      self.last_article_id = article_id
      logging.info(f"Initializing last article id to {article_id}")
      return None

    if article_id != self.last_article_id:
      self.last_article_id = article_id
      logging.info(f"New article detected from {self.name}: {latest_article.title}")
      return self.parse_article(latest_article)

    logging.info(f"No new articles found for {self.name} (last ID: {self.last_article_id})")
    return None
