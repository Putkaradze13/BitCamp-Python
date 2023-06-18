# App prompts user input and returns amount of characters in user input

user_input = input('What is the input string? ')

length = len(user_input.replace(' ', ''))

print(f'"{user_input}" has {length} characters')