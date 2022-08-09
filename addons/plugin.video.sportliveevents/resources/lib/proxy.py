# -*- coding: utf-8 -*-


import threading

import requests


try:  # Python 3
    from http.server import BaseHTTPRequestHandler
except ImportError:  # Python 2
    from BaseHTTPServer import BaseHTTPRequestHandler

try:  # Python 3
    from socketserver import TCPServer
except ImportError:  # Python 2
    from SocketServer import TCPServer


import xbmcaddon, xbmc
addon = xbmcaddon.Addon('plugin.video.sportliveevents')

class Proxy(BaseHTTPRequestHandler):

    server_inst = None

    @staticmethod
    def start():
        """ Start the Proxy. """

        def start_proxy():
            """ Start the Proxy. """
            Proxy.server_inst = TCPServer(('127.0.0.1', 0), Proxy)

            port = Proxy.server_inst.socket.getsockname()[1]
            addon.setSetting('proxyport', str(port))

            Proxy.server_inst.serve_forever()

        thread = threading.Thread(target=start_proxy)
        thread.start()

        return thread

    @staticmethod
    def stop():
        """ Stop the Proxy. """
        if Proxy.server_inst:
            Proxy.server_inst.shutdown()
    def do_HEAD(self):

        self.send_response(200)
        self.end_headers()
    def do_GET(self):  
        path = self.path 
        if 'MLB=' in path:
            try:
                m3u_url = (path).split('MLB=')[-1]
    
                if 'm3u8' in m3u_url:
    
                    result = requests.get(m3u_url, verify=False, timeout = 30).content
                    result = result.decode(encoding='utf-8', errors='strict')
                    mainuri =     addon.getSetting("mainurikey")
                    changedurikey =     addon.getSetting("changedurikey")
    
                    manifest_data = result.replace(mainuri,changedurikey)
    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/x-mpegURL')
                    self.end_headers()
                    self.wfile.write(manifest_data.encode(encoding='utf-8', errors='strict'))
                elif (m3u_url).endswith('.ts'):
                    result=requests.get(m3u_url, verify=False, timeout = 30).content
                
                    self.send_response(200)
                    self.send_header('Content-Type', 'video/mp2t')
                    
                    self.send_header('Content-Length', len(result))
                    self.end_headers()
    
                    self.wfile.write(result)

            except Exception as exc: 
                xbmc.log('blad w proxy: %s'%str(exc), level=xbmc.LOGINFO)
                self.send_response(500)
                self.end_headers()
        
        elif 'LIVEPLY=' in path:
            try:
                m3u_url = (path).split('LIVEPLY=')[-1]
                hea={
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                    'Referer':'https://www.liveply.me/',
                }
                if 'm3u8' in m3u_url:
    
                    result = requests.get(m3u_url, headers=hea, verify=False, timeout = 30).content
                    result = result.decode(encoding='utf-8', errors='strict')
                    mainuri =     'https://'
                    proxyport = addon.getSetting('proxyport')
                    
                    changedurikey ='http://127.0.0.1:{port}/LIVEPLY='.format(port=proxyport)+'https://'
    
                    manifest_data = result.replace(mainuri,changedurikey)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/x-mpegURL')
                    self.end_headers()
                    self.wfile.write(manifest_data.encode(encoding='utf-8', errors='strict'))
                elif 'seckeyserv.me' in m3u_url:
                    
                    from requests.adapters import HTTPAdapter
                    from requests.packages.urllib3.util.ssl_ import create_urllib3_context

                    class KeyAdapter(HTTPAdapter):
                        def init_poolmanager(self, *args, **kwargs):
                            context = create_urllib3_context(ciphers="DEFAULT:!DHE:!SHA1:!SHA256:!SHA384")
                            context.set_ecdh_curve("prime256v1")
                            kwargs["ssl_context"] = context
                            return super(KeyAdapter, self).init_poolmanager(*args, **kwargs)

                    sess = requests.Session()
                    sess.mount("https://key.seckeyserv.me/", KeyAdapter())
                    
                    result = sess.get(m3u_url, headers=hea).content
                    print(result)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/octet-stream')
                    self.end_headers()
                    self.wfile.write(result)
                elif (m3u_url).endswith('.ts'):
                    #result=requests.get(m3u_url, headers=hea, verify=False, timeout = 30).content
                    print()
                    self.send_response(302)
                    #self.send_response(200)
                    self.send_header('Location', m3u_url)
                    self.send_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0')
                    self.send_header('Referer', 'https://www.liveply.me/')
                    #self.send_header('Content-Type', 'video/mp2t')
                    self.end_headers()
                    #self.wfile.write(result)

            except Exception as exc: 
                xbmc.log('blad w proxy: %s'%str(exc), level=xbmc.LOGINFO)
                self.send_response(500)
                self.end_headers()

