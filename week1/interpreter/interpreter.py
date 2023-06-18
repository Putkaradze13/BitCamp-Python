# App prompts the user for an arithmetic expression and then calculates
# and outputs the result as a floating-point value formatted to one decimal place

x, y, z = input('Expression: ').strip().split(' ',)

result = eval(x + y + z)

print(float(result))