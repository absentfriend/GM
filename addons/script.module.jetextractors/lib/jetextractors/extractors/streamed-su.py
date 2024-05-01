from typing import List
import requests, re, random
from bs4 import BeautifulSoup

from ..util import find_iframes

from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
categories = ['basketball']
class Streamedsu(Extractor):
    def __init__(self) -> None:
        self.domains = ["streamed.su"]
        self.categories = categories
        self.name = "Streamedsu"
        # self.short_name = ""



    def get_games(self):
        games = []
        for category in self.categories:
            category_url = f"https://{self.domains[0]}/category/{category}"
            r = requests.get(category_url)

            soup = BeautifulSoup(r.text, "html.parser")
            target = soup.find('div', class_='w-full md:w-1/2 !w-full')

            if target:
                for a in target.find_all('a'):
                    h1 = a.find('h1')
                   
                    if h1:
                        title = h1.get('title', '')
                        href = a.get('href', '')
                        if href.startswith("/"):
                            href = f"https://{self.domains[0]}" + href
                        time_div_1 = a.find('div', class_='font-bold text-red-500')
                        time_1 = time_div_1.text.strip() if time_div_1 else None 

                       
                        if not time_1:
                            time_div_2 = a.find('div', class_='')
                            time_2 = time_div_2.text.strip() if time_div_2 else None 
                        else:
                            time_2 = None  

                        
                        if time_1 or time_2:
                            time = time_1 if time_1 else time_2
                            combined_title = f"{time}  {title}"
                        else:
                            combined_title = title 

                       
                        combined_title = f"{time}  {title}" if time else title

                        games.append(Game(title=combined_title, links=[Link(address=href, is_links=True)]))

        return games

    def get_links(self, url: str):
        links = []
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        for link in soup.select("div.w-full > a"):
            parts = link.get("href").split("/")
            rand = random.randint(1, 3)
            links.append(Link(f"https://inst{rand}.ignores.top/js/{parts[2]}/{parts[3]}/playlist.m3u8", is_direct=True, headers={"Referer": "https://vipstreams.in/", "Origin": "https://vipstreams.in"}))
        return links
