# The app prompts user for upper level of number and generates random number between 1 and n number user provided.
# Then program asks user to guess what random number is generated.


import random

def main():
    try:
        n = input('Level: ')
        n = int(n)
        if n > 0:
            random_number = random.randint(1, n)
        else:
            pass
    except ValueError:
        pass

    while True:
        try:
            user_guess = int(input('Guess: '))
            if user_guess < 0:
                pass
            elif user_guess > n:
                pass
            elif user_guess < random_number:
                print('Too small!')
            elif user_guess > random_number:
                print('Too large!')
            else:
                print('Just right!')
                break
        except ValueError:
            pass

if __name__ == '__main__':
    main()