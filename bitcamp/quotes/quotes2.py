

author_quotes = {
    'Gandalf': 'It isn\'t despair, for despair is only for those who see the end beyond all doubt. We don\'t.',
    'God': 'When you do things right, people won\'t be sure you\'ve done anything at all.',
    'BoJack Horseman': 'One day, you\'re gonna look around and you\'re going to realize that everybody loves you, but nobody likes you. And that is the loneliest feeling in the world.',
    'Batman': 'It\'s not who I am underneath - it\'s what I do that defines me',
    'Yoda': 'Do or don\'t. There isn\'t try',
}

def main():
    question = input('Quotes or Author? ').casefold()

    answer(question)

def answer(q):
    if q == 'quotes':
        quotes = input('What is the quotes? ')
        author = input('Who is author? ')
        print(f'{author} says, \'{quotes}\'')
    elif q == 'author':
        author = input('Gandalf, BoJack Horseman, Batman, Yoda or God? ')
        quotes = author_quotes.get(author)
        print(f'{author} says, \'{quotes}\'')

main()