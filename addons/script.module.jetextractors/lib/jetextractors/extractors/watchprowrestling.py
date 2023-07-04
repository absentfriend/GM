import xbmc
import xbmcgui
import requests
import json
import re
from bs4 import BeautifulSoup as bs
from base64 import b64decode
from typing import List
from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from ..util import jsunpack


BASE_URL = 'https://watchprowrestling.co'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
HEADERS = {"User-Agent": USER_AGENT, 'Accept': '*/*', 'Referer': BASE_URL}
SEARCH_URL = 'https://watchprowrestling.org/page/1/?s='
DEBRID = ['1fichier.com', 'uptobox.com', 'drop.download']
FILTERS = ['download.tfast.store', 'player.wfast.store', 'guccihide.com', 'streamplay.to', 'www.m2list.com', 'vptip.com', 'www.sawlive.net', 'player.restream.io', 'download.cfast.store']
PROGRESS = xbmcgui.DialogProgress()
OK = xbmcgui.Dialog().ok


class WatchProWrestling(Extractor):
    domains = ["watchprowrestling.co"]
    name = "WatchProWrestling"

    def get_games(self) -> List[Game]:
        items = {}
        response = requests.get(BASE_URL, headers=HEADERS)
        soup = bs(response.text, 'html.parser')
        for item in soup.find_all(class_ = 'menu-item'):
            url = item.a['href']
            if not url == '#':
                items[item.text] = item.a['href']
        games = [Game('Search', page='SEARCH'), Game('Most Recent Shows', page='/page/1')]
        for item in items.keys():
            cat = items[item].split(BASE_URL)[1] + 'page/1'
            games.append(Game(item, page=cat))
        return games
    
    def get_games_page(self, page) -> List[Game]:
        games = []
        items = {}
        if 'SEARCH' in page:
            query = from_keyboard()
            if not query:
                quit()
            url = SEARCH_URL + query.replace(' ', '+')
        else:
            if not 'page' in page:
                url = f"{BASE_URL}/page/{page}"
            else:
                url = f"{BASE_URL}/{page}"
        response = requests.get(url, headers=HEADERS)
        soup = bs(response.text, 'html.parser')
        vids = soup.find(class_='video-section')
        if not vids:
            OK('No Items Found', 'No items were found.')
            quit()
        for vid in vids.find_all(class_='item'):
            title = vid.h3.a.text.replace('Watch ', '')
            link = vid.a['href']
            thumbnail = vid.img
            if thumbnail:
                thumbnail = thumbnail['src']
            else:
                thumbnail = ''
            items[title] = {
                'link': link,
                'thumbnail': thumbnail
            }
            games.append(Game(title=title, links=[Link(link, is_links=True)], icon=thumbnail))
        splitted = url.split('/')
        if '?s=' in url:
            page_num = splitted[-2]
            page_url = f"{'/'.join(splitted[:-2])}/{int(page_num) + 1}/{splitted[-1]}"
            next_page = page_url.split(BASE_URL)[1]
        else:
            page_num = splitted[-1]
            page_url = '/'.join(splitted[:-1])
            next_page = f'{page_url.split(BASE_URL)[1]}/{int(page_num) + 1}'
        games.append(Game(f"[COLORyellow]Page {int(page_num)+1}[/COLOR]", page=next_page))
        return games
    
    def get_links(self, url: str) -> List[Link]:
        xbmc.log('WPW Started', xbmc.LOGINFO)
        links = []
        items = []
        non_working = []
        debrid = []
        non_debrid = []
        link = ''
        r = requests.get(url, headers=HEADERS).text
        soup = bs(r, 'html.parser')
        matches = soup.find_all(class_='bk-button-wrapper')
        PROGRESS.create('Gathering Links...')
        PROGRESS.update(0, 'Please wait while your links are being processed.\nThis could take several seconds.')
        counter = 0
        for item in matches:
            if PROGRESS.iscanceled():
                PROGRESS.close()
                quit()
            try:
                percentage = int(counter/len(matches)*100)
                link_label = item.text
                try:
                    link = resolve(item.a['href'])
                except IndexError:
                    link = ''
                if link:
                    links.append(f'{link}|||{link_label}')
            except:
                pass
            PROGRESS.update(percentage, f'Please wait while your links are being processed.\nThis could take several seconds. {percentage}%')
            counter += 1
        PROGRESS.update(100, 'Please wait while your links are being processed.\nThis could take several seconds.  100%\nDone!')
        xbmc.sleep(500)
        PROGRESS.close()
        for link in links:
            splitted1 = link.split('|||')
            label1 = splitted1[1]
            link1 = splitted1[0]
            splitted2 = link1.replace('ffmpeg|', '').replace('hls|', '').split('/')
            if type(splitted2) == list and len(splitted2) > 2:
                label = splitted2[2]
                if label in FILTERS:
                    non_working.append(link1)
                    continue
                if label in DEBRID:
                    debrid.append([f'{label} - {label1} [COLOR green]***Debrid***[/COLOR]', link1])
                else:
                    non_debrid.append([f'{label} - {label1}', link1])

        for label, link in debrid:
            items.append(Link(link, name=label, is_resolveurl=True))
        for label, link in non_debrid:
            if link.startswith('hls|'):
                link = link.replace('hls|', '')
                items.append(Link(link, name=label, is_resolveurl=False, is_hls=True))
            elif link.startswith('ffmpeg|'):
                link = link.replace('ffmpeg|', '')
                items.append(Link(link, name=label, is_resolveurl=False, is_ffmpegdirect=True))
            else:
                items.append(Link(link, name=label, is_resolveurl=True))
        if not items:
            OK('', 'No Links Available')
            quit()
        return items


