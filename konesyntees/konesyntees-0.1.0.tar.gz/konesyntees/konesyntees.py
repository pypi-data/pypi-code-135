"""Main module."""
import cloudscraper
from typing import Optional


def konesyntees(
    input: str, voice: Optional[int] = "1", speed: Optional[float] = "-4"
):

    # error handling
    if len(str(input)) > 100:
        raise ValueError("Text too long! (<100)")

    if len(str(input)) < 5:
        raise TypeError("Text cannot be empty")

    if voice < 0 or voice > 3:
        raise ValueError("Voice must be in the range of 0 .. 3")

    if speed < -9 or speed > 9:
        raise ValueError("Speed must be in the range of -9 .. 9")

    try:
        scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
        request = scraper.get(f"https://teenus.eki.ee/konesyntees?haal={voice}&kiirus={speed}&tekst={input}").json()
        results = request["mp3url"]

        return results
    except:
        raise Exception("Something went wrong. Please try again later.")
