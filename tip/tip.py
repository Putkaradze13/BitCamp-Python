# App accepts amount of paid money as input with '$' sign in front
# and percentage as input with '%' sign at the end, 
# then it removes '$' and '%' signs from both inputs and calculates amount of left tip.

def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace('$', ''))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace('%', ''))
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d)
    

def percent_to_float(p):
    return float(p) 
    

main()