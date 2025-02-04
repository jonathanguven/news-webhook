from fastapi import FastAPI, BackgroundTasks
from app.scheduler import scheduler, poll_news

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "News Webhook Scraper is running!"}

@app.get("/trigger")
def trigger_job(background_tasks: BackgroundTasks):
  # Manually trigger a news fetch
  background_tasks.add_task(poll_news)
  return {"message": "Job triggered"}

# Run scheduler when the application starts
@app.on_event("startup")
def start_scheduler():
  if not scheduler.running:
    scheduler.start()
