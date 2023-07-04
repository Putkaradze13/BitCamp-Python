from um import count

def main():
    test_words_with_um()
    test_space_around_um()
    test_case_insensitive_um()


def test_words_with_um():
    assert count(r'yum') == 0
    assert count(r'yummi') == 0

def test_space_around_um():
    assert count(r'um ') == 1

def test_case_insensitive_um():
    assert count(r'Um') == 1

if __name__=='__main__':
    main()