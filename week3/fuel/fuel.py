# prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.

def main():
    result = fuel_indicator(fuel_in_percentage())
    print(result)

def fuel_in_percentage():
    while True:
        try:
            list = input('Fracton: ').split('/')
            x = int(list[0])
            y = int(list[1])
            if x > y:
                pass
            else:
                return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

def fuel_indicator(x):
    if x >= 99:
        return 'F'
    elif x <= 1:
        return 'E'
    else:
        return (f'{x}%')

main()
