# App prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No

possible_answers = ['42', 'fortytwo',]

# function accepts input, formats it and sends formated input to function 'answer'
def main():
    user_input = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').casefold().replace('-', '').replace(' ', '')
    answer(user_input)

# function 'answer' accepts input and prints 'Yes' if correct and 'No' if it is not.
def answer(i):
    if i in possible_answers:
        print('Yes')
    else:
        print('No')

main()