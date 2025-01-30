import requests
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import DISCORD_WEBHOOK_URL

logging.basicConfig(
  level=logging.INFO,
)
scheduler = BackgroundScheduler()

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

# Schedule the send_message function to run every minute
scheduler.add_job(send_message, 'interval', minutes=1)
scheduler.start()
