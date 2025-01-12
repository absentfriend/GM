from ..models import *
import requests
from bs4 import BeautifulSoup
from ..util import m3u8_src

class TopEmbed(JetExtractor):
    def __init__(self) -> None:
        self.domains = ["topembed.pw"]
        self.name = "TopEmbed"


    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_init(progress, items):
            return items

        r = requests.get(f"https://{self.domains[0]}?all").text
        soup = BeautifulSoup(r, "html.parser")
        for game in soup.select("div.bg-white"):
            title = game.select_one("div.font-bold").text
            links = []
            for channel in game.select("div.mb-4 > div > input"):
                l = channel.get("value")
                if not l.startswith("https"):
                    continue
                link = JetLink(l)
                if "/channel/" in l:
                    link.name = l.split("/")[-1]
                links.append(link)
            items.append(JetItem(title, links))
        
        r = requests.get(f"https://{self.domains[0]}?show_tv=true").text
        soup = BeautifulSoup(r, "html.parser")
        for channel in soup.select("tbody > tr"):
            title = channel.select_one("td").text
            l = channel.select_one("input").get("value")
            link = JetLink(l, name=l.split("/")[-1])
            items.append(JetItem(title, [link]))
        return items


    def get_link(self, url: JetLink) -> JetLink:
        r = requests.get(url.address, headers={"Referer": f"https://{self.domains[0]}/"}).text
        m3u8 = m3u8_src.scan(r)
        return JetLink(m3u8, headers={"Referer": f"https://{self.domains[0]}/", "Origin": f"https://{self.domains[0]}"})
    