# The app expects a line of text as input as a str and returns, as an int,
# the number of times that “um” appears in that text, case-insensitively,
# as a word unto itself, not as a substring of some other word.

import re


def main():
    print(count(input("Text: ")))


def count(s):
    um_in_str = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(um_in_str)


if __name__ == "__main__":
    main()