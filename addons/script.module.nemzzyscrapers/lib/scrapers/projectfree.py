import requestsimport refrom kodi_six import xbmc, xbmcgui, xbmcaddonfrom six import PY2import resolveurldialog = xbmcgui.Dialog()from bs4 import BeautifulSoupNotice = xbmc.LOGNOTICE if PY2 else xbmc.LOGINFOheaders = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}class Scraper:	def __init__(self):		self.Base = 'https://projectfreetv.fun/series/%s'		self.Search = ('%s')		self.links = []	def Index(self,type, term,year,imdb):		try:			if 'TV' in type:				split = re.findall('(S[0-9].*?E[0-9].)',term)[0].replace('S','season-').replace('E','/episode-')				episodefix = re.findall(r'\d+',split)				for numbers in episodefix:					if numbers.startswith(str('0')): numbers2 = numbers.replace('0','') ; split = split.replace(numbers,numbers2)				showname = term.rsplit('S',1)[0]				showname = showname.strip().replace(' ','-')				link = requests.get(self.Base %showname).text				soup = BeautifulSoup(link, 'html5lib')				movie_containers = soup.findAll(class_='video_title')				searchterm = split				for links in movie_containers:					url = links.a['href']					if not 'https' in url: url = ('https:%s' %url)					if searchterm in url:						link2 = requests.get(url, headers=headers).text						soup = BeautifulSoup(link2, 'html5lib')						movie_containers = soup.findAll(class_='tblimg')						for info in movie_containers:							url = info['href']							title = 'Project Free Tv | SD | ' + term							hmf = resolveurl.HostedMediaFile(url)							if hmf.valid_url():								self.links.append({'title': title, 'url': url, 'quality' : '8', 'Debrid' : False, 'Direct' : False})				if len(self.links) < 1: xbmc.log("No Results From ::: ProjectFree" , level=Notice)				else: return self.links			else: xbmc.log("SCRAPER PROJECTFREE TVSHOWS ONLY  ::: %s" %term.title() , level=Notice)		except Exception as c:				xbmc.log("SCRAPER ERROR ProjectFree  ::: %s" %c , level=Notice)