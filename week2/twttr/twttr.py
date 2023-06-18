# prompts the user for a str of text and then outputs
# that same text but with all vowels (A, E, I, O, and U) omitted

vowels = ['a', 'e', 'i', 'o', 'u']

def main():
    str = input('Input: ')
    convert(str)

def convert(str):
    twt_str = ''
    for char in str:
        if char.lower() not in vowels:
            twt_str += char
    print(twt_str)

main()


