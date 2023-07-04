from working import convert
import pytest

def main():
    test_value_error()
    test_value_format()

def test_value_error():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

def test_value_format():
    assert convert(r'10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert(r'9 AM to 5 PM') == '09:00 to 17:00'


if __name__=='__main__':
    main()