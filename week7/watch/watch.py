# The app expects a str of HTML as input, extracts any YouTube URL that’s the value of a src
# attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent
# as a str. 

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>', s):
        url_match = re.search(r'(http(s)*:\/\/(www.)*youtube.com\/embed\/)([a-z_A-Z_0-9]+)', s)
        if url_match:
            split_url = url_match.groups()
            return f'https://youtu.be/{split_url[3]}'


if __name__ == "__main__":
    main()