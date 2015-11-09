# -*- coding: utf-8 -*-

"""
Created on 2015-11-09
:author: Andreas Kaiser (disko@binary-punks.com)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_icons.kotti_configure

        to enable the ``kotti_icons`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_icons'
    settings['kotti.asset_overrides'] = 'kotti_icons:overrides/kotti/'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_static_view('static-kotti_icons', 'kotti_icons:static')

    config.scan(__name__)
