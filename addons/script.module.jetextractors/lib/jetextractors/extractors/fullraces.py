import requests
from bs4 import BeautifulSoup as bs

from ..models import *


class FullRaces(JetExtractor):
    domains = ["fullraces.com"]
    name = "Fullraces"

    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_update(progress):
            return items
            
        base_url = f"https://{self.domains[0]}"
        if params:
            page = int(params['page'])
            url = f'{base_url}/?page{page}'
        else:
            page = 1
            url = base_url
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url, headers=headers, timeout=10).text
        soup = (bs(r, 'html.parser'))
        matches = soup.find_all(class_='short_item')
        for match in matches:
            title = match.h3.a.text
            link = f"{base_url}{match.a['href']}"
            icon = f"{base_url}{match.a.img['src']}"
            items.append(JetItem(title=title, links=[JetLink(link, links=True)], icon=icon))
        items.append(JetItem(f'[COLORyellow]Page {page+1}[/COLOR]', links=[], params={'page': page+1}))
        return items
    
    def get_links(self, url: JetLink) -> List[JetLink]:
        links = []
        title = ''
        link = ''
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url, headers=headers, timeout=self.timeout).text
        soup = bs(r, 'html.parser')
        iframes = soup.find_all('iframe')
        for iframe in iframes:
            link = iframe['src']
            if link.startswith('//'):
                link = f'https:{link}'
            if 'youtube' in link:
                yt_id = link.split('/')[-1]
                link = f'plugin://plugin.video.youtube/play/?video_id={yt_id}'
                title = 'Highlights'
            else:
                title = link.split('/')[2]
            links.append(JetLink(link, name=title, resolveurl=True))
        for button in soup.find_all(class_='su-button'):
            link = button['href']
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
        