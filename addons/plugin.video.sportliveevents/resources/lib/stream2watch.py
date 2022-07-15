# -*- coding: UTF-8 -*-

import sys,re, ast 
import six
from six.moves import urllib_parse

import requests
from requests.compat import urlparse

import datetime
import time

from resources.lib.brotlipython import brotlidec
if sys.version_info >= (3,0,0):
	import html as html
	from resources.lib.cmf3 import parseDOM
else:
	from resources.lib.cmf2 import parseDOM
	import HTMLParser
	html = HTMLParser.HTMLParser()
sess = requests.Session()

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'

main_url = 'https://tv.xn--tream2watch-i9d.com'
headers = {'user-agent': UA,}


def resp_text(resp):
	"""Return decoded response text."""
	if resp and resp.headers.get('content-encoding') == 'br':
		out = []
		# terrible implementation but it's pure Python
		return brotlidec(resp.content, out).decode('utf-8')
	response_content = resp.text

	return response_content.replace("\'",'"')
	
	
def request_sess(url, method='get', data={}, headers={}, result=True, json=False, allow=True , json_data = False):
	if method == 'get':
		resp = sess.get(url, headers=headers, timeout=15, verify=False, allow_redirects=allow)
		
	elif method == 'post':
		if json_data:
			resp = sess.post(url, headers=headers, json=data, timeout=15, verify=False, allow_redirects=allow)
		else:
			resp = sess.post(url, headers=headers, data=data, timeout=15, verify=False, allow_redirects=allow)

	if result:
		return resp.json() if json else resp_text(resp)
	else:
		return resp


def get_delta():

	local = datetime.datetime.now()
	utc =  datetime.datetime.utcnow()
	delta = (int((local - utc).days * 86400 + round((local - utc).seconds, -1)))/3600
	return delta
	
def getRealTime(godzina, minus=-1):

	delta = get_delta()
	try:
		date_time_obj=datetime.datetime.strptime(godzina, '%H:%M')+ datetime.timedelta(hours=minus)
	except TypeError:
		date_time_obj=datetime.datetime(*(time.strptime(godzina, '%H:%M')[0:6]))+ datetime.timedelta(hours=minus)
	date_time_obj = date_time_obj+ datetime.timedelta(hours=int(delta))

	return date_time_obj.strftime("%H:%M")
		
def ListMenu():
	return [{'title':'Channels','href':'kanal','image':'x','plot':'Stream2watch - channels', 'mode':'listchannels:stream2watch'}, {'title':'Schedule','href':'dzien','image':'x','plot':'Cricfree - schedule', 'mode':'listschedule:stream2watch'}]

def ListSchedule(url):
	zz=''
	out=[]
	if 'dzien' in url:
		nturl = main_url
	else:
		nturl = url

	srt = False
	html = request_sess(nturl, 'get', headers=headers)
	if 'dzien' in url:
		html = parseDOM(html,'div', attrs={'class': "dropdown.*?"})[0]##
	#	for href,title in re.findall('href="([^"]+)".*?<\/span>([^<]+)<', html,re.DOTALL):
		for href,title in re.findall('href="([^"]+)">([^<]+)<', html,re.DOTALL):

			if title.lower() == 'tv':
				continue
			elif href =='/':
				continue
			out.append({'title':title,'href':main_url+href,'image':title, 'empty':'false','mode':'listschedule:stream2watch'})
	else:
		srt = True
		html = parseDOM(html,'tbody')[0]
		ids = [(a.start(), a.end()) for a in re.finditer('<tr class="stream-box"', html)]
		ids.append( (-1,-1) )
		
		
		for i in range(len(ids[:-1])):
			item = html[ ids[i][1]:ids[i+1][0] ]
			if re.findall('data\-islive="([^"]+)"',item,re.DOTALL):
				image = parseDOM(item, 'img', ret='src')[0]
				title = parseDOM(item, 'p')[1].replace('/n','')
	
				href = parseDOM(item, 'a', ret='href')[0]
				czas = parseDOM(item,'span', attrs={'class': "stream-live"})[0]
				title = czas+' ' +title
				title = 'z'+ title if title.startswith(('00:','01:','02:','03:')) else title  
				
				out.append({'title':title,'href':href, 'image':image}) 
	if srt and out:
		out = PosortujData(out)

	return out	
	
def PosortujData(out):
	outx=[]
	out = sorted(out, key=lambda x: x.get('title', None))
	for t in out:

		title=html.unescape(t.get('title', None)).replace('z0','0')
		czas=re.findall('(.+?)\s',title,re.DOTALL)[0]

		godz = getRealTime(czas, minus = -1)
		title = title.replace(czas,'[COLOR khaki]'+godz+'[/COLOR]')
		outx.append({'title':title,'href':t.get('href', None),'image':t.get('image', None),'empty':'false','mode':'getlinks:stream2watch'})
	return outx	
	
