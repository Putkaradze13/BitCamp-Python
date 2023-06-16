# prompts the user for a str in English and then outputs the “emojized” version of that str,
# converting any codes (or aliases) therein to their corresponding emoji.

import emoji

def main():
    output()

def output():
    try:
        user_input = input('Input: ')
        print(f'Output: {emoji.emojize(user_input)}')
    except ValueError:
        pass

if __name__ == '__main__':
    main()