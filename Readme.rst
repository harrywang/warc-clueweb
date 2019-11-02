warc-clueweb: Python library to work with ClueWeb09 WARC files
==============================================================

`ClueWeb09 <http://www.lemurproject.org/clueweb09.php/>`_ dataset consists of
~1 billion web pages crawled in January and February 2009.
It is used by several tracks of the `TREC <http://trec.nist.gov/>`_ conference.

The dataset is available in the WARC 0.18 format.
However, there are certain caveats with ClueWeb's files.
First, it does not use the standard \\r\\n end-of-line markers.
Moreover, some records are
`ill-formed <http://lintool.github.com/Cloud9/docs/content/clue.html#malformed>`_.

This library is a fork of
`internetarchive/warc <https://github.com/internetarchive/warc>`_
that can handle ClueWeb09 dataset.

Documentation
-------------
Only minor modifications to the original library were made.
The original documentation of the warc library still holds.
It is available at http://warc.readthedocs.org/.

License
-------
This software is licensed under GPL v2. See `LICENSE <http://github.com/cdegroc/warc-clueweb/blob/master/LICENSE>`_ file for details.
