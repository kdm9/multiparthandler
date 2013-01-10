multiparthandler:
================

A module to allow urllib2 to POST to multipart/form-data forms.
This is an updated version of MultipartPostHandler, by Will Holcomb.
The original module has been modernised, and made compatible with Python 3.x.

License:
=======
multiparthandler-0.2.0 is licensed under the LGPL v2.1 <br />
Copyright 2012 by Kevin Murray. All rights reserved. <br />
NOTE: This is not an official updated version, and is not affiliated
with the original author.

Usage:
======
Enables the use of multipart/form-data for posting forms

Example:
=======
(Adapted from MultipartPostHandler's example)
```
>>>import multiparthandler
>>>import urllib2
>>>import cookielib
>>>cookies = cookielib.CookieJar()
>>>opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
...                        multiparthandler.multiparthandler)
>>>params = { "username" : "bob", "password" : "riviera",
...          "file" : open("filename", "rb") }
>>>opener.open("http://wwww.bobsite.com/upload/", params)
```
Further Examples can be found in the unittests provided in the ```tests/``
directory.
