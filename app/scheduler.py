import logging
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import NEWS_SOURCES, DISCORD_WEBHOOK_URL
from app.discord import send_discord_webhook

from app.news_sources.standard_rss import StandardRSS

logging.basicConfig(level=logging.INFO)
scheduler = BackgroundScheduler()

news_sources = [
  StandardRSS("NBC News", NEWS_SOURCES["nbc"]),
  StandardRSS("CBS News", NEWS_SOURCES["cbs"]),  # no image
  StandardRSS("NY Post", NEWS_SOURCES["nypost"]),
  StandardRSS("ABC News", NEWS_SOURCES["abc"]),
  StandardRSS("Forbes", NEWS_SOURCES["forbes"]),
  StandardRSS("Bloomberg Tech", NEWS_SOURCES["bloomberg-tech"]),
  StandardRSS("Bloomberg Markets", NEWS_SOURCES["bloomberg-markets"]),
  StandardRSS("Bloomberg Politics", NEWS_SOURCES["bloomberg-politics"]),
  StandardRSS("Bloomberg Wealth", NEWS_SOURCES["bloomberg-wealth"]),
  StandardRSS("Apple", NEWS_SOURCES["apple"]),
  StandardRSS("Google News", NEWS_SOURCES["google-news"]),  # no working RSS
  StandardRSS("CNN", NEWS_SOURCES["cnn"]),
  StandardRSS("CNBC", NEWS_SOURCES["cnbc"]),  # no image
  StandardRSS("Washington Post", NEWS_SOURCES["washington-post"]),  # no image
  StandardRSS("Fox News", NEWS_SOURCES["fox"]),
  StandardRSS("Time", NEWS_SOURCES["time"]),  # no image
  StandardRSS("USA Today", NEWS_SOURCES["usa-today"]),  # no working RSS
  StandardRSS("Huffpost", NEWS_SOURCES["huffpost"]), # no image
  StandardRSS("Economist", NEWS_SOURCES["economist"]),  # no image
  StandardRSS("Independent", NEWS_SOURCES["independent"]),
  StandardRSS("Buzzfeed", NEWS_SOURCES["buzzfeed"]),
  StandardRSS("The Atlantic", NEWS_SOURCES["the-atlantic"]),  # no image
  StandardRSS("National Geographic", NEWS_SOURCES["national-geographic"]),  # no working RSS
]

# Sends a message to Discord channel via webhook
def send_message():
  if not DISCORD_WEBHOOK_URL:
    logging.error("Discord webhook URL not set")
    return

  payload = {
    "content": "Hello, World!",
  }

  try:
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    if response.status_code == 204:
      logging.info("Message sent to Discord")
    else:
      logging.error("Failed to send message to Discord")
  except Exception as e:
    logging.error(f"Error sending message to Discord: {e}")

# poll from all news sources
def poll_news():
  for source in news_sources:
    article = source.fetch_news()
    if article:
      send_discord_webhook(
        title=article["title"],
        url=article["url"],
        description=article["description"],
        image_url=article["image_url"],
        source_name=source.name
      )

# Schedule the poll_news function to run every minute
scheduler.add_job(poll_news, 'interval', minutes=1)
scheduler.start()
