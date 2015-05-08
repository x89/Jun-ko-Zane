import urllib.request
import urllib.parse
from ..http_codes import http_codes

class Juni:
    def __init__(self, ids):
        '''
        Not sure if necessary. Yolo.
        '''
        assert isinstance(ids, tuple), "We expected a list, we got %s" % type(ids)
        assert len(ids) == 2, "Wanted 2 ID values, got %i" % len(ids)
        self.ids = ids

    def juni_here(self, timeout=120):
        '''
        Sends the 120s ping every 120 seconds to let the server know we're
        still here. We want "Response: OK"
        '''
        # Location: POST https://www.freelancer.com/users/onUpdateOnlineStatus.php
        # It basically only sends shit (your current location and 120. It
        # probaobly uses cookies and/or your IP to establish who you are.

        url = 'https://www.freelancer.com/users/onUpdateOnlineStatus.php'

        the_120_pinger = {
            'cachetimeout': timeout,
            'location': 'https://www.freelancer.com/jobs/1/',
            #TODO: May want to change the location we're coming from
        }

        post_data = urllib.parse.urlencode(the_120_pinger)
        request = urllib.request.Request(url, the_120_pinger)

        print(request)
        #assert req.code == 200, "Response wasn't 200, it was{0}".format(req.code)
        #content = req.read()
        #assert content == b'OK', "Result was %s" % http_code(content)
