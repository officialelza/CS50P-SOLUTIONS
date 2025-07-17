from um import count

def test_1():
    assert count("hi um world") == 1
    assert count("um...") == 1
    assert count("yummy") == 0
    assert count("Hello Um") == 1
    assert count("Hello UM i am um world") == 2
