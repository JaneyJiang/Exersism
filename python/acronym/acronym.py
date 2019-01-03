import re
def abbreviate(words):
    wordlist = re.split('[ -]',words)
    abv = [word[0].upper() for word in wordlist if word and word[0].isalpha()]
    return "".join(abv)
