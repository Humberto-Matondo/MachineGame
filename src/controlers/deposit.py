def theDepositFuncion():

    while True:
        amount = input('\nHow much would you like to deposit? Kz')
        if amount.isdigit(): #this will sheck if the mount is a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than Kz0.')
        else:
            print('Please enter a number.')
    return amount
