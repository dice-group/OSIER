from osier.babelnet.api import get_lemmas_simple

#[[b'label', b'character'],
# [b'C\xc3\xa9line Bara', b'person'],
# [b'Eric Masterson (actor)', b'artist'],
# [b'Frederick William Matthiessen', b'adult (pornographic) actor'],
# [b'Gianna Michaels', b'artist'],
# [b'James Deen', b'person']]
def test_lemmatize_porn_actors():
    lemmas = get_lemmas_simple(b"Eric Masterson (actor)")
    assert len(lemmas) == 0
    #Only give names, no further info
    lemmas = get_lemmas_simple(b"Eric Masterson")
    assert len(lemmas) != 0
    lemmas = get_lemmas_simple(b"actor")
    assert len(lemmas) != 0

    import ipdb; ipdb.set_trace()
