
def main():
    list()

def list():
    grocery_list = {}
    while True:
        try:
            item = input('')
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except (EOFError, KeyError):
            break
        else:
            pass
    ordered_list = sorted(grocery_list)
    for item in ordered_list:
        print(grocery_list[item], item.upper())

main()