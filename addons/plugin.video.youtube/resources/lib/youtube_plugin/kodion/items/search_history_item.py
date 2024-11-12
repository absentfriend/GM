# -*- coding: utf-8 -*-
"""

    Copyright (C) 2014-2016 bromix (plugin.video.youtube)
    Copyright (C) 2016-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

from __future__ import absolute_import, division, unicode_literals

from . import menu_items
from .directory_item import DirectoryItem
from ..constants import PATHS


class SearchHistoryItem(DirectoryItem):
    def __init__(self, context, query, image=None, fanart=None, location=False):
        if image is None:
            image = '{media}/search.png'

        if isinstance(query, dict):
            params = query
            query = params['q']
        else:
            params = {'q': query}
        if location:
            params['location'] = location

        super(SearchHistoryItem, self).__init__(query,
                                                context.create_uri(
                                                    (PATHS.SEARCH, 'query',),
                                                    params=params,
                                                ),
                                                image=image,
                                                fanart=fanart)

        context_menu = [
            menu_items.search_remove(context, query),
            menu_items.search_rename(context, query),
            menu_items.search_clear(context),
            menu_items.separator(),
            menu_items.search_sort_by(context, params, 'relevance'),
            menu_items.search_sort_by(context, params, 'date'),
            menu_items.search_sort_by(context, params, 'viewCount'),
            menu_items.search_sort_by(context, params, 'rating'),
            menu_items.search_sort_by(context, params, 'title'),
        ]
        self.add_context_menu(context_menu)
