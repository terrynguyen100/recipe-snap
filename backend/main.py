from fastapi import FastAPI, HTTPException
import httpx
import configparser
from bs4 import BeautifulSoup
import openai
from scrape_recipe import scrape_recipe

app = FastAPI()

# Load OpenAI API key from config.ini
config = configparser.ConfigParser()
config.read("config.ini")
openai_api_key = config.get("openai", "api_key")

# Set OpenAI API key
openai.api_key = openai_api_key


sample_url = "https://www.inspiredtaste.net/37475/homemade-chicken-noodle-soup-recipe/"

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/get_recipe")
async def get_recipe():
    try:
        metadata = scrape_recipe(sample_url)
        return {"Metadata": metadata}
    except Exception as e:
        return {"Error": str(e)}
