# Hello program with defining function manually
def greet ():
    name = input('What is your name? ').strip().title()
    hello(name)


def hello(user):
    print('Hello, ' + user + ', Nice to meet you!')

greet()
