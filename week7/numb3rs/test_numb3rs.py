from numb3rs import validate

def main():
    test_valid_ip_format()
    test_valid_ip_range()

def test_valid_ip_format():
    assert validate('1.1.1.1') == True
    assert validate('1.1.1') == False
    assert validate('1.1') == False
    assert validate('1') == False

def test_valid_ip_range():
    assert validate('255.255.255.275') == False
    assert validate('255.255.275.255') == False
    assert validate('255.275.255.275') == False
    assert validate('275.255.255.275') == False


if __name__ == "__main__":
    main()