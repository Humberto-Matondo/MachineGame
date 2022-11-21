MAX_BET = 100
MIN_BET = 1

def get_bet():
    while True:
        amount = input('How much would you like to bet on each line? Kz')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between Kz{MIN_BET} and Kz{MAX_BET}.')
        else:
            print('Please enter a number.')
    return amount
