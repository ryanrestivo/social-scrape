import os
import requests

def FB_debug():
    TOKEN = os.environ.get("TOKEN")
    URL = os.environ.get("URL")
    r = requests.post('https://graph.facebook.com/v4.0/', params={'scrape':'true', 'id': URL, 'access_token': TOKEN})
    print(r.status_code)
    print(r.text)
FB_debug()
