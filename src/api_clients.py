import os
import wikipediaapi  # type: ignore
import requests


from typing import List, Dict, Optional


def get_unsplash_image(query: str) -> Optional[List[Dict[str, str]]]:
    """Fetch images from Unsplash based on the query."""
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        raise ValueError("UNSPLASH_ACCESS_KEY is not set in the .env file")
    url = "https://api.unsplash.com/photos/random"

    from typing import Union

    params: Dict[str, Union[str, int]] = {
        "query": query,
        "client_id": access_key,
        "orientation": "landscape",
        "count": 4,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # data is a list of photo dicts
        images: List[Dict[str, str]] = []
        for item in data:
            images.append(
                {
                    "url": item["urls"]["regular"],
                    "photographer_name": item["user"]["name"],
                    "photographer_profile": item["user"]["links"]["html"],
                }
            )
        return images

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from Unsplash: {e}")
        return None


def get_destination_info(destination: str) -> dict[str, str] | None:
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
            "summary": str(page.summary.split("\n")[0]),
            "url": str(page.fullurl),
        }
    else:
        print(f"No Wikipedia page found for {destination}.")
        return None
