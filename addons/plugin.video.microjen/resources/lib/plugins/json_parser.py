from ..plugin import Plugin
import json
import xbmc,xbmcgui

class json_parser(Plugin):
    name = "json_parser"
    description = "add json format support"
    priority = 0

    def parse_list(self, url: str, response):
        if url.endswith(".json") or url.endswith(".zip") or '"items": [' in response :
            response = "".join([s for s in response.strip().splitlines(True) if s.strip()])#remove empty lines from response
            if not response.startswith('{'):
                response = '{'+response
            if not response.endswith('}'):
                response = response+'}'
            try:
                return json.loads(response)["items"]
            except:
                xbmc.log(f"invalid json: {response}", xbmc.LOGINFO)
                return [
                        { 
                            "title": "[COLOR khaki]Ρυθμίσεις Microjen[/COLOR]", 
                            "type": "item", 
                            "link": "settings"
                        }, 
                        {
                            "type": "item",
                            "title": "[COLOR khaki]Clear Cache[/COLOR]",
                            "link": "clear_cache_silent"
                        }, 
                        ]

