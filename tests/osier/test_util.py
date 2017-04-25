from osier.util import generate_id

_ID = "0cc175b9c0f1b6a831c399e269772661"

def test_generate_id():
    byte_string = b"a"
    _id = generate_id(byte_string)
    assert _id == _ID
