import logging
import time
import asyncio
import aiohttp
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import NEWS_SOURCES
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
  # StandardRSS("Google News", NEWS_SOURCES["google-news"]),  # no working RSS
  StandardRSS("CNN", NEWS_SOURCES["cnn"]),
  StandardRSS("CNBC", NEWS_SOURCES["cnbc"]),  # no image
  StandardRSS("Washington Post", NEWS_SOURCES["washington-post"]),  # no image
  StandardRSS("Fox News", NEWS_SOURCES["fox"]),
  StandardRSS("Time", NEWS_SOURCES["time"]),  # no image
  # StandardRSS("USA Today", NEWS_SOURCES["usa-today"]),  # no working RSS
  StandardRSS("Huffpost", NEWS_SOURCES["huffpost"]), # no image
  StandardRSS("Economist", NEWS_SOURCES["economist"]),  # no image
  StandardRSS("Independent", NEWS_SOURCES["independent"]),
  StandardRSS("Buzzfeed", NEWS_SOURCES["buzzfeed"]),
  StandardRSS("The Atlantic", NEWS_SOURCES["the-atlantic"]),  # no image
  # StandardRSS("National Geographic", NEWS_SOURCES["national-geographic"]),  # no working RSS
]

# fetch an individual news source
async def fetch_news_source(session, source):
  try:
    article = await source.fetch_news(session)
    if article:
      send_discord_webhook(
        title=article["title"],
        url=article["url"],
        description=article["description"],
        image_url=article["image_url"],
        source_name=source.name
      )
  except Exception as e:
    logging.error(f"Error fetching news from {source.name}: {e}")

# poll from all news sources
async def poll_news():
  start = time.time()
  async with aiohttp.ClientSession() as session:
    tasks = [fetch_news_source(session, source) for source in news_sources]
    await asyncio.gather(*tasks)
  end = time.time()
  print(f"Fetching took {end - start:.2f} seconds")

def schedule_async_poll():
  asyncio.run(poll_news())

# Schedule the poll_news function to run every minute
scheduler.add_job(schedule_async_poll, 'interval', minutes=1)
scheduler.start()
