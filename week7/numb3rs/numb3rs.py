# The app expects an IPv4 address as input as a str and then returns True or False,
# respectively, if that input is a valid IPv4 address or not.

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    if re.search(regex, ip):
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    main()