# Non-OOP
# Bank Version 1
# Single account

# %%
accountName = 'joe'
accountBal = 100
accountPw = 'soup'

#%%
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')
    print('Press w to quit')
    print()
    
    act = input('What do you wanna do?').lower()[0]
    
    if act == 'b':
        print('Get Balance')
        usrPw = input('Please enter the password')
        if usrPw != accountPw:
            print('Wront PW bitch')
        else:
            print(f'Your balance is: {accountBal}')
            
    elif act == 'd':
        print('Deposit')
        usrDepAmt = int(float(input('Please enter amount to deposit: ')))        
        usrPw = input('Please enter the password')
        
        if usrDepAmt < 0:
            print('Hey dumbfuck, you cannot deposit a negative amount, thats called a withdrawl you retard!')
        elif usrPw != accountPw:
            print('Wront PW bitch')
        else:
            accountBal += usrDepAmt
            print(f'Your new balance is {accountBal}')
            
    elif act == 's':
        print('Show:')
        print(f'    Name: {accountName}')
        print(f'    Balance: {accountBal}')
        print(f'    Password: {accountPw}')
        print()
        
    elif act == 'q':
        break

    elif act == 'w':
        print('Withdraw')

        usrWdAmt = int(float(input('Please enter amount to withdraw: ')))
        usrPw = input('Please enter the password')

        if usrDepAmt < 0:
            print(
                'Hey dumbfuck, you cannot withdraw a negative amount, thats called a deposit you retard!')

        elif usrPw != accountPw:
            print('Wront PW bitch')
        else:
            accountBal -= usrWdAmt
            print(f'Your balance is: {accountBal}')

print('Done')
            
        
            
            
        
    

