from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_value_error()
    test_zero_division()
    test_gauge()

def test_convert():
    assert convert('1/2') == 50

def test_value_error():
    with pytest.raises(ValueError):
        convert('2/1')

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'


if __name__=='__main__':
    main()