def main():
    greeting = input('Greeting: ').strip().casefold()
    print(value(greeting))


def value(greeting):
    if 'hello' in greeting:
        return '$0'
    elif 'h' == greeting[0]:
        return '$20'
    else:
        return '$100'


if __name__ == "__main__":
    main()