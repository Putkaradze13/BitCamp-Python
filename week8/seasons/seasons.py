from datetime import date
from re import fullmatch
from sys import exit
from inflect import engine

class Dates:
    def __init__(self, birth):
        if fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", birth):
            birth = birth.split('-')
            self._date = date(int(birth[0]), int(birth[1]), int(birth[2]))
        else:
            exit("Invalid Date")

    def diff(self, other):
        di = (other - self._date).days*24*60
        return f"{engine().number_to_words(di, andword='').capitalize()} minutes"


def main():
    birth = input("Date of Birth: ")
    birth_date = Dates(birth)
    print(birth_date.diff(date.today()))


if __name__ == "__main__":
    main()