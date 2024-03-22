import requests, re, base64,json
from bs4 import BeautifulSoup
from dateutil.parser import parse
from urllib.parse import urlparse
from datetime import timedelta, datetime

from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from ..util.m3u8_src import scan_page
from ..util import jsunpack, find_iframes
from ..icons import icons


class Methstreams(Extractor):
    def __init__(self) -> None:
        
        self.domains = ["methstreams.com/"]
        self.name = "Meth_com"
        self.short_name = "MS"


    def get_games(self):
        games = []
        leagues = ["f1-streams/1/","streams-live-nba/1/","mlb-streams/","get-nflstreams/live/","college-basketball-streams/4/","mma-streams/1/",
                   "mma-streams/1/","boxing-streams/4/","bjjstreams/1/","bjjstreams/1/","wwestreams/"]
        
        for league in leagues:
            r = requests.get(f"https://{self.domains[0]}"+league).text
            soup = BeautifulSoup(r, "html.parser")
            leagues1= league.replace("streams","").replace("-","").replace("get","").replace("/1/","").replace("/","").replace("4","").replace("live","").replace("collegebasketball","ncaab")
            
            
            
            for game in soup.find_all("a", {"class": "btn-block"}):
                href = game.get("href")
                        # if href.startswith("/"):
                        #     href = f"https://{self.domains[0]}{href}"
                title = game.find("h4").text.strip()
                
                
                
                time = game.find("p").text
                utc_time = None
                if time != "":
                    try:
                        utc_time = parse(time) + timedelta(hours=17)
                    except:
                        try:
                            utc_time = datetime.strptime(time, "%H:%M %p ET - %m/%d/%Y") + timedelta(hours=17)
                        except:
                            pass
                games.append(Game(icon=icons[leagues1.lower()] if leagues1.lower() in icons else None,league=leagues1.upper(),title=title, links=[Link(address=href)], starttime=utc_time))
        return games
                
        
            




    def get_link(self, url):
        iframes = [Link(u) if not isinstance(u, Link) else u for u in find_iframes.find_iframes(url, "", [], [])]
        return iframes[0]