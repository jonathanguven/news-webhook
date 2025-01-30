from app.news_sources.base import NewsSource

class NBC(NewsSource):

  def __init__(self, rss_url):
    super().__init__("NBC News", rss_url)

  def parse_article(self, article):
    return {
      "title": article["title"],
      "url": article["link"],
      "description": article["summary"] if "summary" in article else "No description available",
      "image_url": article["media_content"][0]["url"] if "media_content" in article else None
    }
