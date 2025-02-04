from bs4 import BeautifulSoup
import html
from app.news_sources.base import NewsSource

class StandardRSS(NewsSource):

  def __init__(self, name, rss_url):
    super().__init__(name, rss_url)

  def parse_article(self, article):
    clean_description = self.clean_html(article.get("summary") or article.get("description") or "No description available")
    return {
      "title": article["title"],
      "url": article["link"],
      "description": clean_description,
      "image_url": self.get_image_url(article),
    }

  def clean_html(self, text):
    soup = BeautifulSoup(text, "html.parser")
    return html.unescape(soup.get_text())

  def get_image_url(self, article):

    if "media_content" in article:
      for media in article["media_content"]:
        if "type" in media and media["type"].startswith("image"):
          return media["url"]

    if "media_thumbnail" in article:
      return article["media_thumbnail"][0]["url"]

    if "media_content" in article:
      for media in article["media_content"]:
        if "type" in media and media["type"].startswith("video"):
          if "thumbnail" in media:
            return media["thumbnail"]
          elif "url" in media:
            return media["url"]

    return None
