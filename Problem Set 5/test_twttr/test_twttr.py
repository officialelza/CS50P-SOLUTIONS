from twttr import shorten

def test_twttr_capitals():
    assert shorten("HOLA SOI DORA") == "HL S DR"
    assert shorten("WELCOME TO PYTHON") == "WLCM T PYTHN"
    assert shorten("WEEK 5 OF CS50P") == "WK 5 F CS50P"

def test_twttr_smalls():
    assert shorten("wizard of oz") == "wzrd f z"
    assert shorten("hermonie") == "hrmn"
    assert shorten("interstellular thief") == "ntrstlllr thf"

def test_twttr_c_s():
    assert shorten("Environmental Crisis") == "nvrnmntl Crss"
    assert shorten("Bag of chocolates") == "Bg f chclts"
    assert shorten("alBErt EInsTEin") == "lBrt nsTn"
    assert shorten("Hello, World") == "Hll, Wrld"

