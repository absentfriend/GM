import requests
from bs4 import BeautifulSoup as bs
from ..models import *

class RugbyVideo(JetExtractor):
    domains = ["rugby24.net"]
    name = "RugbyVideo"

    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_init(progress, items):
            return items
        
        base_url = f"https://{self.domains[0]}"
        if params is not None:
            base_url += f"?page{params['page']}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(base_url, headers=headers).text
        soup = (bs(r, 'html.parser'))
        matches = soup.find_all(class_='short_item block_elem')
        for match in matches:
            name = match.h3.a.text.replace('Full Game Replay ', '').rstrip(' Rugby')
            link = f"{base_url}{match.a['href']}"
            icon = f"{base_url}{match.a.img['src']}"
            items.append(JetItem(name, links=[JetLink(link, links=True)], icon=icon))
        
        if params is not None:
            next_page = int(params['page']) + 1
        else:
            next_page = 2
        items.append(JetItem(f"[COLORyellow]Page {next_page}[/COLOR]", links=[], params={"page": next_page}))
        return items
    
    
    def get_links(self, url: JetLink) -> List[JetLink]:
        links = []
        title = ''
        link = ''
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url.address, headers=headers).text
        soup = bs(r, 'html.parser')
        for iframe in soup.select("div.video-responsive > iframe"):
            link = iframe.get("src")
            if link.startswith('//'):
                link = f'https:{link}'
            if 'youtube' in link:
                yt_id = link.split('/')[-1]
                link = f'plugin://plugin.video.youtube/play/?video_id={yt_id}'
                title = 'Highlights'
            else:
                title = link.split('/')[2]
            links.append(JetLink(link, name=title, resolveurl=True))
        return links