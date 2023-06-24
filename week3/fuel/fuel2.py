def main():
    fraction = input('Fracton: ')
    percentage = convert(fraction)
    if percentage == None:
        return
    else:
        result = gauge(percentage)
    print(result)


def convert(fraction):
    while True:
        list = fraction.split('/')
        x = int(list[0])
        y = int(list[1])
        if y == 0:
            raise ZeroDivisionError('Can not divide on zero')
        elif x > y:
            raise ValueError('Invalid Value')
        else:
            return round((x / y) * 100)


def gauge(percentage):
        if percentage >= 99:
            return 'F'
        elif percentage <= 1:
            return 'E'
        else:
            return f'{percentage}%'



if __name__ == "__main__":
    main()