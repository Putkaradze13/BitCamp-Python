# prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time

def main():
    user_time = input('What time is it? ')
    decimal_time = convert(user_time)
    meal(decimal_time)


def convert(t):
    hours, minutes = t.split(':')
    hours = float(hours)
    minutes = float(minutes)
    time = hours + minutes/60

    return time


def meal(dtime):
    dtime = float(dtime)
    if 7 <= dtime <= 8:
        print('breakfast time')
    elif 12 <= dtime <= 13:
        print('lunch time')
    elif 18 <= dtime <= 19:
        print('dinner time')

if __name__ == "__main__":
    main()