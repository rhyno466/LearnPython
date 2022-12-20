#%%
# Non-OOP

#%%
accoutNamesList = []
accouuntBalanceList = []
accountPasswordList = []

def new_account(nme: str, bal: int, pw: str):
    global accoutNamesList, accouuntBalanceList, accountPasswordList
    accoutNamesList.append(nme)
    accouuntBalanceList.append(bal)
    accountPasswordList.append(pw)

def show(acntNum: int):
    global accoutNamesList, accouuntBalanceList, accountPasswordList
    print(f'Account: {acntNum}\n\tName: {accoutNamesList[acntNum]}\n\t \
        Balance: {accouuntBalanceList[acntNum]}\n\t \
        Password: {accountPasswordList[acntNum]}\n')
    
#%%
new_account('Ryne', '1200', 'titty')
new_account('Allison', '5000', 'kitty')
    
# %%
