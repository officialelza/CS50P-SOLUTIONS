from numb3rs import validate

def test_ip_ad():
    assert validate("cat") == False
    assert validate("8.a.b.c") == False
    assert validate("255.255.255.255") == True

def test_ip_ad2():
    assert validate("270.250.33.44") == False
    assert validate("274. 44.21.00") == False
    assert validate("250,33,44.21") == False
def test_ip_ad3():
    assert validate("270.250.33.44.45") == False
    assert validate("270.20.30.290") == False
    assert validate("230.290.30.20") == False
    assert validate("1.555.555.555") == False



