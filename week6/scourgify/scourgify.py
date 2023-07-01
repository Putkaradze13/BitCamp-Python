# Expects the user to provide two command-line arguments:
#   - the name of an existing CSV file to read as input, 
#     whose columns are assumed to be, in order, name and house, and
#   - the name of a new CSV to write as output, whose columns should be, 
#     order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. 
# Assume that each student will have both a first name and last name.

import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], 'w') as file2:
                    writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
                    writer.writeheader()
                    for row in reader:
                        row['first'] = row.pop('name')
                        last_name, first_name = row['first'].split(', ')
                        row['first'] = first_name
                        row['last'] = last_name
                        writer.writerow(row)
        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')

if __name__ == '__main__' :
    main()