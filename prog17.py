import cookielib
import urllib2

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]

url = "http://www.pythonchallenge.com/pc/return/romance.html"
opener = urllib2.build_opener(*handlers)
r = opener.open(urllib2.Request(url))

for cookie in cookies:
        print cookie.name, cookie.value
