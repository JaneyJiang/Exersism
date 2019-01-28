import re
def abbreviate(words):
    wordlist = re.split('[ -]',words)
    abv = [word[0].upper() for word in wordlist if word and word[0].isalpha()]
    return "".join(abv)

'''
#这个是找到第一个单词字母和有间隔隔开的第一个单词字母,的方式
def abbreviate(string):
    firstletters = re.findall("^[a-zA-Z]|[\s\-_][a-zA-Z]", string)
    return ''.join([x[-1].upper() for x in firstletters])
'''
