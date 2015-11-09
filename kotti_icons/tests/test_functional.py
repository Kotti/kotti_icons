# -*- coding: utf-8 -*-

"""
Created on 2015-11-09
:author: Andreas Kaiser (disko@binary-punks.com)
"""


def test_browserconfig(webtest, root, settings):

    resp = webtest.get('/browserconfig.xml')

    assert resp.content_type == 'text/xml'
    assert '<browserconfig>' in resp.body


def test_manifest(webtest, root, settings):

    resp = webtest.get('/manifest.json')

    assert resp.content_type == 'application/json'
    assert resp.json['name'] == settings['kotti.site_title']
    assert 'icons' in resp.json
    assert len(resp.json['icons']) > 0
