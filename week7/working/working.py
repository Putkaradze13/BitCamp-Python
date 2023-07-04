# The app expects a str in either of the 12-hour formats below and returns the corresponding
# str in 24-hour format (i.e., 9:00 to 17:00).

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_format = re.search(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s)
    if valid_format:
        format_components = valid_format.groups()
        if int(format_components[1]) > 12 or int(format_components[5]) > 12:
            raise ValueError
        start_time = new_format(format_components[1], format_components[2], format_components[3])
        end_time = new_format(format_components[5], format_components[6], format_components[7])
        return f'{start_time} to {end_time}'
    else:
        raise ValueError


def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ':00'
        new_time = f'{new_hour:02}' + new_minute
    else:
        new_time = f'{new_hour:02}' + ':' + minute
    return new_time


if __name__ == "__main__":
    main()