class Search(WatchProWrestling):
    domains = ["watchprowrestling.co"]
    name = "WatchProWrestlingSearch"

    def get_games(self) -> List[Game]:
        games = []
        items = {}
        response = requests.get(f'https://{self.domains[0]}', headers=HEADERS)
        soup = bs(response.text, 'html.parser')
        vids = soup.find(class_='video-section')
        if not vids:
            OK('No Items Found', 'No items were found.')
            quit()
        for vid in vids.find_all(class_='item'):
            title = vid.h3.a.text.replace('Watch ', '')
            link = vid.a['href']
            thumbnail = vid.img['src']
            items[title] = {
                'link': link,
                'thumbnail': thumbnail
            }
            games.append(Game(title=title, links=[Link(link, is_links=True)], icon=thumbnail))
        games.append(Game("[COLORyellow]Page 2[/COLOR]", page=2))
        return games


def from_keyboard(default_text='', header='Search'):
    kb = xbmc.Keyboard(default_text, header, False)
    kb.doModal()
    if (kb.isConfirmed()):
        return kb.getText()
    return

def unpack(url:str, referer: str):
    HEADERS['Referer'] = referer
    r = requests.get(url, headers=HEADERS).text
    return jsunpack.unpack(r)

def resolve_hdfree(url: str, referer: str):
    unpacked = unpack(url, referer=referer)
    url2 = re.compile("startframe2='(.+?)'").findall(unpacked)[0]
    return url2

def resolve_educ_top(url: str, referer: str):
    HEADERS['Referer'] = referer
    unpacked = unpack(url, referer=referer)
    url2 = re.compile('iframe src="(.+?)line=').findall(unpacked)[0]
    return url2

def resolve_sawlive(url: str):
    HEADERS['Referer'] = 'https://vptip.com/'
    r = requests.get(url, headers = HEADERS).text
    code = re.compile(r'var maincode="(.+?)"').findall(r)[0]
    line = re.compile(r'var subcode="(.+?)"').findall(r)[0]
    HEADERS ['Referer'] = 'https://www.hdfree.info/'
    r = requests.get(f'https://www.hdfree.info/finalpage/{code}.php?line={line}', headers=HEADERS).text
    try:
        labels = b64decode(re.compile("var labels=atob\('(.+?)'").findall(r)[0]).decode('utf-8')
        substyles = b64decode(re.compile("var substyles=atob\('(.+?)'").findall(r)[0]).decode('utf-8')
        _id = re.compile("var preloadcaptions = '(.+?)_").findall(r)[0]
        return 'https:' + labels.split('src="')[1] + _id
    except IndexError:
        HEADERS['Referer'] = 'https://vptip.com/'
        r = requests.get(url, headers = HEADERS).text
        line = re.compile(r'var subcode="(.+?)"').findall(r)[0]
        referer = f'https://android-database2.firebase-api.com/group2/secure2/?line={line}'
        link = f'https://android-database2.firebase-api.com/AccessLog2/{line}/apache.m3u8'
        return f'{link}|Referer={referer}'
    return
    
def resolve_ntuplay(url: str, referer: str=''):
    if referer:
        HEADERS['Referer'] = referer
    else:
        HEADERS['Referer'] = 'https://vptip.com/'
    r = requests.get(url, headers=HEADERS).text
    link = re.compile("source:'(.+?)'").findall(r)
    if link:
        link = link[0]
        if 'webuit.' in link:
            return resolve_webuit(link, referer=url)
        return f'hls|{link}|Referer={url}'
    return

