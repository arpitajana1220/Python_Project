#This code scrapes profile picture of given github account
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/arpitajana1220"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)