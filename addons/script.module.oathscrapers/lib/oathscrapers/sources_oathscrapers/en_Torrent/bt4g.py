# -*- coding: utf-8 -*-

'''
    OathScrapers module
'''

import re

from oathscrapers import cfScraper
from oathscrapers import parse_qs, urljoin, urlencode
from oathscrapers.modules import client
from oathscrapers.modules import debrid
from oathscrapers.modules import source_utils
from oathscrapers.modules import log_utils

from oathscrapers import custom_base_link
custom_base = custom_base_link(__name__)

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['bt4g.org']
        self.base_link = custom_base or 'https://bt4g.org'
        self.search_link = '/movie/search/%s/byseeders/1'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'aliases': aliases, 'year': year}
            url = urlencode(url)
            return url
        except:
            log_utils.log('bt4g0 - Exception', 1)
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'aliases': aliases, 'year': year}
            url = urlencode(url)
            return url
        except:
            log_utils.log('bt4g1 - Exception', 1)
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
            log_utils.log('bt4g2 - Exception', 1)
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if debrid.status() is False:
                return sources

            if url is None:
                return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            hdlr = 's%02de%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']
            aliases = data['aliases']

            query = ' '.join((title, hdlr))
            query = re.sub('(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', '', query)

            url = urljoin(self.base_link, self.search_link % query)

            #r = client.request(url)
            r = cfScraper.get(url).text
            r = r.replace('&nbsp;', ' ')
            r = client.parseDOM(r, 'div', attrs={'class': 'col s12'})
            posts = client.parseDOM(r, 'div')[1:]
            posts = [i for i in posts if 'magnet/' in i]
            for post in posts:
                try:
                    links = client.parseDOM(post, 'a', ret='href')[0]
                    url = 'magnet:?xt=urn:btih:' + links.lstrip('magnet/')
                    name = client.parseDOM(post, 'a', ret='title')[0]
                    name = client.replaceHTMLCodes(name)

                    if not source_utils.is_match(name, title, hdlr, aliases):
                        continue

                    quality, info = source_utils.get_release_quality(name)
                    try:
                        size = re.findall(r'<b class="cpill .+?-pill">(.+?)</b>', post)[0]
                        dsize, isize = source_utils._size(size)
                    except:
                        dsize, isize = 0.0, ''
                    info.insert(0, isize)

                    info = ' | '.join(info)

                    sources.append({'source': 'Torrent', 'quality': quality, 'language': 'en', 'url': url, 'info': info,
                                    'direct': False, 'debridonly': True, 'size': dsize, 'name': name})
                except:
                    pass

            return sources
        except:
            log_utils.log('bt4g3 - Exception', 1)
            return sources

    def resolve(self, url):
        return url
