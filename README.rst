PGPy2: Pretty Good Privacy for Python
=====================================

Homepage: None yet.

`PGPy2` is a Python (2 and 3) library for implementing Pretty Good Privacy into Python programs, conforming to the OpenPGP specification per RFC 4880.

It is a fork from `PGPy <https://github.com/SecurityInnovation/PGPy>`_.

Features
--------

Currently, PGPy2 can load keys and signatures of all kinds in both ASCII armored and binary formats.

It can create and verify RSA, DSA, and ECDSA signatures, at the moment. It can also encrypt and decrypt messages using RSA and ECDH.

Installation
------------

To install PGPy2, you should be able to do (but it is not yet set up, since the fork):

.. code-block:: bash

    $ pip install PGPy2

Documentation
-------------

`PGPy2 Documentation <https://pgpy2.readthedocs.io/en/latest/>`_ (not set up yet since the fork)

Discussion
----------

Please report any bugs found on the `issue tracker <https://github.com/dkg/PGPy2/issues>`_

You can also join ``#pgpy`` on Freenode to ask questions or get involved

Requirements
------------

- Python 3 >= 3.4; Python 2 >= 2.7

  Tested with: 3.7, 3.6, 3.5, 3.4, 2.7

- `Cryptography <https://pypi.python.org/pypi/cryptography>`_

- `enum34 <https://pypi.python.org/pypi/enum34>`_

- `singledispatch <https://pypi.python.org/pypi/singledispatch>`_

- `pyasn1 <https://pypi.python.org/pypi/pyasn1/>`_

- `six <https://pypi.python.org/pypi/six>`_

License
-------

BSD 3-Clause licensed. See the bundled `LICENSE <https://github.com/dkg/PGPy2/blob/master/LICENSE>`_ file for more details.
