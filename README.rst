CMSplugin redirect
==================

A reusable Django app to add custom redirect actions to Django-CMS.

Note, that this is an early stage of development, so this is probably highly
unstable and unfinished and also might not have a pypi relase, yet.


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-redirect

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-redirect.git#egg=cmsplugin_redirect

Add ``cmsplugin_redirect`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_redirect',
    )


Usage
-----

TODO: Describe usage


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 cmsplugin-redirect
    $ pip install -r test_requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
