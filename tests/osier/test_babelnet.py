from nose.tools import raises

import requests

from osier.babelnet import get_lemmas_simple, get_lemmas

WORD_1 = "city"
WORD_2 = "town"

def test_get_lemmas_simple():
    lemmas = get_lemmas_simple(WORD_1)
    assert b"town" in lemmas

def test_get_lemmas():
    lemmas = get_lemmas(WORD_2)
    assert b"city" in lemmas

@raises(requests.exceptions.HTTPError)
def test_empty_request_lemmas_simple():
    lemmas = get_lemmas_simple(None)
