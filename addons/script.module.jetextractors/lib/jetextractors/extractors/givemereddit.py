import requests, re, base64
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import timedelta, datetime

from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from ..util.m3u8_src import scan_page
from ..util import jsunpack, find_iframes



from ..util.hunter import hunter
from ..util.m3u8_src import scan_page

class GiveMeReddit(Extractor):
    def __init__(self) -> None:
        self.domains = ["givemereddit.eu","official.givemeredditstream.cc","givemenbastreams.com", "givemenflstreams.com"]
        self.name = "Give Me"


    def get_games(self):
        games = []
        r = requests.get(f"https://{self.domains[0]}").text
        soup = BeautifulSoup(r, "html.parser")

        # for competition in soup.select("div.top-tournament"):
        #     sport = " ".join(competition.find("h2").text.split(" ")[1:-2])
        for game in soup.select("div.card-body"):
            name = game.select_one("div.timeline-title").text
            live = game.select_one("div.timeline-local-time").text 
            sport = game.select_one("div.timeline-league").text 
          
            # if not name:
            #     continue
            href = game.find("a").get("href")
            href1= "https://"+self.domains[0]+"/"+ href
            games.append(Game(sport+ "[COLORyellow] | [/COLOR]"+name + "   "+"[COLORred]"+ live+"[/COLOR]",links=[Link(href1)]))
        return games

    def get_link(self, url):
        r = requests.get(url).text
        re_iframe = re.findall(r'iframe class=\"embed-responsive-item\" src=\"(.+?)\"', r)
        if len(re_iframe) != 0:
            r = requests.get(re_iframe[0], headers={"User-Agent": self.user_agent, "Referer": url}).text
        re_hunter = re.findall(r'decodeURIComponent\(escape\(r\)\)}\("(.+?)",(.+?),"(.+?)",(.+?),(.+?),(.+?)\)', r)[0]
        deobfus = hunter(re_hunter[0], int(re_hunter[1]), re_hunter[2], int(re_hunter[3]), int(re_hunter[4]), int(re_hunter[5]))
        m3u8 = scan_page(url, deobfus)
        m3u8.headers["User-Agent"] = self.user_agent
        return m3u8