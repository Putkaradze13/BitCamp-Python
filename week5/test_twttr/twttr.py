vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    str = input('Input: ')
    print(shorten(str))


def shorten(str):
    twt_str = ''
    for char in str:
        if char.lower() not in vowels:
            twt_str += char
    return(twt_str)


if __name__ == "__main__":
    main()