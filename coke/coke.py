# The app prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due.
# Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed. 

coins = [5, 10, 25]
cost = 50
i = 0

while i < cost:
    coin = int(input('Insert Coin: '))
    if coin not in coins:
        print(f'Amount Due: {cost - i}')
    else:
        i += coin
        if i < cost:
            print(f'Amount Due: {cost - i}')
        else:
            print(f'Change Owed: {i - cost}')
            