def ListChannels(url):
	out=[]
	
	
	
	html = request_sess('https://tv.xn--tream2watch-i9d.com/tv-channels/', 'get', headers=headers)	

	result = parseDOM(html,'div', attrs={'class': "layouts-page-content"})[0]

	if 'kanal' in url:
		for chan in parseDOM(result,'h2'):

			titlecateg = re.findall('<strong>([^<]+)<',chan,re.DOTALL)[0]
			out.append({'title':titlecateg,'href':urllib_parse.quote(titlecateg),'mode':'listchannels:stream2watch','image':'channels'})
	else:
		channels = result.split('<h2>')
		kateg = urllib_parse.unquote(url)
		
		for chan in channels:
			if kateg.lower() in chan.lower():
				for href,imag,title in re.findall('href="([^"]+)"><.*?src="([^"]+)".*?>([^<]+)<\/a><\/span><', chan,re.DOTALL):
					href = main_url+href if href.startswith('/') else href
					imag = main_url+imag if imag.startswith('/') else imag

					out.append({'title':title,'href':href,'mode':'getlinks:stream2watch','image':imag})

	return out

def GetLinks(url):
	zz=''
	out=[]
	html = request_sess(url, 'get', headers=headers)

	maintitle = re.findall('data\-title\s*=\s*"([^"]+)"',html,re.DOTALL)[0]
	result =  parseDOM(html,'div', attrs={'class': "stream-box-sources-list"})[0]
	links = parseDOM(result,'span', attrs={'class': "stream-source-stream-title"}) 

	for link in links :
		href = re.findall('href="([^"]+)"',link,re.DOTALL)[0]

		if '/frames/' in href:
			continue
		title = re.findall('^([^<]+)<',link,re.DOTALL)[0]
		title = '[B]'+maintitle +' - [COLOR orange]'+title+'[/COLOR][/B]'
		image = parseDOM(link, 'img', ret='src')[0]
		out.append({'title':title,'href':href,'mode':'playvid:stream2watch','image':image})
	
	return out
	
def GetVid(url):

	video_url = ''
	html = request_sess(url, 'get', headers=headers)
	host = urlparse(url).netloc
	iframe = parseDOM(html, 'iframe', ret='src')#[0]
	if iframe:
		headers.update({'referer': url})
		nturl = 'http://'+host+iframe[0]
		html = request_sess(nturl, 'get', headers=headers)

		playstream= re.findall('"iframe"\,"([^"]+)"',html, re.DOTALL)
		if playstream:
			
			headers.update({'referer': nturl})
			playstream_url = playstream[0].strip(' ')
			html = request_sess(playstream_url, 'get', headers=headers)

			video_url = ''
			fid = re.findall('fid="([^"]+)"', html,re.DOTALL)
			
			if 'ragnaru.net' in html:
				if fid:
					nturl = 'https://ragnaru.net/jwembed.php?player=desktop&live='+fid[0]
					headers.update({'referer': playstream_url})
					html = request_sess(nturl, 'get', headers=headers)
					video_url = re.findall('file\:\s*"([^"]+)"',html,re.DOTALL)
					if video_url:
						video_url = video_url[0]+ '|User-Agent={ua}&Referer={ref}'.format(ref=nturl,ua=UA)
			elif 'daddylive' in playstream_url:

				from resources.lib import daddy 
				video_url = daddy.GetVid(playstream_url)
			elif 'wikisport.' in playstream_url:
				vid = re.findall('new Clappr\.Player.*?source\:\s*"([^"]+)"',html,re.DOTALL)

				if vid:
					if 'googleusercontent.com/gadgets/proxy' in vid[0]:
						video_url = vid[0].split('url=')[-1]+ '|User-Agent={ua}&Referer={ref}'.format(ref=playstream_url,ua=UA)
					else:
						video_url = vid[0]+ '|User-Agent={ua}&Referer={ref}'.format(ref=playstream_url,ua=UA)
			elif 'eplayer.click/' in html:
				from resources.lib import klubsports #as mod
				iframe = re.findall('iframe src="([^"]+)"', html,re.DOTALL)[0]
				
				video_url = klubsports.GetVid(iframe)
				
			else:
				try:
					nturl = re.findall('iframe src="([^"]+)"',html,re.DOTALL)[0]
					headers.update({'referer': playstream_url})
					resp = request_sess(nturl, 'get', headers=headers, result=False)
					html = resp.text
					packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
					packeds = packer.findall(html)
					unpacked = ''
			
					if packeds:
						import resources.lib.jsunpack as jsunpack
						for packed in packeds:
							unpacked += jsunpack.unpack(packed)
					video_url = re.findall('var src="([^"]+)"',unpacked,re.DOTALL)
					if video_url:
						video_url = video_url[0]+ '|User-Agent={ua}&Referer={ref}'.format(ref=nturl,ua=UA)
				except:
					pass
	return video_url
