# Score categories
# Change the values as you see fit
YACHT = (lambda x:50 if x.count(x[0])==5 else 0)
ONES = (lambda x: digitsCount(x,1))
TWOS = (lambda x: digitsCount(x,2))
THREES = (lambda x: digitsCount(x,3))
FOURS = (lambda x: digitsCount(x,4))
FIVES = (lambda x: digitsCount(x,5))
SIXES = (lambda x: digitsCount(x,6))
FULL_HOUSE = (lambda x: sum(x) if IsDigitsPartTwoGroup2And3(x) else 0)
FOUR_OF_A_KIND = (lambda x: digitsPartFourSame(x))
LITTLE_STRAIGHT = (lambda x: 30 if isStraight(x,1) else 0)
BIG_STRAIGHT = (lambda x: 30 if isStraight(x,2) else 0)
CHOICE = (lambda x: sum(x))

#dice is list with five digits in [1,2,3,4,5,6]
def digitsCount(dice, digit):
    return digit* dice.count(digit)

def isStraight(dice, start_dice):
    littleStraight = set([1,2,3,4,5])
    bigStraight = set([2,3,4,5,6])
    diceSet= set(dice)
    if start_dice == 1:
        if diceSet == littleStraight:
            return True
    elif start_dice == 2:
        if diceSet == bigStraight:
            return True
    return False
def IsDigitsPartTwoGroup2And3(dice):
    diceSet= set(dice)
    if len(diceSet) != 2:
        return False

    for each in diceSet:
        if dice.count(each) < 2:
            return False
    return True
def digitsPartFourSame(dice):
    diceSet = set(dice)
    if len(diceSet) > 2:
        return 0
    for each in diceSet:
        if dice.count(each) >=4:
            return each*4
    return 0

def score(dice, category):
   return category(dice)
