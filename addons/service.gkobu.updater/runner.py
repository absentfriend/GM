# -*- coding: utf-8 -*-
import xbmc, xbmcaddon, os, json
import main
from resources.lib import set_fen, set_theoath, set_tmdbhelper, set_subsgr, set_seren, set_alivegr, set_youtube, set_gui, set_stalker, monitor, addonupdatesprog, stopservices
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

# @contextmanager
# def busy_dialog():
    # xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    # try:
        # yield
    # finally:
        # xbmc.executebuiltin('Dialog.Close(busydialognocancel)')



if __name__ == '__main__':
    if not addon.getSetting('gkobu_version_fixed') == 'true':
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
            # set_theoath.setTheOathSettings()
        if not addon.getSetting('set_fen') == 'false':
            # with busy_dialog():
                set_fen.setFenSettings()
        if not addon.getSetting('set_tmdbhelper') == 'false':
            # with busy_dialog():
                set_tmdbhelper.setTMDBhSettings()
        if not addon.getSetting('set_subtitlesgr') == 'false':
            # with busy_dialog():
                set_subsgr.setSubsGRSettings()
        if not addon.getSetting('set_seren') == 'false':
            # with busy_dialog():
                set_seren.setSerenSettings()
        if not addon.getSetting('set_alivegr') == 'false':
            # with busy_dialog():
                set_alivegr.setAliveGRSettings()
        if not addon.getSetting('set_youtube') == 'false':
            # with busy_dialog():
                set_youtube.setYoutubeSettings()
        if not addon.getSetting('set_gui') == 'false':
            # with busy_dialog():
                set_gui.setguiSettings()
        # with busy_dialog():
        set_stalker.setpvrstalker()
        if not addon.getSetting('fix_winner') == 'true':
            if main.addon_remover(['plugin.video.winner','plugin.video.duffyou'], True):
                addon.setSetting('fix_winner', 'true')
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
        if main.addon.getSetting('addon.updates.monitor') == 'true':
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
        stopservices.StopAllRunning(servicelisttostop)
