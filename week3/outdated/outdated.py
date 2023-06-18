# program that prompts the user for a date, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again.

months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

def main():
    format_date()

def format_date():
    while True:
        try:
            date = input('Date: ').strip()
            if '/' in date:
                m, d, y = date.split('/')
            elif ',' in date:
                date = date.replace(',', '')
                m, d, y = date.split(' ')
                if m in months:
                    m = months.index(m)+1
            else:
                pass
            m = int(m)
            d = int(d)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f'{y}-{m:02}-{d:02}')
                break
        except (ValueError, UnboundLocalError):
            pass
        else:
            pass


main()
