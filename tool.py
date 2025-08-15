import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool
async def get_weather(
    context: RunContext,
    city: str
) -> str:
    """
    Get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3"
        )
        if response.status_code == 200:
            weather_text = response.text.strip()
            logging.info(f"Weather for {city}: {weather_text}")
            return weather_text
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Error: Unable to retrieve weather data for {city}."
    except Exception as e:
        logging.error(f"Exception occurred while getting weather for {city}: {e}")
        return f"Error: An exception occurred while retrieving weather data for {city}."


@function_tool
async def search_web(
    context: RunContext,
    query: str
) -> str:
    """
    Search the web using DuckDuckGo and return the results.
    """
    try:
        search = DuckDuckGoSearchRun()
        results = search.run(query)
        logging.info(f"Search results for '{query}': {results}")
        return results or "No results found."
    except Exception as e:
        logging.error(f"Exception occurred while searching for '{query}': {e}")
        return f"Error: An exception occurred while searching for '{query}'."
