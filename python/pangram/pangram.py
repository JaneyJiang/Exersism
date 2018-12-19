def is_pangram(sentence):
    alphaSet = set('abcdefghijklmnopqrstuvwxyz')
    return alphaSet.issubset(sentence.lower())
