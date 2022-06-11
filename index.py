import falcon
import requests
import os

from wsgiref.simple_server import make_server
from falcon_caching import Cache

from dotenv import load_dotenv
load_dotenv()

try:
    APP_TOKEN = os.getenv("MAPILLARY_APP_TOKEN", None)
    VERSION = os.getenv("VERCEL_GIT_COMMIT_SHA", 1)
except KeyError:
    print("Environment not ready: see README for required keys")
    exit(1)

cache = Cache(
    config={
        'CACHE_EVICTION_STRATEGY': 'time-based',  # how records are evicted
        'CACHE_TYPE': 'simple'  # what backend to use to store the cache
    })


class ThumbResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        imgkey = req.get_param('key') or ''
        resp.content_type = falcon.MEDIA_TEXT
        if not len(imgkey) > 5:
            resp.text = 'key parameter is required'
            return
        imgurl = cache.get(imgkey)
        if imgurl:
            raise falcon.HTTPMovedPermanently(
                location=imgurl
            )
        url = "https://graph.mapillary.com/" + \
            "%s?access_token=%s&fields=thumb_256_url" % (imgkey, APP_TOKEN)
        r = requests.get(url)
        if r.json().get('thumb_256_url'):
            imgurl = r.json().get('thumb_256_url')
            cache.set(imgkey, imgurl)
            raise falcon.HTTPMovedPermanently(
                location=imgurl
            )
        else:
            raise falcon.HTTPServiceUnavailable(
                title=r.text, retry_after=30
            )


app = application = falcon.App(middleware=cache.middleware)
app.add_route('/thumb', ThumbResource())


if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
