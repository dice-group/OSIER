import requests
import json

#ENDPOINT = "http://babelnet.aksw.org"
ENDPOINT = "http://localhost:4567"

def get_most_specific_term(terms):
    payload = json.dumps(terms)
    URI = ENDPOINT + "/terms/mostspecific"
    r = requests.post(url=URI,data=payload)
    r.raise_for_status()
    reply = r.content.decode("utf-8")
    _unicode = json.loads(reply)
    return _unicode

def _request(word, route):
    URI = ENDPOINT + route
    params = {'word': word}
    r = requests.get(URI, params=params)
    r.raise_for_status()
    reply = r.content.decode("utf-8")
    _unicode = json.loads(reply)
    return _unicode

def get_lemmas_simple(word):
    return get_synset_lemma_simple(word)

def get_lemmas(word):
    return get_synset_lemma(word)

def get_synset_lemma(word):
    _unicode = _request(word, "/synset/lemma")
    return list(map(lambda x: x.encode("utf-8"), _unicode))

def get_synset_lemma_simple(word):
    _unicode = _request(word, "/synset/lemma/simple")
    return list(map(lambda x: x.encode("utf-8"), _unicode))

def get_synset_sense(word):
    return _request(word, "/synset/sense")

def get_synset_sense_main(word):
    return _request(word, "/synset/sense/main")

def get_synset_pos(word):
    return _request(word, "/synset/pos")

def get_synset_category(word):
    return _request(word, "/synset/category")

def get_synset_category_with_super(word):
    return _request(word, "/synset/category/withsuper")

def get_synset_compound(word):
    return _request(word, "/synset/compound")

def get_synset_domain(word):
    return _request(word, "/synset/domain")

def get_synset_edge(word):
    return _request(word, "/synset/edge")

def get_synset_example(word):
    return _request(word, "/synset/example")

def get_synset_gloss(word):
    return _request(word, "/synset/gloss")

def get_synset_image(word):
    return _request(word, "/synset/image")

def get_synset_image_one(word):
    return _request(word, "/synset/image/one")

def get_synset_uri_geonames(word):
    return _request(word, "/synset/uri/geonames")

def get_synset_uri_dbpedia(word):
    return _request(word, "/synset/uri/dbpedia")

def get_synset_uri_yago(word):
    return _request(word, "/synset/uri/yago")

def get_synset_other_forms(word):
    return _request(word, "/synset/otherforms")

def get_synset_translation(word):
    return _request(word, "/synset/translation")
