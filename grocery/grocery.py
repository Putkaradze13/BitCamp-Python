# The app prompts the user for items, one per line, until the user inputs control-d
# (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.

def main():
    list()

def list():
    grocery = {}
    while True:
        try:
            item = input().upper()
            if item in grocery:
                amount = grocery[item]
                amount += 1
                grocery[item] = amount
            else:
                grocery.update({item: 1})
        except EOFError:
            sorted_list = sorted(grocery.items())
            converted_dict = dict(sorted_list)
            for item, amount in converted_dict.items():
                print(amount, item)
            break
        except KeyError:
            pass
        else:
            pass


main()