from plates import is_valid

def test_plates1():
    assert is_valid("c") == False
    assert is_valid("cs") == True
    assert is_valid("cs50") == True
    assert is_valid("23") == False



def test_plates2():
    assert is_valid("CHFRS") == True
    assert is_valid("23FR") == False


def test_plates3():
    assert is_valid("AA22AA") == False
    assert is_valid("AAA022") == False
    assert is_valid("AAA220") == True


def test_plates4():
    assert is_valid("cs.,9n") == False
    assert is_valid("De !o") == False
    assert is_valid("AAAA22") == True



