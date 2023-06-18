# license plate validation.
    
def main():
    plate = input("Plate: ")
    if check_length(plate) and is_alnum(plate) and check_first_two(plate) and check_zero(plate) and nums_not_in_center(plate):
        print("Valid")
    else:
        print("Invalid")

def check_length(s):
    return 2 <= len(s) <= 6

def is_alnum(s):
    return s.isalnum()

def check_first_two(s):
    return s[:2].isalpha()

def check_zero(s):
    return s[2] != '0'

def nums_not_in_center(s):
    center = s[2:-2]
    return not any(char.isdigit() for char in center)

main()