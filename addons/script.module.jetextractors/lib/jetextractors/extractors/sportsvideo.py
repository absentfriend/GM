import requests, re
from bs4 import BeautifulSoup as bs
from ..models import *


class SportsVideo(JetExtractor):
    domains = ["nfl-video.com", "nhlvideo.net", "mlblive.net", "rugby24.net", "fullfightreplays.com", "basketball-video.com"]
    name = "SportsVideo"

    def get_items(self, params: Optional[dict] = None, progress: Optional[JetExtractorProgress] = None) -> List[JetItem]:
        items = []
        if self.progress_init(progress, items):
            return items
        
        if params is None:
            items.append(JetItem(title="NFL", links=[], params={"page": "0"}))
            items.append(JetItem(title="NHL", links=[], params={"page": "1"}))
            items.append(JetItem(title="MLB", links=[], params={"page": "2"}))
            items.append(JetItem(title="Rugby", links=[], params={"page": "3"}))
            items.append(JetItem(title="MMA", links=[], params={"page": "4"}))
            items.append(JetItem(title="NBA", links=[], params={"page": "5"}))
        else:
            page = int(params["page"])
            domain = self.domains[page]
            base_url = f"https://{domain}"

            if "href" not in params:
                r = requests.get(base_url, verify="basketball" not in domain, timeout=self.timeout).text
                soup = bs(r, "html.parser")
                for li in soup.select_one("ul#list_cat").select("li"):
                    if li.get("class") != None:
                        continue
                    cat_name = li.text.strip()
                    cat_a = li.next
                    if cat_a.get("rel") != None:
                        continue
                    cat_href = cat_a.get("href")
                    if cat_href == None:
                        continue
                    href = "/" + "/".join(cat_href.split("/")[3:])
                    items.append(JetItem(title=cat_name, links=[], params={"page": page, "href": href}))
            else:
                url = base_url + params["href"]
                headers = {"User-Agent": self.user_agent, "Referer": base_url}
                r = requests.get(url, headers=headers, verify="basketball" not in domain, timeout=self.timeout).text
                soup = (bs(r, 'html.parser'))
                matches = soup.find_all(class_='short_item block_elem')
                for match in matches:
                    name = match.h3.a.text.replace('Full Game Replay ', '').rstrip(' NHL')
                    link = f"{base_url}{match.a['href']}"
                    icon = f"{base_url}{match.a.img['src']}"
                    items.append(JetItem(name, links=[JetLink(link, links=True)], icon=icon))
                next_page_btn = soup.select("a.swchItem")
                if len(next_page_btn) > 0 and next_page_btn[-1].text == "»":
                    href = next_page_btn[-1].get('href')
                    if not href.startswith("/"):
                        href = params["href"] + href
                    page = int(re.findall(r"spages\('(.+?)'", next_page_btn[-1].get('onclick'))[0])
                    items.append(JetItem(f"[COLORyellow]Page {page}[/COLOR]", links=[], params={"page": page, "href": href}))
        
        return items

    
    def get_links(self, url: JetLink) -> List[JetLink]:
        links = []
        title = ''
        link = ''
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url.address, headers=headers, verify="basketball" not in url.address).text
        if "basketball" not in url.address:
            soup = bs(r, 'html.parser')
            alt_links = soup.find_all(class_='su-button su-button-style-default')
            if alt_links:
                for alt_link in alt_links:
                    link = alt_link.get('href')
                    if link:
                        title = link.split('/')[2]
                        links.append(JetLink(link, name=title, resolveurl=True))
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
            return links
        else:
            soup = bs(r, 'html.parser')
            iframes = soup.find_all(class_='su-button')
            for iframe in iframes:
                link = iframe['href']
                if link.startswith('//'):
                    link = f'https:{link}'
                response = requests.get(link, headers=headers, verify=False).text
                soup = bs(response, 'html.parser')
                iframe_ = soup.find('iframe')
                if not iframe_: continue
                link = iframe_['src']
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