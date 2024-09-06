import requests
from bs4 import BeautifulSoup as bs
from ..models import *

class BasketballVideo(JetExtractor):
    domains = ["basketball-video.com"]
    name = "BasketballVideo"

    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_update(progress):
            return items
        
        base_url = f"https://{self.domains[0]}"
        if params is not None:
            base_url += f"?page{params['page']}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(base_url, headers=headers, timeout=self.timeout).text
        soup = (bs(r, 'html.parser'))
        matches = soup.find_all(class_='short_item block_elem')
        for match in matches:
            name = match.h3.a.text.replace('Full Game Replay ', '').rstrip(' NHL')
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
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url.address, headers=headers, timeout=self.timeout).text
        soup = bs(r, 'html.parser')
        iframes = soup.find_all('iframe')
        for iframe in iframes:
            link = iframe['src']
            if link.startswith('//'):
                link = f'https:{link}'
                title = link.split('/')[2]
                links.append(JetLink(link, name=title, resolveurl=True))
        button = soup.find(class_='su-button')
        if button:
            link = button['href']
            title = link.split('/')[2]
            links.append(JetLink(link, name=title, resolveurl=True))
        return links
        