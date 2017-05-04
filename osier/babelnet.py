import requests
import json

ENDPOINT = "http://babelnet.aksw.org/"
# /sense
# /sense/main
# /pos

def get_lemmas_simple(word):
    return _request(word, "/lemma/simple")

def get_lemmas(word):
    return _request(word, "/lemma")

def _request(word, route):
    URI = ENDPOINT + route
    params = {'word': word}
    r = requests.get(URI, params=params)
    r.raise_for_status()
    reply = r.content.decode("utf-8")
    _unicode = json.loads(reply)
    _bytes = list(map(lambda x: x.encode("utf-8"), _unicode))
    return _bytes
