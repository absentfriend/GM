# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, os, json
import main
from resources.lib import monitor
# from contextlib import contextmanager
from datetime import date, datetime, timedelta

addon = main.addon
lasttimecheck = addon.getSetting('lasttimecheck')
latest_version = addon.getAddonInfo('version')
serviceversion = addon.getSetting('service_ver')
if lasttimecheck == '' or lasttimecheck is None:
    lasttimecheck = '2000-01-01 12:00:00.000000'
if serviceversion == '' or serviceversion is None:
    serviceversion = '0.0.0'

age = int(float(addon.getSetting('mininsleep')))
servicelisttostop = []
KODIV = xbmc.getInfoLabel("System.BuildVersion")[:2]
# @contextmanager
# def busy_dialog():
    # xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    # try:
        # yield
    # finally:
        # xbmc.executebuiltin('Dialog.Close(busydialognocancel)')

def isenabled(addonid):
    query = '{ "jsonrpc": "2.0", "id": 1, "method": "Addons.GetAddonDetails", "params": { "addonid": "%s", "properties" : ["name", "thumbnail", "fanart", "enabled", "installed", "path", "dependencies"] } }' % addonid
    addonDetails = xbmc.executeJSONRPC(query)
    details_result = json.loads(addonDetails)
    if "error" in details_result:
        return False
    elif details_result['result']['addon']['enabled'] == True:
        return True
    else:
        return False


if __name__ == '__main__':
    if not addon.getSetting('gkobu_version_fixed') == KODIV:
        from resources.lib import firstrun
        firstrun.gkobu_version_check()
    while xbmc.getCondVisibility("Window.isVisible(yesnodialog)") or xbmc.getCondVisibility("Window.isVisible(okdialog)"):
        if monitor.waitForAbort(3):
            sys.exit()
    xbmc.executebuiltin('Dialog.Close(all,true)')
    xbmc.executebuiltin('ActivateWindow(10000)')
    try:
        timechecked = datetime.strptime(lasttimecheck, '%Y-%m-%d %H:%M:%S.%f')
    except:
        import time
        timechecked = datetime(*(time.strptime(lasttimecheck, '%Y-%m-%d %H:%M:%S.%f')[0:6]))
    if datetime.now() - timechecked > timedelta(minutes=age) or serviceversion != latest_version:
        # with busy_dialog():
            # from resources.lib import set_theoath
            # set_theoath.setTheOathSettings()
        if isenabled('plugin.video.scrubsv2'):
            if not addon.getSetting('set_scrubsv2') == 'false':
                # with busy_dialog():
                    from resources.lib import set_scrubsv2
                    set_scrubsv2.setScrubsSettings()
        if isenabled('plugin.video.fen'):
            if not addon.getSetting('set_fen') == 'false':
                # with busy_dialog():
                    from resources.lib import set_fen
                    set_fen.setFenSettings()
        if isenabled('plugin.video.themoviedb.helper'):
            if not addon.getSetting('set_tmdbhelper') == 'false':
                # with busy_dialog():
                    from resources.lib import set_tmdbhelper
                    set_tmdbhelper.setTMDBhSettings()
        if isenabled('service.subtitles.subtitles.gr'):
            if not addon.getSetting('set_subtitlesgr') == 'false':
                # with busy_dialog():
                    from resources.lib import set_subsgr
                    set_subsgr.setSubsGRSettings()
        if isenabled('plugin.video.seren'):
            if not addon.getSetting('set_seren') == 'false':
                # with busy_dialog():
                    from resources.lib import set_seren
                    set_seren.setSerenSettings()
        if isenabled('plugin.video.AliveGR'):
            if not addon.getSetting('set_alivegr') == 'false':
                # with busy_dialog():
                    from resources.lib import set_alivegr
                    set_alivegr.setAliveGRSettings()
        if isenabled('plugin.video.youtube'):
            if not addon.getSetting('set_youtube') == 'false':
                # with busy_dialog():
                    from resources.lib import set_youtube
                    set_youtube.setYoutubeSettings()
        if not addon.getSetting('set_gui') == 'false':
            # with busy_dialog():
                from resources.lib import set_gui
                set_gui.setguiSettings()
        # with busy_dialog():
        from resources.lib import set_stalker
        set_stalker.setpvrstalker()
        if not addon.getSetting('fix_winner') == 'true':
            if main.addon_remover(['plugin.video.winner','plugin.video.duffyou'], False):
                addon.setSetting('fix_winner', 'true')
        if not addon.getSetting('fix_madtitansports') == 'true':
            if main.addon_remover(['plugin.video.madtitansports'], False):
                addon.setSetting('fix_madtitansports', 'true')
        # with busy_dialog():
        main.reporescue()
        addon.setSetting('lasttimecheck', str(datetime.now()))
        update_toggle = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":"general.addonupdates"}, "id":1}'
        resp_toggle = xbmc.executeJSONRPC(update_toggle)
        toggle = json.loads(resp_toggle)
        if toggle['result']['value'] != 0:
            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
        if monitor.waitForAbort(1):
            sys.exit()
        addon.setSetting('service_ver', latest_version)
        if addon.getSetting('addon.updates.monitor') == 'true':
            xbmc.executebuiltin('RunScript("special://home/addons/service.gkobu.updater/resources/lib/addonupdatesprog.py")')
            # with busy_dialog():
                # addonupdatesprog.progress()
        else:
            xbmc.executebuiltin('UpdateAddonRepos()')
    else:
        update_toggle = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":"general.addonupdates"}, "id":1}'
        resp_toggle = xbmc.executeJSONRPC(update_toggle)
        toggle = json.loads(resp_toggle)
        if toggle['result']['value'] != 0:
            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"general.addonupdates","value":0}}')
        if monitor.waitForAbort(1):
            sys.exit()
        xbmc.executebuiltin('UpdateAddonRepos()')
    if len(servicelisttostop) > 0:
        if monitor.waitForAbort(10):
            sys.exit()
        # with busy_dialog():
        from resources.lib import stopservices
        stopservices.StopAllRunning(servicelisttostop)
