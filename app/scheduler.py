import logging
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import NEWS_SOURCES, DISCORD_WEBHOOK_URL
from app.discord import send_discord_webhook

from app.news_sources.abc import ABC
from app.news_sources.nbc import NBC
from app.news_sources.nypost import NYPost
from app.news_sources.standard_rss import StandardRSS

logging.basicConfig(level=logging.INFO)
scheduler = BackgroundScheduler()

news_sources = [
  # NBC(NEWS_SOURCES["nbc"]),
  # StandardRSS("CBS News", NEWS_SOURCES["cbs"]),
  # NYPost(NEWS_SOURCES["nypost"]),
  # ABC(NEWS_SOURCES["abc"]),
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
