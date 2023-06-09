# The app program that prompts consumers users to input a fruit
# and then outputs the number of calories in one portion of that fruit.

fruits = {
    'apple': '130',
    'avocado': '50',
    'banana': '110',
    'cantaloupe': '50',
    'grapefruit': '60',
    'grapes': '90',
    'honeydew': '50',
    'kiwifruit': '90',
    'lemon': '15',
    'lime': '20',
    'nectarine': '60',
    'orange': '80',
    'peach': '60',
    'pear': '100',
    'pineapple': '50',
    'plums': '70',
    'strawberries': '50',
    'sweet cherries': '100',
    'tangerine': '50',
    'watermelon': '80',
}

def main():
    fruit = input('Item: ').lower()
    nutrition_fact(fruit)

def nutrition_fact(fruit):
    if fruit in fruits:
        cal = fruits.get(fruit)
        print(f'Calories: {cal}')
    else:
        return

main()