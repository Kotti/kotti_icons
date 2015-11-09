# -*- coding: utf-8 -*-

"""
Created on 2015-11-09
:author: Andreas Kaiser (disko@binary-punks.com)
"""

from pytest import fixture


def test_browserconfig(app, dummy_request):
    from kotti_icons.views import browserconfig
    assert browserconfig(dummy_request) == {}


def test_manifest(app, dummy_request):
    from kotti_icons.views import manifest
    result = manifest(dummy_request)
    assert 'name' in result
    assert 'icons' in result
    assert len(result['icons']) > 0
