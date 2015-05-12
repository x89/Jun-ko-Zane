import urllib.request
import urllib.parse
from ..http_codes import http_codes

class Helo:
    '''
    Basically we want to send a "hello" request to the server with our
    "location" which could change (to make it look like we're moving around the
    server and not sticking to one position. The default is every 120 seconds.
    Best guess is that this is a server side setting and if you don't respond
    then they will drop you from the people they need to send notifications to
    to save bandwidth.
    '''
    def __init__(self):
        self.url = 'https://www.freelancer.com/users/onUpdateOnlineStatus.php'
        self.header = 'application/x-www-form-urlencoded'
        self.post_data = {
                'cachetimeout': 120,
                'location': 'https://www.freelancer.com/jobs/myskills/1/'
                }

    def helo:
        post_data = urllib.parse.urlencode(self.post_data)
        req = urllib.request(url, data)
        request = urllib.request.Request(self.url, post_data)
        # Sleep 120 and do again, in a thread/fork?
        #TODO: Complete :)
