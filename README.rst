kotti_icons
***********

Add a full set of icons / favicons to your `Kotti`_ site.

|build_status|_

This extension injects a set of icon links into the head section of Kotti's master templates.
It also provides two views, registered for the root node of your site:

  - `browserconfig.xml`_
  - `manifest.json`_

Development happens at https://github.com/Kotti/kotti_icons

.. _browserconfig.xml: https://msdn.microsoft.com/de-de/library/dn320426(v=vs.85).aspx#specifying_tile_images_and_assets
.. _manifest.json: https://w3c.github.io/manifest/#icons-member
.. |build_status| image:: https://secure.travis-ci.org/Kotti/kotti_icons.png?branch=master
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

Contributions to kotti_icons are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/Kotti/kotti_icons/issues
.. _Github repository: https://github.com/Kotti/kotti_icons
