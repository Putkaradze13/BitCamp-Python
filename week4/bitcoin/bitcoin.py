# The app accepts amount of bitcoins as argument and uses api to convert it into USD.

import requests
import sys

def main():
    convert()

def convert():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    elif sys.argv[1].isalpha():
        sys.exit('Command-line argument is not a number')
    else:
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            rate = response.json()['bpi']['USD']['rate_float']
            n = float(sys.argv[1])
        except (requests.RequestException, ValueError):
            return
    amount = float(rate * n)
    print(f"${amount:,.4f}")


if __name__=='__main__':
    main()