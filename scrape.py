import os
import requests
import json

def FB_debug():
    TOKEN = os.environ.get("TOKEN")
    URL = os.environ.get("URL")
    r = requests.post('https://graph.facebook.com/v4.0/', params={'scrape':'true', 'id': URL, 'access_token': TOKEN})
    print(r.status_code)
    print(r.text)
    title = json.loads(r.text)['title'].strip()
    description = json.loads(r.text)['description'].strip()
    try:
        image = json.loads(r.text)['image'][0]['url']
    except Exception as e: #for stories that don't have images
        print(e)
        image = 'no image'
    message = "Your scrape is\n*Link:* `"+URL+"`\n*Title:* "+title+"\n*Description:* "+description+"\n*Photo:* "+image
    print(message)
FB_debug()
