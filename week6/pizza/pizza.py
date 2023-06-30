# expects exactly one command-line argument, the name of a CSV file in Pinocchio’s format,
# and outputs a table formatted as ASCII art using tabulate,
# Format the table using the library’s grid format. 
# If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .csv, or if the specified file does not exist, 
# the program should instead exit via sys.exit.

import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers='keys', tablefmt="grid"))
        except FileNotFoundError:
            sys.exit('File does not exist')

if __name__ == '__main__' :
    main()