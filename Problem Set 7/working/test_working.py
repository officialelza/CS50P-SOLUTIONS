import pytest
from working import convert

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("8 PM to 4 AM") == "20:00 to 04:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 6:20 PM") == "09:00 to 18:20"

def test_2():
    assert convert("12 AM to 8 AM") == "00:00 to 08:00"
    assert convert("3:50 PM to 12 AM") == "15:50 to 00:00"
    assert convert("12 PM to 7 PM") == "12:00 to 19:00"


def test_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00AM - 17:00PM")

