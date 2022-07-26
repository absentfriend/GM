# -*- coding: utf-8 -*-

'''
    Tulip library
    Author Twilight0

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
'''

from tulip.compat import range, urlencode, parse_qsl


def percent(count, total):

    return min(int(round(count * 100 / total)), 100)


def enum(**enums):

    try:
        return type(b'Enum', (), enums)
    except TypeError:
        return type('Enum', (), enums)


def list_divider(list_, chunks):

    """
    This function can split a list into smaller parts.
    Can help creating pages
    :param list_: A list, can be a list of dictionaries
    :param chunks: How many items are required on each item of the final list
    :return: List of lists
    """

    return [list_[i:i + chunks] for i in range(0, len(list_), chunks)]


def merge_dicts(d1, d2):

    d = d1.copy()
    d.update(d2)

    return d


def form_data_conversion(form_data):

    if isinstance(form_data, dict):
        return urlencode(form_data)
    elif isinstance(form_data, str):
        return dict(parse_qsl(form_data))
    else:
        pass  # won't do any conversion on other types
