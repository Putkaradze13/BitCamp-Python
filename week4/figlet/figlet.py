# The app expects zero or two command-line arguments according what
# it prints user input text with random font or lets user to choose font from list


from random import choice
import sys

from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()

def main():
    check_argvs()

def check_argvs():
    try:
        if len(sys.argv) == 1:
            random_font()
        elif len(sys.argv) == 3:
            user_font()
        else:
            sys.exit('Too many or to less arguments')
    except ValueError:
        pass


def random_font():
    user_txt = input('Input: ')
    random_font = choice(fonts)
    figlet.setFont(font=random_font)
    print(f'Output: {figlet.renderText(user_txt)}')
    return

def user_font():
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')
    else:
        user_txt = input('Input: ')
        user_font = sys.argv[2]
        figlet.setFont(font=user_font)
        print(f'Output: \n{figlet.renderText(user_txt)}')
        return

if __name__ == '__main__':
    main()