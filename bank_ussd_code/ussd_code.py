def ussd_code(ussd):
    Password = '3030'
    balance = 1000000
    bank_option = ['Send Money', 'Buy airtime', 'Check balance']
    bank_type = ['GT-BANK', 'ACCESS BANK', 'ZENITH BANK', 'WE-MA BANK', 'FIRST BANK']
    for i, j in enumerate(bank_option):
        print(i, j)

    option = int(input('Enter option (0,1,2) to make transaction : '))

    # TO CHECK BALANCE
    if option == 2:
        while True:
            pass_word = (input('Enter password : '))
            if pass_word == Password:
                print('\nYour balance is : $', str(balance))
                break
            else:
                print('incorrect password')
                continue

    # TO SEND MONEY
    elif option == 0:
        for i, j in enumerate(bank_type):
            print(i, j)
        input('choose bank (0,1,2,3....) : ')
        while True:
            number = (input('enter account number : '))
            if len(number) == 10:
                break
            else:
                print('Incorrect account no. Try again!!')
                continue
        amount = input('Enter amount you want to send : ')

        while True:
            pass_word1 = input('Enter password to send money : ')
            if pass_word1 == Password:
                remain_balance = balance - int(amount)
                print('')
                print('$' + amount, ' Sent.....Thank you for banking with us.')
                print('Remaining balance is $', remain_balance)
                break
            else:
                print('incorrect password')
                continue

    # TO BUY AIR-TIME
    elif option == 1:
        amount1 = input('Enter amount you want to recharge : ')

        while True:
            number = (input('enter phone number : '))
            if len(number) == 11:
                break
            else:
                print('incorrect phone number')
                continue

        while True:
            pass_word1 = input('Enter password to send airtime : ')
            if pass_word1 == Password:
                remain_balance = balance - int(amount1)
                print('')
                print(amount1, ' Recharge successfully.')
                print('Remaining balance is $', remain_balance)
                break
            else:
                print('incorrect password')
                continue


ussd_code(input('enter ussd code: '))
