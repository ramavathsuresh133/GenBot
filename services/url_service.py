"""
url_service.py - URL scraping service with retry & timeout handling
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from core.logger import logger

DEFAULT_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

def _create_session() -> requests.Session:
    """Create a requests Session with automatic retry on transient errors."""
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=1,            # waits 1s, 2s, 4s between retries
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def scrape_url(url: str) -> str:
    """Scrape visible text from a given URL with retry support."""
    try:
        session = _create_session()
        headers = {"User-Agent": "Mozilla/5.0"}
        response = session.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Clean non-visible tags
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        cleaned_text = text.strip()
        logger.info(f"Successfully scraped {len(cleaned_text)} characters from {url}")
        return cleaned_text

    except requests.exceptions.Timeout:
        logger.error(f"URL scraping timed out after {DEFAULT_TIMEOUT}s: {url}")
        raise RuntimeError(
            f"The website took too long to respond (timed out after {DEFAULT_TIMEOUT}s). "
            "Please check the URL or try again later."
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error while scraping {url}: {e}")
        raise RuntimeError(
            "Could not connect to the website. Please check the URL and your internet connection."
        )
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error while scraping {url}: {e}")
        raise RuntimeError(f"The website returned an error: {e.response.status_code}")
    except Exception as e:
        logger.error(f"URL scraping failed: {e}")
        raise RuntimeError(f"Failed to fetch or parse URL: {e}")
