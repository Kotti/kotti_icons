# -*- coding: utf-8 -*-

from pyramid.view import view_config

from kotti import get_settings


@view_config(name='manifest.json', root_only=True, renderer='json')
def manifest(request):
    """ Web App Manifest - see https://w3c.github.io/manifest/#icons-member

    :param request: Current request
    :type request: :class:`kotti.request.request`

    :result: Manifest dictionary
    :rtype: dict
    """

    result = {
        'name': get_settings()['kotti.site_title'],
        'icons': [],
    }
    for size, density in (
            ('36x36', '0.75'),
            ('48x48', '1.0'),
            ('72x72', '1.5'),
            ('96x96', '2.0'),
            ('144x144', '3.0'),
            ('192x192', '4.0')):
        result['icons'].append({
            'src': request.static_url(
                'kotti_icons:static/android-icon-{}.png'.format(size)),
            'sizes': size,
            'type': 'img/png',
            'density': density,
        })

    return result


@view_config(name='browserconfig.xml', root_only=True,
             renderer='kotti_icons:templates/browserconfig.xml.pt')
def browserconfig(request):
    """ Browser configuration for Microsoft browsers.
    See https://msdn.microsoft.com/de-de/library/dn320426(v=vs.85).aspx

    :param request: Current request
    :type request: :class:`kotti.request.request`

    :result: Empty dictionary
    :rtype: dict
    """

    request.response.content_type = 'text/xml'

    return {}
