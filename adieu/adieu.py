# The app prompts the user for names, one per line, until the user inputs control-d.
# Assume that the user will input at least one name. Then bid adieu to those names,
# separating two names with one 'and', three names with two commas and one 'and',
# and names with commas and one 'and'

import inflect

p = inflect.engine()

def main():
    text = ['Adieu', 'adieu']
    while True:
        try:
            text.append(input('Name: '))
        except EOFError:
            print('')
            break
    text[2] = 'to ' + text[2]

    if len(text) == 3:
        new_text = p.join(text, conj='')
    elif len(text) == 4:
        new_text = p.join(text, final_sep='')
    else:
        new_text = p.join(text)

    print(new_text)

if __name__ == '__main__':
    main()