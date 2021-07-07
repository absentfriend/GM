# -*- coding: utf-8 -*-


import re, base64

from six import ensure_text

from oathscrapers import cfScraper
from oathscrapers import parse_qs, urljoin, urlencode
from oathscrapers.modules import client
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['fsapi.xyz']
        self.base_link = 'https://fsapi.xyz'
        self.search_link = '/movie/%s'
        self.search_link2 = '/tv-imdb/%s-%s-%s'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url is None: return

            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if url is None:
                return sources

            hostDict = hostprDict + hostDict

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            if 'tvshowtitle' in data:
                query = self.search_link2 % (data['imdb'], data['season'], data['episode'])
            else:
                query = self.search_link % data['imdb']

            url = urljoin(self.base_link, query)
            posts = cfScraper.get(url, headers=self.headers).text
            r = re.findall('<a href="(.+?)" rel', posts)
            urls = [u.split('url=')[1] for u in r]
            urls = [ensure_text(base64.b64decode(url), errors='ignore') for url in urls]
            urls = ['https:' + url if url.startswith('//') else url for url in urls]
            urls = list(set(urls))
            #log_utils.log('fsapi_all_urls: ' + repr(urls))

            for url in urls:

                valid, host = source_utils.is_host_valid(url, hostDict)
                if valid:
                    quality, _ = source_utils.get_release_quality(url)
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})

                elif ('vidembed' in url and '/goto.' in url) or '/hls/' in url:
                    sources.append({'source': host, 'quality': 'sd', 'language': 'en', 'url': url, 'direct': True, 'debridonly': False})

                elif 'vidnext' in url:
                    try:
                        r = cfScraper.get(url, headers=self.headers).text
                        links = client.parseDOM(r, 'li', ret='data-video')
                        for url in links:
                            url = url if url.startswith('http') else 'https:{0}'.format(url)
                            valid, host = source_utils.is_host_valid(url, hostDict)
                            if valid:
                                sources.append({'source': host, 'quality': 'sd', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
                    except:
                        pass

                elif 'vidsrc' in url:
                    try:
                        r = cfScraper.get(url, headers={'User-Agent': client.agent(), 'Referer': 'https://v2.vidsrc.me'}).text
                        r = re.findall('data-hash="(.+?)"', r)[0]
                        r = 'https://v2.vidsrc.me/src/%s' % r
                        r2 = cfScraper.get(r, headers={'User-Agent': client.agent(), 'Referer': 'https://v2.vidsrc.me'}).text
                        links = re.findall("'player' src='(.+?)'", r2)
                        links = [link + '|Referer=https://vidsrc.me' for link in links]
                        for url in links:
                            url = url if url.startswith('http') else 'https:{0}'.format(url)
                            sources.append({'source': 'CDN', 'quality': '720p', 'language': 'en', 'url': url, 'direct': True, 'debridonly': False})
                    except:
                        pass

                # elif '2embed' in url:
                    # try:
                        # r = cfScraper.get(url, headers={'User-Agent': client.agent(), 'Referer': url}).text
                        # items = re.compile('data-id="(.+?)">.+?</a>').findall(r)

                        # for item in items:
                            # item = 'https://www.2embed.ru/ajax/embed/play?id=%s&_token=' % item
                            # log_utils.log('fsapi_2embed_item: ' + repr(item))
                            # url = cfScraper.get(item, headers={'User-Agent': client.agent(), 'Referer': item}).text
                            # log_utils.log('fsapi_2embed_url: ' + repr(url))
                            # urls = re.findall('"link":"(.+?)","sources"', url)
                            # log_utils.log('fsapi_2embed_urls: ' + repr(urls))
                            # for url in urls:
                                # if 'vidcloud.pro' in url:
                                    # r = cfScraper.get(url, headers={'User-Agent': client.agent(), 'Referer': url}).text
                                    # r = re.findall('sources = \[{"file":"(.+?)","type"', r)[0]
                                    # r = r.replace('\\', '')
                                    # valid, host = source_utils.is_host_valid(url, hostDict)
                                    # quality, info = source_utils.get_release_quality(url, url)
                                    # sources.append(
                                        # {'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': r,
                                         # 'direct': False, 'debridonly': False})
                                # else:
                                    # valid, host = source_utils.is_host_valid(url, hostDict)
                                    # if valid:
                                        # quality, info = source_utils.get_release_quality(url, url)
                                        # sources.append(
                                            # {'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url,
                                             # 'direct': False,
                                             # 'debridonly': False})
                    # except:
                        # pass

            return sources
        except:
            log_utils.log('FSAPI Exception', 1)
            return sources

    def resolve(self, url):
        return url
