# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
#Nouvelle source de streaming FILMS ET SÉRIES
import re

from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import siteManager
from resources.lib.util import cUtil


#URL_MAIN='https://filmoflix.dad/'
SITE_IDENTIFIER = 'filmoflix'
SITE_NAME = 'FilmoFlix'
SITE_DESC = 'FilmoFlix est un site pour regarder des films et séries en streaming en qualité HD'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

key_search_movies = '#searchsomemovies'
key_search_series = '#searchsomeseries'

# Pour les Films
MOVIE_NEWS = ('film/', 'showMovies')
MOVIE_GENRES = ('film/', 'showGenres')
MOVIE_ANNEES = (True, 'showMovieYears')

# Pour les Series
SERIE_NEWS = ('serie/', 'showMovies')
SERIE_GENRES = ('serie/', 'showSeriesGenres')
SERIE_VF = ('serie/series-vf/', 'showMovies')
SERIE_VOSTFR = ('serie/series-vostfr/', 'showMovies')
SERIE_ANNEES = (True, 'showSerieYears')

URL_SEARCH = ('index.php?do=search', 'showMovies')
URL_SEARCH_MOVIES = (key_search_movies, 'showMovies')
URL_SEARCH_SERIES = (key_search_series, 'showMovies')

# recherche utilisé quand on n'utilise pas le globale
MY_SEARCH_MOVIES = (True, 'showSearchMovie')
MY_SEARCH_SERIES = (True, 'showSearchSerie')

# Menu GLOBALE HOME
MOVIE_MOVIE = (True, 'showMenuMovies')
SERIE_SERIES = (True, 'showMenuTvShows')


def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showMenuMovies', 'Films', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showMenuTvShows', 'Séries', 'series.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    

