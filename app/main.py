from fastapi import FastAPI
from app.scheduler import scheduler

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "News Webhook Scraper is running!"}

@app.get("/trigger")
def trigger_job():
  # Manually trigger a message to Discord
  from app.scheduler import send_message
  send_message()
  return {"message": "Job triggered"}

# Run scheduler when the application starts
@app.on_event("startup")
def start_scheduler():
  if not scheduler.running:
    scheduler.start()
