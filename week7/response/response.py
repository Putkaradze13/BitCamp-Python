# The app prompts the user for an email address via input and then prints Valid or Invalid, 
# respectively, if the input is a syntatically valid email address.

from validator_collection import checkers

def main():
    print(validate(input("What's your email address?: ")))


def validate(e):
    if checkers.is_email(e) == True:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()