import requestsimport refrom kodi_six import xbmc, xbmcgui, xbmcaddonfrom six import PY2from bs4 import BeautifulSoupdialog = xbmcgui.Dialog()Notice = xbmc.LOGNOTICE if PY2 else xbmc.LOGINFOua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}class Scraper:	def __init__(self):		self.Base = 'https://torrentgalaxy.to/torrents.php?search=%s#results&sort=seeders&order=desc'		self.Search = ('')		self.links = []	def Index(self,type, term,year,imdb):		try:			if type == 'TV':				MovieName = term				term = term.replace(' ','+')				link = requests.get(self.Base % term.lower(),headers=ua).text				soup = BeautifulSoup(link,'html.parser')				r = soup.find('div', class_={'tgxtable'})				for magnets in r.select('a[href*=magnet]'):					try:						magnet = magnets['href']						if MovieName.lower() in magnet.lower():							if 'uhd' in magnet.lower(): sort = '5' ; qual = '4K UHD'							elif '2160' in magnet.lower(): sort = '5'; qual = '4K UHD'							elif '1080' in magnet.lower(): sort = '6'; qual = 'FHD'							elif '720' in magnet.lower(): sort = '7'; qual = 'HD'							elif 'hdtv' in magnet.lower(): sort = '7'; qual = 'HD'							else : sort = '8'; qual = 'SD'							title = ('[COLOR yellow]Torrent Galaxy ( Debrid ) | %s | %s' % (qual,MovieName))							self.links.append({'title': title, 'url': magnet, 'quality' : sort, 'Debrid' : True, 'Direct' : False})					except: pass				if len(self.links) <= 1: xbmc.log("No Results From ::: TorrentGalaxy" , level=Notice) 				else: return self.links			else:				MovieName = term				term = term.replace(' ','+')				SearchLink = ('%s+%s' % (term,year))				link = requests.get(self.Base % SearchLink,headers=ua).text				soup = BeautifulSoup(link,'html.parser')				r = soup.find('div', class_={'tgxtable'})				for magnets in r.select('a[href*=magnet]'):					magnet = magnets['href']					if MovieName.lower() in magnet.lower():						if 'uhd' in magnet.lower(): sort = '5' ; qual = '4K UHD'						elif '2160' in magnet.lower(): sort = '5'; qual = '4K UHD'						elif '1080' in magnet.lower(): sort = '6'; qual = 'FHD'						elif '720' in magnet.lower(): sort = '7'; qual = 'HD'						else : sort = '8'; qual = 'SD'						title = ('[COLOR yellow]Torrent Galaxy ( Debrid ) | %s | %s' % (qual,MovieName))						self.links.append({'title': title, 'url': magnet, 'quality' : sort, 'Debrid' : True, 'Direct' : False})				if len(self.links) <= 1: xbmc.log("No Results From ::: TorrentGalaxy" , level=Notice) 				else: return self.links		except Exception as c:				xbmc.log("SCRAPER ERROR TorrentGalaxy  ::: %s" %c , level=Notice)