from plates import is_valid

def main():
    test_isnot_valid()

def test_isnot_valid():
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('GOODBYE') == False
    assert is_valid('50256') == False
    assert is_valid('CS50..') == False


def test_is_valid():
    assert is_valid('CS50') == True
    assert is_valid('HELLO') == True


if __name__=='__main__':
    main()