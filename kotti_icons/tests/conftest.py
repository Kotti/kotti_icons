# -*- coding: utf-8 -*-

"""
Created on 2015-11-09
:author: Andreas Kaiser (disko@binary-punks.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():

    return {
        'kotti.site_title': 'kotti_icons test suite',
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_icons.kotti_configure'}
