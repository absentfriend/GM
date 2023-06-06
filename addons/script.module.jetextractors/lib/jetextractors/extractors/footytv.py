
import requests, re, datetime
from bs4 import BeautifulSoup

from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from ..util import jsunpack

class FootyBiteTV(Extractor):
    def __init__(self) -> None:
        self.domains = ["footybite.tv", "www.footybite.tv"]
        self.name = "FootyBiteTV"

    def get_games(self):
        games = []
        r = requests.get(f"https://{self.domains[0]}").text
        soup = BeautifulSoup(r, "html.parser")

        for game in soup.find_all("tr"):#, class_="et4"): # Loop through each <a> element
            name = game.select_one("td.et4").text # Get text of <a> element
            game_time = game.select_one("td.et3").text.split(":")
            hour = int(game_time[0])
            minute = int(game_time[1])
            utc_time = datetime.datetime.now().replace(hour=hour, minute=minute) + datetime.timedelta(hours=23)
            
            if not name: # Skip if name is empty
                continue
            href = game.find("a").get("href") # Get href attribute from a element
            games.append(Game(name, starttime=utc_time, links=[Link(href)]))
        return games

    def get_link(self, url):
        # iframes = [Link(u) if not isinstance(u, Link) else u for u in find_iframes.find_iframes(url, "", [], [])]
        # return iframes[0]

        # Get link
        r = requests.get(url).text
        re_iframe = re.findall(r'iframe.+?src="(.+?)"', r)[0] # Get iframe src

        # Get first iframe and get link to second iframe
        r_iframe = requests.get(re_iframe, headers={"Referer": url}).text # Request iframe URL
        re_iframe2 = re.findall(r'iframe.+?src="(.+?)"', r_iframe)[0]

        # Get second iframe
        r_iframe2 = requests.get(re_iframe2, headers={"Referer": re_iframe}).text # Request iframe URL
        re_packed = re.findall(r"(eval\(function\(p,a,c,k,e,d\).+?{}\)\))", r_iframe2)[0] # Get obfuscated javascript
        deobfus_packed = jsunpack.unpack(re_packed) # Deobfuscate re_packed
        m3u8 = re.findall(r'var src="(.+?)"', deobfus_packed)[0] # Get url from deobfuscated javascript
        return Link(m3u8, headers={"Referer": re_iframe2, "User-Agent": self.user_agent})


