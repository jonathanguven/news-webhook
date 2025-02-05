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
  async def fetch_news(self, session):
    logging.info(f"Fetching news from {self.name}")
    try:
      async with session.get(self.rss_url) as response:
        response_text = await response.text()

      feed = feedparser.parse(response_text)
      if not feed.entries:
        logging.info(f"No new articles found for {self.name}")
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
        # return self.parse_article(latest_article)

      if article_id != self.last_article_id:
        self.last_article_id = article_id
        logging.info(f"New article detected from {self.name}: {latest_article.title}")
        return self.parse_article(latest_article)

      logging.info(f"No new articles found for {self.name} (last ID: {self.last_article_id})")
      return None

    except Exception as e:
      logging.error(f"Error fetching news from {self.name}: {e}")
      return None
