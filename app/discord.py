import requests
import logging
import json

from app.config import WEBHOOK_URLS

def send_discord_webhook(title, url, description, image_url, source_name):
  if not WEBHOOK_URLS:
    logging.error("No Webhook URLs found")
    return

  embed = {
    "title": title,
    "url": url,
    "description": description,
    "color": 16711680,
    "image": {"url": image_url} if image_url else None,
    "footer": {"text": f"Source: {source_name}"}
  }

  payload = {"embeds": [embed]}

  headers = {"Content-Type": "application/json"}

  try:
    for webhook in WEBHOOK_URLS:
      response = requests.post(webhook, data=json.dumps(payload), headers=headers)
      if response.status_code == 204:
        logging.info(f"Sent from {source_name}: {title}")
      else:
        logging.error(f"Failed to send: {response.status_code}, {response.text}")
  except Exception as e:
    logging.error(f"Error sending webhook: {e}")
