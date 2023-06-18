# prompts the user for a greeting. If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
# It ignores any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively

def main():
    bank_policy(input('Greeting: ').replace(' ', '').casefold())

def bank_policy(input):
    if 'hello' in input:
        print('$0')
    elif 'h' == input[0]:
        print('$20')
    else:
        print('$100')

main()