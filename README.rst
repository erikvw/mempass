|pypi| |travis| |codecov| |downloads|

Mempass
-------

Simple memorizable password generator

See http://xkcd.com/936/

Adapted from https://github.com/jesterpm/bin/blob/master/mkpasswd


.. code-block:: bash

    pip install mempass


on the command line

.. code-block:: bash

    $ mempass 4
    password: celeriac waggable endoss oxytocia
    score: Strong! (4)


in python

.. code-block:: python

    >>> from mempass import mkpassword
    >>> password = mkpassword(4)
    >>> print(password)
    celeriac waggable endoss oxytocia

or

.. code-block:: python

    >>> from mempass import PasswordGenerator
    >>> pwgen = PasswordGenerator(nwords=4)
    >>> print(pwgen.password)
    celeriac waggable endoss oxytocia

    >>> print(pwgen.score)
    4

    >>> print(pwgen.warning)
    ""

    >>> print(pwgen.suggestions)
    ""


.. |pypi| image:: https://img.shields.io/pypi/v/mempass.svg
    :target: https://pypi.python.org/pypi/mempass
    
.. |travis| image:: https://travis-ci.com/erikvw/mempass.svg?branch=develop
    :target: https://travis-ci.com/erikvw/mempass
    
.. |codecov| image:: https://codecov.io/gh/erikvw/mempass/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/erikvw/mempass

.. |downloads| image:: https://pepy.tech/badge/mempass
   :target: https://pepy.tech/project/mempass
