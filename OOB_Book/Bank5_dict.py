#%%
accountList = []

def newAccount(aName: str, aBal: float, aPw: str):
 global accountList
 newAccountDict = {'Name': aName,
                   'Balance': aBal,
                   'Password': aPw
                   }
 accountList.append(newAccountDict)
 
def show(acntNum: int):
    global accountList
    thisAccnt = accountList[acntNum]
    print(f'Account: {acntNum}\n\tName: {thisAccnt["Name"]}\n\t \
        Balance: {thisAccnt["balance"]}\n\t \
        Password: {thisAccnt["Password"]}\n')
# %%
newAccount('Ryne', 50, 'Titty')
newAccount('Allison', 5000.50, 'kitty')
# %%
