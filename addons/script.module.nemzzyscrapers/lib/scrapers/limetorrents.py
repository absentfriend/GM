import requestsimport refrom kodi_six import xbmc, xbmcgui, xbmcaddonfrom six import PY2dialog = xbmcgui.Dialog()ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",      "Referer" : "https://www.limetorrents.info/"}Notice = xbmc.LOGNOTICE if PY2 else xbmc.LOGINFOclass Scraper:	def __init__(self):		self.Base = 'https://limetorrents.torrentbay.to/'		self.Search = ('search/movies/%s/seeds/1/')		self.SearchTv = ('search/tv/%s/seeds/1/')		self.links = []	def Index(self,type, term,year,imdb):		try:			if type == 'TV':				MovieName = term				term = term.replace(' ','-')				link = requests.get(self.Base+self.SearchTv %term, headers=ua).text				match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]				pattern = r'''href=['"].*?torrent/(.*?).torrent.*?title=(.*?)['"]'''				getlinks = re.findall(pattern,match)				if not getlinks: return False				for link,name in getlinks:						link2 = ('magnet:?xt=urn:btih:%s&dn=%s' % (link,name))						if 'uhd' in name.lower(): sort = '5' ; qual = '4K UHD'						elif '2160' in name.lower(): sort = '5'; qual = '4K UHD'						elif '1080' in name.lower(): sort = '6'; qual = 'FHD'						elif '720' in name.lower(): sort = '7'; qual = 'HD'						elif 'hdtv' in name.lower(): sort = '7'; qual = 'HD'						else : sort = '8'; qual = 'SD'						title = ('LimeTorrents ( Debrid ) | %s | %s' %(qual,MovieName))						self.links.append({'title': title, 'url': link2, 'quality' : sort, 'Debrid' : True, 'Direct' : False})				if len(self.links) < 1: xbmc.log("No Results From ::: Limetorrents" , level=Notice) 				else: return self.links			else:				MovieName = term				term = term.replace(' ','+')				link = requests.get(self.Base+self.Search %term, headers=ua).text				match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]				pattern = r'''href=['"].*?torrent/(.*?).torrent.*?title=(.*?)['"]'''				getlinks = re.findall(pattern,match)				if not getlinks: return False				for link,name in getlinks:					if year.strip() in name:						link2 = ('magnet:?xt=urn:btih:%s&dn=%s' % (link,name))						if 'uhd' in name.lower(): sort = '5' ; qual = '4K UHD'						elif '2160' in name.lower(): sort = '5'; qual = '4K UHD'						elif '1080' in name.lower(): sort = '6'; qual = 'FHD'						elif '720' in name.lower(): sort = '7'; qual = 'HD'						elif 'hdtv' in name.lower(): sort = '7'; qual = 'HD'						else : sort = '8'; qual = 'SD'						title = ('LimeTorrents ( Debrid ) | %s | %s' %(qual,MovieName))						self.links.append({'title': title, 'url': link2, 'quality' : sort, 'Debrid' : True, 'Direct' : False})				if len(self.links) < 1: xbmc.log("No Results From ::: LimeTorrents" , level=Notice) 				else: return self.links		except Exception as c:				xbmc.log("SCRAPER ERROR LIMETORRENTS  ::: %s" %c , level=Notice)