import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

NEWS_SOURCES = {
  "nbc": "https://www.nbcnews.com/rss"
}
