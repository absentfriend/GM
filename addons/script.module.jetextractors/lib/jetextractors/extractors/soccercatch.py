import requests
import datetime
import re
from bs4 import BeautifulSoup as bs
from base64 import b64decode
from typing import List
from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from xbmcgui import Dialog


class SoccerCatch(Extractor):
    domains = ["soccercatch.com"]
    name = "SoccerCatch"

    def get_games(self) -> List[Game]:
        dates = self.get_dates()
        games = [Game(title=date[0], page=date[1]) for date in dates]
        return games
    
    def get_games_page(self, date) -> List[Game]:
        games = []
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.post(f"{base_url}/api/matches/date?date={date}", headers=headers).text
        soup = (bs(r, 'html.parser'))
        matches = soup.find_all('a', class_='match-list-content')
        for match in matches:
            url = f"{base_url}{match['href']}"
            home = match.find(class_='match-list-home')
            away = match.find(class_='match-list-away')
            home_name = home.img['alt']
            home_icon = home.img['src']
            away_name = away.img['alt']
            name = f'{home_name} vs {away_name}'
            games.append(Game(name, links=[Link(url, is_links=True)], icon=home_icon))
        return games
    
    def get_links(self, url: str) -> List[Link]:
        links = []
        links2 = []
        base_url = f"https://{self.domains[0]}"
        headers = {"User-Agent": self.user_agent, "Referer": base_url}
        r = requests.get(url, headers=headers).text
        soup = bs(r, 'html.parser')
        highlights = soup.find(class_ = "iframe-responsive")
        if highlights:
            embed = highlights.get("data-src")
            if embed:
                link = bs(embed, "html.parser").iframe.get("src")
                if 'youtube' in link:
                    yt_id = link.split('/')[-1]
                    link = f'plugin://plugin.video.youtube/play/?video_id={yt_id}'
                links2.append(["Highlights", link])
        
        replays = soup.find(class_ = "code-block")
        if replays:
            embed = replays.get("data-src")
            if embed:
                data_url = bs(embed, "html.parser").find(class_="archive-link").get("data-url")
                if data_url:
                    link = b64decode(data_url).decode("utf-8")
                    splitted = link.split('/')
                    _url = "https://footyarchive.com/api/matches/" + splitted[-1]
                    headers['Referer'] = 'https://footyarchive.com/'
                    try:
                        r = requests.get(_url, headers=headers).json()
                        vids = r.get('content')
                        for vid in vids:
                            for content in vid['content']:
                                title = content.get('title', '').split(' - ')
                                if len(title) > 1:
                                    title = title[1]
                                else:
                                    title = title[0]
                                link = b64decode(content['base64']).decode("utf-8")
                                splitted = link.split('/')
                                link_host = splitted[2]
                                title = f'{title} - {link_host}'
                                if 'payskip.org' in link:
                                    continue
                                links2.append([title, link])
                    except:
                        pass
        if links2:
            for title, link in links2:
                links.append(Link(link, name=title, is_resolveurl=True))
        return links       
    
    def get_dates(self):
        dates = []
        d = datetime.date(2021,1,18)
        while d <= datetime.date.today():
            dates.append([datetime.datetime.strftime(d,'%A, %B %d, %Y'), datetime.datetime.strftime(d,'%d-%m-%Y')])
            d += datetime.timedelta(days=1)
        return list(reversed(dates))