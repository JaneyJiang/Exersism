import re
def verify(isbn):
    #findall the digists and end X.
    numbers = ''.join(re.findall('[\d]+|X$',isbn))
    if len(numbers) != 10:
        return False
    #caculate the isbn formalulate
    return sum([int(num)*i if num!='X' else 10*i for i,num in enumerate(numbers[::-1],1) ])%11==0