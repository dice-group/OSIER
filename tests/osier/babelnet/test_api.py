from nose.tools import raises, nottest

import requests

from osier.babelnet.api import get_lemmas_simple, get_lemmas, get_synset_lemma, \
    get_synset_lemma_simple, get_synset_sense, get_synset_sense_main, \
    get_synset_pos, get_synset_category, get_synset_compound, \
    get_synset_domain, get_synset_edge, get_synset_example, \
    get_synset_gloss, get_synset_image, get_synset_image_one, \
    get_synset_uri_geonames, get_synset_uri_dbpedia, get_synset_uri_yago, \
    get_synset_other_forms, get_synset_translation, get_most_specific_term

WORD_1 = "city"
WORD_2 = "town"

def test_get_lemmas_simple():
    lemmas = get_lemmas_simple(WORD_1)
    assert b"town" in lemmas

def test_get_lemmas():
    lemmas = get_lemmas(WORD_2)
    assert b"city" in lemmas

def test_get_synset_lemma():
    lemmas = get_synset_lemma(WORD_1)
    assert b"town" in lemmas

def test_get_synset_lemma_simple():
    lemmas = get_synset_lemma_simple(WORD_2)
    assert b"city" in lemmas

SENSE = {
    'bKeyConcept': False,
    'freebaseId': '056mk',
    'frequency': 438,
    'language': 'EN',
    'lemma': 'metropolis',
    'pos': 'NOUN',
    'position': 1,
    'pronunciations': {
        'audios': [
            {'filename': 'En-us-metropolis.ogg', 'language': 'EN', 'lemma': 'metropolis'}
        ],
        'transcriptions': ['[/mɪˈtɹɒpəlɪs/]']
    },
    'sensekey': '',
    'sensenumber': 0,
    'simpleLemma': 'metropolis',
    'source': 'WIKI',
    'synsetID': {'id': 'bn:00019319n', 'pos': 'NOUN', 'source': 'BABELNET'},
    'translationInfo': ''
}
def test_get_synset_sense():
    senses = get_synset_sense(WORD_1)
    assert SENSE in senses

SENSE_MAIN = {
    'bKeyConcept': False,
    'freebaseId': '056mk',
    'frequency': 0,
    'language': 'EN',
    'lemma': 'metropolis',
    'pos': 'NOUN',
    'position': 2,
    'pronunciations': {
        'audios': [
            {'filename': 'En-us-metropolis.ogg', 'language': 'EN', 'lemma': 'metropolis'}
        ],
        'transcriptions': ['[/mɪˈtɹɒpəlɪs/]']
    },
    'sensekey': 'metropolis%1:15:00::',
    'sensenumber': 1,
    'simpleLemma': 'metropolis',
    'source': 'WN',
    'synsetID': {'id': 'bn:00019319n', 'pos': 'NOUN', 'source': 'BABELNET'},
    'translationInfo': '',
    'wordNetOffset': '08524735n'
}
def test_get_synset_sense_main():
    senses = get_synset_sense_main(WORD_1)
    assert SENSE_MAIN in senses

def test_get_synset_pos():
    pos = get_synset_pos(WORD_2)
    assert pos == ['NOUN']

def test_get_synset_category():
    categories = get_synset_category(WORD_1)
    assert "Demographics" in categories
    assert "Administrative_divisions_of_the_United_States_by_state" in categories

def test_get_synset_compound():
    compounds = get_synset_compound(WORD_2)
    assert "urban_town" in compounds
    assert "border_town" in compounds

def test_get_synset_domain():
    domains = get_synset_domain(WORD_1)
    assert 'GEOGRAPHY_AND_PLACES 1.0' in domains
    assert 'ART_ARCHITECTURE_AND_ARCHAEOLOGY 0.367137153184' in domains

def test_get_synset_edge():
    edges = get_synset_edge(WORD_2)
    assert 'EN_~_bn:00012257n_0.68293_0.42052' in edges

def test_get_synset_example():
    examples = get_synset_example(WORD_1)
    assert 'Ancient Troy was a great city' in examples

def test_get_synset_gloss():
    glosses = get_synset_gloss(WORD_2)
    assert 'An urban area with a fixed boundary that is smaller than a city' in glosses

def test_get_synset_image():
    images = get_synset_image(WORD_1)
    assert 'https://upload.wikimedia.org/wikipedia/commons/9/95/Cahill_expressway_from_bridge.jpg' in images

#Does not work
@nottest
def test_get_synset_image_one():
    image = get_synset_image_one(WORD_1)
    import ipdb; ipdb.set_trace()

def test_get_get_synset_uri_geonames():
    uris = get_synset_uri_geonames(WORD_2)
    assert 'http://www.geonames.org/5879092' in uris

def test_get_get_synset_uri_dbpedia():
    uris = get_synset_uri_dbpedia(WORD_2)
    assert 'http://DBpedia.org/resource/Town' in uris

def test_get_get_synset_uri_yago():
    uris = get_synset_uri_yago(WORD_2)
    assert 'http://yago-knowledge.org/resource/Ithiel_Town' in uris

#Does not work
@nottest
def test_get_synset_other_forms():
    otherforms = get_synset_other_forms(WORD_1)
    import ipdb; ipdb.set_trace()

def test_get_synset_translation():
    translations = get_synset_translation(WORD_1)
    assert 'WNTR:JA:大_都_市_。_0.42857_3_7 WNTR:ES:metrópoli_0.85714_6_7' in translations


@raises(requests.exceptions.HTTPError)
def test_empty_request_lemmas_simple():
    lemmas = get_lemmas_simple(None)

def test_get_most_specific_term():
    terms = ["cardinal", "priest", "person"]
    most_specific_term = get_most_specific_term(terms)
    assert most_specific_term == "cardinal"
