# %%
import random

# %%
suits = ("Sapdes", "Hearts", "Clubs", "Diamonds")
ranks = ("Ace", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "Qieen", "King")

ncards = 8

# %%


def getCard(deckListIn):
    thisCard = deckListIn.pop()

    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)

    return deckListOut


# %%
print("Welcome to Higher or Lower\n")
print(
    "You have to choose whether the next card to be shown will be higher or lower than the current card."
)
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.")

# %%
startingDeckList = []

for suit in suits:
    for thisVal, rank in enumerate(ranks):
        cardDict = {'rank': rank, 'suit': suit, 'val': thisVal + 1}
        startingDeckList.append(cardDict)

# %%
score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    curCardDict = getCard(gameDeckList)
    curCardRank = curCardDict['rank']
    curCardVal = curCardDict['val']
    curCardSuit = curCardDict['suit']
    curCardStr = f'{curCardRank} of {curCardSuit}'
    print(f'Starting card is: {curCardStr}\n')

    for cardNum in range(0, ncards):
        answer = input(
            f'Will the next card be higher or lower than the {curCardStr}? (enter h or l) ')
        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardVal = nextCardDict['val']
        nextCardSuit = nextCardDict['suit']
        nextCardStr = f'{nextCardRank} of {nextCardSuit}'
        print(f'Next card is {nextCardStr}')
        
        if answer == 'h':
            if nextCardVal > curCardVal:
                print('Correct bitch, it was higher!!/n')
                score += 20
            else:
                print('Sorry motherfucker, it was lower!!/n')
                score -= 15
                
        elif answer == 'l':
            if nextCardVal < curCardVal:
                score += 20
                print('Correct bitch, it was lower!!/n')
            else:
                print('Sorry motherfucker, it was higher!!/n')
                score -= 15
        print(f'Your score is {score}\n')
        curCardRank = nextCardRank
        curCardVal = nextCardVal
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain =='q':
        break
        
        
        
                
                
            
            
            
                
        
        
# %%
