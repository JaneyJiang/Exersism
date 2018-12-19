import random
import itertools
from string import ascii_uppercase as upperletters

words = [''.join(p) for p in itertools.product(upperletters,upperletters)]
digits = [str(t).zfill(3) for t in range(1000)]
names = [l+p for l,p in itertools.product(words,digits)]
random.shuffle(names)
NameFactory = iter(names)

class Robot(object):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.name = next(NameFactory)

