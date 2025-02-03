from app.news_sources.base import NewsSource

class Forbes(NewsSource):

  def __init__(self, rss_url):
    super().__init__("Forbes", rss_url)

  def parse_article(self, article):
    return {
      "title": article["title"],
      "url": article["link"],
      "description": article["summary"] if hasattr(article, "summary") else "No description available",
      "image_url": self.get_image_url(article),
    }

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
