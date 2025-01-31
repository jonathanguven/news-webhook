import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

NEWS_SOURCES = {
  "nbc": "http://feeds.nbcnews.com/feeds/topstories",
  "cbs": "https://www.cbsnews.com/latest/rss/main"
}
