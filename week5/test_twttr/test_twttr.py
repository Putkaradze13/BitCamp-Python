from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('twIttEr') == 'twttr'
    assert shorten('1twitter') == '1twttr'
    assert shorten('twitter.') == 'twttr.'



if __name__ == "__main__":
    main()