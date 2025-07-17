from seasons import days_to_mins

def test_days():
    assert days_to_mins(609) == "Eight hundred seventy-six thousand, nine hundred sixty minutes"
    assert days_to_mins(365) == "Five hundred twenty-five thousand, six hundred minutes"