def showMenuMovies():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)


    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_ANNEES[1], 'Films (Années)', 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMenuTvShows():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Séries', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Série (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ANNEES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_ANNEES[1], 'Séries (Années)', 'annees.png', oOutputParameterHandler)

     
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Séries (VF)', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Série (VOSTFR)', 'vostfr.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearchSerie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = key_search_series + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSearchMovie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = key_search_movies + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showGenres():
    oGui = cGui()
    listegenre = [['Action', 'action'], ['Animation', 'animation'], ['Aventure', 'aventure'],
                  ['Biopic', 'biopic'], ['Comédie', 'comedie'], ['Documentaire', 'documentaire'],
                  ['Drame', 'drame'], ['Famille', 'famille'], ['Fantastique', 'fantastique'],
                  ['Guerre', 'guerre'], ['Historique', 'historique'], ['Epouvante et Horreur', 'epouvante-horreur'],
                  ['Espionnage', 'espionnage'], ['Policier', 'policier'], ['Romance', 'romance'],
                  ['Science-Fiction', 'science-fiction'], ['Thriller', 'thriller'], ['western', 'western']]

    oOutputParameterHandler = cOutputParameterHandler()
    for sTitle, sUrl in listegenre:
        oOutputParameterHandler.addParameter('siteUrl', 'film/' + sUrl)
        oGui.addGenre(SITE_IDENTIFIER, 'showMovies', sTitle, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMovieYears():
    import datetime
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    for i in reversed(range(1955, int(datetime.datetime.now().year) + 1)):
        sYear = str(i)
        oOutputParameterHandler.addParameter('siteUrl', 'film/annee/' + sYear)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sYear, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    
def showSeriesGenres():
    oGui = cGui()
    listegenre = [['Action', 'action-s'], ['Animation', 'animation-s'], ['Aventure', 'aventure-s'], ['Biopic', 'biopic-s'], ['Comédie', 'comedie-s'],
             ['Documentaire', 'documentaire-s'], ['Drame', 'drame-s'], ['Famille', 'famille-s'],
             ['Fantastique', 'fantastique-s'], ['Guerre', 'guerre-s'], ['Historique', 'historique-s'], ['Horreur', 'horreur-s'],
             ['Judiciaire', 'judiciare-s'], ['Musique', 'musical-s'], ['Policier', 'policier-s'], ['Romance', 'romance-s'],
             ['Science-Fiction', 'science-fiction-s'], ['Thriller', 'thriller-s'],['western', 'western-s']]

    oOutputParameterHandler = cOutputParameterHandler()
    for sTitle, sUrl in listegenre:
        oOutputParameterHandler.addParameter('siteUrl', 'serie/' + sUrl)
        oGui.addGenre(SITE_IDENTIFIER, 'showMovies', sTitle, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSerieYears():
    import datetime
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    for i in reversed(range(1959, int(datetime.datetime.now().year) + 1)):
        sYear = str(i)
        oOutputParameterHandler.addParameter('siteUrl', 'serie/annee/' + sYear)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sYear, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    bSearchMovie = False
    bSearchSerie = False

    if sSearch:
        oUtil = cUtil()
        if key_search_movies in sSearch:
            sSearch = sSearch.replace(key_search_movies, '')
            bSearchMovie = True
        if key_search_series in sSearch:
            sSearch = sSearch.replace(key_search_series, '')
            bSearchSerie = True
        sSearchText = oUtil.CleanName(sSearch)
        sSearch = sSearch.replace(' ', '+').replace('%20', '+')

        pdata = 'do=search&subaction=search&story=' + sSearch
#        pdata = 'do=search&subaction=search&search_start=0&full_search=0&result_from=1&story=' + sSearch
        oRequest = cRequestHandler(URL_MAIN + URL_SEARCH[0])
        oRequest.setRequestType(1)
        oRequest.addHeaderEntry('Referer', URL_MAIN)
        oRequest.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        oRequest.addHeaderEntry('Accept-Language', 'fr-FR,fr;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6')
        oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
        oRequest.addParametersLine(pdata)
        sHtmlContent = oRequest.request()

        # lien thumb titre year 
        sPattern = '<div class="th-item">.+?href="([^"]+)".+?src="([^"]+)" alt="([^"]+)".+?Date de sortie:<\/span> (\d+)'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        if not'http' in sUrl:
            sUrl = URL_MAIN + sUrl  # dépend de la pagination
        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('Referer', URL_MAIN)
        sHtmlContent = oRequest.request()

        # lien thumb titre 
        sPattern = '<div class="th-item">.+?href="([^"]+)".+?src="([^"]+)" alt="([^"]+)"'

    aResult = oParser.parse(sHtmlContent, sPattern)
   
    if aResult[0]:
        sYear = ''
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            if sSearch:
                sYear = aEntry[3]
            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb
            sTitle = aEntry[2]
            if bSearchMovie:
                if '/serie' in sUrl2:
                    continue
            if bSearchSerie:
                if '/serie' not in sUrl2:
                    continue

            if sSearch:
                if not oUtil.CheckOccurence(sSearchText, sTitle):
                    continue  # Filtre de recherche

            sDisplayTitle = sTitle
            if sSearch and not bSearchMovie and not bSearchSerie:
                mark1 = 'Série' #pour marquer (tag) les séries lors du résultat de recherche global
                mark2 = 'Film'  #pour marquer (tag) les films lors du résultat de recherche global
                
                if '/serie' in sUrl2:
                    sDisplayTitle =('%s (%s)') % (sDisplayTitle, mark1)       #marquage de series 
                else:
                    sDisplayTitle =('%s (%s)') % (sDisplayTitle, mark2)       #marquage de films

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)

            if '/serie' not in sUrl2:
                oGui.addMovie(SITE_IDENTIFIER, 'showMovieLinks', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addTV(SITE_IDENTIFIER, 'showSaisons', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)

    else:
        oGui.addText(SITE_IDENTIFIER)

    if not sSearch:
        sNextPage, sPaging = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', 'Page ' + sPaging, oOutputParameterHandler)

        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = 'navigation.+?<span>\d+</span> <a href="([^"]+).+?>([^<]+)</a></div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sNextPage = aResult[1][0][0]
        sNumberMax = aResult[1][0][1]
        sNumberNext = re.search('page/([0-9]+)', sNextPage).group(1)
        sPaging = sNumberNext + '/' + sNumberMax
        return sNextPage, sPaging

    return False, 'none'

# afficher les Saisons
def showSaisons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sDesc = ''
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = '<div class="saisontab clearfix"'
    sEnd = '<div class="full-ser-keywords">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = '<a class="th-in" href="([^"]*)".*?data-src="([^"]*)".*?class="th-title nowrap">(.+?)</div'
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in reversed(aResult[1]):

            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb
            sSaison = aEntry[2]  # SAISON 2
            

            sTitle = ("%s %s") % (sMovieTitle, sSaison)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)

            oGui.addSeason(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        oGui.addText(SITE_IDENTIFIER)

    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<a href="([^"]*)">\s*<div class="fsa-ep">(.+?)\s*<span'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sUrl2 = aEntry[0]
            
            sEpisode = aEntry[1].replace('é', 'e').strip()
            if 'http' not in sUrl2:
                sUrl2 = URL_MAIN[:-1] + sUrl2
            sTitle = sMovieTitle + '' + sEpisode

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addEpisode(SITE_IDENTIFIER, 'showSerieLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        oGui.addText(SITE_IDENTIFIER)

    oGui.setEndOfDirectory()


def showSerieLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')

    oParser = cParser()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

#    sPattern = "class=\"lien.+?playEpisode.+?\'([^\']*).+?'([^\']*)"
    sPattern = "getxfield\(this, '(\d+)', '(.+?)'"
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            videoId = aEntry[0]
            xfield = aEntry[1]

            hosterName = sLang = ''
            oHoster = None  # Initialisation en dehors de la boucle

            if '_' in xfield:
                hosterName, sLang = xfield.strip().split('_')
                sLang = sLang.upper()
            else:
                hosterName = xfield.strip()

            oHoster = cHosterGui().checkHoster(hosterName)

            if not oHoster:
                continue

            # Ajouter cette logique
            if not sLang:
                sLang = 'VF'

            sDisplayTitle = ('%s (%s) [COLOR coral]%s[/COLOR]') % (sTitle, sLang, hosterName)
            
            postdata = 'id=' + videoId + '&xfield=' + xfield + '&action=playEpisode'
            sUrl2 = URL_MAIN + 'engine/inc/serial/app/ajax/Season.php'


            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            oOutputParameterHandler.addParameter('postdata', postdata)

            oGui.addLink(SITE_IDENTIFIER, 'showSerieHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    cook = oInputParameterHandler.getValue('cook')
    postdata = oInputParameterHandler.getValue('postdata')

    oRequest = cRequestHandler(sUrl)
    oRequest.setRequestType(1)
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    oRequest.addHeaderEntry('Cookie', cook)
    oRequest.addParametersLine(postdata)
    sHtmlContent = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe src=\"([^\"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sHosterUrl = aResult[1][0]
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


def showMovieLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    cook = oRequestHandler.GetCookies()

    oParser = cParser()
    sPattern = 'property="og:description".+?content="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = ''
    if aResult[0]:
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis : ', aResult[1][0])
    sStart = '<ul class="player-list">'
    sEnd = '<div class="full-ser-keywords">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    sPattern = "lien fx-row.+?\"getxfield.+?(\d+).+?\'([^\']*).+?'([^\']*).+?pl-5\">([^<]+)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            videoId = aEntry[0]
            xfield = aEntry[1]
            sQual = aEntry[3]
            token = aEntry[2]
            hosterName = sLang = ''
            oHoster = None  # Initialisation en dehors de la boucle

            if '_' in xfield:
                hosterName, sLang = xfield.strip().split('_')
                sLang = sLang.upper()
            else:
                hosterName = xfield.strip()

            oHoster = cHosterGui().checkHoster(hosterName)

            if not oHoster:
                continue

            # Ajouter cette logique
            if not sLang and '_vostfr' not in xfield:
                sLang = 'VF'
               
            sUrl2 = URL_MAIN + 'engine/ajax/getxfield.php?id=' + videoId + '&xfield=' + xfield + '&token=' + token

            sDisplayTitle = ('%s [%s] (%s) [COLOR coral]%s[/COLOR]') % (sTitle, sQual, sLang, hosterName)

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sQual', sQual)
            oOutputParameterHandler.addParameter('referer', sUrl)
            oOutputParameterHandler.addParameter('cook', cook)
            
            oGui.addMovie(SITE_IDENTIFIER, 'showMovieHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    referer = oInputParameterHandler.getValue('referer')
    cook = oInputParameterHandler.getValue('cook')
    postdata = oInputParameterHandler.getValue('postdata')

    oRequest = cRequestHandler(sUrl)
    oRequest.setRequestType(1)
    oRequest.addHeaderEntry('Referer', referer)
    oRequest.addHeaderEntry('Content-Type', 'application/x-www-form-urlencoded')
    oRequest.addHeaderEntry('Cookie', cook) 
    oRequest.addParametersLine(postdata)
    sHtmlContent = oRequest.request()

    oParser = cParser()
    sPattern = '<iframe src=\"([^\"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sHosterUrl = aResult[1][0]
        oHoster = cHosterGui().checkHoster(sHosterUrl)
        if oHoster:
            oHoster.setDisplayName(sMovieTitle)
            oHoster.setFileName(sMovieTitle)
            cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
