import os
import os
import wikipediaapi
import requests


def get_unsplash_image(query: str) -> dict | None:
    """Fetch an image from Unsplash based on the query."""
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        raise ValueError("UNSPLASH_ACCESS_KEY is not set in the .env file")
    url = "https://api.unsplash.com/photos/random"

    params = {
        "query": query,
        "client_id": access_key,
        "orientation": "landscape",
        "count": 4,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "url": data["urls"]["regular"],
            "photographer_name": data["user"]["name"],
            "photographer_profile": data["user"]["links"]["html"],
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from Unsplash: {e}")
        return None


def get_destination_info(destination: str) -> dict | None:
    """
    Fetches a summary and URL for a given destination from Wikipedia.
    """
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="TravelInspoBot/1.0 (andwatiian@gmail.com)",
        language="en",
    )
    page = wiki_wiki.page(destination)

    if page.exists():
        return {
            "Summary": page.summary.split("\n")[0],
            "URL": page.fullurl,
        }
    else:
        print(f"No Wikipedia page found for {destination}.")
        return None
