"""
Plugin for ResolveUrl
Copyright (C) 2020 gujal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import re
from resolveurl.plugins.lib import helpers
from resolveurl import common
from resolveurl.resolver import ResolveUrl, ResolverError
from six.moves import urllib_error


class StreamTapeResolver(ResolveUrl):
    name = "streamtape"
    domains = ['streamtape.com']
    pattern = r'(?://|\.)(streamtape\.com)/(?:e|v)/([0-9a-zA-Z]+)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.FF_USER_AGENT,
                   'Referer': 'https://{0}/'.format(host)}
        try:
            r = self.net.http_GET(web_url, headers=headers).content
        except urllib_error.HTTPError:
            raise ResolverError('Video deleted or removed.')
            return
        src = re.search(r'''ById\('.+?=\s*(["']//[^;<]+)''', r)
        if src:
            src_url = ''
            parts = src.group(1).split('+')
            for part in parts:
                p1 = re.findall(r'''['"]([^'"]*)''', part)[0]
                p2 = 0
                if 'substring' in part:
                    subs = part.split(".substring(")
                    for sub in subs:
                        if '&' not in sub:
                            p2 += int(sub[:-1])
                src_url += p1[p2:]
            src_url += '&stream=1'
            src_url = 'https:' + src_url if src_url.startswith('//') else src_url
            return helpers.get_redirect_url(src_url, headers) + helpers.append_headers(headers)
        raise ResolverError('Video cannot be located.')

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://{host}/e/{media_id}')
