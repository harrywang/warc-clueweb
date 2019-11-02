warc-clueweb: Python library to work with ClueWeb09 WARC files
==============================================================

# setup

I added one sample data file and the following instructions:

only works with python 2.7
```
$ $ vitrualenv venv
$ source venv/bin/activate
$ python setup.py install
$ python extract_sample.py
None 219
http://www.locksmithsportspicks.com/tarver-woods-odds/ 24478
http://www.locorunning.co.nz/bandito.shtml 13599
http://www.lodgekyle.co.uk/grand_lodge.html 2924
http://www.lodinet.com/tmiller/ 2543
http://www.lodmell.com/legal-services.html 13166
http://www.loewe-uk.com/uk/loewe-ag/updates.html 19176
http://www.logansart.com/blackhawkstout.html 3756
http://www.loganskline.com/ 7998
http://www.logcabinfarm.com/ 9161
http://www.loghill.com/localsites.html 2698
http://www.loghomeservices.net/request_estimate.htm 5688
http://www.logicity.co.uk/ 4100
http://www.logicmusic.net/music.htm 20005
http://www.logixmobile.com/products/bulksms/gsm_modem.asp 15797
http://www.logocreator.com/logo-generator.html 15324
http://www.logodesignengine.com/directory/Design/ 4089
http://www.lohas.it/naturalstep1.html 7076
http://www.loiano.italy.freehotelguide.com/ 20270
http://www.lol.de/2008/09/14/guten-tag-lol-de-fans 36673
http://www.lolotrailcenter.com/about.htm 17974
http://www.lomulder.nl/ 65919
http://www.lonardivini.it/en/ilvino.html 4236
http://www.loncapa.org/beforeyoustart.html 11586
http://www.lonchaney.com/lc5/jr/jrpages/jrmovk.html 8444
http://www.londonelizabethhotel.co.uk/booking/contact.php 7172
http://www.londonfood.org.uk/technical_advice.shtml 4387
http://www.londonfoodfilmfiesta.co.uk/Artmai%7E1/Warsaw.htm 17647
http://www.londonhotelsdeal.com/ 9520
http://www.londonmountaineeringclub.com/Fronwydyr.asp 9696
http://www.londonpianotrio.com/ 8612
http://www.londonscottish.com/content/blogcategory/0/35/ 49485
http://www.londonservice.net/londra/trasferimenti-londra-taxi/British-airways-Aeroporto-di-Palermo.phtml 26004
http://www.lonemountainranch.com/fall/yellowstonepark/ 12039
http://www.loneoakkennels.net/ 18636
http://www.lonergan.org/ 15900
http://www.lonergan.org/online_books/Liddy/table_of_contents.htm 11129
http://www.lonestarford.com/contact-form.htm 19124
http://www.lonestarnights.com/ 22975
http://www.long-beach-criminal-defense.com/courthouse_torrance.html 10490
http://www.long-sunday.net/long_sunday/2005/12/critique_of_vio_1.html 10838
http://www.longchi.com.cn/en/cjjs.asp 14780
http://www.longhomecoffeesc.com/ 14821
http://www.longhornvillage.com/contactus.html 32039
http://www.longislandsubaruclub.com/members.html 39176
http://www.longrunfishingcharters.com/Saltwater_Sportsman.htm 23140
http://www.longviewkelsohomes.com/About_Washington/page_1415280.html 41213
http://www.longvillemotel.com/ 18318
http://www.longwaveinc.com/SeaportE_QualityAssurance.aspx 11082
http://www.lonniedoneganinc.com/discography.htm 2083
http://www.lookhere.co.za/ 6297
```


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
