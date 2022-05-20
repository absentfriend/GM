# -*- coding: UTF-8 -*-

import sys,re,os
import six
from six.moves import urllib_parse

import requests
from requests.compat import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmc, xbmcvfs
if six.PY3:
	basestring = str
	unicode = str
	xrange = range
	from resources.lib.cmf3 import parseDOM
else:
	from resources.lib.cmf2 import parseDOM
	
from resources.lib import jsunpack
import resolveurl

import json
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = dict(urllib_parse.parse_qsl(sys.argv[2][1:]))
addon = xbmcaddon.Addon(id='plugin.video.tvseriesvideo')

PATH			= addon.getAddonInfo('path')
if six.PY2:
	DATAPATH		= xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
else:
	DATAPATH		= xbmcvfs.translatePath(addon.getAddonInfo('profile'))

RESOURCES	   = PATH+'/resources/'
FANART=RESOURCES+'../fanart.jpg'
if six.PY2:
	napisy = xbmc.translatePath('special://temp/napisy.txt')
else:
	napisy = xbmcvfs.translatePath('special://temp/napisy.txt')


exlink = params.get('url', None)
nazwa= params.get('title', None)
rys = params.get('image', None)

page = params.get('page',[1])[0]

MAIN_URL ='https://www.tvseries.video' 

UA= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
TIMEOUT=15

headers = {'User-Agent': UA,}
sess = requests.Session()
sess2 = requests.Session()
def build_url(query):
	return base_url + '?' + urllib_parse.urlencode(query)

def add_item(url, name, image, mode, itemcount=1, page=1,fanart=FANART, infoLabels=False,contextmenu=None,IsPlayable=False, folder=False):

	if six.PY3:	
		list_item = xbmcgui.ListItem(name)

	else:
		list_item = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
	if IsPlayable:
		list_item.setProperty("IsPlayable", 'True')	
		
	if not infoLabels:
		infoLabels={'title': name}	
	list_item.setInfo(type="video", infoLabels=infoLabels)	
	list_item.setArt({'thumb': image, 'poster': image, 'banner': image, 'fanart': fanart})
	
	if contextmenu:
		out=contextmenu
		list_item.addContextMenuItems(out, replaceItems=True)
	else:
		out = []
		out.append(('Informacja', 'XBMC.Action(Info)'),)
		list_item.addContextMenuItems(out, replaceItems=False)

	xbmcplugin.addDirectoryItem(
		handle=addon_handle,
		url = build_url({'mode': mode, 'url' : url, 'page' : page, 'title':name,'image':image}),			
		listitem=list_item,
		isFolder=folder)
	xbmcplugin.addSortMethod(addon_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE, label2Mask = "%R, %Y, %P")
	
