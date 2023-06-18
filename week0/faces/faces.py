# An application accepts string as input and returns the same input with any :) converted to 🙂 and any :( converted to 🙁.

def main():
    str = input('Hello:) ')
    convert(str)

def convert(str):
    if ':)' in str or ':(' in str:
        print(str.replace(':)', '🙂').replace(':(', '🙁'))

main()