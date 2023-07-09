import pytest
from seasons import Dates
from datetime import date

def main():
    test_valid()
    test_invalid()


def test_valid():
    birth = Dates("2022-09-29")
    assert birth.diff(date(2022, 9, 29)) == "Zero minutes"
    birth = Dates("2021-09-29")
    assert birth.diff(date(2022, 9, 29)) == "Five hundred twenty-five thousand, six hundred minutes"
    birth = Dates("2020-09-29")
    assert birth.diff(date(2022, 9, 29)) == "One million, fifty-one thousand, two hundred minutes"


def test_invalid():
    with pytest.raises(SystemExit):
        birth = Dates("22-12-22")
        birth = Dates("July 17, 1984")
        birth = Dates("01-01-2000")