def home():
	add_item('|latest|', 'Latest episodes', 'DefaultTVShows.png', "listmain",fanart=FANART, folder=True)	

	add_item('https://www.tvseries.video/list/A', '[B]TV shows - alphabetical list[/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)	
	add_item('https://www.tvseries.video/genres/Action', '[B]TV shows - genres[/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)	
	add_item('https://www.tvseries.video/networks/abc', '[B]TV shows - networks[/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)	
	add_item('https://www.tvseries.video/years/2022', '[B]TV shows - years[/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)
	
	add_item('|popular|', '[B][COLOR orange]Recently Added Movies[/COLOR][/B]', 'DefaultTVShows.png', "listmain",fanart=FANART, folder=True)	
	add_item('https://www.tvseries.video/movies', '[COLOR orange][B]Movies - all[/COLOR][/B]', 'DefaultTVShows.png', "listmain",fanart=FANART, folder=True)	
	add_item('https://www.tvseries.video/movies/years/2022', '[COLOR orange][B]Movies - years[/COLOR][/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)
	add_item('https://www.tvseries.video/movies/genres/Action', '[COLOR orange][B]Movies - genres[/COLOR][/B]', 'DefaultTVShows.png', "listmenu",fanart=FANART, folder=True)	


	
	
	
	add_item('', '[B][COLOR lightblue]Search[/COLOR][/B]', 'DefaultAddonsSearch.png', "search", folder=True)	
	
	
def ListSearch(url):
	html=getUrlReqOk(url)
	
	result = parseDOM(html,'div', attrs={'class': "row sresultctn"})
	
	links = parseDOM(result,'div', attrs={'class': "card blue-grey.*?"})
	
	
	for link in links:
		try:
			href = parseDOM(link,'a', ret="href")[0]
		except:

			pass
		imag = parseDOM(link,'img', ret="src")[0]
		if 'default' in imag:
			imag = parseDOM(link,'img', ret="data-src")[0]
		href = MAIN_URL + href if href.startswith('/') else href
		imag = MAIN_URL + imag if imag.startswith('/') else imag

		imag = re.sub('\/\d+\.jpg','/300.jpg',imag)
		tyt = re.findall('title">([^<]+)<', link,re.DOTALL+re.I)[0]
		mod = 'listseasons'
		if '/movies/' in href:
			mod = 'getLinks'
		add_item(name=PLchar(tyt), url=href, mode=mod, image=imag, infoLabels={'plot':PLchar(tyt)},folder=True, IsPlayable=False)
	if links:
		xbmcplugin.endOfDirectory(addon_handle)
	else:
		xbmcgui.Dialog().notification('[COLOR red][B]Info[/B][/COLOR]', "[COLOR red][B]0 shows found[/B][/COLOR]", xbmcgui.NOTIFICATION_INFO, 5000)

def ListMain(typ, pg):
	zz= ''

	url = MAIN_URL
	if 'http' in typ:
		url = typ
		if  '?page=' in url:
			url = re.sub('\?page\=\d+', '?page=%d'%int(pg),   url)  
		else:

			url = url+'?page=%d'%int(pg)
		ntpage = re.sub('\?page\=\d+', '?page=%d'%(int(pg)+1),   url)

	html=getUrlReqOk(url)
	lastpage = re.findall('popularctn".*?lastPagev\s*=\s*(\d+)', html, re.DOTALL)
	nextpage = False
	if lastpage:
		lastpage = int(lastpage[0])
		nextpage = True if lastpage > int(pg) else False
	if 'http' in typ:
		result = parseDOM(html,'div', attrs={'class': "popularctn"})[0] 
	else:
		result = parseDOM(html,'div', attrs={'class': "ilatestctn"})[0] if  '|latest|' in typ else parseDOM(html,'div', attrs={'class': "popularctn"})[0] 

	links = parseDOM(result,'div', attrs={'class': "col.*?content"}) 
	
	for link in links:

		href = parseDOM(link,'a', ret="href")[0]
		tyt = parseDOM(link,'span', attrs={'class': "card-title"})[0] 
		imag = parseDOM(link,'img', ret="data-src")[0]
		action = parseDOM(link,'div', attrs={'class': "card-action"})
		
		tyt = tyt+ ' '+action[0] if action else tyt

		href = MAIN_URL + href if href.startswith('/') else href
		imag = MAIN_URL + imag if imag.startswith('/') else imag
		modemy = 'listseasons'
		isplay = False
		fold = True

		if '/movies/' in href:
			modemy = 'getLinks'
		add_item(name=PLchar(tyt), url=href, mode=modemy, image=imag, infoLabels={'plot':PLchar(tyt)},folder=fold, IsPlayable=isplay)
	if nextpage:
		add_item(name='[COLOR blue]>> next page >>[/COLOR]', url=ntpage, mode='listmain', image=imag, infoLabels={'plot':'[COLOR blue]>> next page >>[/COLOR]'},folder=True, IsPlayable=False, page = int(pg)+1)
	if links:
		xbmcplugin.endOfDirectory(addon_handle)

def ListMenu(url):
	html=getUrlReqOk(url)

	result = re.findall('menu".*?<div(.+?)<\/div>', html,re.DOTALL+re.I)[0]

	for href,tytul in re.findall('href="([^"]+)".*?>([^<]+)<', result,re.DOTALL+re.I):
		href = MAIN_URL + href if href.startswith('/') else href
		add_item(name=PLchar(tytul), url=href, mode='listmain', image=rys, infoLabels={'plot':PLchar(tytul)},folder=True, IsPlayable=False)	
	
	xbmcplugin.endOfDirectory(addon_handle)


def ListLinks(url):




	links=getLinks(exlink)
	
	itemz=links
	items = len(links)

	for f in itemz:
		modemy='playLink'
		isplay=True
		fold=False
		add_item(name=f.get('title'), url=f.get('href'), mode=modemy, image=f.get('img'), infoLabels={'code':f.get('code'),'plot':f.get('plot'),'genre':f.get('genre')}, itemcount=items,folder=fold, IsPlayable=isplay)	
	
	
	
	xbmcplugin.setContent(addon_handle, 'movies')	
	xbmcplugin.addSortMethod(addon_handle, sortMethod=xbmcplugin.SORT_METHOD_NONE, label2Mask = "%R, %Y, %P")
	xbmcplugin.endOfDirectory(addon_handle)


def ResetFilters(typ):
	addon.setSetting(typ+'katN','all')
	addon.setSetting(typ+'katV','')
	addon.setSetting(typ+'rokN','all')
	addon.setSetting(typ+'rokV','')
	xbmc.executebuiltin('Container.Refresh')

def getLinks(url):
	
	html=getUrlReqOk(url)
	
	serwery = re.findall('data\-vid1="([^"]+)">([^<]+)<',html,re.DOTALL)
	for href, serw in serwery:
		serw = re.findall('(\d+)',serw,re.DOTALL)[0]
		href = MAIN_URL + href if href.startswith('/') else href
		href = href.replace('&amp;','&')
		add_item(name=nazwa+'- Server '+str(serw), url=href+'|'+url, mode='getserver', image=rys, infoLabels={'plot':nazwa},folder=True, IsPlayable=False)
		
		

	xbmcplugin.endOfDirectory(addon_handle)	

def getVidEmbed(cryptodata):
	import base64
	try:  
		from Cryptodome import Random
		from Cryptodome.Cipher import AES
		from Cryptodome.Util import Padding
	except ImportError:
		from Crypto import Random
		from Crypto.Cipher import AES
		from Crypto.Util import Padding
	password = "25742532592138496744665879883281"
	iv = '9225679083961858'
	BLOCK_SIZE = 16
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
	unpad = lambda s: s[:-ord(s[len(s) - 1:])]
	def encrypt(raw, password, iv):
		private_key = password.encode("utf-8")
		raw = pad(raw)
	
		iv = iv.encode("utf-8")
	
		iv=iv[:16]
		cipher = AES.new(private_key, AES.MODE_CBC, iv)
		return base64.b64encode(cipher.encrypt(raw.encode("utf-8")))
	
	
	def decrypt(enc, password, iv):
		private_key = password.encode("utf-8")
		enc = base64.b64decode(enc)
		
		iv = iv.encode("utf-8")
		cipher = AES.new(private_key, AES.MODE_CBC, iv)
		return unpad(cipher.decrypt(enc))


	decrypted = decrypt(cryptodata, password, iv)
	if six.PY3:
		decrypted = decrypted.decode(encoding='utf-8', errors='strict')
	id,koniec = re.findall('^([^\&]+)(.*?)$',decrypted,re.DOTALL)[0]
	encrypted = encrypt(id, password, iv)
	if six.PY3:
		encrypted = encrypted.decode(encoding='utf-8', errors='strict')
	if encrypted.endswith('='):
		koniec+='none'
	
	


	headers = {
		'Host': 'vidembed.me',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
		'referer': 'https://vidembed.me/',
		'x-requested-with': 'XMLHttpRequest',
		'dnt': '1',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		
		
	}
	
	response = sess2.get('https://vidembed.me/ajax/user/panel', headers=headers, verify=False)
	
	
	nturl = 'https://vidembed.me/encrypt-ajax.php?id='+encrypted+koniec+'&alias='+id
	
	
	
	
	
	headers = {
		'Host': 'vidembed.me',
		
		
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
		'referer': 'https://vidembed.me/',
		'x-requested-with': 'XMLHttpRequest',
		'dnt': '1',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		
		
	}
	
	

	resp = sess2.get(nturl, headers=headers, cookies = sess2.cookies, verify=False).json()
	
	crdata = resp.get('data', None)

	decrypted = decrypt(crdata, password, iv)
	if six.PY3:
		decrypted = decrypted.decode(encoding='utf-8', errors='strict')
	
	jsdata = json.loads(decrypted.replace('"label":"Auto"','"label":"666"'))
	qualities = jsdata.get('source', None)
	ab=max(qualities,key=lambda items:int(items["label"].replace(' P','')))  
	link = ab.get('file', None)+'|User-Agent='+UA+'&Referer=https://vidembed.me/@resolved@'
	return link
	
def decodeJsonCrypto(var_data, tt):
	var_pass = re.findall('var\s*pass\s*=\s*"([^"]+)',tt,re.DOTALL)[0]
	var_pass = var_pass.encode(encoding='utf-8', errors='strict') if six.PY3 else var_pass
	from binascii import unhexlify, hexlify
	
	import base64;
	import hashlib;
    
	try:  
	
		from Cryptodome.Cipher import AES
	
	except ImportError:
	
		from Crypto.Cipher import AES
	

	
	ct = base64.b64decode(var_data.get('ct',None));
	try:
		iv = bytes.fromhex(var_data.get('iv',None));
		salt = bytes.fromhex(var_data.get('s',None));
	except:
		iv = unhexlify(var_data.get('iv',None));
		salt = unhexlify(var_data.get('s',None));
	md = hashlib.md5();

	md.update(var_pass);
	md.update(salt);
	cache0 = md.digest();
	md = hashlib.md5();
	md.update(cache0);
	md.update(var_pass);
	md.update(salt);
	cache1 = md.digest();
	key = cache0 + cache1;
	cipher = AES.new(key, AES.MODE_CBC, iv);
	result = cipher.decrypt(ct);
	if six.PY3:
		result = result.decode(encoding='utf-8', errors='strict')
	result= result.replace('\/','/')

	packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
	packed = packer.findall(result)
	
	
	packed =packed[0]
	zx=''
	unpacked = jsunpack.unpack(packed)
	unpacked = string_escape(unpacked.replace("\\'",'"').replace('\\\\/','/').replace('\\/\\/','//').replace("\\'",'"'))

	src = ''
	try:
		abc = re.findall('load\(({.*?})\);',unpacked,re.DOTALL)[0]
		import calendar
		
		timestampdzis = calendar.timegm(timeNow().timetuple())*1000
		abc2 = string_escape(abc.replace("\\",'').replace('"+Date.now()+"',str(timestampdzis)).replace('"+encodeURI(document.referrer)+"','').replace('sources','"sources"').replace('tracks','"tracks"'))
		
		abc = json.loads(abc2)
		src = abc.get('sources', None)[0].get('file', None)
		src = 'https:' + src if src.startswith('//') else src
		
		src = src.replace('res=360','res=720')
	except:
		pass
	return src
	
	
def timeNow():
	from datetime import datetime
	import time
	now=datetime.utcnow()

	czas=now.strftime('%Y-%m-%d')

	try:
		format_date=datetime.strptime(czas, '%Y-%m-%d')
	except TypeError:
		format_date=datetime(*(time.strptime(czas, '%Y-%m-%d')[0:6]))	

	return format_date	

def getSeriesDatabase(url):
	url,ref = url.split('|')
	headers.update({'Referer': ref})
	html = sess2.get(url, headers=headers, verify=False).text
	
	packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
	packed = packer.findall(html)

	if packed:
	
		packed =packed[0]
		unpacked = jsunpack.unpack(packed)
		unpacked = string_escape(unpacked.replace("\\'",'"'))
		var_data = re.findall('var data="({[^}]+})', unpacked, re.DOTALL)[0]
		
		var_data = json.loads(var_data)
		if 'sojson' in unpacked:
			dt = re.findall('null,"([^"]+)',unpacked,re.DOTALL)[0]
			tt = "".join("".join(chr(int(x))) for x in re.split('[a-zA-Z]', dt))
			abcd = decodeJsonCrypto(var_data, tt)
		#	xbmc.log('@#@tttttttttttttttttttttttttttttttttttttttttt: %s' % str(tt), xbmc.LOGNOTICE)
		#	xbmc.log('@#@CHANNEL-VIDEO-LINK: %s' % str(unpacked), xbmc.LOGNOTICE)
			if abcd:
				xx = sess2.get(abcd, headers=headers, verify=False).url
			
				return xx+'|User-Agent='+UA
			else:
				return ''
	else:
		return url

def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')         
             .decode('unicode-escape') 
             .encode('latin1')         
             .decode(encoding))   
			 
def getServer(url):
	
	url,ref = url.split('|')
	html, resp_url = getUrlReqOk(url, ref = url, content = False)
	
	
	stream_vidembed = ''
	tyt = nazwa.replace('- Server','')
	tak = False
	
	if 'vidembed' in resp_url or '/membed.net/' in resp_url:
		tak=True

		add_item(name=tyt + ' - '+'Main server - vidembed', url=resp_url, mode='playvid', image=rys, infoLabels={'plot':tyt},folder=False, IsPlayable=True)
		hh=re.findall('"linkserver" data\-status="\d+" data\-video="([^"]+)">([^<]+)<',html,re.DOTALL)
		for href,host in hh:
			add_item(name=tyt + ' - '+host, url=href, mode='playvid', image=rys, infoLabels={'plot':tyt},folder=False, IsPlayable=True)
	elif 'vidsrc.me' in resp_url:
		tak=False
		hh=re.findall('data-hash="([^"]+)".*?"name">([^<]+)',html,re.DOTALL)
		sc=''.join(['%s=%s;'%(c.name, c.value) for c in sess.cookies])
		for hash,host in hh:
			tak=True
			href = 'https://source.vidsrc.me/source/'+hash+'|'+sc
		
			add_item(name=tyt + ' - '+host, url=href, mode='playvid', image=rys, infoLabels={'plot':tyt},folder=False, IsPlayable=True)
	
	elif '2embedplayer' in resp_url:
		html = html.replace("\'",'"')

		headersx = {
			'Host': '2embedplayer.net',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://2embedplayer.net',
			'dnt': '1',
			'referer': resp_url,
			'upgrade-insecure-requests': '1',
			'sec-fetch-dest': 'iframe',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',

		}
		
		data = 'button-click=ZEhKMVpTLVF0LVBTLVF0TkRBNExTLVF5TnprdEwtMC1WMk5Ea3dPLTBrM08tMGN3LVBESS01&button-referer='
		
		content = requests.post(resp_url, headers=headersx, data=data,verify=False).content
		if six.PY3:
			content = content.decode(encoding='utf-8', errors='strict')

		headersx = {
			'Host': '2embedplayer.net',
			'user-agent': UA,
			'accept': '*/*',
			'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'x-requested-with': 'XMLHttpRequest',
			'origin': 'https://2embedplayer.net',
			'dnt': '1',
			'referer': resp_url,
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			
			
		}
		toki = re.findall('load_sources\("([^"]+)',content,re.DOTALL)[0]
		data = 'token='+toki
		
		
		content = sess.post('https://2embedplayer.net/response.php', headers=headersx, data=data, verify=False).content
		if six.PY3:
			content = content.decode(encoding='utf-8', errors='strict')

		serwery = re.findall('(data\-id.*?)<\/li>',content,re.DOTALL)
		for serw in serwery:
			
			id=serwid=host=qual = ''
			try:
				id,serwid,host,qual = re.findall('id="([^"]+)".*?server="([^"]+)".*?<\/div>(.*?)<\/div>.*?quality">([^<]+)',serw,re.DOTALL)[0]
			except:
				pass
			if id and serwid and host and qual:
				tak =True
				href = 'https://2embedplayer.net/playvideo.php?video_id=%s&server_id=%s&token=%s&init=1'%(id,serwid,toki)

				hh = nazwa +' - '+host.replace('\n','')
				add_item(name=hh, url=href+'|'+resp_url, mode='playvid', image=rys, infoLabels={'plot':nazwa},folder=False, IsPlayable=True)
		
		
		
	elif 'gomo.to' in resp_url:
		
		if 'Episode not available' in html:
			tak = False
			xbmcgui.Dialog().notification('[COLOR red][B]Info[/B][/COLOR]', "[COLOR red][B]This episode is not available.[/B][/COLOR]", xbmcgui.NOTIFICATION_INFO, 5000)
		else:
			
			
			mirrors = re.findall('data\-value\s*=\s*"([^"]+)"\s*onclick',html,re.DOTALL)
			m = 1
			for x in mirrors:
				hh = nazwa +' - '+'mirror %s'%(str(m))
				href = 'https://gomo.to/show/plan-te-terre/01-06?src='+x
				add_item(name=hh, url=href+'|'+resp_url, mode='playvid', image=rys, infoLabels={'plot':nazwa},folder=False, IsPlayable=True)
				m+=1
				tak = True

	elif 'series.database' in resp_url:
		
		
		result = parseDOM(html,'ul', attrs={'class': "list-server-items"})[0] 
		
		
		main_href = urlparse(resp_url).netloc
		pocz = 'https://'+main_href
		for href,host in re.findall('href="([^"]+)"><li>([^<]+)<',result,re.DOTALL):
			hh = nazwa +' - '+host
			href = 'https:' + href if href.startswith('//') else href
			href = pocz + href if href.startswith('/') else href
			mod = 'getserver'
			fold = True
			ispla = False
			if 'series.database' in href:
				mod = 'playvid'
				fold = False
				ispla = True
			

			
			add_item(name=host, url=href+'|'+resp_url, mode=mod, image=rys, infoLabels={'plot':nazwa},folder=fold, IsPlayable=ispla)	
			tak = True

		
	if tak:
		xbmcplugin.endOfDirectory(addon_handle)	

def ListSeasons(exlink,org_tit):

	episodes =  getEpisodes(exlink)
	
	imag=episodes[0].get('img')
	plot = episodes[0].get('plot')
	seasons =  splitToSeasons(episodes)
	
	for i in sorted(seasons.keys()):
		aa=urllib_parse.quote(str(seasons[i]))
		
	
		add_item(name=i, url=urllib_parse.quote(str(seasons[i])), mode='listEpisodes2', image=imag, infoLabels={'plot':plot}, folder=True)	
	xbmcplugin.endOfDirectory(addon_handle)
	
def splitToSeasons(input):
	out={}
	seasons = [x.get('season') for x in input]
	for s in set(seasons):
		out['Season %02d'%s]=[input[i] for i, j in enumerate(seasons) if j == s]
	return out
def ListEpisodes2(exlink):
	episodes = eval(urllib_parse.unquote(exlink))
	itemz=episodes
	items = len(episodes)
	
	for f in itemz:
		add_item(name=f.get('title'), url=f.get('href'), mode='getLinks', image=f.get('img'), folder=True, infoLabels={'plot':f.get('plot')}, itemcount=items, IsPlayable=False)	
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def ListEpisodes(exlink):
	episodes = getEpisodes(exlink)
	itemz=episodes
	items = len(episodes)
	for f in itemz:
		add_item(name=f.get('title'), url=f.get('href'), mode='getLinks', image=f.get('img'), folder=True, infoLabels={'plot':f.get('title')}, itemcount=items, IsPlayable=False)		
	
	xbmcplugin.endOfDirectory(addon_handle)
	
def getEpisodes(url):
	

	html = getUrlReqOk(url)

	out=[]

	result = parseDOM(html,'div', attrs={'class': "eplist"})[0]

	seasons  = parseDOM(result,'li', attrs={'class': "active"}) 
	
	
	for seas in seasons:

		ses = re.findall('expand_less<\/i>.*?(\d+).*?<',seas,re.DOTALL+re.IGNORECASE)[0]	
		
		episodes = parseDOM(seas,'div', attrs={'class': "stepisode"})
		for episode in episodes:
			epis = re.findall('stepisodenb">.*?(\d+).*?<',episode,re.DOTALL+re.IGNORECASE)

			cdn = parseDOM(episode,'div', attrs={'class': "stepisodelink"})[0]
			href = parseDOM(cdn,'a', ret="href")[0]
			tytul = parseDOM(cdn,'a')[0] 
			jaki = ' - S%02dE%02d'%(int(ses),int(epis[0]))

			href = MAIN_URL + href if href.startswith('/') else href

			jaki = ' - '+PLchar(tytul)+' - S%02dE%02d'%(int(ses),int(epis[0]))

			tyt = nazwa + jaki
			
			plot = re.findall('stssumary"><p>(.*?)<\/p>',html,re.DOTALL+re.IGNORECASE)
			plot = plot [0] if plot else tyt
			plot = re.sub("<[^>]*>","",plot)
			out.append({'title':tyt,'href':href,'img':rys,'plot':plot,'genre':'', 'season' : int(ses),'episode' : int(epis[0]) if epis else '',})
	return out	

def getUrlReqOk(url,ref='', content=True):	

	headersok = {
	'User-Agent': UA,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
	'Connection': 'keep-alive',
	'Referer': ref,}
	
	
	resp=sess.get(url, headers=headersok,verify=False)
	if content:
		content = resp.content
		if six.PY3:
			content = content.decode(encoding='utf-8', errors='strict') 
		return content
	else:
		content = resp.content
		if six.PY3:
			content = content.decode(encoding='utf-8', errors='strict') 
		return content, resp.url
	
def getEmbedplayer(urlref):
	url,ref = urlref.split('|')
	headersx = {
		'Host': '2embedplayer.net',
		'user-agent': UA,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
		'dnt': '1',
		'referer': ref,
		'upgrade-insecure-requests': '1',
		'sec-fetch-dest': 'iframe',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		
		
	}
	content = sess.get(url, headers=headersx, verify=False).content
	if six.PY3:
		content = content.decode(encoding='utf-8', errors='strict') 
	src = re.findall('iframe.*?src\s*=\s*"([^"]+)"\s*scrollin',content,re.DOTALL)
	stream_url = ''

	if src:
	
		src = 'https:' + src[0] if src[0].startswith('//') else src[0]
		import resolveurl
		stream_url = resolveurl.resolve(src)
	return stream_url

def getVidsrc(url):
	zz=''
	
	url,cuk = url.split('|')
	cook = dict(urllib_parse.parse_qsl(cuk))

	headers = {
	
		
		'user-agent': UA,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
	
		'referer': 'https://v2.vidsrc.me/',
	
	}
	
	content = sess.get(url, headers=headers, cookies=cook, verify=False).content
	if six.PY3:
		content = content.decode(encoding='utf-8', errors='strict') 
	content = content.replace("\'",'"')
	

	src = re.findall('src:\s*"([^"]+)"',content,re.DOTALL)[0]
	src = 'https:' + src if src.startswith('//') else src
	resp = sess.get(src, headers=headers, cookies=sess.cookies, verify=False)#.content
	
	resp_url = resp.url
	content=resp.content
	if six.PY3:
		content = content.decode(encoding='utf-8', errors='strict') 
	content = content.replace("\'",'"')
	#if six.PY3:
	#	content = content.decode(encoding='utf-8', errors='strict') 
	#content = content.replace("\'",'"')
	#hls = re.findall('loadSource\("([^"]+)"',content,re.DOTALL)#[0]
	#if hls:
	#	stream_url=hls[0]+'|User-Agent='+UA+'&Referer=https://vidsrc.stream/'
	#else:
	#	src2 = re.findall('src:\s*"([^"]+)"',content,re.DOTALL)[0]
	#	src2 = 'https://v2.vidsrc.me' + src2 if src2.startswith('/') else src2
	#	headers.update({'Referer': src})
	#	resp = sess.get(src2, headers=headers, cookies=sess.cookies, verify=False)
	#	
	#	resp_url = resp.url
	#	content=resp.content
	#	if six.PY3:
	#		content = content.decode(encoding='utf-8', errors='strict') 
	#	content = content.replace("\'",'"')
		
	if 'vidsrc.xyz/v/' in resp_url:
		headers = {
			'Host': 'vidsrc.xyz',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
			'accept': '*/*',
			'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'x-requested-with': 'XMLHttpRequest',
			'origin': 'https://vidsrc.xyz',
			'dnt': '1',
			'referer': resp_url,
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			
			
		}
		
		data = 'r=https%3A%2F%2Fv2.vidsrc.me%2F&d=vidsrc.xyz'
		id = resp_url.split('/v/')[-1]
		
		response = sess.post('https://vidsrc.xyz/api/source/'+id, headers=headers, data=data, verify=False).json()
		qualities = response.get("data", None)
		ab=max(qualities,key=lambda items:int(items["label"].replace('p','')))  
		stream_url = ab.get('file', None)+'|User-Agent='+UA+'&Referer=https://vidsrc.xyz/@resolved@'
	
	elif 'vidsrc.stream/pro' in resp_url:
	
		path = re.findall('var path = "(\/\/.*?)"',content,re.DOTALL)[0]
		path = 'https:' + path if path.startswith('/') else path
		
		
		host = urlparse(path).netloc
		headersx = {
			'Host': host,
			'user-agent': UA,
			'accept': '*/*',
			'accept-language': 'pl,en-US;q=0.7,en;q=0.3',
			'origin': 'https://vidsrc.stream',
			'dnt': '1',
			'referer': 'https://vidsrc.stream/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			
			
		}
		contentx = sess.get(path, headers=headersx, verify=False).content
		
		stream_url = re.findall('loadSource\("([^"]+)"',content,re.DOTALL)[0]
		#stream_url = re.findall('"file"\:\s*"([^"]+)"',content,re.DOTALL)[0]
		stream_url+='|User-Agent='+UA+'&Referer=https://vidsrc.stream/'
	else:
	
	
		import resolveurl
		stream_url = resolveurl.resolve(resp_url)
	return stream_url

def getGomoto(link):
	zz=''
	headersx = {
    
    'User-Agent':UA,
    'Accept': '*/*',
    'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',}

	html = sess2.get(link, headers=headersx, verify=False).content
	if six.PY3:
		html = html.decode(encoding='utf-8', errors='strict')
	html = html.replace("\'",'"')

	tc = re.findall('var\s*tc\s*=\s*"([^"]+)"',html,re.DOTALL)
	if tc:
		
		
		_token = re.findall('"\_token"\:\s*"([^"]+)"',html,re.DOTALL)[0]
		tokenCode = tc[0]
		
		x_token = tokenCode[5:22][::-1]+ "22" + "593860"
		data = 'tokenCode='+tokenCode+'&_token='+_token
	headersx.update({'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','x-token':x_token,'Referer': link})
	
	response = sess2.post('https://gomo.to/decoding_v3.php', headers=headersx, verify=False, data=data).json()
	src = response[0]
	resp_url = sess2.get(src, headers=headersx, verify=False).url
	stream_url =''
	try:
		import resolveurl
		stream_url = resolveurl.resolve(resp_url)
	except:	
		pass
	return stream_url
	
def PlayVid(exlink):
	exc = None

	link = exlink
	if 'vidsrc.me' in link:
		link = getVidsrc(link)
	elif '2embedplayer' in link:
		link = getEmbedplayer(link)
	elif 'gomo.to' in link:
		link = getGomoto(link)
	elif 'series.database' in link:
		link = getSeriesDatabase(link)
		
		
	else:	
	
		
		
		try:
			
			link = resolveurl.resolve(link)
			dfsfs=''
		except Exception as error:
			
			link = None
			pass
	
	if link:
		
		
			
		link = link.replace('@resolved@','')
		play_item = xbmcgui.ListItem(path=link)
		xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)	
	else:
		msg = "[COLOR red][B]This video doesn't exists in our servers or has been deleted.[/B][/COLOR]"
		msg = exc if exc else msg
		xbmcgui.Dialog().notification('[COLOR red][B]Error[/B][/COLOR]', msg, xbmcgui.NOTIFICATION_INFO, 5000)

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
	char = char.replace('&#8222;','"').replace('&#8221;','"')	
	char = char.replace('[&hellip;]',"...")
	char = char.replace('&#038;',"&").replace('&#38;',"&")
	char = char.replace('&#039;',"'").replace('&#39;',"'")
	char = char.replace('&quot;','"').replace('&oacute;','ó').replace('&rsquo;',"'")
	char = char.replace('&nbsp;',".").replace('&amp;','&').replace('&eacute;','e')
	return char	
def PLcharx(char):
	char=char.replace("\xb9","ą").replace("\xa5","Ą").replace("\xe6","ć").replace("\xc6","Ć")
	char=char.replace("\xea","ę").replace("\xca","Ę").replace("\xb3","ł").replace("\xa3","Ł")
	char=char.replace("\xf3","ó").replace("\xd3","Ó").replace("\x9c","ś").replace("\x8c","Ś")
	char=char.replace("\x9f","ź").replace("\xaf","Ż").replace("\xbf","ż").replace("\xac","Ź")
	char=char.replace("\xf1","ń").replace("\xd1","Ń").replace("\x8f","Ź");
	return char	
	
	
def router(paramstring):
	params = dict(urllib_parse.parse_qsl(paramstring))
	if params:	
		mode = params.get('mode', None)

		if mode =="listmain":
			ListMain(exlink, page)
		elif mode =="listmenu":
			ListMenu(exlink)
			
		elif mode == 'getserver':
			getServer(exlink)
			
		elif mode =="listmovies":
			ListSubsMov(exlink,page)

		elif mode == 'getLinks':

			getLinks(exlink)
		elif mode == 'playvid':
			PlayVid(exlink)	

		elif mode == 'listseasons':
		
			ListSeasons(exlink,nazwa)
		elif mode == 'listEpisodes2':
			ListEpisodes2(exlink)
		
		
		elif mode == 'listepisodes':
			ListEpisodes(exlink)	
		elif mode=='search':
			query = xbmcgui.Dialog().input(u'Search...', type=xbmcgui.INPUT_ALPHANUM)
			if query:	  
				query=query.replace(' ','+')
				ListSearch('https://www.tvseries.video/searchshow?name='+query)
			else:
				pass
	else:
		home()
		xbmcplugin.endOfDirectory(addon_handle)	
if __name__ == '__main__':
	router(sys.argv[2][1:])