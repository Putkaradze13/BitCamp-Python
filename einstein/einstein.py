# Application prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer

m = int(input('What mass? '))

E = m * (300000000*300000000)

print(E)