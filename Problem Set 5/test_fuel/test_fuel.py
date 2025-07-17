from fuel import convert, gauge
import pytest

def test_convert():
     assert convert("1/2") == 50
     assert convert("1/4") == 25
     assert convert("99/100") == 99
     assert convert("1/100") == 1
     with pytest.raises(ZeroDivisionError):
          convert("2/0")
     with pytest.raises(ValueError):
          convert("cat/dog")


def test_gauge():
     assert gauge(50) == "50%"
     assert gauge(75) == "75%"
     assert gauge(1) == "E"
     assert gauge(99) == "F"

