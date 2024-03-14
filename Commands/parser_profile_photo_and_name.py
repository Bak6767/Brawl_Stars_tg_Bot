from bs4 import BeautifulSoup
import requests
import brawlstats
from dotenv import load_dotenv
import os

load_dotenv()

async def pars_profile_photo(profile_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    url = f"https://brawlbot.xyz/stats/player/{profile_id}"
    req = requests.get(url, headers=headers)
    
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(req.text)
    
    with open("index.html", "r", encoding="utf-8") as file:
        src = file.read()
    
    soup = BeautifulSoup(src, "lxml")
    brawl_name = soup.find_all(class_="text-2xl font-bold mb-3 text-white")
    
    for i in brawl_name:
        result = i.mark.text
        print(result)
    
