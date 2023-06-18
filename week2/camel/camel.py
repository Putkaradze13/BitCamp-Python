# App converts a camelCase string to a Python-style snake_case string.

def main():
    camel_case = input('camelCase: ')
    convert(camel_case)

def convert(camel_case):
    py_case = ""
    for char in camel_case:
        if char.isupper():
            py_case += '_' + char.lower()
        else:
            py_case += char
    print(py_case)


main()