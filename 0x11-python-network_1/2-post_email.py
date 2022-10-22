#!/usr/bin/python3
"""
Takes an email and URL and sends a Post Request with email as a parameter
and displays the body of the response
decoded in UTF-8
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    data = urllib.parse.urlencode({
        'email': sys.argv[2]
    }).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        data = r.read().decode('utf-8')
        print(data)
