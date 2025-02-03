from app.news_sources.base import NewsSource

class StandardRSS(NewsSource):

  def __init__(self, name, rss_url):
    super().__init__(name, rss_url)

  def parse_article(self, article):
    return {
      "title": article["title"],
      "url": article["link"],
      "description": article["summary"] if hasattr(article, "summary") else "No description available",
      "image_url": article["media_content"][0]["url"] if "media_content" in article else None
    }
