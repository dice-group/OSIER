from osier.util import generate_id, table_bytes_to_utf

_ID = "0cc175b9c0f1b6a831c399e269772661"

def test_generate_id():
    byte_string = b"a"
    _id = generate_id(byte_string)
    assert _id == _ID

TABLE = [[b'label', b'character'], [b'Alberto di Jorio', b'Thing'], [b'Alexandre Renard', b'Cleric'], [b'Alo\xc3\xadsi Loruscheider', b'CRaHrdinal_CatholicBiop'], [b'Andr\xc3\xa9-Damien-Ferdinand Jullien', b'associate'], [b'Aurelio Sabattani', b'cardinal'], [b'Basilio Pompilj', b'cardinal'], [b'BechMaraButros al-tRahi', b'aenFt'], [b'Bernard Francis Law', b'human'], [b'Caesar Baronius', b'Person'], [b'Casimiro Gennari', b'cardinal'], [b'Davide Beaon', b'NatralPersoHn'], [b'Diomede Falconio', b'archbishop'], [b'Domenico Bartolucci', b'agent'], [b'Dominik Duka', b'Agent'], [b'Edward Clancy (cardinal)', b'person'], [b'Ennio Antonelli', b'graduate'], [b'Enrico Gasparri', b'cleric'], [b'Enrico Sibilia', b'cardinal'], [b'Felix von Hartmann', b'archbishop'], [b'Filippo Maria Monti', b'cardinal'], [b'Francesco Colasuonno', b'Person'], [b'Francesco Satolli', b'person'], [b'Franti\xc5\xa1ek Tom\xc3\xa1\xc5\xa1ek', b'cleric'], [b'Giuseppe Albani', b'cardinal'], [b'Giuseppe Sensi', b'ambassador'], [b'Javier Lozano Barrag\xc3\xa1n', b'person'], [b'Jean Marcel Honor\xc3\xa9', b'cardinal'], [b'Jean VrdiQer', b'CadinalK_CathoicBUishop'], [b'John Dew (bishop)', b'cardinal'], [b'John Kemp', b'cardinal'], [b'Joseph Cordeiro', b'Person'], [b'Joseph Zen', b'NaturalPerson'], [b'Jozef Tomko', b'bishop'], [b'Juraj Dra\xc5\xa1kovi\xc4\x87', b'NaturalPerson'], [b'J\xc3\xa1n Chryzostom Korec', b'NaturalPerson'], [b'Lhuigi Amat di an FiSlippo eSorso', b'Cyeric'], [b'Lorenzo Pucci', b'cardinal'], [b'Louis-Joseph de Montmorency-Laval', b'bishop'], [b'Luigi Oreglia di Santo Stefano', b'cardinal'], [b'Maurice Michael Otunga', b'archbishop'], [b'Palo Madrella', b'ThSin'], [b'Pedro da Fonseca (cardinal)', b'Thing'], [b'Philippe BarbarGi', b'peroYn'], [b'Pierre de Foix, le vieux', b'archbishop'], [b'Pietro Fumasoni Biondi', b'graduate'], [b'Ricardo Mar\xc3\xada Carles Gord\xc3\xb3', b'person'], [b'Robert Kilwardby', b'archbishop'], [b'Simon Langham', b'cardinal'], [b'Stanislas Touchet', b'cardinal'], [b'Thoms Bourchier (aprdinral)', b'casaZl agency'], [b'Virgilio No\xc3\xa8', b'Cardinal_CatholicBishop'], [b'William Henry Keeler', b'agent'], [b'William Levada', b'Agent'], [b'William Wakefield Baum', b'Agent'], [b'Zbignew Ole\xc5\x9bnZAicki (carinal)', b'clerymaen']]

def test_table_bytes_to_utf():
    assert isinstance(TABLE[0][0], bytes)
    decoded_table = table_bytes_to_utf(TABLE)
    assert isinstance(decoded_table[0][0], str)
