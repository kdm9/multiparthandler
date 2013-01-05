Module to allow urllib2 to POST to multipart/form-data forms
This is an updated version of MultipartPostHandler, which

License:
=======
MultipartPostHandler-0.2.0 is licensed under the LGPL v2.1 <br />
Copyright 2012 by Kevin Murray. All rights reserved. <br />
NOTE: This is not an official updated version, and is not affiliated
with the original author.

Usage:
======
Enables the use of multipart/form-data for posting forms

Example:
=======
```
>>>import MultipartPostHandler, urllib2, cookielib

>>>cookies = cookielib.CookieJar()
>>>opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
...                        MultipartPostHandler.MultipartPostHandler)
>>>params = { "username" : "bob", "password" : "riviera",
...          "file" : open("filename", "rb") }
>>>opener.open("http://wwww.bobsite.com/upload/", params)
```

Further Examples can be found in the unittests provided as part of this module.
