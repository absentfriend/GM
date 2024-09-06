import requests, re, random
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import timedelta, datetime

from ..util import find_iframes
from ..models import *
categories = ["basketball","american-football","baseball","motor-sports","rugby","cricket","afl","football",
              "hockey","fight","tennis","golf","darts","other"]

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers = {"User-Agent":user_agent, "referrer": 'daddylive.me', "Connection":'keep-alive', 'Accept':'audio/webm,audio/ogg,udio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5'}

class Streamedsu(JetExtractor):
    def __init__(self) -> None:
        self.domains = ["streamed.su", "embedme.top"]
        self.categories = categories
        self.name = "Streamedsu"

    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_init(progress, items):
            return items
        
        for category in self.categories:
            if self.progress_update(progress, category):
                return items

            category_url = f"https://{self.domains[0]}/category/{category}"            
            r = requests.get(category_url, headers=headers, timeout=self.timeout)
                                    
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
                        utc_time = None
                        if time != "":
                            try:
                                utc_time = parse(time) + timedelta(hours=0)
                            except:
                                try:
                                    utc_time1 = datetime.strptime(time, "%H:%M %p ET - %m/%d/%Y") + timedelta(hours=0)
                                except:
                                    pass
                         
                        league = category
                        if league is "basketball":league = "nba"
                        if league is "american-football":league = "nfl"
                        if league is "baseball":league = "mlb"
                        if league is "hockey":league = "nhl"
                        if league is "football":league = "soccer"
                            
                        combined_title = f"  {title}" if time else title
                        # utc_time1="[COLORblue]"+utc_time+"[/COLOR]"
                        items.append(JetItem(league=league.upper(),title=combined_title, links=[JetLink(address=href, links=True)], starttime=utc_time))

        return items

    def get_links(self, url: JetLink) -> List[JetLink]:
        links = []
        r = requests.get(url.address, headers=headers).text
        soup = BeautifulSoup(r, "html.parser")
        for link in soup.select("a.w-full"):
            parts = link.get("href").split("/")
            regex = '<h2.+?>(.+?)<.+?title=\"(.+?)\".+?<div>(.+?)<\/div>'
            splitter = re.compile(regex).findall(str(link))
            title_part = f"{splitter[0][1]} {splitter[0][0]} - {splitter[0][-1]}"            
            title_part2 = title_part.encode('latin1').decode('utf-8')
            links.append(JetLink(f"https://embedme.top/embed/{parts[3]}/{parts[2]}/{parts[4]}", name = title_part2))
        return links
    
    def get_link(self, url: JetLink) -> JetLink:
        r = requests.get(url).text
        info = re.findall(r'k="(.+?)",i="(.+?)",s="(.+?)",l=\["(.+?)"\],h="(.+?)"', r)[0]
        return JetLink(f"https://{info[3]}.{info[4]}/{info[0]}/js/{info[1]}/{info[2]}/playlist.m3u8", headers={"Referer": url})


