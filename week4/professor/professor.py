# The app prompts user for level (1, 2 or 3) for difficulty,
# then randomly generates ten (10) math problems formatted as 'X + Y ='.

from random import randint

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1 or level > 3:
                raise ValueError()
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    score = 0

    for i in range(10):
        wrong_try = 0
        if level == 1:
            x = randint(0, 9)
            y = randint(0, 9)
        elif level == 2:
            x = randint(10, 99)
            y = randint(10, 99)
        else:
            x = randint(100, 999)
            y = randint(100, 999)

        while True:
            print(f'{x} + {y} = ', end='')
            answer = input()

            if answer == str(x + y):
                score += 1
                break
            elif answer != str(x + y) and wrong_try != 2:
                print('EEE')
                wrong_try += 1
                continue
            else:
                print(f'{x} + {y} = {x + y}')
                break
    print(f'score: {score}')


if __name__ == "__main__":
    main()