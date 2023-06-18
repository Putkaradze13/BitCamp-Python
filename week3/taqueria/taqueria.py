# The app enables user to place an order, prompting them for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far,

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    result = order()
    print(result)

def order():
    total = 0
    while True:
        try:
            item = input('Item: ').title()
            if item in menu:
                price = menu.get(item)
                total += price
                print(f'Total: ${format(total, ".2f")}')
        except EOFError:
            print(f'\nTotal: ${format(total, ".2f")}')
            return


main()