def resolve_webuit(url: str, referer: str):
    HEADERS['Referer'] = referer
    r = requests.get(url, headers=HEADERS).text
    lines = r.splitlines()
    if lines:
        track = lines[-1]
        url2 = url.replace('webuit', 'wiki').replace('/lb/', '/wiki/').replace('index.m3u8', track)
        return f'hls|{url2}|Referer={referer}'
    return

def resolve_m2list(url:str):
    HEADERS['Referer'] = url
    _id, main_id = re.compile('mirror=(.+?)&mainid=(.+?$)').findall(url)[0]
    url2 = f'https://www.m2list.com/2023update/db/{main_id}_cache.php'
    r = requests.get(url2, headers=HEADERS).text
    x = re.compile('json="(.+?)"').findall(r)
    if not x:
        return
    try:
        x = b64decode(x[0]).decode('utf-8')
        x = json.loads(x)
    except:
        return
    
    video_id = ''
    link = ''
    try:
        video_id = x[_id.replace('tdmrep', 'dmrep')]
    except KeyError:
        return
    if not video_id:
        return
    
    embed_DmRep_type1 = f'https://www.dailymotion.com/embed/video/{video_id}'
    embed_FSCFull = f'https://developer1-vioef.android-devs.top/f/{video_id}.db|Referer=https://developer1-vioef.android-devs.top/'
    embed_FSCRep = f'https://developer1-vioef.android-devs.top/f/{video_id}.db|Referer=https://developer1-vioef.android-devs.top/'
    embed_pvphd = link = f'https://player2.pvpstage.com/f/{video_id}.480|Referer=https://player2.pvpstage.com/'
    embed_Host4Full = f"https://sanji12.affliate.net/10th_March_2023/embed/mod/pvphd.php?source={video_id}" # Needs Prefix?
    
    types = {
        'fscfull': embed_FSCFull,
        'tubehdfull': embed_pvphd,
        'h3full': embed_pvphd,
        'h4full': embed_Host4Full,
        'host3lp': embed_pvphd,
        'tuberep': embed_pvphd,
        'dmlp': embed_DmRep_type1,
        'tubelp': embed_pvphd,
        'fscrep': [
            embed_FSCRep,
            embed_pvphd
        ],
        'dmrep': embed_DmRep_type1
    }
    _id_splitted = _id.split('_')
    code = _id_splitted[0]
    if len(_id_splitted) > 1:
        chack_id = f'{code}_count{_id_splitted[1]}'
    else:
        chack_id = chack_id = f'{code}_count'
    link = types.get(code, '')
    if not link:
        return
    if type(link) == list:
        chack = x.get(chack_id, '')
        if chack == '1':
            link = link[0]
        else:
            link = link[1]
    return link

def resolve_vptip(url: str):
    HEADERS['Referer'] = BASE_URL
    r = requests.get(url, headers=HEADERS)
    soup = bs(r.text, 'html.parser')
    iframe = soup.find('iframe')
    if iframe:
        link = iframe['src']
        if link.startswith('//'):
            link = 'https:' + link
        return link
    return

def resolve_wikisport(url: str):
    HEADERS['Referer'] = 'https://vptip.com/'
    r = requests.get(url, headers=HEADERS).text
    soup = bs(r, 'html.parser')
    iframe = soup.find('iframe')
    url2 = iframe['src']
    if 'ntuplay' in url2:
        return resolve_ntuplay(url2, referer=url)
    return url2

def resolve_embedstream(url:str):
    from .embedstream import Embedstream
    es = Embedstream()
    link = es.get_link(url)
    return f'{link}|Referer=https://www.nolive.me/'

def resolve_guccihide(url:str):
    HEADERS['Referer'] = 'https://vptip.com/'
    r = requests.get(url, headers=HEADERS).text
    try:
        r = jsunpack.unpack(r)
    except:
        return 
    link = re.compile('file:"(.+?)"').findall(r)
    if not link:
        return
    link = link[0]
    return f'hls|{link}|Referer={url}'

def resolve(url: str):
    url1 = ''
    if 'vptip.com' in url:
        url1 = resolve_vptip(url)
    if url1:
        if 'sawlive' in url1:
            return resolve_sawlive(url1)
        elif 'wikisport.click' in url1:
            return resolve_wikisport(url1)
        elif 'ntuplay' in url1:
            return resolve_ntuplay(url1)
        elif 'm2list' in url1:
            return resolve_m2list(url1)
        elif 'embedstream.me' in url1:
            return resolve_embedstream(url1)
        elif 'guccihide' in url1:
            return resolve_guccihide(url1)
        else:
            return url1 
    return url