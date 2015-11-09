kotti_icons
***********

Add a full set of icons / favicons to your `Kotti`_ site.

|pypi|_
|downloads_month|_
|license|_
|build_status_stable|_

.. |pypi| image:: https://img.shields.io/pypi/v/kotti_icons.svg?style=flat-square
.. _pypi: https://pypi.python.org/pypi/kotti_icons/

.. |downloads_month| image:: https://img.shields.io/pypi/dm/kotti_icons.svg?style=flat-square
.. _downloads_month: https://pypi.python.org/pypi/kotti_icons/

.. |license| image:: https://img.shields.io/pypi/l/kotti_icons.svg?style=flat-square
.. _license: http://www.repoze.org/LICENSE.txt

.. |build_status_stable| image:: https://img.shields.io/travis/Kotti/kotti_icons/production.svg?style=flat-square
.. _build_status_stable: http://travis-ci.org/Kotti/kotti_icons

This extension injects a set of icon links into the head section of Kotti's master templates.
It also registers two views for the root node of your site:

  - `browserconfig.xml`_
  - `manifest.json`_

Development happens at https://github.com/Kotti/kotti_icons

.. _browserconfig.xml: https://msdn.microsoft.com/de-de/library/dn320426(v=vs.85).aspx#specifying_tile_images_and_assets
.. _manifest.json: https://w3c.github.io/manifest/#icons-member
.. _build_status: http://travis-ci.org/Kotti/kotti_icons
.. _Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_icons.kotti_configure

Add your own icon set
=====================

To replace the icons in this this packe with your own, you first need to configure an `asset override`_ in your package's ``includeme``::

    config.override_asset(
        to_override='kotti_icons:static',
        override_with='your_package:path/to/directory/with/icons')

Then place your icon set in this directory.

You can generate a full set of icons for your site by uploading a single image to one of the many available online tools, for example:

    - http://www.favicon-generator.org/
    - http://realfavicongenerator.net/

.. _asset override: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/assets.html#overriding-assets

Development
===========

|build_status_master|_

.. |build_status_master| image:: https://img.shields.io/travis/Kotti/kotti_icons/master.svg?style=flat-square
.. _build_status_master: http://travis-ci.org/Kotti/kotti_icons

Contributions to kotti_icons are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/Kotti/kotti_icons/issues
.. _Github repository: https://github.com/Kotti/kotti_icons
