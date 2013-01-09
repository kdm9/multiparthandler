import unittest
import tempfile
import os
try:  # Py3 hackery, needs to be tested w/ 2to3
    import urllib2 as a_urllib
except ImportError:
    import urllib.request as a_urllib
import re
from MultipartPostHandler import MultipartPostHandler


class MultipartPostHandler_t(unittest.TestCase):
    
    validator_url = "http://validator.w3.org/check"
    test_url = ("http://www.w3.org/History/19921103-hypertext/hypertext/WWW/"
        "TheProject.html")
    # Uncomment this, and the tests should fail
    # test_url = "http://www.google.com/"
    opener = a_urllib.build_opener(MultipartPostHandler)
    validator_result_re = r"3 Errors, 4 warning\(s\)"  # expected re pattern

    def setUp(self):
        self.test_html = str(self.opener.open(self.test_url).read()).\
                encode("UTF-8")

    def test_post_as_file(self):
        tmp_fd, tmp_fn = tempfile.mkstemp(suffix=".html")
        with open(tmp_fn, "w") as tmp_fh:
            tmp_fh.write(self.test_html)
        params = {
            "ss" : "0", # show source
            "doctype" : "Inline",
            "uploaded_file" : open(tmp_fn, "r")
            }
        response_html = bytes(self.opener.open(self.validator_url,
            params).read()).encode("UTF-8")
        os.remove(tmp_fn)
        re_match = re.search(self.validator_result_re, response_html)
        self.assertTrue(re_match is not None)

    def test_post_as_var(self):
        params = {
            "ss" : "0", # show source
            "doctype" : "Inline",
            "fragment" : self.test_html
            }
        response_html = bytes(self.opener.open(self.validator_url,
            params).read()).encode("UTF-8")
        re_match = re.search(self.validator_result_re, response_html)
        self.assertTrue(re_match is not None)



if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
