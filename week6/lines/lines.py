# The app expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py, or if the specified file does not exist,
# the program should instead exit via sys.exit.

import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-3:] != '.py':
        sys.exit('Not a Python file')
    else:
        try:
            lines = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.lstrip().startswith('#') and line.lstrip() != '':
                        lines += 1
            print(lines)
        except FileNotFoundError:
            sys.exit('File does not exist')

if __name__ == '__main__' :
    main()