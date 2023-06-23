def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    if s[2] == '0':
        return False
    center = s[2:-2]
    if any(char.isdigit() for char in center):
        return False
    return True



if __name__ == "__main__":
    main()