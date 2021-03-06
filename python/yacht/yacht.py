# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    diceSet = set(dice)
    littleStraight = set([1,2,3,4,5])
    bigStraight = set([2,3,4,5,6])
    if category == YACHT:
        if dice.count(dice[category])==5:
            return 50
    elif (category == ONES or 
            category == TWOS or 
            category == THREES or 
            category == FOURS or
            category == FIVES or
            category == SIXES):
        return dice.count(category)*category
    elif category == FULL_HOUSE:
        if len(diceSet)==2:
            for each in diceSet:
                if dice.count(each) < 2:
                    return 0
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        if len(diceSet)<=2:
            for each in diceSet:
                if dice.count(each) >= 4:
                    return each*4
    elif category == LITTLE_STRAIGHT:
        if diceSet == littleStraight:
            return 30
    elif category == BIG_STRAIGHT:
        if diceSet == bigStraight:
            return 30
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
    return 0

