import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv

from config import REQUIRED_KEYS
from utils.scraper_utils import (
    fetch_and_process_page,
    get_browser_config,
    get_llm_strategy,
)

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Define request model
class CrawlRequest(BaseModel):
    url: str  # URL parameter passed in the POST request

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/crawl-reels/")
async def crawl_reels(request: CrawlRequest):
    """
    API Endpoint to crawl reels based on a given URL.
    """
    browser_config = get_browser_config()
    llm_strategy = get_llm_strategy()
    session_id = "reel_crawl_session"
    all_reels = []

    try:
        async with AsyncWebCrawler(config=browser_config) as crawler:
            reels, no_results_found = await fetch_and_process_page(
                crawler,
                request.url,  # Use URL from the request body
                llm_strategy,
                session_id,
            )

            if no_results_found:
                return {"message": "No reels found."}

            all_reels.extend(reels)

            # Pause to avoid rate limits
            await asyncio.sleep(2)

        return {"reels": all_reels}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with `uvicorn main:app --reload`
